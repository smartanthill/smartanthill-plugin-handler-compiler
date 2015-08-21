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

import antlr4

from smartanthill_phc.antlr_parser import CLexer, CParser
from smartanthill_phc.builtin import create_builtins
from smartanthill_phc.common.antlr_helper import dump_antlr_tree
from smartanthill_phc.common.compiler import Compiler, Ctx, process_syntax_tree
from smartanthill_phc.common.visitor import dump_tree,\
    check_all_nodes_reachables
from smartanthill_phc.parser import c_parse_tree_to_syntax_tree
from smartanthill_phc.rewrite import rewrite_code
from smartanthill_phc.root import RootNode
from smartanthill_phc.state import create_states


class _Helper(object):
    '''
    Agregate class to hold parser related stuff
    '''

    def __init__(self, file_name):
        self.file_name = file_name
        self.file_stream = antlr4.FileStream(file_name)
        self.clexer = CLexer.CLexer(self.file_stream)
        self.token_stream = antlr4.CommonTokenStream(self.clexer)
        self.cparser = CParser.CParser(self.token_stream)


def process_file(file_name, func_name, dump):
    '''
    Process a c input file, and returns an string with output text
    '''

    helper = _Helper(file_name)
    ptree = helper.cparser.compilationUnit()

    if dump:
        print '\n'.join(dump_antlr_tree(ptree))

    c = Compiler()
    root = c.init_node(RootNode(), Ctx.ROOT)
    builtin = create_builtins(c, Ctx.BUILTIN)
    root.set_builtins(builtin)
    source = c_parse_tree_to_syntax_tree(c, ptree)
    root.set_source(source)

    if dump:
        print
        print '\n'.join(dump_tree(root))

    check_all_nodes_reachables(c, root)
    process_syntax_tree(c, root)

    create_states(c, root, func_name)

    if dump:
        print
        print '\n'.join(dump_tree(root))

    async = rewrite_code(c, root, helper.token_stream)

    return async
