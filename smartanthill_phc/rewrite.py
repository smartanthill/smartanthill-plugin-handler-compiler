# Copyright (C) 2015 OLogN Technologies AG
#
# This source file is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License version 2
# as published by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

from datetime import date

from smartanthill_phc.TokenStreamRewriter import TokenStreamRewriter
from smartanthill_phc.common.visitor import NodeVisitor, visit_node
from smartanthill_phc.parser import get_declarator_name
from smartanthill_phc.root import NonBlockingData


def rewrite_code(compiler, root, token_stream, struct_name):
    '''
    Rewrites code tree
    '''
    rewriter = TokenStreamRewriter(token_stream)
    visitor = _RewriteVisitor(compiler, rewriter, token_stream, struct_name)
    visit_node(visitor, root)

    text = rewriter.getText()

    compiler.check_stage('rewrite')

    return text


def write_header(compiler, root, token_stream, struct_name, include_guard):
    '''
    Rewrites code tree
    '''
    nb = root.get_scope(NonBlockingData)
    text = _write_header_file(token_stream, struct_name, include_guard, nb)

    compiler.check_stage('header')

    return text


_header_file_banner = [
    "Copyright (C) %s OLogN Technologies AG\n" % date.today().year,
    "This program is free software; you can redistribute it and/or modify",
    "it under the terms of the GNU General Public License version 2 as",
    "published by the Free Software Foundation.\n",
    "This program is distributed in the hope that it will be useful,",
    "but WITHOUT ANY WARRANTY; without even the implied warranty of",
    "MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the",
    "GNU General Public License for more details.\n",
    "You should have received a copy of the GNU General Public License along",
    "with this program; if not, write to the Free Software Foundation, Inc.,",
    "51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA\n",
]


def _write_header_file(token_stream, struct_name, include_guard, nb):

    txt = "/*" + (76 * "*") + "\n"
    for each in _header_file_banner:
        txt += "    " + each + "\n"

    txt += (76 * "*") + "*/\n\n"

    txt += "#if !defined %s\n" % include_guard
    txt += "#define %s\n\n" % include_guard

    txt += "#include <stdint.h>\n\n\n"

    txt += "typedef struct _%s {\n" % struct_name
    txt += "uint8_t sa_next;\n"

    for each in nb.refs_moved_var_decls:
        start = each.ctx.declarationSpecifier(0).start
        stop = each.ctx.initDeclaratorList().initDeclarator(
            0).declarator().stop

        tk = token_stream.getText((start.tokenIndex, stop.tokenIndex))
        txt += str(tk)
        txt += ";\n"

    txt += "} %s;\n\n" % struct_name
    txt += "#endif // %s\n" % include_guard

    return txt


class _RewriteVisitor(NodeVisitor):

    '''
    Visitor class for plugin rewrite
    '''

    def __init__(self, compiler, writer, token_stream, type_name):
        '''
        Constructor
        '''
        self._c = compiler
        self._w = writer
        self._tokens = token_stream
        self._tn = type_name
        self._nb = None

    def default_visit(self, node):
        '''
        Default action when a node specific action is not found
        '''
        self._c.report_error(
            node.ctx, "Statement rewrite not supported")

    def _visit_expression(self, expr):
        '''
        Helper method to create an expression visitor an call it
        '''
        visit_node(self, expr)

    def visit_RootNode(self, node):
        self._nb = node.get_scope(NonBlockingData)
        visit_node(self, node.child_source)

    def visit_PluginSourceNode(self, node):
        visit_node(self, node.child_declaration_list)

    def visit_DeclarationListNode(self, node):
        for each in node.childs_declarations:
            visit_node(self, each)

    def visit_FunctionDeclNode(self, node):
        visit_node(self, node.child_statement_list)

    def visit_StmtListNode(self, node):
        for each in node.childs_statements:
            visit_node(self, each)

    def visit_NopStmtNode(self, node):
        # Nothing to do here
        pass

    def visit_VariableDeclarationStmtNode(self, node):

        if self._nb.is_moved_var_decl(node):

            decl_list = node.ctx.initDeclaratorList()
            assert decl_list is not None
            assert len(decl_list.initDeclarator()) == 1
            tk = get_declarator_name(decl_list.initDeclarator(0).declarator())

            if node.child_initializer is not None:
                self._w.replaceTokens(
                    node.ctx.start, tk.symbol,
                    u"sa_state->%s" % node.txt_name)
            else:
                self._w.deleteTokens(node.ctx.start, node.ctx.stop)

        if node.child_initializer is not None:
            self._visit_expression(node.child_initializer)

    def visit_ExpressionStmtNode(self, node):
        self._visit_expression(node.child_expression)

    def visit_BlockingCallStmtNode(self, node):

        self._visit_expression(node.child_expression)

        n = node.child_expression.txt_name
        wf = node.ref_waitingfor_arg.txt_name
        args = node.child_expression.child_argument_list.childs_arguments
        assert len(args) >= 1
        arg0_ctx = args[0].ctx
        arg0 = self._tokens.getText((arg0_ctx.start, arg0_ctx.stop))

        if n == "papi_sleep":
            txt = u"papi_wait_handler_add_wait_for_timeout( %s, %s );" % (
                wf, arg0)
            self._w.replaceTokens(node.ctx.start, node.ctx.stop, txt)
        else:
            if n == "papi_wait_for_spi_send":
                f = u"papi_start_sending_spi_command_16"
                w = u"spi_send"
            elif n == "papi_wait_for_i2c_send":
                f = u"papi_start_sending_i2c_command_16"
                w = u"i2c_send"
            elif n == "papi_wait_for_spi_receive":
                f = u"papi_start_receiving_spi_data_16"
                w = u"spi_receive"
            elif n == "papi_wait_for_i2c_receive":
                f = u"papi_start_receiving_i2c_data_16"
                w = u"i2c_receive"
            else:
                assert False

            self._w.replaceToken(
                node.child_expression.ctx.Identifier().symbol, f)

            txt = u"papi_wait_handler_add_wait_for_%s( %s, %s );" % (
                w, wf, arg0)

    def visit_ReturnStmtNode(self, node):
        if node.child_expression is not None:
            self._visit_expression(node.child_expression)

    def visit_IfElseStmtNode(self, node):
        self._visit_expression(node.child_expression)
        visit_node(self, node.child_if_branch)
        if node.child_else_branch is not None:
            visit_node(self, node.child_else_branch)

    def visit_StateMachineStmtNode(self, node):

        assert len(node.childs_states) != 0

        txt = u"\n\nswitch(sa_state->sa_next) {"
        for each in node.childs_states:

            txt += u"\ncase %s: goto label_%s;" % (each.txt_id, each.txt_id)
#            visit_node(self, each.child_statement_list)

        txt += u"\ndefault: sa_state->sa_next = 0; return -1; /* TBD */"
        txt += u"\n}"
        txt += u"\nlabel_0:;"  # mb: add semicolon after label
        if node.ctx.line is not None:
            txt += u"\n//#line %s\n" % node.ctx.line

        self._w.insertAfterToken(node.ctx, txt)

    def visit_NextStateStmtNode(self, node):

        nxt = node.ref_next_state.txt_id
        txt = u"\nsa_state->sa_next = %s;" % nxt

        if node.ref_next_state.wait_condition is None:
            txt += u"\nreturn PLUGIN_DEBUG;"
            # we add a nop here, because C compiler will complain if next
            # statement is a declaration.
            # Only pure statements allowed right after a label
            # Adding a NOP will silence it
            txt += u"\nlabel_%s: /* nop */ ;" % nxt
        else:
            txt += u"\nreturn PLUGIN_WAITING;"
            txt += u"\nlabel_%s:" % nxt

            n = node.ref_next_state.wait_condition.txt_name
            args = node.ref_next_state.wait_condition.\
                child_argument_list.childs_arguments
            assert len(args) >= 1
            arg0_ctx = args[0].ctx
            arg0 = self._tokens.getText((arg0_ctx.start, arg0_ctx.stop))

            wf = node.ref_next_state.ref_waitingfor_arg.txt_name
            if n == "papi_sleep":
                f = u"timeout(%s, %s)" % (0, wf)
            elif n == "papi_wait_for_spi_send":
                f = u"spi_send(%s, %s)" % (wf, arg0)
            elif n == "papi_wait_for_i2c_send":
                f = u"i2c_send(%s, %s)" % (wf, arg0)
            elif n == "papi_wait_for_spi_receive":
                f = u"spi_receive(%s, %s)" % (wf, arg0)
            elif n == "papi_wait_for_i2c_receive":
                f = u"i2c_receive(%s, %s)" % (wf, arg0)
            else:
                assert False

            txt += u" if(papi_wait_handler_is_waiting_for_%s)" % f
            txt += u" return PLUGIN_WAITING;"

        if node.ctx.stop.line is not None:
            txt += u"\n//#line %s\n" % node.ctx.stop.line

        self._w.insertAfterToken(node.ctx.stop, txt)

    def visit_InitStateStmtNode(self, node):

        txt = u"\n%s* sa_state = (%s*)%s;" % (self._tn, self._tn, node.txt_arg)
        txt += u"\nsa_state->sa_next = 0;"
        self._w.insertAfterToken(node.ctx, txt)

    def visit_ReturnStateStmtNode(self, node):

        txt = u"sa_state->sa_next = 0;"
        self._w.insertBeforeToken(node.ctx.start, txt)

    def visit_StateDataCastStmtNode(self, node):
        self._w.insertAfterToken(
            node.ctx,
            u"\n%s* sa_state = (%s*)%s;" % (self._tn, self._tn, node.txt_arg))

    def visit_DontCareExprNode(self, node):
        for each in node.childs_expressions:
            visit_node(self, each)

    def visit_TypeCastExprNode(self, node):
        visit_node(self, node.child_expression)

    def visit_LiteralExprNode(self, node):
        # nothing to do here
        pass

    def visit_VariableExprNode(self, node):

        if node.ref_decl is not None:
            if self._nb.is_moved_var_decl(node.ref_decl):
                self._w.replaceToken(
                    node.ctx.symbol,
                    u"(sa_state->%s)" % node.txt_name)

    def visit_FunctionCallExprNode(self, node):
        visit_node(self, node.child_argument_list)

    def visit_ArgumentListNode(self, node):
        for each in node.childs_arguments:
            visit_node(self, each)
