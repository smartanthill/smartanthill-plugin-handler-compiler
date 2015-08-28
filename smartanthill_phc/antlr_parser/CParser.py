# Generated from java-escape by ANTLR 4.5
# encoding: utf-8
from __future__ import print_function
from antlr4 import *
from io import StringIO
package = globals().get("__package__", None)
ischild = len(package)>0 if package is not None else False
if ischild:
    from .CListener import CListener
    from .CVisitor import CVisitor
else:
    from CListener import CListener
    from CVisitor import CVisitor

def serializedATN():
    with StringIO() as buf:
        buf.write(u"\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\3")
        buf.write(u"k\u0341\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t")
        buf.write(u"\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write(u"\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4")
        buf.write(u"\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30")
        buf.write(u"\t\30\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t")
        buf.write(u"\35\4\36\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$")
        buf.write(u"\t$\4%\t%\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t")
        buf.write(u",\4-\t-\4.\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63")
        buf.write(u"\t\63\4\64\t\64\4\65\t\65\4\66\t\66\3\2\3\2\3\2\3\2\3")
        buf.write(u"\2\3\2\3\2\3\2\6\2u\n\2\r\2\16\2v\3\2\3\2\3\2\3\2\3\2")
        buf.write(u"\3\2\3\2\5\2\u0080\n\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3")
        buf.write(u"\2\3\2\3\2\3\2\3\2\3\2\5\2\u008f\n\2\3\2\3\2\3\2\3\2")
        buf.write(u"\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\7\2\u009e\n\2\f")
        buf.write(u"\2\16\2\u00a1\13\2\3\3\3\3\3\3\7\3\u00a6\n\3\f\3\16\3")
        buf.write(u"\u00a9\13\3\3\4\3\4\3\4\3\4\3\4\3\4\5\4\u00b1\n\4\3\5")
        buf.write(u"\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5")
        buf.write(u"\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5")
        buf.write(u"\3\5\3\5\3\5\3\5\3\5\3\5\7\5\u00d4\n\5\f\5\16\5\u00d7")
        buf.write(u"\13\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\5\6\u00e0\n\6\3\7\3")
        buf.write(u"\7\3\7\3\7\3\7\5\7\u00e7\n\7\3\b\3\b\3\b\7\b\u00ec\n")
        buf.write(u"\b\f\b\16\b\u00ef\13\b\3\t\3\t\3\n\6\n\u00f4\n\n\r\n")
        buf.write(u"\16\n\u00f5\3\n\5\n\u00f9\n\n\3\n\3\n\3\n\5\n\u00fe\n")
        buf.write(u"\n\3\13\3\13\3\13\3\13\3\13\5\13\u0105\n\13\3\f\3\f\3")
        buf.write(u"\f\7\f\u010a\n\f\f\f\16\f\u010d\13\f\3\r\3\r\3\r\3\r")
        buf.write(u"\3\r\5\r\u0114\n\r\3\16\3\16\3\17\3\17\3\17\3\17\3\17")
        buf.write(u"\3\17\3\17\3\17\3\17\5\17\u0121\n\17\3\20\3\20\5\20\u0125")
        buf.write(u"\n\20\3\20\3\20\6\20\u0129\n\20\r\20\16\20\u012a\3\20")
        buf.write(u"\3\20\3\20\3\20\3\20\5\20\u0132\n\20\3\21\3\21\3\22\3")
        buf.write(u"\22\5\22\u0138\n\22\3\22\3\22\3\22\5\22\u013d\n\22\3")
        buf.write(u"\23\3\23\5\23\u0141\n\23\3\23\3\23\5\23\u0145\n\23\5")
        buf.write(u"\23\u0147\n\23\3\24\3\24\3\24\7\24\u014c\n\24\f\24\16")
        buf.write(u"\24\u014f\13\24\3\25\3\25\5\25\u0153\n\25\3\25\3\25\5")
        buf.write(u"\25\u0157\n\25\3\26\3\26\5\26\u015b\n\26\3\26\3\26\3")
        buf.write(u"\26\3\26\3\26\3\26\5\26\u0163\n\26\3\26\3\26\3\26\3\26")
        buf.write(u"\3\26\3\26\3\26\5\26\u016c\n\26\3\27\3\27\3\27\7\27\u0171")
        buf.write(u"\n\27\f\27\16\27\u0174\13\27\3\30\3\30\3\30\5\30\u0179")
        buf.write(u"\n\30\3\31\3\31\3\31\3\31\3\31\3\32\3\32\3\33\3\33\3")
        buf.write(u"\33\3\33\3\33\5\33\u0187\n\33\3\34\3\34\3\34\3\34\3\34")
        buf.write(u"\3\34\3\34\3\34\3\34\3\34\5\34\u0193\n\34\3\35\5\35\u0196")
        buf.write(u"\n\35\3\35\3\35\3\36\3\36\3\36\3\36\3\36\3\36\5\36\u01a0")
        buf.write(u"\n\36\3\36\3\36\3\36\7\36\u01a5\n\36\f\36\16\36\u01a8")
        buf.write(u"\13\36\3\36\5\36\u01ab\n\36\3\36\3\36\3\36\3\36\3\36")
        buf.write(u"\7\36\u01b2\n\36\f\36\16\36\u01b5\13\36\3\36\3\36\3\36")
        buf.write(u"\3\36\3\36\3\36\6\36\u01bd\n\36\r\36\16\36\u01be\3\36")
        buf.write(u"\3\36\3\36\3\36\3\36\3\36\3\36\7\36\u01c8\n\36\f\36\16")
        buf.write(u"\36\u01cb\13\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3")
        buf.write(u"\36\3\36\3\36\5\36\u01d7\n\36\3\36\7\36\u01da\n\36\f")
        buf.write(u"\36\16\36\u01dd\13\36\3\37\3\37\7\37\u01e1\n\37\f\37")
        buf.write(u"\16\37\u01e4\13\37\3\37\5\37\u01e7\n\37\3 \3 \3 \7 \u01ec")
        buf.write(u"\n \f \16 \u01ef\13 \3 \3 \5 \u01f3\n \3!\6!\u01f6\n")
        buf.write(u"!\r!\16!\u01f7\3!\3!\3!\6!\u01fd\n!\r!\16!\u01fe\3!\5")
        buf.write(u"!\u0202\n!\5!\u0204\n!\3\"\3\"\3\"\7\"\u0209\n\"\f\"")
        buf.write(u"\16\"\u020c\13\"\3#\3#\5#\u0210\n#\3$\3$\5$\u0214\n$")
        buf.write(u"\3$\5$\u0217\n$\3%\3%\3%\3%\3%\3%\3%\7%\u0220\n%\f%\16")
        buf.write(u"%\u0223\13%\3%\5%\u0226\n%\3%\3%\3%\3%\7%\u022c\n%\f")
        buf.write(u"%\16%\u022f\13%\3%\3%\3%\3%\3%\7%\u0236\n%\f%\16%\u0239")
        buf.write(u"\13%\3%\3%\3%\3%\3%\3%\3%\3%\3%\5%\u0244\n%\3%\5%\u0247")
        buf.write(u"\n%\3%\3%\3%\7%\u024c\n%\f%\16%\u024f\13%\3%\5%\u0252")
        buf.write(u"\n%\3%\3%\3%\3%\3%\7%\u0259\n%\f%\16%\u025c\13%\3%\3")
        buf.write(u"%\3%\3%\3%\3%\6%\u0264\n%\r%\16%\u0265\3%\3%\3%\3%\3")
        buf.write(u"%\3%\3%\3%\3%\3%\3%\5%\u0273\n%\3%\7%\u0276\n%\f%\16")
        buf.write(u"%\u0279\13%\3&\3&\3\'\3\'\3\'\3\'\5\'\u0281\n\'\3\'\3")
        buf.write(u"\'\5\'\u0285\n\'\3(\3(\5(\u0289\n(\3(\3(\3(\3(\3(\5(")
        buf.write(u"\u0290\n(\3(\7(\u0293\n(\f(\16(\u0296\13(\3)\6)\u0299")
        buf.write(u"\n)\r)\16)\u029a\3)\3)\3*\3*\3*\3*\3*\3*\5*\u02a5\n*")
        buf.write(u"\3+\3+\3+\3+\3+\6+\u02ac\n+\r+\16+\u02ad\3+\3+\3+\3,")
        buf.write(u"\3,\3,\3,\3,\3,\5,\u02b9\n,\3-\3-\3-\3-\3-\3-\3-\3-\3")
        buf.write(u"-\3-\3-\5-\u02c6\n-\3.\3.\7.\u02ca\n.\f.\16.\u02cd\13")
        buf.write(u".\3.\3.\3/\3/\5/\u02d3\n/\3\60\5\60\u02d6\n\60\3\60\3")
        buf.write(u"\60\3\61\3\61\3\61\3\61\3\61\3\61\3\61\5\61\u02e1\n\61")
        buf.write(u"\3\61\3\61\3\61\3\61\3\61\3\61\5\61\u02e9\n\61\3\62\3")
        buf.write(u"\62\3\62\3\62\3\62\3\62\3\62\3\62\3\62\3\62\3\62\3\62")
        buf.write(u"\3\62\3\62\3\62\3\62\3\62\5\62\u02fc\n\62\3\62\3\62\5")
        buf.write(u"\62\u0300\n\62\3\62\3\62\5\62\u0304\n\62\3\62\3\62\3")
        buf.write(u"\62\3\62\3\62\3\62\5\62\u030c\n\62\3\62\3\62\5\62\u0310")
        buf.write(u"\n\62\3\62\3\62\3\62\5\62\u0315\n\62\3\63\3\63\3\63\3")
        buf.write(u"\63\3\63\3\63\3\63\3\63\3\63\5\63\u0320\n\63\3\63\5\63")
        buf.write(u"\u0323\n\63\3\64\7\64\u0326\n\64\f\64\16\64\u0329\13")
        buf.write(u"\64\3\64\3\64\3\65\3\65\3\65\5\65\u0330\n\65\3\66\7\66")
        buf.write(u"\u0333\n\66\f\66\16\66\u0336\13\66\3\66\3\66\7\66\u033a")
        buf.write(u"\n\66\f\66\16\66\u033d\13\66\3\66\3\66\3\66\2\7\2\b:")
        buf.write(u"HN\67\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,")
        buf.write(u".\60\62\64\668:<>@BDFHJLNPRTVXZ\\^`bdfhj\2\20\4\2BBD")
        buf.write(u"D\7\2AACCEEHHMN\3\2EG\4\2AACC\3\2?@\3\2;>\3\2^_\3\2S")
        buf.write(u"]\b\2\t\t\24\24\34\34\"\"%%\64\64\n\2\3\5\f\f\21\21\25")
        buf.write(u"\25\32\33\37 \'(./\3\2\3\5\4\2##&&\6\2\r\r\35\35))--")
        buf.write(u"\5\2\7\7\31\31\62\62\u039d\2\u008e\3\2\2\2\4\u00a2\3")
        buf.write(u"\2\2\2\6\u00b0\3\2\2\2\b\u00b2\3\2\2\2\n\u00df\3\2\2")
        buf.write(u"\2\f\u00e6\3\2\2\2\16\u00e8\3\2\2\2\20\u00f0\3\2\2\2")
        buf.write(u"\22\u00fd\3\2\2\2\24\u0104\3\2\2\2\26\u0106\3\2\2\2\30")
        buf.write(u"\u0113\3\2\2\2\32\u0115\3\2\2\2\34\u0120\3\2\2\2\36\u0131")
        buf.write(u"\3\2\2\2 \u0133\3\2\2\2\"\u013c\3\2\2\2$\u0146\3\2\2")
        buf.write(u"\2&\u0148\3\2\2\2(\u0156\3\2\2\2*\u016b\3\2\2\2,\u016d")
        buf.write(u"\3\2\2\2.\u0175\3\2\2\2\60\u017a\3\2\2\2\62\u017f\3\2")
        buf.write(u"\2\2\64\u0186\3\2\2\2\66\u0192\3\2\2\28\u0195\3\2\2\2")
        buf.write(u":\u019f\3\2\2\2<\u01de\3\2\2\2>\u01e8\3\2\2\2@\u0203")
        buf.write(u"\3\2\2\2B\u0205\3\2\2\2D\u020d\3\2\2\2F\u0216\3\2\2\2")
        buf.write(u"H\u0246\3\2\2\2J\u027a\3\2\2\2L\u0284\3\2\2\2N\u0286")
        buf.write(u"\3\2\2\2P\u0298\3\2\2\2R\u02a4\3\2\2\2T\u02a6\3\2\2\2")
        buf.write(u"V\u02b8\3\2\2\2X\u02c5\3\2\2\2Z\u02c7\3\2\2\2\\\u02d2")
        buf.write(u"\3\2\2\2^\u02d5\3\2\2\2`\u02e8\3\2\2\2b\u0314\3\2\2\2")
        buf.write(u"d\u0322\3\2\2\2f\u0327\3\2\2\2h\u032f\3\2\2\2j\u0334")
        buf.write(u"\3\2\2\2lm\b\2\1\2mn\t\2\2\2n\u008f\5\2\2\7op\7!\2\2")
        buf.write(u"p\u008f\5\2\2\5q\u008f\7c\2\2r\u008f\7d\2\2su\7e\2\2")
        buf.write(u"ts\3\2\2\2uv\3\2\2\2vt\3\2\2\2vw\3\2\2\2w\u008f\3\2\2")
        buf.write(u"\2xy\7\65\2\2yz\5\16\b\2z{\7\66\2\2{\u008f\3\2\2\2|}")
        buf.write(u"\7c\2\2}\177\7\65\2\2~\u0080\5\4\3\2\177~\3\2\2\2\177")
        buf.write(u"\u0080\3\2\2\2\u0080\u0081\3\2\2\2\u0081\u008f\7\66\2")
        buf.write(u"\2\u0082\u0083\t\3\2\2\u0083\u008f\5\6\4\2\u0084\u0085")
        buf.write(u"\7!\2\2\u0085\u0086\7\65\2\2\u0086\u0087\5D#\2\u0087")
        buf.write(u"\u0088\7\66\2\2\u0088\u008f\3\2\2\2\u0089\u008a\7,\2")
        buf.write(u"\2\u008a\u008b\7\65\2\2\u008b\u008c\5D#\2\u008c\u008d")
        buf.write(u"\7\66\2\2\u008d\u008f\3\2\2\2\u008el\3\2\2\2\u008eo\3")
        buf.write(u"\2\2\2\u008eq\3\2\2\2\u008er\3\2\2\2\u008et\3\2\2\2\u008e")
        buf.write(u"x\3\2\2\2\u008e|\3\2\2\2\u008e\u0082\3\2\2\2\u008e\u0084")
        buf.write(u"\3\2\2\2\u008e\u0089\3\2\2\2\u008f\u009f\3\2\2\2\u0090")
        buf.write(u"\u0091\f\f\2\2\u0091\u0092\7\67\2\2\u0092\u0093\5\16")
        buf.write(u"\b\2\u0093\u0094\78\2\2\u0094\u009e\3\2\2\2\u0095\u0096")
        buf.write(u"\f\n\2\2\u0096\u0097\7a\2\2\u0097\u009e\7c\2\2\u0098")
        buf.write(u"\u0099\f\t\2\2\u0099\u009a\7`\2\2\u009a\u009e\7c\2\2")
        buf.write(u"\u009b\u009c\f\b\2\2\u009c\u009e\t\2\2\2\u009d\u0090")
        buf.write(u"\3\2\2\2\u009d\u0095\3\2\2\2\u009d\u0098\3\2\2\2\u009d")
        buf.write(u"\u009b\3\2\2\2\u009e\u00a1\3\2\2\2\u009f\u009d\3\2\2")
        buf.write(u"\2\u009f\u00a0\3\2\2\2\u00a0\3\3\2\2\2\u00a1\u009f\3")
        buf.write(u"\2\2\2\u00a2\u00a7\5\f\7\2\u00a3\u00a4\7R\2\2\u00a4\u00a6")
        buf.write(u"\5\f\7\2\u00a5\u00a3\3\2\2\2\u00a6\u00a9\3\2\2\2\u00a7")
        buf.write(u"\u00a5\3\2\2\2\u00a7\u00a8\3\2\2\2\u00a8\5\3\2\2\2\u00a9")
        buf.write(u"\u00a7\3\2\2\2\u00aa\u00b1\5\2\2\2\u00ab\u00ac\7\65\2")
        buf.write(u"\2\u00ac\u00ad\5D#\2\u00ad\u00ae\7\66\2\2\u00ae\u00af")
        buf.write(u"\5\6\4\2\u00af\u00b1\3\2\2\2\u00b0\u00aa\3\2\2\2\u00b0")
        buf.write(u"\u00ab\3\2\2\2\u00b1\7\3\2\2\2\u00b2\u00b3\b\5\1\2\u00b3")
        buf.write(u"\u00b4\5\6\4\2\u00b4\u00d5\3\2\2\2\u00b5\u00b6\f\f\2")
        buf.write(u"\2\u00b6\u00b7\t\4\2\2\u00b7\u00d4\5\b\5\r\u00b8\u00b9")
        buf.write(u"\f\13\2\2\u00b9\u00ba\t\5\2\2\u00ba\u00d4\5\b\5\f\u00bb")
        buf.write(u"\u00bc\f\n\2\2\u00bc\u00bd\t\6\2\2\u00bd\u00d4\5\b\5")
        buf.write(u"\13\u00be\u00bf\f\t\2\2\u00bf\u00c0\t\7\2\2\u00c0\u00d4")
        buf.write(u"\5\b\5\n\u00c1\u00c2\f\b\2\2\u00c2\u00c3\t\b\2\2\u00c3")
        buf.write(u"\u00d4\5\b\5\t\u00c4\u00c5\f\7\2\2\u00c5\u00c6\7H\2\2")
        buf.write(u"\u00c6\u00d4\5\b\5\b\u00c7\u00c8\f\6\2\2\u00c8\u00c9")
        buf.write(u"\7L\2\2\u00c9\u00d4\5\b\5\7\u00ca\u00cb\f\5\2\2\u00cb")
        buf.write(u"\u00cc\7I\2\2\u00cc\u00d4\5\b\5\6\u00cd\u00ce\f\4\2\2")
        buf.write(u"\u00ce\u00cf\7J\2\2\u00cf\u00d4\5\b\5\5\u00d0\u00d1\f")
        buf.write(u"\3\2\2\u00d1\u00d2\7K\2\2\u00d2\u00d4\5\b\5\4\u00d3\u00b5")
        buf.write(u"\3\2\2\2\u00d3\u00b8\3\2\2\2\u00d3\u00bb\3\2\2\2\u00d3")
        buf.write(u"\u00be\3\2\2\2\u00d3\u00c1\3\2\2\2\u00d3\u00c4\3\2\2")
        buf.write(u"\2\u00d3\u00c7\3\2\2\2\u00d3\u00ca\3\2\2\2\u00d3\u00cd")
        buf.write(u"\3\2\2\2\u00d3\u00d0\3\2\2\2\u00d4\u00d7\3\2\2\2\u00d5")
        buf.write(u"\u00d3\3\2\2\2\u00d5\u00d6\3\2\2\2\u00d6\t\3\2\2\2\u00d7")
        buf.write(u"\u00d5\3\2\2\2\u00d8\u00e0\5\b\5\2\u00d9\u00da\5\b\5")
        buf.write(u"\2\u00da\u00db\7O\2\2\u00db\u00dc\5\16\b\2\u00dc\u00dd")
        buf.write(u"\7P\2\2\u00dd\u00de\5\n\6\2\u00de\u00e0\3\2\2\2\u00df")
        buf.write(u"\u00d8\3\2\2\2\u00df\u00d9\3\2\2\2\u00e0\13\3\2\2\2\u00e1")
        buf.write(u"\u00e7\5\n\6\2\u00e2\u00e3\5\2\2\2\u00e3\u00e4\t\t\2")
        buf.write(u"\2\u00e4\u00e5\5\f\7\2\u00e5\u00e7\3\2\2\2\u00e6\u00e1")
        buf.write(u"\3\2\2\2\u00e6\u00e2\3\2\2\2\u00e7\r\3\2\2\2\u00e8\u00ed")
        buf.write(u"\5\f\7\2\u00e9\u00ea\7R\2\2\u00ea\u00ec\5\f\7\2\u00eb")
        buf.write(u"\u00e9\3\2\2\2\u00ec\u00ef\3\2\2\2\u00ed\u00eb\3\2\2")
        buf.write(u"\2\u00ed\u00ee\3\2\2\2\u00ee\17\3\2\2\2\u00ef\u00ed\3")
        buf.write(u"\2\2\2\u00f0\u00f1\5\n\6\2\u00f1\21\3\2\2\2\u00f2\u00f4")
        buf.write(u"\5\24\13\2\u00f3\u00f2\3\2\2\2\u00f4\u00f5\3\2\2\2\u00f5")
        buf.write(u"\u00f3\3\2\2\2\u00f5\u00f6\3\2\2\2\u00f6\u00f8\3\2\2")
        buf.write(u"\2\u00f7\u00f9\5\26\f\2\u00f8\u00f7\3\2\2\2\u00f8\u00f9")
        buf.write(u"\3\2\2\2\u00f9\u00fa\3\2\2\2\u00fa\u00fb\7Q\2\2\u00fb")
        buf.write(u"\u00fe\3\2\2\2\u00fc\u00fe\5T+\2\u00fd\u00f3\3\2\2\2")
        buf.write(u"\u00fd\u00fc\3\2\2\2\u00fe\23\3\2\2\2\u00ff\u0105\5\32")
        buf.write(u"\16\2\u0100\u0105\5\34\17\2\u0101\u0105\5\62\32\2\u0102")
        buf.write(u"\u0105\5\64\33\2\u0103\u0105\5\66\34\2\u0104\u00ff\3")
        buf.write(u"\2\2\2\u0104\u0100\3\2\2\2\u0104\u0101\3\2\2\2\u0104")
        buf.write(u"\u0102\3\2\2\2\u0104\u0103\3\2\2\2\u0105\25\3\2\2\2\u0106")
        buf.write(u"\u010b\5\30\r\2\u0107\u0108\7R\2\2\u0108\u010a\5\30\r")
        buf.write(u"\2\u0109\u0107\3\2\2\2\u010a\u010d\3\2\2\2\u010b\u0109")
        buf.write(u"\3\2\2\2\u010b\u010c\3\2\2\2\u010c\27\3\2\2\2\u010d\u010b")
        buf.write(u"\3\2\2\2\u010e\u0114\58\35\2\u010f\u0110\58\35\2\u0110")
        buf.write(u"\u0111\7S\2\2\u0111\u0112\5L\'\2\u0112\u0114\3\2\2\2")
        buf.write(u"\u0113\u010e\3\2\2\2\u0113\u010f\3\2\2\2\u0114\31\3\2")
        buf.write(u"\2\2\u0115\u0116\t\n\2\2\u0116\33\3\2\2\2\u0117\u0121")
        buf.write(u"\t\13\2\2\u0118\u0119\7\6\2\2\u0119\u011a\7\65\2\2\u011a")
        buf.write(u"\u011b\t\f\2\2\u011b\u0121\7\66\2\2\u011c\u0121\5\60")
        buf.write(u"\31\2\u011d\u0121\5\36\20\2\u011e\u0121\5*\26\2\u011f")
        buf.write(u"\u0121\5J&\2\u0120\u0117\3\2\2\2\u0120\u0118\3\2\2\2")
        buf.write(u"\u0120\u011c\3\2\2\2\u0120\u011d\3\2\2\2\u0120\u011e")
        buf.write(u"\3\2\2\2\u0120\u011f\3\2\2\2\u0121\35\3\2\2\2\u0122\u0124")
        buf.write(u"\5 \21\2\u0123\u0125\7c\2\2\u0124\u0123\3\2\2\2\u0124")
        buf.write(u"\u0125\3\2\2\2\u0125\u0126\3\2\2\2\u0126\u0128\79\2\2")
        buf.write(u"\u0127\u0129\5\"\22\2\u0128\u0127\3\2\2\2\u0129\u012a")
        buf.write(u"\3\2\2\2\u012a\u0128\3\2\2\2\u012a\u012b\3\2\2\2\u012b")
        buf.write(u"\u012c\3\2\2\2\u012c\u012d\7:\2\2\u012d\u0132\3\2\2\2")
        buf.write(u"\u012e\u012f\5 \21\2\u012f\u0130\7c\2\2\u0130\u0132\3")
        buf.write(u"\2\2\2\u0131\u0122\3\2\2\2\u0131\u012e\3\2\2\2\u0132")
        buf.write(u"\37\3\2\2\2\u0133\u0134\t\r\2\2\u0134!\3\2\2\2\u0135")
        buf.write(u"\u0137\5$\23\2\u0136\u0138\5&\24\2\u0137\u0136\3\2\2")
        buf.write(u"\2\u0137\u0138\3\2\2\2\u0138\u0139\3\2\2\2\u0139\u013a")
        buf.write(u"\7Q\2\2\u013a\u013d\3\2\2\2\u013b\u013d\5T+\2\u013c\u0135")
        buf.write(u"\3\2\2\2\u013c\u013b\3\2\2\2\u013d#\3\2\2\2\u013e\u0140")
        buf.write(u"\5\34\17\2\u013f\u0141\5$\23\2\u0140\u013f\3\2\2\2\u0140")
        buf.write(u"\u0141\3\2\2\2\u0141\u0147\3\2\2\2\u0142\u0144\5\62\32")
        buf.write(u"\2\u0143\u0145\5$\23\2\u0144\u0143\3\2\2\2\u0144\u0145")
        buf.write(u"\3\2\2\2\u0145\u0147\3\2\2\2\u0146\u013e\3\2\2\2\u0146")
        buf.write(u"\u0142\3\2\2\2\u0147%\3\2\2\2\u0148\u014d\5(\25\2\u0149")
        buf.write(u"\u014a\7R\2\2\u014a\u014c\5(\25\2\u014b\u0149\3\2\2\2")
        buf.write(u"\u014c\u014f\3\2\2\2\u014d\u014b\3\2\2\2\u014d\u014e")
        buf.write(u"\3\2\2\2\u014e\'\3\2\2\2\u014f\u014d\3\2\2\2\u0150\u0157")
        buf.write(u"\58\35\2\u0151\u0153\58\35\2\u0152\u0151\3\2\2\2\u0152")
        buf.write(u"\u0153\3\2\2\2\u0153\u0154\3\2\2\2\u0154\u0155\7P\2\2")
        buf.write(u"\u0155\u0157\5\20\t\2\u0156\u0150\3\2\2\2\u0156\u0152")
        buf.write(u"\3\2\2\2\u0157)\3\2\2\2\u0158\u015a\7\23\2\2\u0159\u015b")
        buf.write(u"\7c\2\2\u015a\u0159\3\2\2\2\u015a\u015b\3\2\2\2\u015b")
        buf.write(u"\u015c\3\2\2\2\u015c\u015d\79\2\2\u015d\u015e\5,\27\2")
        buf.write(u"\u015e\u015f\7:\2\2\u015f\u016c\3\2\2\2\u0160\u0162\7")
        buf.write(u"\23\2\2\u0161\u0163\7c\2\2\u0162\u0161\3\2\2\2\u0162")
        buf.write(u"\u0163\3\2\2\2\u0163\u0164\3\2\2\2\u0164\u0165\79\2\2")
        buf.write(u"\u0165\u0166\5,\27\2\u0166\u0167\7R\2\2\u0167\u0168\7")
        buf.write(u":\2\2\u0168\u016c\3\2\2\2\u0169\u016a\7\23\2\2\u016a")
        buf.write(u"\u016c\7c\2\2\u016b\u0158\3\2\2\2\u016b\u0160\3\2\2\2")
        buf.write(u"\u016b\u0169\3\2\2\2\u016c+\3\2\2\2\u016d\u0172\5.\30")
        buf.write(u"\2\u016e\u016f\7R\2\2\u016f\u0171\5.\30\2\u0170\u016e")
        buf.write(u"\3\2\2\2\u0171\u0174\3\2\2\2\u0172\u0170\3\2\2\2\u0172")
        buf.write(u"\u0173\3\2\2\2\u0173-\3\2\2\2\u0174\u0172\3\2\2\2\u0175")
        buf.write(u"\u0178\7c\2\2\u0176\u0177\7S\2\2\u0177\u0179\5\20\t\2")
        buf.write(u"\u0178\u0176\3\2\2\2\u0178\u0179\3\2\2\2\u0179/\3\2\2")
        buf.write(u"\2\u017a\u017b\7-\2\2\u017b\u017c\7\65\2\2\u017c\u017d")
        buf.write(u"\5D#\2\u017d\u017e\7\66\2\2\u017e\61\3\2\2\2\u017f\u0180")
        buf.write(u"\t\16\2\2\u0180\63\3\2\2\2\u0181\u0187\t\17\2\2\u0182")
        buf.write(u"\u0183\7\b\2\2\u0183\u0184\7\65\2\2\u0184\u0185\7c\2")
        buf.write(u"\2\u0185\u0187\7\66\2\2\u0186\u0181\3\2\2\2\u0186\u0182")
        buf.write(u"\3\2\2\2\u0187\65\3\2\2\2\u0188\u0189\7+\2\2\u0189\u018a")
        buf.write(u"\7\65\2\2\u018a\u018b\5D#\2\u018b\u018c\7\66\2\2\u018c")
        buf.write(u"\u0193\3\2\2\2\u018d\u018e\7+\2\2\u018e\u018f\7\65\2")
        buf.write(u"\2\u018f\u0190\5\20\t\2\u0190\u0191\7\66\2\2\u0191\u0193")
        buf.write(u"\3\2\2\2\u0192\u0188\3\2\2\2\u0192\u018d\3\2\2\2\u0193")
        buf.write(u"\67\3\2\2\2\u0194\u0196\5<\37\2\u0195\u0194\3\2\2\2\u0195")
        buf.write(u"\u0196\3\2\2\2\u0196\u0197\3\2\2\2\u0197\u0198\5:\36")
        buf.write(u"\2\u01989\3\2\2\2\u0199\u019a\b\36\1\2\u019a\u01a0\7")
        buf.write(u"c\2\2\u019b\u019c\7\65\2\2\u019c\u019d\58\35\2\u019d")
        buf.write(u"\u019e\7\66\2\2\u019e\u01a0\3\2\2\2\u019f\u0199\3\2\2")
        buf.write(u"\2\u019f\u019b\3\2\2\2\u01a0\u01db\3\2\2\2\u01a1\u01a2")
        buf.write(u"\f\b\2\2\u01a2\u01a6\7\67\2\2\u01a3\u01a5\5\62\32\2\u01a4")
        buf.write(u"\u01a3\3\2\2\2\u01a5\u01a8\3\2\2\2\u01a6\u01a4\3\2\2")
        buf.write(u"\2\u01a6\u01a7\3\2\2\2\u01a7\u01aa\3\2\2\2\u01a8\u01a6")
        buf.write(u"\3\2\2\2\u01a9\u01ab\5\f\7\2\u01aa\u01a9\3\2\2\2\u01aa")
        buf.write(u"\u01ab\3\2\2\2\u01ab\u01ac\3\2\2\2\u01ac\u01da\78\2\2")
        buf.write(u"\u01ad\u01ae\f\7\2\2\u01ae\u01af\7\67\2\2\u01af\u01b3")
        buf.write(u"\7\"\2\2\u01b0\u01b2\5\62\32\2\u01b1\u01b0\3\2\2\2\u01b2")
        buf.write(u"\u01b5\3\2\2\2\u01b3\u01b1\3\2\2\2\u01b3\u01b4\3\2\2")
        buf.write(u"\2\u01b4\u01b6\3\2\2\2\u01b5\u01b3\3\2\2\2\u01b6\u01b7")
        buf.write(u"\5\f\7\2\u01b7\u01b8\78\2\2\u01b8\u01da\3\2\2\2\u01b9")
        buf.write(u"\u01ba\f\6\2\2\u01ba\u01bc\7\67\2\2\u01bb\u01bd\5\62")
        buf.write(u"\32\2\u01bc\u01bb\3\2\2\2\u01bd\u01be\3\2\2\2\u01be\u01bc")
        buf.write(u"\3\2\2\2\u01be\u01bf\3\2\2\2\u01bf\u01c0\3\2\2\2\u01c0")
        buf.write(u"\u01c1\7\"\2\2\u01c1\u01c2\5\f\7\2\u01c2\u01c3\78\2\2")
        buf.write(u"\u01c3\u01da\3\2\2\2\u01c4\u01c5\f\5\2\2\u01c5\u01c9")
        buf.write(u"\7\67\2\2\u01c6\u01c8\5\62\32\2\u01c7\u01c6\3\2\2\2\u01c8")
        buf.write(u"\u01cb\3\2\2\2\u01c9\u01c7\3\2\2\2\u01c9\u01ca\3\2\2")
        buf.write(u"\2\u01ca\u01cc\3\2\2\2\u01cb\u01c9\3\2\2\2\u01cc\u01cd")
        buf.write(u"\7E\2\2\u01cd\u01da\78\2\2\u01ce\u01cf\f\4\2\2\u01cf")
        buf.write(u"\u01d0\7\65\2\2\u01d0\u01d1\5> \2\u01d1\u01d2\7\66\2")
        buf.write(u"\2\u01d2\u01da\3\2\2\2\u01d3\u01d4\f\3\2\2\u01d4\u01d6")
        buf.write(u"\7\65\2\2\u01d5\u01d7\5B\"\2\u01d6\u01d5\3\2\2\2\u01d6")
        buf.write(u"\u01d7\3\2\2\2\u01d7\u01d8\3\2\2\2\u01d8\u01da\7\66\2")
        buf.write(u"\2\u01d9\u01a1\3\2\2\2\u01d9\u01ad\3\2\2\2\u01d9\u01b9")
        buf.write(u"\3\2\2\2\u01d9\u01c4\3\2\2\2\u01d9\u01ce\3\2\2\2\u01d9")
        buf.write(u"\u01d3\3\2\2\2\u01da\u01dd\3\2\2\2\u01db\u01d9\3\2\2")
        buf.write(u"\2\u01db\u01dc\3\2\2\2\u01dc;\3\2\2\2\u01dd\u01db\3\2")
        buf.write(u"\2\2\u01de\u01e2\7E\2\2\u01df\u01e1\5\62\32\2\u01e0\u01df")
        buf.write(u"\3\2\2\2\u01e1\u01e4\3\2\2\2\u01e2\u01e0\3\2\2\2\u01e2")
        buf.write(u"\u01e3\3\2\2\2\u01e3\u01e6\3\2\2\2\u01e4\u01e2\3\2\2")
        buf.write(u"\2\u01e5\u01e7\5<\37\2\u01e6\u01e5\3\2\2\2\u01e6\u01e7")
        buf.write(u"\3\2\2\2\u01e7=\3\2\2\2\u01e8\u01ed\5@!\2\u01e9\u01ea")
        buf.write(u"\7R\2\2\u01ea\u01ec\5@!\2\u01eb\u01e9\3\2\2\2\u01ec\u01ef")
        buf.write(u"\3\2\2\2\u01ed\u01eb\3\2\2\2\u01ed\u01ee\3\2\2\2\u01ee")
        buf.write(u"\u01f2\3\2\2\2\u01ef\u01ed\3\2\2\2\u01f0\u01f1\7R\2\2")
        buf.write(u"\u01f1\u01f3\7b\2\2\u01f2\u01f0\3\2\2\2\u01f2\u01f3\3")
        buf.write(u"\2\2\2\u01f3?\3\2\2\2\u01f4\u01f6\5\24\13\2\u01f5\u01f4")
        buf.write(u"\3\2\2\2\u01f6\u01f7\3\2\2\2\u01f7\u01f5\3\2\2\2\u01f7")
        buf.write(u"\u01f8\3\2\2\2\u01f8\u01f9\3\2\2\2\u01f9\u01fa\58\35")
        buf.write(u"\2\u01fa\u0204\3\2\2\2\u01fb\u01fd\5\24\13\2\u01fc\u01fb")
        buf.write(u"\3\2\2\2\u01fd\u01fe\3\2\2\2\u01fe\u01fc\3\2\2\2\u01fe")
        buf.write(u"\u01ff\3\2\2\2\u01ff\u0201\3\2\2\2\u0200\u0202\5F$\2")
        buf.write(u"\u0201\u0200\3\2\2\2\u0201\u0202\3\2\2\2\u0202\u0204")
        buf.write(u"\3\2\2\2\u0203\u01f5\3\2\2\2\u0203\u01fc\3\2\2\2\u0204")
        buf.write(u"A\3\2\2\2\u0205\u020a\7c\2\2\u0206\u0207\7R\2\2\u0207")
        buf.write(u"\u0209\7c\2\2\u0208\u0206\3\2\2\2\u0209\u020c\3\2\2\2")
        buf.write(u"\u020a\u0208\3\2\2\2\u020a\u020b\3\2\2\2\u020bC\3\2\2")
        buf.write(u"\2\u020c\u020a\3\2\2\2\u020d\u020f\5$\23\2\u020e\u0210")
        buf.write(u"\5F$\2\u020f\u020e\3\2\2\2\u020f\u0210\3\2\2\2\u0210")
        buf.write(u"E\3\2\2\2\u0211\u0217\5<\37\2\u0212\u0214\5<\37\2\u0213")
        buf.write(u"\u0212\3\2\2\2\u0213\u0214\3\2\2\2\u0214\u0215\3\2\2")
        buf.write(u"\2\u0215\u0217\5H%\2\u0216\u0211\3\2\2\2\u0216\u0213")
        buf.write(u"\3\2\2\2\u0217G\3\2\2\2\u0218\u0219\b%\1\2\u0219\u021a")
        buf.write(u"\7\65\2\2\u021a\u021b\5F$\2\u021b\u021c\7\66\2\2\u021c")
        buf.write(u"\u0247\3\2\2\2\u021d\u0221\7\67\2\2\u021e\u0220\5\62")
        buf.write(u"\32\2\u021f\u021e\3\2\2\2\u0220\u0223\3\2\2\2\u0221\u021f")
        buf.write(u"\3\2\2\2\u0221\u0222\3\2\2\2\u0222\u0225\3\2\2\2\u0223")
        buf.write(u"\u0221\3\2\2\2\u0224\u0226\5\f\7\2\u0225\u0224\3\2\2")
        buf.write(u"\2\u0225\u0226\3\2\2\2\u0226\u0227\3\2\2\2\u0227\u0247")
        buf.write(u"\78\2\2\u0228\u0229\7\67\2\2\u0229\u022d\7\"\2\2\u022a")
        buf.write(u"\u022c\5\62\32\2\u022b\u022a\3\2\2\2\u022c\u022f\3\2")
        buf.write(u"\2\2\u022d\u022b\3\2\2\2\u022d\u022e\3\2\2\2\u022e\u0230")
        buf.write(u"\3\2\2\2\u022f\u022d\3\2\2\2\u0230\u0231\5\f\7\2\u0231")
        buf.write(u"\u0232\78\2\2\u0232\u0247\3\2\2\2\u0233\u0237\7\67\2")
        buf.write(u"\2\u0234\u0236\5\62\32\2\u0235\u0234\3\2\2\2\u0236\u0239")
        buf.write(u"\3\2\2\2\u0237\u0235\3\2\2\2\u0237\u0238\3\2\2\2\u0238")
        buf.write(u"\u023a\3\2\2\2\u0239\u0237\3\2\2\2\u023a\u023b\7\"\2")
        buf.write(u"\2\u023b\u023c\5\f\7\2\u023c\u023d\78\2\2\u023d\u0247")
        buf.write(u"\3\2\2\2\u023e\u023f\7\67\2\2\u023f\u0240\7E\2\2\u0240")
        buf.write(u"\u0247\78\2\2\u0241\u0243\7\65\2\2\u0242\u0244\5> \2")
        buf.write(u"\u0243\u0242\3\2\2\2\u0243\u0244\3\2\2\2\u0244\u0245")
        buf.write(u"\3\2\2\2\u0245\u0247\7\66\2\2\u0246\u0218\3\2\2\2\u0246")
        buf.write(u"\u021d\3\2\2\2\u0246\u0228\3\2\2\2\u0246\u0233\3\2\2")
        buf.write(u"\2\u0246\u023e\3\2\2\2\u0246\u0241\3\2\2\2\u0247\u0277")
        buf.write(u"\3\2\2\2\u0248\u0249\f\7\2\2\u0249\u024d\7\67\2\2\u024a")
        buf.write(u"\u024c\5\62\32\2\u024b\u024a\3\2\2\2\u024c\u024f\3\2")
        buf.write(u"\2\2\u024d\u024b\3\2\2\2\u024d\u024e\3\2\2\2\u024e\u0251")
        buf.write(u"\3\2\2\2\u024f\u024d\3\2\2\2\u0250\u0252\5\f\7\2\u0251")
        buf.write(u"\u0250\3\2\2\2\u0251\u0252\3\2\2\2\u0252\u0253\3\2\2")
        buf.write(u"\2\u0253\u0276\78\2\2\u0254\u0255\f\6\2\2\u0255\u0256")
        buf.write(u"\7\67\2\2\u0256\u025a\7\"\2\2\u0257\u0259\5\62\32\2\u0258")
        buf.write(u"\u0257\3\2\2\2\u0259\u025c\3\2\2\2\u025a\u0258\3\2\2")
        buf.write(u"\2\u025a\u025b\3\2\2\2\u025b\u025d\3\2\2\2\u025c\u025a")
        buf.write(u"\3\2\2\2\u025d\u025e\5\f\7\2\u025e\u025f\78\2\2\u025f")
        buf.write(u"\u0276\3\2\2\2\u0260\u0261\f\5\2\2\u0261\u0263\7\67\2")
        buf.write(u"\2\u0262\u0264\5\62\32\2\u0263\u0262\3\2\2\2\u0264\u0265")
        buf.write(u"\3\2\2\2\u0265\u0263\3\2\2\2\u0265\u0266\3\2\2\2\u0266")
        buf.write(u"\u0267\3\2\2\2\u0267\u0268\7\"\2\2\u0268\u0269\5\f\7")
        buf.write(u"\2\u0269\u026a\78\2\2\u026a\u0276\3\2\2\2\u026b\u026c")
        buf.write(u"\f\4\2\2\u026c\u026d\7\67\2\2\u026d\u026e\7E\2\2\u026e")
        buf.write(u"\u0276\78\2\2\u026f\u0270\f\3\2\2\u0270\u0272\7\65\2")
        buf.write(u"\2\u0271\u0273\5> \2\u0272\u0271\3\2\2\2\u0272\u0273")
        buf.write(u"\3\2\2\2\u0273\u0274\3\2\2\2\u0274\u0276\7\66\2\2\u0275")
        buf.write(u"\u0248\3\2\2\2\u0275\u0254\3\2\2\2\u0275\u0260\3\2\2")
        buf.write(u"\2\u0275\u026b\3\2\2\2\u0275\u026f\3\2\2\2\u0276\u0279")
        buf.write(u"\3\2\2\2\u0277\u0275\3\2\2\2\u0277\u0278\3\2\2\2\u0278")
        buf.write(u"I\3\2\2\2\u0279\u0277\3\2\2\2\u027a\u027b\7c\2\2\u027b")
        buf.write(u"K\3\2\2\2\u027c\u0285\5\f\7\2\u027d\u027e\79\2\2\u027e")
        buf.write(u"\u0280\5N(\2\u027f\u0281\7R\2\2\u0280\u027f\3\2\2\2\u0280")
        buf.write(u"\u0281\3\2\2\2\u0281\u0282\3\2\2\2\u0282\u0283\7:\2\2")
        buf.write(u"\u0283\u0285\3\2\2\2\u0284\u027c\3\2\2\2\u0284\u027d")
        buf.write(u"\3\2\2\2\u0285M\3\2\2\2\u0286\u0288\b(\1\2\u0287\u0289")
        buf.write(u"\5P)\2\u0288\u0287\3\2\2\2\u0288\u0289\3\2\2\2\u0289")
        buf.write(u"\u028a\3\2\2\2\u028a\u028b\5L\'\2\u028b\u0294\3\2\2\2")
        buf.write(u"\u028c\u028d\f\3\2\2\u028d\u028f\7R\2\2\u028e\u0290\5")
        buf.write(u"P)\2\u028f\u028e\3\2\2\2\u028f\u0290\3\2\2\2\u0290\u0291")
        buf.write(u"\3\2\2\2\u0291\u0293\5L\'\2\u0292\u028c\3\2\2\2\u0293")
        buf.write(u"\u0296\3\2\2\2\u0294\u0292\3\2\2\2\u0294\u0295\3\2\2")
        buf.write(u"\2\u0295O\3\2\2\2\u0296\u0294\3\2\2\2\u0297\u0299\5R")
        buf.write(u"*\2\u0298\u0297\3\2\2\2\u0299\u029a\3\2\2\2\u029a\u0298")
        buf.write(u"\3\2\2\2\u029a\u029b\3\2\2\2\u029b\u029c\3\2\2\2\u029c")
        buf.write(u"\u029d\7S\2\2\u029dQ\3\2\2\2\u029e\u029f\7\67\2\2\u029f")
        buf.write(u"\u02a0\5\20\t\2\u02a0\u02a1\78\2\2\u02a1\u02a5\3\2\2")
        buf.write(u"\2\u02a2\u02a3\7a\2\2\u02a3\u02a5\7c\2\2\u02a4\u029e")
        buf.write(u"\3\2\2\2\u02a4\u02a2\3\2\2\2\u02a5S\3\2\2\2\u02a6\u02a7")
        buf.write(u"\7\63\2\2\u02a7\u02a8\7\65\2\2\u02a8\u02a9\5\20\t\2\u02a9")
        buf.write(u"\u02ab\7R\2\2\u02aa\u02ac\7e\2\2\u02ab\u02aa\3\2\2\2")
        buf.write(u"\u02ac\u02ad\3\2\2\2\u02ad\u02ab\3\2\2\2\u02ad\u02ae")
        buf.write(u"\3\2\2\2\u02ae\u02af\3\2\2\2\u02af\u02b0\7\66\2\2\u02b0")
        buf.write(u"\u02b1\7Q\2\2\u02b1U\3\2\2\2\u02b2\u02b9\5X-\2\u02b3")
        buf.write(u"\u02b9\5Z.\2\u02b4\u02b9\5^\60\2\u02b5\u02b9\5`\61\2")
        buf.write(u"\u02b6\u02b9\5b\62\2\u02b7\u02b9\5d\63\2\u02b8\u02b2")
        buf.write(u"\3\2\2\2\u02b8\u02b3\3\2\2\2\u02b8\u02b4\3\2\2\2\u02b8")
        buf.write(u"\u02b5\3\2\2\2\u02b8\u02b6\3\2\2\2\u02b8\u02b7\3\2\2")
        buf.write(u"\2\u02b9W\3\2\2\2\u02ba\u02bb\7c\2\2\u02bb\u02bc\7P\2")
        buf.write(u"\2\u02bc\u02c6\5V,\2\u02bd\u02be\7\13\2\2\u02be\u02bf")
        buf.write(u"\5\20\t\2\u02bf\u02c0\7P\2\2\u02c0\u02c1\5V,\2\u02c1")
        buf.write(u"\u02c6\3\2\2\2\u02c2\u02c3\7\17\2\2\u02c3\u02c4\7P\2")
        buf.write(u"\2\u02c4\u02c6\5V,\2\u02c5\u02ba\3\2\2\2\u02c5\u02bd")
        buf.write(u"\3\2\2\2\u02c5\u02c2\3\2\2\2\u02c6Y\3\2\2\2\u02c7\u02cb")
        buf.write(u"\79\2\2\u02c8\u02ca\5\\/\2\u02c9\u02c8\3\2\2\2\u02ca")
        buf.write(u"\u02cd\3\2\2\2\u02cb\u02c9\3\2\2\2\u02cb\u02cc\3\2\2")
        buf.write(u"\2\u02cc\u02ce\3\2\2\2\u02cd\u02cb\3\2\2\2\u02ce\u02cf")
        buf.write(u"\7:\2\2\u02cf[\3\2\2\2\u02d0\u02d3\5\22\n\2\u02d1\u02d3")
        buf.write(u"\5V,\2\u02d2\u02d0\3\2\2\2\u02d2\u02d1\3\2\2\2\u02d3")
        buf.write(u"]\3\2\2\2\u02d4\u02d6\5\16\b\2\u02d5\u02d4\3\2\2\2\u02d5")
        buf.write(u"\u02d6\3\2\2\2\u02d6\u02d7\3\2\2\2\u02d7\u02d8\7Q\2\2")
        buf.write(u"\u02d8_\3\2\2\2\u02d9\u02da\7\30\2\2\u02da\u02db\7\65")
        buf.write(u"\2\2\u02db\u02dc\5\16\b\2\u02dc\u02dd\7\66\2\2\u02dd")
        buf.write(u"\u02e0\5V,\2\u02de\u02df\7\22\2\2\u02df\u02e1\5V,\2\u02e0")
        buf.write(u"\u02de\3\2\2\2\u02e0\u02e1\3\2\2\2\u02e1\u02e9\3\2\2")
        buf.write(u"\2\u02e2\u02e3\7$\2\2\u02e3\u02e4\7\65\2\2\u02e4\u02e5")
        buf.write(u"\5\16\b\2\u02e5\u02e6\7\66\2\2\u02e6\u02e7\5V,\2\u02e7")
        buf.write(u"\u02e9\3\2\2\2\u02e8\u02d9\3\2\2\2\u02e8\u02e2\3\2\2")
        buf.write(u"\2\u02e9a\3\2\2\2\u02ea\u02eb\7*\2\2\u02eb\u02ec\7\65")
        buf.write(u"\2\2\u02ec\u02ed\5\16\b\2\u02ed\u02ee\7\66\2\2\u02ee")
        buf.write(u"\u02ef\5V,\2\u02ef\u0315\3\2\2\2\u02f0\u02f1\7\20\2\2")
        buf.write(u"\u02f1\u02f2\5V,\2\u02f2\u02f3\7*\2\2\u02f3\u02f4\7\65")
        buf.write(u"\2\2\u02f4\u02f5\5\16\b\2\u02f5\u02f6\7\66\2\2\u02f6")
        buf.write(u"\u02f7\7Q\2\2\u02f7\u0315\3\2\2\2\u02f8\u02f9\7\26\2")
        buf.write(u"\2\u02f9\u02fb\7\65\2\2\u02fa\u02fc\5\16\b\2\u02fb\u02fa")
        buf.write(u"\3\2\2\2\u02fb\u02fc\3\2\2\2\u02fc\u02fd\3\2\2\2\u02fd")
        buf.write(u"\u02ff\7Q\2\2\u02fe\u0300\5\16\b\2\u02ff\u02fe\3\2\2")
        buf.write(u"\2\u02ff\u0300\3\2\2\2\u0300\u0301\3\2\2\2\u0301\u0303")
        buf.write(u"\7Q\2\2\u0302\u0304\5\16\b\2\u0303\u0302\3\2\2\2\u0303")
        buf.write(u"\u0304\3\2\2\2\u0304\u0305\3\2\2\2\u0305\u0306\7\66\2")
        buf.write(u"\2\u0306\u0315\5V,\2\u0307\u0308\7\26\2\2\u0308\u0309")
        buf.write(u"\7\65\2\2\u0309\u030b\5\22\n\2\u030a\u030c\5\16\b\2\u030b")
        buf.write(u"\u030a\3\2\2\2\u030b\u030c\3\2\2\2\u030c\u030d\3\2\2")
        buf.write(u"\2\u030d\u030f\7Q\2\2\u030e\u0310\5\16\b\2\u030f\u030e")
        buf.write(u"\3\2\2\2\u030f\u0310\3\2\2\2\u0310\u0311\3\2\2\2\u0311")
        buf.write(u"\u0312\7\66\2\2\u0312\u0313\5V,\2\u0313\u0315\3\2\2\2")
        buf.write(u"\u0314\u02ea\3\2\2\2\u0314\u02f0\3\2\2\2\u0314\u02f8")
        buf.write(u"\3\2\2\2\u0314\u0307\3\2\2\2\u0315c\3\2\2\2\u0316\u0317")
        buf.write(u"\7\27\2\2\u0317\u0318\7c\2\2\u0318\u0323\7Q\2\2\u0319")
        buf.write(u"\u031a\7\16\2\2\u031a\u0323\7Q\2\2\u031b\u031c\7\n\2")
        buf.write(u"\2\u031c\u0323\7Q\2\2\u031d\u031f\7\36\2\2\u031e\u0320")
        buf.write(u"\5\16\b\2\u031f\u031e\3\2\2\2\u031f\u0320\3\2\2\2\u0320")
        buf.write(u"\u0321\3\2\2\2\u0321\u0323\7Q\2\2\u0322\u0316\3\2\2\2")
        buf.write(u"\u0322\u0319\3\2\2\2\u0322\u031b\3\2\2\2\u0322\u031d")
        buf.write(u"\3\2\2\2\u0323e\3\2\2\2\u0324\u0326\5h\65\2\u0325\u0324")
        buf.write(u"\3\2\2\2\u0326\u0329\3\2\2\2\u0327\u0325\3\2\2\2\u0327")
        buf.write(u"\u0328\3\2\2\2\u0328\u032a\3\2\2\2\u0329\u0327\3\2\2")
        buf.write(u"\2\u032a\u032b\7\2\2\3\u032bg\3\2\2\2\u032c\u0330\5j")
        buf.write(u"\66\2\u032d\u0330\5\22\n\2\u032e\u0330\7Q\2\2\u032f\u032c")
        buf.write(u"\3\2\2\2\u032f\u032d\3\2\2\2\u032f\u032e\3\2\2\2\u0330")
        buf.write(u"i\3\2\2\2\u0331\u0333\5\24\13\2\u0332\u0331\3\2\2\2\u0333")
        buf.write(u"\u0336\3\2\2\2\u0334\u0332\3\2\2\2\u0334\u0335\3\2\2")
        buf.write(u"\2\u0335\u0337\3\2\2\2\u0336\u0334\3\2\2\2\u0337\u033b")
        buf.write(u"\58\35\2\u0338\u033a\5\22\n\2\u0339\u0338\3\2\2\2\u033a")
        buf.write(u"\u033d\3\2\2\2\u033b\u0339\3\2\2\2\u033b\u033c\3\2\2")
        buf.write(u"\2\u033c\u033e\3\2\2\2\u033d\u033b\3\2\2\2\u033e\u033f")
        buf.write(u"\5Z.\2\u033fk\3\2\2\2ev\177\u008e\u009d\u009f\u00a7\u00b0")
        buf.write(u"\u00d3\u00d5\u00df\u00e6\u00ed\u00f5\u00f8\u00fd\u0104")
        buf.write(u"\u010b\u0113\u0120\u0124\u012a\u0131\u0137\u013c\u0140")
        buf.write(u"\u0144\u0146\u014d\u0152\u0156\u015a\u0162\u016b\u0172")
        buf.write(u"\u0178\u0186\u0192\u0195\u019f\u01a6\u01aa\u01b3\u01be")
        buf.write(u"\u01c9\u01d6\u01d9\u01db\u01e2\u01e6\u01ed\u01f2\u01f7")
        buf.write(u"\u01fe\u0201\u0203\u020a\u020f\u0213\u0216\u0221\u0225")
        buf.write(u"\u022d\u0237\u0243\u0246\u024d\u0251\u025a\u0265\u0272")
        buf.write(u"\u0275\u0277\u0280\u0284\u0288\u028f\u0294\u029a\u02a4")
        buf.write(u"\u02ad\u02b8\u02c5\u02cb\u02d2\u02d5\u02e0\u02e8\u02fb")
        buf.write(u"\u02ff\u0303\u030b\u030f\u0314\u031f\u0322\u0327\u032f")
        buf.write(u"\u0334\u033b")
        return buf.getvalue()


class CParser ( Parser ):

    grammarFileName = "java-escape"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ u"<INVALID>", u"'__m128'", u"'__m128d'", u"'__m128i'", 
                     u"'__extension__'", u"'__stdcall'", u"'__declspec'", 
                     u"'auto'", u"'break'", u"'case'", u"'char'", u"'const'", 
                     u"'continue'", u"'default'", u"'do'", u"'double'", 
                     u"'else'", u"'enum'", u"'extern'", u"'float'", u"'for'", 
                     u"'goto'", u"'if'", u"'inline'", u"'int'", u"'long'", 
                     u"'register'", u"'restrict'", u"'return'", u"'short'", 
                     u"'signed'", u"'sizeof'", u"'static'", u"'struct'", 
                     u"'switch'", u"'typedef'", u"'union'", u"'unsigned'", 
                     u"'void'", u"'volatile'", u"'while'", u"'_Alignas'", 
                     u"'_Alignof'", u"'_Atomic'", u"'_Bool'", u"'_Complex'", 
                     u"'_Generic'", u"'_Imaginary'", u"'_Noreturn'", u"'_Static_assert'", 
                     u"'_Thread_local'", u"'('", u"')'", u"'['", u"']'", 
                     u"'{'", u"'}'", u"'<'", u"'<='", u"'>'", u"'>='", u"'<<'", 
                     u"'>>'", u"'+'", u"'++'", u"'-'", u"'--'", u"'*'", 
                     u"'/'", u"'%'", u"'&'", u"'|'", u"'&&'", u"'||'", u"'^'", 
                     u"'!'", u"'~'", u"'?'", u"':'", u"';'", u"','", u"'='", 
                     u"'*='", u"'/='", u"'%='", u"'+='", u"'-='", u"'<<='", 
                     u"'>>='", u"'&='", u"'^='", u"'|='", u"'=='", u"'!='", 
                     u"'->'", u"'.'", u"'...'" ]

    symbolicNames = [ u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"<INVALID>", u"Auto", 
                      u"Break", u"Case", u"Char", u"Const", u"Continue", 
                      u"Default", u"Do", u"Double", u"Else", u"Enum", u"Extern", 
                      u"Float", u"For", u"Goto", u"If", u"Inline", u"Int", 
                      u"Long", u"Register", u"Restrict", u"Return", u"Short", 
                      u"Signed", u"Sizeof", u"Static", u"Struct", u"Switch", 
                      u"Typedef", u"Union", u"Unsigned", u"Void", u"Volatile", 
                      u"While", u"Alignas", u"Alignof", u"Atomic", u"Bool", 
                      u"Complex", u"Generic", u"Imaginary", u"Noreturn", 
                      u"StaticAssert", u"ThreadLocal", u"LeftParen", u"RightParen", 
                      u"LeftBracket", u"RightBracket", u"LeftBrace", u"RightBrace", 
                      u"Less", u"LessEqual", u"Greater", u"GreaterEqual", 
                      u"LeftShift", u"RightShift", u"Plus", u"PlusPlus", 
                      u"Minus", u"MinusMinus", u"Star", u"Div", u"Mod", 
                      u"And", u"Or", u"AndAnd", u"OrOr", u"Caret", u"Not", 
                      u"Tilde", u"Question", u"Colon", u"Semi", u"Comma", 
                      u"Assign", u"StarAssign", u"DivAssign", u"ModAssign", 
                      u"PlusAssign", u"MinusAssign", u"LeftShiftAssign", 
                      u"RightShiftAssign", u"AndAssign", u"XorAssign", u"OrAssign", 
                      u"Equal", u"NotEqual", u"Arrow", u"Dot", u"Ellipsis", 
                      u"Identifier", u"Constant", u"StringLiteral", u"LineDirective", 
                      u"PragmaDirective", u"Whitespace", u"Newline", u"BlockComment", 
                      u"LineComment" ]

    RULE_unaryExpression = 0
    RULE_argumentExpressionList = 1
    RULE_castExpression = 2
    RULE_logicalOrExpression = 3
    RULE_conditionalExpression = 4
    RULE_assignmentExpression = 5
    RULE_expression = 6
    RULE_constantExpression = 7
    RULE_declaration = 8
    RULE_declarationSpecifier = 9
    RULE_initDeclaratorList = 10
    RULE_initDeclarator = 11
    RULE_storageClassSpecifier = 12
    RULE_typeSpecifier = 13
    RULE_structOrUnionSpecifier = 14
    RULE_structOrUnion = 15
    RULE_structDeclaration = 16
    RULE_specifierQualifierList = 17
    RULE_structDeclaratorList = 18
    RULE_structDeclarator = 19
    RULE_enumSpecifier = 20
    RULE_enumeratorList = 21
    RULE_enumerator = 22
    RULE_atomicTypeSpecifier = 23
    RULE_typeQualifier = 24
    RULE_functionSpecifier = 25
    RULE_alignmentSpecifier = 26
    RULE_declarator = 27
    RULE_directDeclarator = 28
    RULE_pointer = 29
    RULE_parameterTypeList = 30
    RULE_parameterDeclaration = 31
    RULE_identifierList = 32
    RULE_typeName = 33
    RULE_abstractDeclarator = 34
    RULE_directAbstractDeclarator = 35
    RULE_typedefName = 36
    RULE_initializer = 37
    RULE_initializerList = 38
    RULE_designation = 39
    RULE_designator = 40
    RULE_staticAssertDeclaration = 41
    RULE_statement = 42
    RULE_labeledStatement = 43
    RULE_compoundStatement = 44
    RULE_blockItem = 45
    RULE_expressionStatement = 46
    RULE_selectionStatement = 47
    RULE_iterationStatement = 48
    RULE_jumpStatement = 49
    RULE_compilationUnit = 50
    RULE_externalDeclaration = 51
    RULE_functionDefinition = 52

    ruleNames =  [ u"unaryExpression", u"argumentExpressionList", u"castExpression", 
                   u"logicalOrExpression", u"conditionalExpression", u"assignmentExpression", 
                   u"expression", u"constantExpression", u"declaration", 
                   u"declarationSpecifier", u"initDeclaratorList", u"initDeclarator", 
                   u"storageClassSpecifier", u"typeSpecifier", u"structOrUnionSpecifier", 
                   u"structOrUnion", u"structDeclaration", u"specifierQualifierList", 
                   u"structDeclaratorList", u"structDeclarator", u"enumSpecifier", 
                   u"enumeratorList", u"enumerator", u"atomicTypeSpecifier", 
                   u"typeQualifier", u"functionSpecifier", u"alignmentSpecifier", 
                   u"declarator", u"directDeclarator", u"pointer", u"parameterTypeList", 
                   u"parameterDeclaration", u"identifierList", u"typeName", 
                   u"abstractDeclarator", u"directAbstractDeclarator", u"typedefName", 
                   u"initializer", u"initializerList", u"designation", u"designator", 
                   u"staticAssertDeclaration", u"statement", u"labeledStatement", 
                   u"compoundStatement", u"blockItem", u"expressionStatement", 
                   u"selectionStatement", u"iterationStatement", u"jumpStatement", 
                   u"compilationUnit", u"externalDeclaration", u"functionDefinition" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    Auto=7
    Break=8
    Case=9
    Char=10
    Const=11
    Continue=12
    Default=13
    Do=14
    Double=15
    Else=16
    Enum=17
    Extern=18
    Float=19
    For=20
    Goto=21
    If=22
    Inline=23
    Int=24
    Long=25
    Register=26
    Restrict=27
    Return=28
    Short=29
    Signed=30
    Sizeof=31
    Static=32
    Struct=33
    Switch=34
    Typedef=35
    Union=36
    Unsigned=37
    Void=38
    Volatile=39
    While=40
    Alignas=41
    Alignof=42
    Atomic=43
    Bool=44
    Complex=45
    Generic=46
    Imaginary=47
    Noreturn=48
    StaticAssert=49
    ThreadLocal=50
    LeftParen=51
    RightParen=52
    LeftBracket=53
    RightBracket=54
    LeftBrace=55
    RightBrace=56
    Less=57
    LessEqual=58
    Greater=59
    GreaterEqual=60
    LeftShift=61
    RightShift=62
    Plus=63
    PlusPlus=64
    Minus=65
    MinusMinus=66
    Star=67
    Div=68
    Mod=69
    And=70
    Or=71
    AndAnd=72
    OrOr=73
    Caret=74
    Not=75
    Tilde=76
    Question=77
    Colon=78
    Semi=79
    Comma=80
    Assign=81
    StarAssign=82
    DivAssign=83
    ModAssign=84
    PlusAssign=85
    MinusAssign=86
    LeftShiftAssign=87
    RightShiftAssign=88
    AndAssign=89
    XorAssign=90
    OrAssign=91
    Equal=92
    NotEqual=93
    Arrow=94
    Dot=95
    Ellipsis=96
    Identifier=97
    Constant=98
    StringLiteral=99
    LineDirective=100
    PragmaDirective=101
    Whitespace=102
    Newline=103
    BlockComment=104
    LineComment=105

    def __init__(self, input):
        super(CParser, self).__init__(input)
        self.checkVersion("4.5")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class UnaryExpressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(CParser.UnaryExpressionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CParser.RULE_unaryExpression

     
        def copyFrom(self, ctx):
            super(CParser.UnaryExpressionContext, self).copyFrom(ctx)


    class FunctionExpressionContext(UnaryExpressionContext):

        def __init__(self, parser, ctx): # actually a CParser.UnaryExpressionContext)
            super(CParser.FunctionExpressionContext, self).__init__(parser)
            self.copyFrom(ctx)

        def Identifier(self):
            return self.getToken(CParser.Identifier, 0)
        def argumentExpressionList(self):
            return self.getTypedRuleContext(CParser.ArgumentExpressionListContext,0)


        def enterRule(self, listener):
            if isinstance( listener, CListener ):
                listener.enterFunctionExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, CListener ):
                listener.exitFunctionExpression(self)

        def accept(self, visitor):
            if isinstance( visitor, CVisitor ):
                return visitor.visitFunctionExpression(self)
            else:
                return visitor.visitChildren(self)


    class DotExpressionContext(UnaryExpressionContext):

        def __init__(self, parser, ctx): # actually a CParser.UnaryExpressionContext)
            super(CParser.DotExpressionContext, self).__init__(parser)
            self.copyFrom(ctx)

        def unaryExpression(self):
            return self.getTypedRuleContext(CParser.UnaryExpressionContext,0)

        def Identifier(self):
            return self.getToken(CParser.Identifier, 0)

        def enterRule(self, listener):
            if isinstance( listener, CListener ):
                listener.enterDotExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, CListener ):
                listener.exitDotExpression(self)

        def accept(self, visitor):
            if isinstance( visitor, CVisitor ):
                return visitor.visitDotExpression(self)
            else:
                return visitor.visitChildren(self)


    class ParenthesizedExpressionContext(UnaryExpressionContext):

        def __init__(self, parser, ctx): # actually a CParser.UnaryExpressionContext)
            super(CParser.ParenthesizedExpressionContext, self).__init__(parser)
            self.copyFrom(ctx)

        def expression(self):
            return self.getTypedRuleContext(CParser.ExpressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, CListener ):
                listener.enterParenthesizedExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, CListener ):
                listener.exitParenthesizedExpression(self)

        def accept(self, visitor):
            if isinstance( visitor, CVisitor ):
                return visitor.visitParenthesizedExpression(self)
            else:
                return visitor.visitChildren(self)


    class LiteralExpressionContext(UnaryExpressionContext):

        def __init__(self, parser, ctx): # actually a CParser.UnaryExpressionContext)
            super(CParser.LiteralExpressionContext, self).__init__(parser)
            self.copyFrom(ctx)

        def Constant(self):
            return self.getToken(CParser.Constant, 0)

        def enterRule(self, listener):
            if isinstance( listener, CListener ):
                listener.enterLiteralExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, CListener ):
                listener.exitLiteralExpression(self)

        def accept(self, visitor):
            if isinstance( visitor, CVisitor ):
                return visitor.visitLiteralExpression(self)
            else:
                return visitor.visitChildren(self)


    class PostIncrementExpressionContext(UnaryExpressionContext):

        def __init__(self, parser, ctx): # actually a CParser.UnaryExpressionContext)
            super(CParser.PostIncrementExpressionContext, self).__init__(parser)
            self.copyFrom(ctx)

        def unaryExpression(self):
            return self.getTypedRuleContext(CParser.UnaryExpressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, CListener ):
                listener.enterPostIncrementExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, CListener ):
                listener.exitPostIncrementExpression(self)

        def accept(self, visitor):
            if isinstance( visitor, CVisitor ):
                return visitor.visitPostIncrementExpression(self)
            else:
                return visitor.visitChildren(self)


    class ArrowExpressionContext(UnaryExpressionContext):

        def __init__(self, parser, ctx): # actually a CParser.UnaryExpressionContext)
            super(CParser.ArrowExpressionContext, self).__init__(parser)
            self.copyFrom(ctx)

        def unaryExpression(self):
            return self.getTypedRuleContext(CParser.UnaryExpressionContext,0)

        def Identifier(self):
            return self.getToken(CParser.Identifier, 0)

        def enterRule(self, listener):
            if isinstance( listener, CListener ):
                listener.enterArrowExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, CListener ):
                listener.exitArrowExpression(self)

        def accept(self, visitor):
            if isinstance( visitor, CVisitor ):
                return visitor.visitArrowExpression(self)
            else:
                return visitor.visitChildren(self)


    class IndexExpressionContext(UnaryExpressionContext):

        def __init__(self, parser, ctx): # actually a CParser.UnaryExpressionContext)
            super(CParser.IndexExpressionContext, self).__init__(parser)
            self.copyFrom(ctx)

        def unaryExpression(self):
            return self.getTypedRuleContext(CParser.UnaryExpressionContext,0)

        def expression(self):
            return self.getTypedRuleContext(CParser.ExpressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, CListener ):
                listener.enterIndexExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, CListener ):
                listener.exitIndexExpression(self)

        def accept(self, visitor):
            if isinstance( visitor, CVisitor ):
                return visitor.visitIndexExpression(self)
            else:
                return visitor.visitChildren(self)


    class SizeOfTypeExpressionContext(UnaryExpressionContext):

        def __init__(self, parser, ctx): # actually a CParser.UnaryExpressionContext)
            super(CParser.SizeOfTypeExpressionContext, self).__init__(parser)
            self.copyFrom(ctx)

        def typeName(self):
            return self.getTypedRuleContext(CParser.TypeNameContext,0)


        def enterRule(self, listener):
            if isinstance( listener, CListener ):
                listener.enterSizeOfTypeExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, CListener ):
                listener.exitSizeOfTypeExpression(self)

        def accept(self, visitor):
            if isinstance( visitor, CVisitor ):
                return visitor.visitSizeOfTypeExpression(self)
            else:
                return visitor.visitChildren(self)


    class IdentifierExpressionContext(UnaryExpressionContext):

        def __init__(self, parser, ctx): # actually a CParser.UnaryExpressionContext)
            super(CParser.IdentifierExpressionContext, self).__init__(parser)
            self.copyFrom(ctx)

        def Identifier(self):
            return self.getToken(CParser.Identifier, 0)

        def enterRule(self, listener):
            if isinstance( listener, CListener ):
                listener.enterIdentifierExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, CListener ):
                listener.exitIdentifierExpression(self)

        def accept(self, visitor):
            if isinstance( visitor, CVisitor ):
                return visitor.visitIdentifierExpression(self)
            else:
                return visitor.visitChildren(self)


    class UnaryOperatorExpressionContext(UnaryExpressionContext):

        def __init__(self, parser, ctx): # actually a CParser.UnaryExpressionContext)
            super(CParser.UnaryOperatorExpressionContext, self).__init__(parser)
            self.copyFrom(ctx)

        def castExpression(self):
            return self.getTypedRuleContext(CParser.CastExpressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, CListener ):
                listener.enterUnaryOperatorExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, CListener ):
                listener.exitUnaryOperatorExpression(self)

        def accept(self, visitor):
            if isinstance( visitor, CVisitor ):
                return visitor.visitUnaryOperatorExpression(self)
            else:
                return visitor.visitChildren(self)


    class AlignOfTypeExpressionContext(UnaryExpressionContext):

        def __init__(self, parser, ctx): # actually a CParser.UnaryExpressionContext)
            super(CParser.AlignOfTypeExpressionContext, self).__init__(parser)
            self.copyFrom(ctx)

        def typeName(self):
            return self.getTypedRuleContext(CParser.TypeNameContext,0)


        def enterRule(self, listener):
            if isinstance( listener, CListener ):
                listener.enterAlignOfTypeExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, CListener ):
                listener.exitAlignOfTypeExpression(self)

        def accept(self, visitor):
            if isinstance( visitor, CVisitor ):
                return visitor.visitAlignOfTypeExpression(self)
            else:
                return visitor.visitChildren(self)


    class SizeOfExpressionContext(UnaryExpressionContext):

        def __init__(self, parser, ctx): # actually a CParser.UnaryExpressionContext)
            super(CParser.SizeOfExpressionContext, self).__init__(parser)
            self.copyFrom(ctx)

        def unaryExpression(self):
            return self.getTypedRuleContext(CParser.UnaryExpressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, CListener ):
                listener.enterSizeOfExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, CListener ):
                listener.exitSizeOfExpression(self)

        def accept(self, visitor):
            if isinstance( visitor, CVisitor ):
                return visitor.visitSizeOfExpression(self)
            else:
                return visitor.visitChildren(self)


    class StringLiteralExpressionContext(UnaryExpressionContext):

        def __init__(self, parser, ctx): # actually a CParser.UnaryExpressionContext)
            super(CParser.StringLiteralExpressionContext, self).__init__(parser)
            self.copyFrom(ctx)

        def StringLiteral(self, i=None):
            if i is None:
                return self.getTokens(CParser.StringLiteral)
            else:
                return self.getToken(CParser.StringLiteral, i)

        def enterRule(self, listener):
            if isinstance( listener, CListener ):
                listener.enterStringLiteralExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, CListener ):
                listener.exitStringLiteralExpression(self)

        def accept(self, visitor):
            if isinstance( visitor, CVisitor ):
                return visitor.visitStringLiteralExpression(self)
            else:
                return visitor.visitChildren(self)


    class PreIncrementExpressionContext(UnaryExpressionContext):

        def __init__(self, parser, ctx): # actually a CParser.UnaryExpressionContext)
            super(CParser.PreIncrementExpressionContext, self).__init__(parser)
            self.copyFrom(ctx)

        def unaryExpression(self):
            return self.getTypedRuleContext(CParser.UnaryExpressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, CListener ):
                listener.enterPreIncrementExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, CListener ):
                listener.exitPreIncrementExpression(self)

        def accept(self, visitor):
            if isinstance( visitor, CVisitor ):
                return visitor.visitPreIncrementExpression(self)
            else:
                return visitor.visitChildren(self)



    def unaryExpression(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CParser.UnaryExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 0
        self.enterRecursionRule(localctx, 0, self.RULE_unaryExpression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 140
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                localctx = CParser.PreIncrementExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 107
                _la = self._input.LA(1)
                if not(_la==CParser.PlusPlus or _la==CParser.MinusMinus):
                    self._errHandler.recoverInline(self)
                else:
                    self.consume()
                self.state = 108
                self.unaryExpression(5)
                pass

            elif la_ == 2:
                localctx = CParser.SizeOfExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 109
                self.match(CParser.Sizeof)
                self.state = 110
                self.unaryExpression(3)
                pass

            elif la_ == 3:
                localctx = CParser.IdentifierExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 111
                self.match(CParser.Identifier)
                pass

            elif la_ == 4:
                localctx = CParser.LiteralExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 112
                self.match(CParser.Constant)
                pass

            elif la_ == 5:
                localctx = CParser.StringLiteralExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 114 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 113
                        self.match(CParser.StringLiteral)

                    else:
                        raise NoViableAltException(self)
                    self.state = 116 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,0,self._ctx)

                pass

            elif la_ == 6:
                localctx = CParser.ParenthesizedExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 118
                self.match(CParser.LeftParen)
                self.state = 119
                self.expression()
                self.state = 120
                self.match(CParser.RightParen)
                pass

            elif la_ == 7:
                localctx = CParser.FunctionExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 122
                self.match(CParser.Identifier)
                self.state = 123
                self.match(CParser.LeftParen)
                self.state = 125
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CParser.Sizeof) | (1 << CParser.Alignof) | (1 << CParser.LeftParen) | (1 << CParser.Plus))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (CParser.PlusPlus - 64)) | (1 << (CParser.Minus - 64)) | (1 << (CParser.MinusMinus - 64)) | (1 << (CParser.Star - 64)) | (1 << (CParser.And - 64)) | (1 << (CParser.Not - 64)) | (1 << (CParser.Tilde - 64)) | (1 << (CParser.Identifier - 64)) | (1 << (CParser.Constant - 64)) | (1 << (CParser.StringLiteral - 64)))) != 0):
                    self.state = 124
                    self.argumentExpressionList()


                self.state = 127
                self.match(CParser.RightParen)
                pass

            elif la_ == 8:
                localctx = CParser.UnaryOperatorExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 128
                _la = self._input.LA(1)
                if not(((((_la - 63)) & ~0x3f) == 0 and ((1 << (_la - 63)) & ((1 << (CParser.Plus - 63)) | (1 << (CParser.Minus - 63)) | (1 << (CParser.Star - 63)) | (1 << (CParser.And - 63)) | (1 << (CParser.Not - 63)) | (1 << (CParser.Tilde - 63)))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self.consume()
                self.state = 129
                self.castExpression()
                pass

            elif la_ == 9:
                localctx = CParser.SizeOfTypeExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 130
                self.match(CParser.Sizeof)
                self.state = 131
                self.match(CParser.LeftParen)
                self.state = 132
                self.typeName()
                self.state = 133
                self.match(CParser.RightParen)
                pass

            elif la_ == 10:
                localctx = CParser.AlignOfTypeExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 135
                self.match(CParser.Alignof)
                self.state = 136
                self.match(CParser.LeftParen)
                self.state = 137
                self.typeName()
                self.state = 138
                self.match(CParser.RightParen)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 157
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 155
                    la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
                    if la_ == 1:
                        localctx = CParser.IndexExpressionContext(self, CParser.UnaryExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_unaryExpression)
                        self.state = 142
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 143
                        self.match(CParser.LeftBracket)
                        self.state = 144
                        self.expression()
                        self.state = 145
                        self.match(CParser.RightBracket)
                        pass

                    elif la_ == 2:
                        localctx = CParser.DotExpressionContext(self, CParser.UnaryExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_unaryExpression)
                        self.state = 147
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 148
                        self.match(CParser.Dot)
                        self.state = 149
                        self.match(CParser.Identifier)
                        pass

                    elif la_ == 3:
                        localctx = CParser.ArrowExpressionContext(self, CParser.UnaryExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_unaryExpression)
                        self.state = 150
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 151
                        self.match(CParser.Arrow)
                        self.state = 152
                        self.match(CParser.Identifier)
                        pass

                    elif la_ == 4:
                        localctx = CParser.PostIncrementExpressionContext(self, CParser.UnaryExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_unaryExpression)
                        self.state = 153
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 154
                        _la = self._input.LA(1)
                        if not(_la==CParser.PlusPlus or _la==CParser.MinusMinus):
                            self._errHandler.recoverInline(self)
                        else:
                            self.consume()
                        pass

             
                self.state = 159
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class ArgumentExpressionListContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(CParser.ArgumentExpressionListContext, self).__init__(parent, invokingState)
            self.parser = parser

        def assignmentExpression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(CParser.AssignmentExpressionContext)
            else:
                return self.getTypedRuleContext(CParser.AssignmentExpressionContext,i)


        def getRuleIndex(self):
            return CParser.RULE_argumentExpressionList

        def enterRule(self, listener):
            if isinstance( listener, CListener ):
                listener.enterArgumentExpressionList(self)

        def exitRule(self, listener):
            if isinstance( listener, CListener ):
                listener.exitArgumentExpressionList(self)

        def accept(self, visitor):
            if isinstance( visitor, CVisitor ):
                return visitor.visitArgumentExpressionList(self)
            else:
                return visitor.visitChildren(self)




    def argumentExpressionList(self):

        localctx = CParser.ArgumentExpressionListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_argumentExpressionList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 160
            self.assignmentExpression()
            self.state = 165
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CParser.Comma:
                self.state = 161
                self.match(CParser.Comma)
                self.state = 162
                self.assignmentExpression()
                self.state = 167
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class CastExpressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(CParser.CastExpressionContext, self).__init__(parent, invokingState)
            self.parser = parser

        def unaryExpression(self):
            return self.getTypedRuleContext(CParser.UnaryExpressionContext,0)


        def typeName(self):
            return self.getTypedRuleContext(CParser.TypeNameContext,0)


        def castExpression(self):
            return self.getTypedRuleContext(CParser.CastExpressionContext,0)


        def getRuleIndex(self):
            return CParser.RULE_castExpression

        def enterRule(self, listener):
            if isinstance( listener, CListener ):
                listener.enterCastExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, CListener ):
                listener.exitCastExpression(self)

        def accept(self, visitor):
            if isinstance( visitor, CVisitor ):
                return visitor.visitCastExpression(self)
            else:
                return visitor.visitChildren(self)




    def castExpression(self):

        localctx = CParser.CastExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_castExpression)
        try:
            self.state = 174
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 168
                self.unaryExpression(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 169
                self.match(CParser.LeftParen)
                self.state = 170
                self.typeName()
                self.state = 171
                self.match(CParser.RightParen)
                self.state = 172
                self.castExpression()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class LogicalOrExpressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(CParser.LogicalOrExpressionContext, self).__init__(parent, invokingState)
            self.parser = parser

        def castExpression(self):
            return self.getTypedRuleContext(CParser.CastExpressionContext,0)


        def logicalOrExpression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(CParser.LogicalOrExpressionContext)
            else:
                return self.getTypedRuleContext(CParser.LogicalOrExpressionContext,i)


        def getRuleIndex(self):
            return CParser.RULE_logicalOrExpression

        def enterRule(self, listener):
            if isinstance( listener, CListener ):
                listener.enterLogicalOrExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, CListener ):
                listener.exitLogicalOrExpression(self)

        def accept(self, visitor):
            if isinstance( visitor, CVisitor ):
                return visitor.visitLogicalOrExpression(self)
            else:
                return visitor.visitChildren(self)



    def logicalOrExpression(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CParser.LogicalOrExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 6
        self.enterRecursionRule(localctx, 6, self.RULE_logicalOrExpression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 177
            self.castExpression()
            self._ctx.stop = self._input.LT(-1)
            self.state = 211
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,8,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 209
                    la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
                    if la_ == 1:
                        localctx = CParser.LogicalOrExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_logicalOrExpression)
                        self.state = 179
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 180
                        _la = self._input.LA(1)
                        if not(((((_la - 67)) & ~0x3f) == 0 and ((1 << (_la - 67)) & ((1 << (CParser.Star - 67)) | (1 << (CParser.Div - 67)) | (1 << (CParser.Mod - 67)))) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self.consume()
                        self.state = 181
                        self.logicalOrExpression(11)
                        pass

                    elif la_ == 2:
                        localctx = CParser.LogicalOrExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_logicalOrExpression)
                        self.state = 182
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 183
                        _la = self._input.LA(1)
                        if not(_la==CParser.Plus or _la==CParser.Minus):
                            self._errHandler.recoverInline(self)
                        else:
                            self.consume()
                        self.state = 184
                        self.logicalOrExpression(10)
                        pass

                    elif la_ == 3:
                        localctx = CParser.LogicalOrExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_logicalOrExpression)
                        self.state = 185
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 186
                        _la = self._input.LA(1)
                        if not(_la==CParser.LeftShift or _la==CParser.RightShift):
                            self._errHandler.recoverInline(self)
                        else:
                            self.consume()
                        self.state = 187
                        self.logicalOrExpression(9)
                        pass

                    elif la_ == 4:
                        localctx = CParser.LogicalOrExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_logicalOrExpression)
                        self.state = 188
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 189
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CParser.Less) | (1 << CParser.LessEqual) | (1 << CParser.Greater) | (1 << CParser.GreaterEqual))) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self.consume()
                        self.state = 190
                        self.logicalOrExpression(8)
                        pass

                    elif la_ == 5:
                        localctx = CParser.LogicalOrExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_logicalOrExpression)
                        self.state = 191
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 192
                        _la = self._input.LA(1)
                        if not(_la==CParser.Equal or _la==CParser.NotEqual):
                            self._errHandler.recoverInline(self)
                        else:
                            self.consume()
                        self.state = 193
                        self.logicalOrExpression(7)
                        pass

                    elif la_ == 6:
                        localctx = CParser.LogicalOrExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_logicalOrExpression)
                        self.state = 194
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 195
                        self.match(CParser.And)
                        self.state = 196
                        self.logicalOrExpression(6)
                        pass

                    elif la_ == 7:
                        localctx = CParser.LogicalOrExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_logicalOrExpression)
                        self.state = 197
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 198
                        self.match(CParser.Caret)
                        self.state = 199
                        self.logicalOrExpression(5)
                        pass

                    elif la_ == 8:
                        localctx = CParser.LogicalOrExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_logicalOrExpression)
                        self.state = 200
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 201
                        self.match(CParser.Or)
                        self.state = 202
                        self.logicalOrExpression(4)
                        pass

                    elif la_ == 9:
                        localctx = CParser.LogicalOrExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_logicalOrExpression)
                        self.state = 203
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 204
                        self.match(CParser.AndAnd)
                        self.state = 205
                        self.logicalOrExpression(3)
                        pass

                    elif la_ == 10:
                        localctx = CParser.LogicalOrExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_logicalOrExpression)
                        self.state = 206
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 207
                        self.match(CParser.OrOr)
                        self.state = 208
                        self.logicalOrExpression(2)
                        pass

             
                self.state = 213
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class ConditionalExpressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(CParser.ConditionalExpressionContext, self).__init__(parent, invokingState)
            self.parser = parser

        def logicalOrExpression(self):
            return self.getTypedRuleContext(CParser.LogicalOrExpressionContext,0)


        def expression(self):
            return self.getTypedRuleContext(CParser.ExpressionContext,0)


        def conditionalExpression(self):
            return self.getTypedRuleContext(CParser.ConditionalExpressionContext,0)


        def getRuleIndex(self):
            return CParser.RULE_conditionalExpression

        def enterRule(self, listener):
            if isinstance( listener, CListener ):
                listener.enterConditionalExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, CListener ):
                listener.exitConditionalExpression(self)

        def accept(self, visitor):
            if isinstance( visitor, CVisitor ):
                return visitor.visitConditionalExpression(self)
            else:
                return visitor.visitChildren(self)




    def conditionalExpression(self):

        localctx = CParser.ConditionalExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_conditionalExpression)
        try:
            self.state = 221
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 214
                self.logicalOrExpression(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 215
                self.logicalOrExpression(0)
                self.state = 216
                self.match(CParser.Question)
                self.state = 217
                self.expression()
                self.state = 218
                self.match(CParser.Colon)
                self.state = 219
                self.conditionalExpression()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class AssignmentExpressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(CParser.AssignmentExpressionContext, self).__init__(parent, invokingState)
            self.parser = parser

        def conditionalExpression(self):
            return self.getTypedRuleContext(CParser.ConditionalExpressionContext,0)


        def unaryExpression(self):
            return self.getTypedRuleContext(CParser.UnaryExpressionContext,0)


        def assignmentExpression(self):
            return self.getTypedRuleContext(CParser.AssignmentExpressionContext,0)


        def getRuleIndex(self):
            return CParser.RULE_assignmentExpression

        def enterRule(self, listener):
            if isinstance( listener, CListener ):
                listener.enterAssignmentExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, CListener ):
                listener.exitAssignmentExpression(self)

        def accept(self, visitor):
            if isinstance( visitor, CVisitor ):
                return visitor.visitAssignmentExpression(self)
            else:
                return visitor.visitChildren(self)




    def assignmentExpression(self):

        localctx = CParser.AssignmentExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_assignmentExpression)
        self._la = 0 # Token type
        try:
            self.state = 228
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 223
                self.conditionalExpression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 224
                self.unaryExpression(0)
                self.state = 225
                _la = self._input.LA(1)
                if not(((((_la - 81)) & ~0x3f) == 0 and ((1 << (_la - 81)) & ((1 << (CParser.Assign - 81)) | (1 << (CParser.StarAssign - 81)) | (1 << (CParser.DivAssign - 81)) | (1 << (CParser.ModAssign - 81)) | (1 << (CParser.PlusAssign - 81)) | (1 << (CParser.MinusAssign - 81)) | (1 << (CParser.LeftShiftAssign - 81)) | (1 << (CParser.RightShiftAssign - 81)) | (1 << (CParser.AndAssign - 81)) | (1 << (CParser.XorAssign - 81)) | (1 << (CParser.OrAssign - 81)))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self.consume()
                self.state = 226
                self.assignmentExpression()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ExpressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(CParser.ExpressionContext, self).__init__(parent, invokingState)
            self.parser = parser

        def assignmentExpression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(CParser.AssignmentExpressionContext)
            else:
                return self.getTypedRuleContext(CParser.AssignmentExpressionContext,i)


        def getRuleIndex(self):
            return CParser.RULE_expression

        def enterRule(self, listener):
            if isinstance( listener, CListener ):
                listener.enterExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, CListener ):
                listener.exitExpression(self)

        def accept(self, visitor):
            if isinstance( visitor, CVisitor ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)




    def expression(self):

        localctx = CParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 230
            self.assignmentExpression()
            self.state = 235
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CParser.Comma:
                self.state = 231
                self.match(CParser.Comma)
                self.state = 232
                self.assignmentExpression()
                self.state = 237
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ConstantExpressionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(CParser.ConstantExpressionContext, self).__init__(parent, invokingState)
            self.parser = parser

        def conditionalExpression(self):
            return self.getTypedRuleContext(CParser.ConditionalExpressionContext,0)


        def getRuleIndex(self):
            return CParser.RULE_constantExpression

        def enterRule(self, listener):
            if isinstance( listener, CListener ):
                listener.enterConstantExpression(self)

        def exitRule(self, listener):
            if isinstance( listener, CListener ):
                listener.exitConstantExpression(self)

        def accept(self, visitor):
            if isinstance( visitor, CVisitor ):
                return visitor.visitConstantExpression(self)
            else:
                return visitor.visitChildren(self)




    def constantExpression(self):

        localctx = CParser.ConstantExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_constantExpression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 238
            self.conditionalExpression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class DeclarationContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(CParser.DeclarationContext, self).__init__(parent, invokingState)
            self.parser = parser

        def declarationSpecifier(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(CParser.DeclarationSpecifierContext)
            else:
                return self.getTypedRuleContext(CParser.DeclarationSpecifierContext,i)


        def initDeclaratorList(self):
            return self.getTypedRuleContext(CParser.InitDeclaratorListContext,0)


        def staticAssertDeclaration(self):
            return self.getTypedRuleContext(CParser.StaticAssertDeclarationContext,0)


        def getRuleIndex(self):
            return CParser.RULE_declaration

        def enterRule(self, listener):
            if isinstance( listener, CListener ):
                listener.enterDeclaration(self)

        def exitRule(self, listener):
            if isinstance( listener, CListener ):
                listener.exitDeclaration(self)

        def accept(self, visitor):
            if isinstance( visitor, CVisitor ):
                return visitor.visitDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def declaration(self):

        localctx = CParser.DeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_declaration)
        self._la = 0 # Token type
        try:
            self.state = 251
            token = self._input.LA(1)
            if token in [CParser.T__0, CParser.T__1, CParser.T__2, CParser.T__3, CParser.T__4, CParser.T__5, CParser.Auto, CParser.Char, CParser.Const, CParser.Double, CParser.Enum, CParser.Extern, CParser.Float, CParser.Inline, CParser.Int, CParser.Long, CParser.Register, CParser.Restrict, CParser.Short, CParser.Signed, CParser.Static, CParser.Struct, CParser.Typedef, CParser.Union, CParser.Unsigned, CParser.Void, CParser.Volatile, CParser.Alignas, CParser.Atomic, CParser.Bool, CParser.Complex, CParser.Noreturn, CParser.ThreadLocal, CParser.Identifier]:
                self.enterOuterAlt(localctx, 1)
                self.state = 241 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 240
                        self.declarationSpecifier()

                    else:
                        raise NoViableAltException(self)
                    self.state = 243 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,12,self._ctx)

                self.state = 246
                _la = self._input.LA(1)
                if ((((_la - 51)) & ~0x3f) == 0 and ((1 << (_la - 51)) & ((1 << (CParser.LeftParen - 51)) | (1 << (CParser.Star - 51)) | (1 << (CParser.Identifier - 51)))) != 0):
                    self.state = 245
                    self.initDeclaratorList()


                self.state = 248
                self.match(CParser.Semi)

            elif token in [CParser.StaticAssert]:
                self.enterOuterAlt(localctx, 2)
                self.state = 250
                self.staticAssertDeclaration()

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class DeclarationSpecifierContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(CParser.DeclarationSpecifierContext, self).__init__(parent, invokingState)
            self.parser = parser

        def storageClassSpecifier(self):
            return self.getTypedRuleContext(CParser.StorageClassSpecifierContext,0)


        def typeSpecifier(self):
            return self.getTypedRuleContext(CParser.TypeSpecifierContext,0)


        def typeQualifier(self):
            return self.getTypedRuleContext(CParser.TypeQualifierContext,0)


        def functionSpecifier(self):
            return self.getTypedRuleContext(CParser.FunctionSpecifierContext,0)


        def alignmentSpecifier(self):
            return self.getTypedRuleContext(CParser.AlignmentSpecifierContext,0)


        def getRuleIndex(self):
            return CParser.RULE_declarationSpecifier

        def enterRule(self, listener):
            if isinstance( listener, CListener ):
                listener.enterDeclarationSpecifier(self)

        def exitRule(self, listener):
            if isinstance( listener, CListener ):
                listener.exitDeclarationSpecifier(self)

        def accept(self, visitor):
            if isinstance( visitor, CVisitor ):
                return visitor.visitDeclarationSpecifier(self)
            else:
                return visitor.visitChildren(self)




    def declarationSpecifier(self):

        localctx = CParser.DeclarationSpecifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_declarationSpecifier)
        try:
            self.state = 258
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 253
                self.storageClassSpecifier()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 254
                self.typeSpecifier()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 255
                self.typeQualifier()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 256
                self.functionSpecifier()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 257
                self.alignmentSpecifier()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class InitDeclaratorListContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(CParser.InitDeclaratorListContext, self).__init__(parent, invokingState)
            self.parser = parser

        def initDeclarator(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(CParser.InitDeclaratorContext)
            else:
                return self.getTypedRuleContext(CParser.InitDeclaratorContext,i)


        def getRuleIndex(self):
            return CParser.RULE_initDeclaratorList

        def enterRule(self, listener):
            if isinstance( listener, CListener ):
                listener.enterInitDeclaratorList(self)

        def exitRule(self, listener):
            if isinstance( listener, CListener ):
                listener.exitInitDeclaratorList(self)

        def accept(self, visitor):
            if isinstance( visitor, CVisitor ):
                return visitor.visitInitDeclaratorList(self)
            else:
                return visitor.visitChildren(self)




    def initDeclaratorList(self):

        localctx = CParser.InitDeclaratorListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_initDeclaratorList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 260
            self.initDeclarator()
            self.state = 265
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CParser.Comma:
                self.state = 261
                self.match(CParser.Comma)
                self.state = 262
                self.initDeclarator()
                self.state = 267
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class InitDeclaratorContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(CParser.InitDeclaratorContext, self).__init__(parent, invokingState)
            self.parser = parser

        def declarator(self):
            return self.getTypedRuleContext(CParser.DeclaratorContext,0)


        def initializer(self):
            return self.getTypedRuleContext(CParser.InitializerContext,0)


        def getRuleIndex(self):
            return CParser.RULE_initDeclarator

        def enterRule(self, listener):
            if isinstance( listener, CListener ):
                listener.enterInitDeclarator(self)

        def exitRule(self, listener):
            if isinstance( listener, CListener ):
                listener.exitInitDeclarator(self)

        def accept(self, visitor):
            if isinstance( visitor, CVisitor ):
                return visitor.visitInitDeclarator(self)
            else:
                return visitor.visitChildren(self)




    def initDeclarator(self):

        localctx = CParser.InitDeclaratorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_initDeclarator)
        try:
            self.state = 273
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 268
                self.declarator()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 269
                self.declarator()
                self.state = 270
                self.match(CParser.Assign)
                self.state = 271
                self.initializer()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class StorageClassSpecifierContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(CParser.StorageClassSpecifierContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CParser.RULE_storageClassSpecifier

        def enterRule(self, listener):
            if isinstance( listener, CListener ):
                listener.enterStorageClassSpecifier(self)

        def exitRule(self, listener):
            if isinstance( listener, CListener ):
                listener.exitStorageClassSpecifier(self)

        def accept(self, visitor):
            if isinstance( visitor, CVisitor ):
                return visitor.visitStorageClassSpecifier(self)
            else:
                return visitor.visitChildren(self)




    def storageClassSpecifier(self):

        localctx = CParser.StorageClassSpecifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_storageClassSpecifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 275
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CParser.Auto) | (1 << CParser.Extern) | (1 << CParser.Register) | (1 << CParser.Static) | (1 << CParser.Typedef) | (1 << CParser.ThreadLocal))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class TypeSpecifierContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(CParser.TypeSpecifierContext, self).__init__(parent, invokingState)
            self.parser = parser

        def atomicTypeSpecifier(self):
            return self.getTypedRuleContext(CParser.AtomicTypeSpecifierContext,0)


        def structOrUnionSpecifier(self):
            return self.getTypedRuleContext(CParser.StructOrUnionSpecifierContext,0)


        def enumSpecifier(self):
            return self.getTypedRuleContext(CParser.EnumSpecifierContext,0)


        def typedefName(self):
            return self.getTypedRuleContext(CParser.TypedefNameContext,0)


        def getRuleIndex(self):
            return CParser.RULE_typeSpecifier

        def enterRule(self, listener):
            if isinstance( listener, CListener ):
                listener.enterTypeSpecifier(self)

        def exitRule(self, listener):
            if isinstance( listener, CListener ):
                listener.exitTypeSpecifier(self)

        def accept(self, visitor):
            if isinstance( visitor, CVisitor ):
                return visitor.visitTypeSpecifier(self)
            else:
                return visitor.visitChildren(self)




    def typeSpecifier(self):

        localctx = CParser.TypeSpecifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_typeSpecifier)
        self._la = 0 # Token type
        try:
            self.state = 286
            token = self._input.LA(1)
            if token in [CParser.T__0, CParser.T__1, CParser.T__2, CParser.Char, CParser.Double, CParser.Float, CParser.Int, CParser.Long, CParser.Short, CParser.Signed, CParser.Unsigned, CParser.Void, CParser.Bool, CParser.Complex]:
                self.enterOuterAlt(localctx, 1)
                self.state = 277
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CParser.T__0) | (1 << CParser.T__1) | (1 << CParser.T__2) | (1 << CParser.Char) | (1 << CParser.Double) | (1 << CParser.Float) | (1 << CParser.Int) | (1 << CParser.Long) | (1 << CParser.Short) | (1 << CParser.Signed) | (1 << CParser.Unsigned) | (1 << CParser.Void) | (1 << CParser.Bool) | (1 << CParser.Complex))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self.consume()

            elif token in [CParser.T__3]:
                self.enterOuterAlt(localctx, 2)
                self.state = 278
                self.match(CParser.T__3)
                self.state = 279
                self.match(CParser.LeftParen)
                self.state = 280
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CParser.T__0) | (1 << CParser.T__1) | (1 << CParser.T__2))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self.consume()
                self.state = 281
                self.match(CParser.RightParen)

            elif token in [CParser.Atomic]:
                self.enterOuterAlt(localctx, 3)
                self.state = 282
                self.atomicTypeSpecifier()

            elif token in [CParser.Struct, CParser.Union]:
                self.enterOuterAlt(localctx, 4)
                self.state = 283
                self.structOrUnionSpecifier()

            elif token in [CParser.Enum]:
                self.enterOuterAlt(localctx, 5)
                self.state = 284
                self.enumSpecifier()

            elif token in [CParser.Identifier]:
                self.enterOuterAlt(localctx, 6)
                self.state = 285
                self.typedefName()

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class StructOrUnionSpecifierContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(CParser.StructOrUnionSpecifierContext, self).__init__(parent, invokingState)
            self.parser = parser

        def structOrUnion(self):
            return self.getTypedRuleContext(CParser.StructOrUnionContext,0)


        def Identifier(self):
            return self.getToken(CParser.Identifier, 0)

        def structDeclaration(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(CParser.StructDeclarationContext)
            else:
                return self.getTypedRuleContext(CParser.StructDeclarationContext,i)


        def getRuleIndex(self):
            return CParser.RULE_structOrUnionSpecifier

        def enterRule(self, listener):
            if isinstance( listener, CListener ):
                listener.enterStructOrUnionSpecifier(self)

        def exitRule(self, listener):
            if isinstance( listener, CListener ):
                listener.exitStructOrUnionSpecifier(self)

        def accept(self, visitor):
            if isinstance( visitor, CVisitor ):
                return visitor.visitStructOrUnionSpecifier(self)
            else:
                return visitor.visitChildren(self)




    def structOrUnionSpecifier(self):

        localctx = CParser.StructOrUnionSpecifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_structOrUnionSpecifier)
        self._la = 0 # Token type
        try:
            self.state = 303
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 288
                self.structOrUnion()
                self.state = 290
                _la = self._input.LA(1)
                if _la==CParser.Identifier:
                    self.state = 289
                    self.match(CParser.Identifier)


                self.state = 292
                self.match(CParser.LeftBrace)
                self.state = 294 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 293
                    self.structDeclaration()
                    self.state = 296 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CParser.T__0) | (1 << CParser.T__1) | (1 << CParser.T__2) | (1 << CParser.T__3) | (1 << CParser.Char) | (1 << CParser.Const) | (1 << CParser.Double) | (1 << CParser.Enum) | (1 << CParser.Float) | (1 << CParser.Int) | (1 << CParser.Long) | (1 << CParser.Restrict) | (1 << CParser.Short) | (1 << CParser.Signed) | (1 << CParser.Struct) | (1 << CParser.Union) | (1 << CParser.Unsigned) | (1 << CParser.Void) | (1 << CParser.Volatile) | (1 << CParser.Atomic) | (1 << CParser.Bool) | (1 << CParser.Complex) | (1 << CParser.StaticAssert))) != 0) or _la==CParser.Identifier):
                        break

                self.state = 298
                self.match(CParser.RightBrace)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 300
                self.structOrUnion()
                self.state = 301
                self.match(CParser.Identifier)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class StructOrUnionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(CParser.StructOrUnionContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CParser.RULE_structOrUnion

        def enterRule(self, listener):
            if isinstance( listener, CListener ):
                listener.enterStructOrUnion(self)

        def exitRule(self, listener):
            if isinstance( listener, CListener ):
                listener.exitStructOrUnion(self)

        def accept(self, visitor):
            if isinstance( visitor, CVisitor ):
                return visitor.visitStructOrUnion(self)
            else:
                return visitor.visitChildren(self)




    def structOrUnion(self):

        localctx = CParser.StructOrUnionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_structOrUnion)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 305
            _la = self._input.LA(1)
            if not(_la==CParser.Struct or _la==CParser.Union):
                self._errHandler.recoverInline(self)
            else:
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class StructDeclarationContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(CParser.StructDeclarationContext, self).__init__(parent, invokingState)
            self.parser = parser

        def specifierQualifierList(self):
            return self.getTypedRuleContext(CParser.SpecifierQualifierListContext,0)


        def structDeclaratorList(self):
            return self.getTypedRuleContext(CParser.StructDeclaratorListContext,0)


        def staticAssertDeclaration(self):
            return self.getTypedRuleContext(CParser.StaticAssertDeclarationContext,0)


        def getRuleIndex(self):
            return CParser.RULE_structDeclaration

        def enterRule(self, listener):
            if isinstance( listener, CListener ):
                listener.enterStructDeclaration(self)

        def exitRule(self, listener):
            if isinstance( listener, CListener ):
                listener.exitStructDeclaration(self)

        def accept(self, visitor):
            if isinstance( visitor, CVisitor ):
                return visitor.visitStructDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def structDeclaration(self):

        localctx = CParser.StructDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_structDeclaration)
        self._la = 0 # Token type
        try:
            self.state = 314
            token = self._input.LA(1)
            if token in [CParser.T__0, CParser.T__1, CParser.T__2, CParser.T__3, CParser.Char, CParser.Const, CParser.Double, CParser.Enum, CParser.Float, CParser.Int, CParser.Long, CParser.Restrict, CParser.Short, CParser.Signed, CParser.Struct, CParser.Union, CParser.Unsigned, CParser.Void, CParser.Volatile, CParser.Atomic, CParser.Bool, CParser.Complex, CParser.Identifier]:
                self.enterOuterAlt(localctx, 1)
                self.state = 307
                self.specifierQualifierList()
                self.state = 309
                _la = self._input.LA(1)
                if ((((_la - 51)) & ~0x3f) == 0 and ((1 << (_la - 51)) & ((1 << (CParser.LeftParen - 51)) | (1 << (CParser.Star - 51)) | (1 << (CParser.Colon - 51)) | (1 << (CParser.Identifier - 51)))) != 0):
                    self.state = 308
                    self.structDeclaratorList()


                self.state = 311
                self.match(CParser.Semi)

            elif token in [CParser.StaticAssert]:
                self.enterOuterAlt(localctx, 2)
                self.state = 313
                self.staticAssertDeclaration()

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class SpecifierQualifierListContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(CParser.SpecifierQualifierListContext, self).__init__(parent, invokingState)
            self.parser = parser

        def typeSpecifier(self):
            return self.getTypedRuleContext(CParser.TypeSpecifierContext,0)


        def specifierQualifierList(self):
            return self.getTypedRuleContext(CParser.SpecifierQualifierListContext,0)


        def typeQualifier(self):
            return self.getTypedRuleContext(CParser.TypeQualifierContext,0)


        def getRuleIndex(self):
            return CParser.RULE_specifierQualifierList

        def enterRule(self, listener):
            if isinstance( listener, CListener ):
                listener.enterSpecifierQualifierList(self)

        def exitRule(self, listener):
            if isinstance( listener, CListener ):
                listener.exitSpecifierQualifierList(self)

        def accept(self, visitor):
            if isinstance( visitor, CVisitor ):
                return visitor.visitSpecifierQualifierList(self)
            else:
                return visitor.visitChildren(self)




    def specifierQualifierList(self):

        localctx = CParser.SpecifierQualifierListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_specifierQualifierList)
        try:
            self.state = 324
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 316
                self.typeSpecifier()
                self.state = 318
                la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
                if la_ == 1:
                    self.state = 317
                    self.specifierQualifierList()


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 320
                self.typeQualifier()
                self.state = 322
                la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
                if la_ == 1:
                    self.state = 321
                    self.specifierQualifierList()


                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class StructDeclaratorListContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(CParser.StructDeclaratorListContext, self).__init__(parent, invokingState)
            self.parser = parser

        def structDeclarator(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(CParser.StructDeclaratorContext)
            else:
                return self.getTypedRuleContext(CParser.StructDeclaratorContext,i)


        def getRuleIndex(self):
            return CParser.RULE_structDeclaratorList

        def enterRule(self, listener):
            if isinstance( listener, CListener ):
                listener.enterStructDeclaratorList(self)

        def exitRule(self, listener):
            if isinstance( listener, CListener ):
                listener.exitStructDeclaratorList(self)

        def accept(self, visitor):
            if isinstance( visitor, CVisitor ):
                return visitor.visitStructDeclaratorList(self)
            else:
                return visitor.visitChildren(self)




    def structDeclaratorList(self):

        localctx = CParser.StructDeclaratorListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_structDeclaratorList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 326
            self.structDeclarator()
            self.state = 331
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CParser.Comma:
                self.state = 327
                self.match(CParser.Comma)
                self.state = 328
                self.structDeclarator()
                self.state = 333
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class StructDeclaratorContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(CParser.StructDeclaratorContext, self).__init__(parent, invokingState)
            self.parser = parser

        def declarator(self):
            return self.getTypedRuleContext(CParser.DeclaratorContext,0)


        def constantExpression(self):
            return self.getTypedRuleContext(CParser.ConstantExpressionContext,0)


        def getRuleIndex(self):
            return CParser.RULE_structDeclarator

        def enterRule(self, listener):
            if isinstance( listener, CListener ):
                listener.enterStructDeclarator(self)

        def exitRule(self, listener):
            if isinstance( listener, CListener ):
                listener.exitStructDeclarator(self)

        def accept(self, visitor):
            if isinstance( visitor, CVisitor ):
                return visitor.visitStructDeclarator(self)
            else:
                return visitor.visitChildren(self)




    def structDeclarator(self):

        localctx = CParser.StructDeclaratorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_structDeclarator)
        self._la = 0 # Token type
        try:
            self.state = 340
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 334
                self.declarator()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 336
                _la = self._input.LA(1)
                if ((((_la - 51)) & ~0x3f) == 0 and ((1 << (_la - 51)) & ((1 << (CParser.LeftParen - 51)) | (1 << (CParser.Star - 51)) | (1 << (CParser.Identifier - 51)))) != 0):
                    self.state = 335
                    self.declarator()


                self.state = 338
                self.match(CParser.Colon)
                self.state = 339
                self.constantExpression()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class EnumSpecifierContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(CParser.EnumSpecifierContext, self).__init__(parent, invokingState)
            self.parser = parser

        def enumeratorList(self):
            return self.getTypedRuleContext(CParser.EnumeratorListContext,0)


        def Identifier(self):
            return self.getToken(CParser.Identifier, 0)

        def getRuleIndex(self):
            return CParser.RULE_enumSpecifier

        def enterRule(self, listener):
            if isinstance( listener, CListener ):
                listener.enterEnumSpecifier(self)

        def exitRule(self, listener):
            if isinstance( listener, CListener ):
                listener.exitEnumSpecifier(self)

        def accept(self, visitor):
            if isinstance( visitor, CVisitor ):
                return visitor.visitEnumSpecifier(self)
            else:
                return visitor.visitChildren(self)




    def enumSpecifier(self):

        localctx = CParser.EnumSpecifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_enumSpecifier)
        self._la = 0 # Token type
        try:
            self.state = 361
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 342
                self.match(CParser.Enum)
                self.state = 344
                _la = self._input.LA(1)
                if _la==CParser.Identifier:
                    self.state = 343
                    self.match(CParser.Identifier)


                self.state = 346
                self.match(CParser.LeftBrace)
                self.state = 347
                self.enumeratorList()
                self.state = 348
                self.match(CParser.RightBrace)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 350
                self.match(CParser.Enum)
                self.state = 352
                _la = self._input.LA(1)
                if _la==CParser.Identifier:
                    self.state = 351
                    self.match(CParser.Identifier)


                self.state = 354
                self.match(CParser.LeftBrace)
                self.state = 355
                self.enumeratorList()
                self.state = 356
                self.match(CParser.Comma)
                self.state = 357
                self.match(CParser.RightBrace)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 359
                self.match(CParser.Enum)
                self.state = 360
                self.match(CParser.Identifier)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class EnumeratorListContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(CParser.EnumeratorListContext, self).__init__(parent, invokingState)
            self.parser = parser

        def enumerator(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(CParser.EnumeratorContext)
            else:
                return self.getTypedRuleContext(CParser.EnumeratorContext,i)


        def getRuleIndex(self):
            return CParser.RULE_enumeratorList

        def enterRule(self, listener):
            if isinstance( listener, CListener ):
                listener.enterEnumeratorList(self)

        def exitRule(self, listener):
            if isinstance( listener, CListener ):
                listener.exitEnumeratorList(self)

        def accept(self, visitor):
            if isinstance( visitor, CVisitor ):
                return visitor.visitEnumeratorList(self)
            else:
                return visitor.visitChildren(self)




    def enumeratorList(self):

        localctx = CParser.EnumeratorListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_enumeratorList)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 363
            self.enumerator()
            self.state = 368
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,33,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 364
                    self.match(CParser.Comma)
                    self.state = 365
                    self.enumerator() 
                self.state = 370
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,33,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class EnumeratorContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(CParser.EnumeratorContext, self).__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(CParser.Identifier, 0)

        def constantExpression(self):
            return self.getTypedRuleContext(CParser.ConstantExpressionContext,0)


        def getRuleIndex(self):
            return CParser.RULE_enumerator

        def enterRule(self, listener):
            if isinstance( listener, CListener ):
                listener.enterEnumerator(self)

        def exitRule(self, listener):
            if isinstance( listener, CListener ):
                listener.exitEnumerator(self)

        def accept(self, visitor):
            if isinstance( visitor, CVisitor ):
                return visitor.visitEnumerator(self)
            else:
                return visitor.visitChildren(self)




    def enumerator(self):

        localctx = CParser.EnumeratorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_enumerator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 371
            self.match(CParser.Identifier)
            self.state = 374
            _la = self._input.LA(1)
            if _la==CParser.Assign:
                self.state = 372
                self.match(CParser.Assign)
                self.state = 373
                self.constantExpression()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class AtomicTypeSpecifierContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(CParser.AtomicTypeSpecifierContext, self).__init__(parent, invokingState)
            self.parser = parser

        def typeName(self):
            return self.getTypedRuleContext(CParser.TypeNameContext,0)


        def getRuleIndex(self):
            return CParser.RULE_atomicTypeSpecifier

        def enterRule(self, listener):
            if isinstance( listener, CListener ):
                listener.enterAtomicTypeSpecifier(self)

        def exitRule(self, listener):
            if isinstance( listener, CListener ):
                listener.exitAtomicTypeSpecifier(self)

        def accept(self, visitor):
            if isinstance( visitor, CVisitor ):
                return visitor.visitAtomicTypeSpecifier(self)
            else:
                return visitor.visitChildren(self)




    def atomicTypeSpecifier(self):

        localctx = CParser.AtomicTypeSpecifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_atomicTypeSpecifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 376
            self.match(CParser.Atomic)
            self.state = 377
            self.match(CParser.LeftParen)
            self.state = 378
            self.typeName()
            self.state = 379
            self.match(CParser.RightParen)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class TypeQualifierContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(CParser.TypeQualifierContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CParser.RULE_typeQualifier

        def enterRule(self, listener):
            if isinstance( listener, CListener ):
                listener.enterTypeQualifier(self)

        def exitRule(self, listener):
            if isinstance( listener, CListener ):
                listener.exitTypeQualifier(self)

        def accept(self, visitor):
            if isinstance( visitor, CVisitor ):
                return visitor.visitTypeQualifier(self)
            else:
                return visitor.visitChildren(self)




    def typeQualifier(self):

        localctx = CParser.TypeQualifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_typeQualifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 381
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CParser.Const) | (1 << CParser.Restrict) | (1 << CParser.Volatile) | (1 << CParser.Atomic))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class FunctionSpecifierContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(CParser.FunctionSpecifierContext, self).__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(CParser.Identifier, 0)

        def getRuleIndex(self):
            return CParser.RULE_functionSpecifier

        def enterRule(self, listener):
            if isinstance( listener, CListener ):
                listener.enterFunctionSpecifier(self)

        def exitRule(self, listener):
            if isinstance( listener, CListener ):
                listener.exitFunctionSpecifier(self)

        def accept(self, visitor):
            if isinstance( visitor, CVisitor ):
                return visitor.visitFunctionSpecifier(self)
            else:
                return visitor.visitChildren(self)




    def functionSpecifier(self):

        localctx = CParser.FunctionSpecifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_functionSpecifier)
        self._la = 0 # Token type
        try:
            self.state = 388
            token = self._input.LA(1)
            if token in [CParser.T__4, CParser.Inline, CParser.Noreturn]:
                self.enterOuterAlt(localctx, 1)
                self.state = 383
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CParser.T__4) | (1 << CParser.Inline) | (1 << CParser.Noreturn))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self.consume()

            elif token in [CParser.T__5]:
                self.enterOuterAlt(localctx, 2)
                self.state = 384
                self.match(CParser.T__5)
                self.state = 385
                self.match(CParser.LeftParen)
                self.state = 386
                self.match(CParser.Identifier)
                self.state = 387
                self.match(CParser.RightParen)

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class AlignmentSpecifierContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(CParser.AlignmentSpecifierContext, self).__init__(parent, invokingState)
            self.parser = parser

        def typeName(self):
            return self.getTypedRuleContext(CParser.TypeNameContext,0)


        def constantExpression(self):
            return self.getTypedRuleContext(CParser.ConstantExpressionContext,0)


        def getRuleIndex(self):
            return CParser.RULE_alignmentSpecifier

        def enterRule(self, listener):
            if isinstance( listener, CListener ):
                listener.enterAlignmentSpecifier(self)

        def exitRule(self, listener):
            if isinstance( listener, CListener ):
                listener.exitAlignmentSpecifier(self)

        def accept(self, visitor):
            if isinstance( visitor, CVisitor ):
                return visitor.visitAlignmentSpecifier(self)
            else:
                return visitor.visitChildren(self)




    def alignmentSpecifier(self):

        localctx = CParser.AlignmentSpecifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_alignmentSpecifier)
        try:
            self.state = 400
            la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 390
                self.match(CParser.Alignas)
                self.state = 391
                self.match(CParser.LeftParen)
                self.state = 392
                self.typeName()
                self.state = 393
                self.match(CParser.RightParen)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 395
                self.match(CParser.Alignas)
                self.state = 396
                self.match(CParser.LeftParen)
                self.state = 397
                self.constantExpression()
                self.state = 398
                self.match(CParser.RightParen)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class DeclaratorContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(CParser.DeclaratorContext, self).__init__(parent, invokingState)
            self.parser = parser

        def directDeclarator(self):
            return self.getTypedRuleContext(CParser.DirectDeclaratorContext,0)


        def pointer(self):
            return self.getTypedRuleContext(CParser.PointerContext,0)


        def getRuleIndex(self):
            return CParser.RULE_declarator

        def enterRule(self, listener):
            if isinstance( listener, CListener ):
                listener.enterDeclarator(self)

        def exitRule(self, listener):
            if isinstance( listener, CListener ):
                listener.exitDeclarator(self)

        def accept(self, visitor):
            if isinstance( visitor, CVisitor ):
                return visitor.visitDeclarator(self)
            else:
                return visitor.visitChildren(self)




    def declarator(self):

        localctx = CParser.DeclaratorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_declarator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 403
            _la = self._input.LA(1)
            if _la==CParser.Star:
                self.state = 402
                self.pointer()


            self.state = 405
            self.directDeclarator(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class DirectDeclaratorContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(CParser.DirectDeclaratorContext, self).__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(CParser.Identifier, 0)

        def declarator(self):
            return self.getTypedRuleContext(CParser.DeclaratorContext,0)


        def directDeclarator(self):
            return self.getTypedRuleContext(CParser.DirectDeclaratorContext,0)


        def typeQualifier(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(CParser.TypeQualifierContext)
            else:
                return self.getTypedRuleContext(CParser.TypeQualifierContext,i)


        def assignmentExpression(self):
            return self.getTypedRuleContext(CParser.AssignmentExpressionContext,0)


        def parameterTypeList(self):
            return self.getTypedRuleContext(CParser.ParameterTypeListContext,0)


        def identifierList(self):
            return self.getTypedRuleContext(CParser.IdentifierListContext,0)


        def getRuleIndex(self):
            return CParser.RULE_directDeclarator

        def enterRule(self, listener):
            if isinstance( listener, CListener ):
                listener.enterDirectDeclarator(self)

        def exitRule(self, listener):
            if isinstance( listener, CListener ):
                listener.exitDirectDeclarator(self)

        def accept(self, visitor):
            if isinstance( visitor, CVisitor ):
                return visitor.visitDirectDeclarator(self)
            else:
                return visitor.visitChildren(self)



    def directDeclarator(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CParser.DirectDeclaratorContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 56
        self.enterRecursionRule(localctx, 56, self.RULE_directDeclarator, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 413
            token = self._input.LA(1)
            if token in [CParser.Identifier]:
                self.state = 408
                self.match(CParser.Identifier)

            elif token in [CParser.LeftParen]:
                self.state = 409
                self.match(CParser.LeftParen)
                self.state = 410
                self.declarator()
                self.state = 411
                self.match(CParser.RightParen)

            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 473
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,46,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 471
                    la_ = self._interp.adaptivePredict(self._input,45,self._ctx)
                    if la_ == 1:
                        localctx = CParser.DirectDeclaratorContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_directDeclarator)
                        self.state = 415
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 416
                        self.match(CParser.LeftBracket)
                        self.state = 420
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CParser.Const) | (1 << CParser.Restrict) | (1 << CParser.Volatile) | (1 << CParser.Atomic))) != 0):
                            self.state = 417
                            self.typeQualifier()
                            self.state = 422
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)

                        self.state = 424
                        _la = self._input.LA(1)
                        if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CParser.Sizeof) | (1 << CParser.Alignof) | (1 << CParser.LeftParen) | (1 << CParser.Plus))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (CParser.PlusPlus - 64)) | (1 << (CParser.Minus - 64)) | (1 << (CParser.MinusMinus - 64)) | (1 << (CParser.Star - 64)) | (1 << (CParser.And - 64)) | (1 << (CParser.Not - 64)) | (1 << (CParser.Tilde - 64)) | (1 << (CParser.Identifier - 64)) | (1 << (CParser.Constant - 64)) | (1 << (CParser.StringLiteral - 64)))) != 0):
                            self.state = 423
                            self.assignmentExpression()


                        self.state = 426
                        self.match(CParser.RightBracket)
                        pass

                    elif la_ == 2:
                        localctx = CParser.DirectDeclaratorContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_directDeclarator)
                        self.state = 427
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 428
                        self.match(CParser.LeftBracket)
                        self.state = 429
                        self.match(CParser.Static)
                        self.state = 433
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CParser.Const) | (1 << CParser.Restrict) | (1 << CParser.Volatile) | (1 << CParser.Atomic))) != 0):
                            self.state = 430
                            self.typeQualifier()
                            self.state = 435
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)

                        self.state = 436
                        self.assignmentExpression()
                        self.state = 437
                        self.match(CParser.RightBracket)
                        pass

                    elif la_ == 3:
                        localctx = CParser.DirectDeclaratorContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_directDeclarator)
                        self.state = 439
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 440
                        self.match(CParser.LeftBracket)
                        self.state = 442 
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        while True:
                            self.state = 441
                            self.typeQualifier()
                            self.state = 444 
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)
                            if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CParser.Const) | (1 << CParser.Restrict) | (1 << CParser.Volatile) | (1 << CParser.Atomic))) != 0)):
                                break

                        self.state = 446
                        self.match(CParser.Static)
                        self.state = 447
                        self.assignmentExpression()
                        self.state = 448
                        self.match(CParser.RightBracket)
                        pass

                    elif la_ == 4:
                        localctx = CParser.DirectDeclaratorContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_directDeclarator)
                        self.state = 450
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 451
                        self.match(CParser.LeftBracket)
                        self.state = 455
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CParser.Const) | (1 << CParser.Restrict) | (1 << CParser.Volatile) | (1 << CParser.Atomic))) != 0):
                            self.state = 452
                            self.typeQualifier()
                            self.state = 457
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)

                        self.state = 458
                        self.match(CParser.Star)
                        self.state = 459
                        self.match(CParser.RightBracket)
                        pass

                    elif la_ == 5:
                        localctx = CParser.DirectDeclaratorContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_directDeclarator)
                        self.state = 460
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 461
                        self.match(CParser.LeftParen)
                        self.state = 462
                        self.parameterTypeList()
                        self.state = 463
                        self.match(CParser.RightParen)
                        pass

                    elif la_ == 6:
                        localctx = CParser.DirectDeclaratorContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_directDeclarator)
                        self.state = 465
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 466
                        self.match(CParser.LeftParen)
                        self.state = 468
                        _la = self._input.LA(1)
                        if _la==CParser.Identifier:
                            self.state = 467
                            self.identifierList()


                        self.state = 470
                        self.match(CParser.RightParen)
                        pass

             
                self.state = 475
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,46,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class PointerContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(CParser.PointerContext, self).__init__(parent, invokingState)
            self.parser = parser

        def typeQualifier(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(CParser.TypeQualifierContext)
            else:
                return self.getTypedRuleContext(CParser.TypeQualifierContext,i)


        def pointer(self):
            return self.getTypedRuleContext(CParser.PointerContext,0)


        def getRuleIndex(self):
            return CParser.RULE_pointer

        def enterRule(self, listener):
            if isinstance( listener, CListener ):
                listener.enterPointer(self)

        def exitRule(self, listener):
            if isinstance( listener, CListener ):
                listener.exitPointer(self)

        def accept(self, visitor):
            if isinstance( visitor, CVisitor ):
                return visitor.visitPointer(self)
            else:
                return visitor.visitChildren(self)




    def pointer(self):

        localctx = CParser.PointerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_pointer)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 476
            self.match(CParser.Star)
            self.state = 480
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CParser.Const) | (1 << CParser.Restrict) | (1 << CParser.Volatile) | (1 << CParser.Atomic))) != 0):
                self.state = 477
                self.typeQualifier()
                self.state = 482
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 484
            _la = self._input.LA(1)
            if _la==CParser.Star:
                self.state = 483
                self.pointer()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ParameterTypeListContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(CParser.ParameterTypeListContext, self).__init__(parent, invokingState)
            self.parser = parser

        def parameterDeclaration(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(CParser.ParameterDeclarationContext)
            else:
                return self.getTypedRuleContext(CParser.ParameterDeclarationContext,i)


        def getRuleIndex(self):
            return CParser.RULE_parameterTypeList

        def enterRule(self, listener):
            if isinstance( listener, CListener ):
                listener.enterParameterTypeList(self)

        def exitRule(self, listener):
            if isinstance( listener, CListener ):
                listener.exitParameterTypeList(self)

        def accept(self, visitor):
            if isinstance( visitor, CVisitor ):
                return visitor.visitParameterTypeList(self)
            else:
                return visitor.visitChildren(self)




    def parameterTypeList(self):

        localctx = CParser.ParameterTypeListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_parameterTypeList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 486
            self.parameterDeclaration()
            self.state = 491
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,49,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 487
                    self.match(CParser.Comma)
                    self.state = 488
                    self.parameterDeclaration() 
                self.state = 493
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,49,self._ctx)

            self.state = 496
            _la = self._input.LA(1)
            if _la==CParser.Comma:
                self.state = 494
                self.match(CParser.Comma)
                self.state = 495
                self.match(CParser.Ellipsis)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ParameterDeclarationContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(CParser.ParameterDeclarationContext, self).__init__(parent, invokingState)
            self.parser = parser

        def declarator(self):
            return self.getTypedRuleContext(CParser.DeclaratorContext,0)


        def declarationSpecifier(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(CParser.DeclarationSpecifierContext)
            else:
                return self.getTypedRuleContext(CParser.DeclarationSpecifierContext,i)


        def abstractDeclarator(self):
            return self.getTypedRuleContext(CParser.AbstractDeclaratorContext,0)


        def getRuleIndex(self):
            return CParser.RULE_parameterDeclaration

        def enterRule(self, listener):
            if isinstance( listener, CListener ):
                listener.enterParameterDeclaration(self)

        def exitRule(self, listener):
            if isinstance( listener, CListener ):
                listener.exitParameterDeclaration(self)

        def accept(self, visitor):
            if isinstance( visitor, CVisitor ):
                return visitor.visitParameterDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def parameterDeclaration(self):

        localctx = CParser.ParameterDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_parameterDeclaration)
        self._la = 0 # Token type
        try:
            self.state = 513
            la_ = self._interp.adaptivePredict(self._input,54,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 499 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 498
                        self.declarationSpecifier()

                    else:
                        raise NoViableAltException(self)
                    self.state = 501 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,51,self._ctx)

                self.state = 503
                self.declarator()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 506 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 505
                    self.declarationSpecifier()
                    self.state = 508 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CParser.T__0) | (1 << CParser.T__1) | (1 << CParser.T__2) | (1 << CParser.T__3) | (1 << CParser.T__4) | (1 << CParser.T__5) | (1 << CParser.Auto) | (1 << CParser.Char) | (1 << CParser.Const) | (1 << CParser.Double) | (1 << CParser.Enum) | (1 << CParser.Extern) | (1 << CParser.Float) | (1 << CParser.Inline) | (1 << CParser.Int) | (1 << CParser.Long) | (1 << CParser.Register) | (1 << CParser.Restrict) | (1 << CParser.Short) | (1 << CParser.Signed) | (1 << CParser.Static) | (1 << CParser.Struct) | (1 << CParser.Typedef) | (1 << CParser.Union) | (1 << CParser.Unsigned) | (1 << CParser.Void) | (1 << CParser.Volatile) | (1 << CParser.Alignas) | (1 << CParser.Atomic) | (1 << CParser.Bool) | (1 << CParser.Complex) | (1 << CParser.Noreturn) | (1 << CParser.ThreadLocal))) != 0) or _la==CParser.Identifier):
                        break

                self.state = 511
                _la = self._input.LA(1)
                if ((((_la - 51)) & ~0x3f) == 0 and ((1 << (_la - 51)) & ((1 << (CParser.LeftParen - 51)) | (1 << (CParser.LeftBracket - 51)) | (1 << (CParser.Star - 51)))) != 0):
                    self.state = 510
                    self.abstractDeclarator()


                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class IdentifierListContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(CParser.IdentifierListContext, self).__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self, i=None):
            if i is None:
                return self.getTokens(CParser.Identifier)
            else:
                return self.getToken(CParser.Identifier, i)

        def getRuleIndex(self):
            return CParser.RULE_identifierList

        def enterRule(self, listener):
            if isinstance( listener, CListener ):
                listener.enterIdentifierList(self)

        def exitRule(self, listener):
            if isinstance( listener, CListener ):
                listener.exitIdentifierList(self)

        def accept(self, visitor):
            if isinstance( visitor, CVisitor ):
                return visitor.visitIdentifierList(self)
            else:
                return visitor.visitChildren(self)




    def identifierList(self):

        localctx = CParser.IdentifierListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_identifierList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 515
            self.match(CParser.Identifier)
            self.state = 520
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CParser.Comma:
                self.state = 516
                self.match(CParser.Comma)
                self.state = 517
                self.match(CParser.Identifier)
                self.state = 522
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class TypeNameContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(CParser.TypeNameContext, self).__init__(parent, invokingState)
            self.parser = parser

        def specifierQualifierList(self):
            return self.getTypedRuleContext(CParser.SpecifierQualifierListContext,0)


        def abstractDeclarator(self):
            return self.getTypedRuleContext(CParser.AbstractDeclaratorContext,0)


        def getRuleIndex(self):
            return CParser.RULE_typeName

        def enterRule(self, listener):
            if isinstance( listener, CListener ):
                listener.enterTypeName(self)

        def exitRule(self, listener):
            if isinstance( listener, CListener ):
                listener.exitTypeName(self)

        def accept(self, visitor):
            if isinstance( visitor, CVisitor ):
                return visitor.visitTypeName(self)
            else:
                return visitor.visitChildren(self)




    def typeName(self):

        localctx = CParser.TypeNameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_typeName)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 523
            self.specifierQualifierList()
            self.state = 525
            _la = self._input.LA(1)
            if ((((_la - 51)) & ~0x3f) == 0 and ((1 << (_la - 51)) & ((1 << (CParser.LeftParen - 51)) | (1 << (CParser.LeftBracket - 51)) | (1 << (CParser.Star - 51)))) != 0):
                self.state = 524
                self.abstractDeclarator()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class AbstractDeclaratorContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(CParser.AbstractDeclaratorContext, self).__init__(parent, invokingState)
            self.parser = parser

        def pointer(self):
            return self.getTypedRuleContext(CParser.PointerContext,0)


        def directAbstractDeclarator(self):
            return self.getTypedRuleContext(CParser.DirectAbstractDeclaratorContext,0)


        def getRuleIndex(self):
            return CParser.RULE_abstractDeclarator

        def enterRule(self, listener):
            if isinstance( listener, CListener ):
                listener.enterAbstractDeclarator(self)

        def exitRule(self, listener):
            if isinstance( listener, CListener ):
                listener.exitAbstractDeclarator(self)

        def accept(self, visitor):
            if isinstance( visitor, CVisitor ):
                return visitor.visitAbstractDeclarator(self)
            else:
                return visitor.visitChildren(self)




    def abstractDeclarator(self):

        localctx = CParser.AbstractDeclaratorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_abstractDeclarator)
        self._la = 0 # Token type
        try:
            self.state = 532
            la_ = self._interp.adaptivePredict(self._input,58,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 527
                self.pointer()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 529
                _la = self._input.LA(1)
                if _la==CParser.Star:
                    self.state = 528
                    self.pointer()


                self.state = 531
                self.directAbstractDeclarator(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class DirectAbstractDeclaratorContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(CParser.DirectAbstractDeclaratorContext, self).__init__(parent, invokingState)
            self.parser = parser

        def abstractDeclarator(self):
            return self.getTypedRuleContext(CParser.AbstractDeclaratorContext,0)


        def typeQualifier(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(CParser.TypeQualifierContext)
            else:
                return self.getTypedRuleContext(CParser.TypeQualifierContext,i)


        def assignmentExpression(self):
            return self.getTypedRuleContext(CParser.AssignmentExpressionContext,0)


        def parameterTypeList(self):
            return self.getTypedRuleContext(CParser.ParameterTypeListContext,0)


        def directAbstractDeclarator(self):
            return self.getTypedRuleContext(CParser.DirectAbstractDeclaratorContext,0)


        def getRuleIndex(self):
            return CParser.RULE_directAbstractDeclarator

        def enterRule(self, listener):
            if isinstance( listener, CListener ):
                listener.enterDirectAbstractDeclarator(self)

        def exitRule(self, listener):
            if isinstance( listener, CListener ):
                listener.exitDirectAbstractDeclarator(self)

        def accept(self, visitor):
            if isinstance( visitor, CVisitor ):
                return visitor.visitDirectAbstractDeclarator(self)
            else:
                return visitor.visitChildren(self)



    def directAbstractDeclarator(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CParser.DirectAbstractDeclaratorContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 70
        self.enterRecursionRule(localctx, 70, self.RULE_directAbstractDeclarator, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 580
            la_ = self._interp.adaptivePredict(self._input,64,self._ctx)
            if la_ == 1:
                self.state = 535
                self.match(CParser.LeftParen)
                self.state = 536
                self.abstractDeclarator()
                self.state = 537
                self.match(CParser.RightParen)
                pass

            elif la_ == 2:
                self.state = 539
                self.match(CParser.LeftBracket)
                self.state = 543
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CParser.Const) | (1 << CParser.Restrict) | (1 << CParser.Volatile) | (1 << CParser.Atomic))) != 0):
                    self.state = 540
                    self.typeQualifier()
                    self.state = 545
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 547
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CParser.Sizeof) | (1 << CParser.Alignof) | (1 << CParser.LeftParen) | (1 << CParser.Plus))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (CParser.PlusPlus - 64)) | (1 << (CParser.Minus - 64)) | (1 << (CParser.MinusMinus - 64)) | (1 << (CParser.Star - 64)) | (1 << (CParser.And - 64)) | (1 << (CParser.Not - 64)) | (1 << (CParser.Tilde - 64)) | (1 << (CParser.Identifier - 64)) | (1 << (CParser.Constant - 64)) | (1 << (CParser.StringLiteral - 64)))) != 0):
                    self.state = 546
                    self.assignmentExpression()


                self.state = 549
                self.match(CParser.RightBracket)
                pass

            elif la_ == 3:
                self.state = 550
                self.match(CParser.LeftBracket)
                self.state = 551
                self.match(CParser.Static)
                self.state = 555
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CParser.Const) | (1 << CParser.Restrict) | (1 << CParser.Volatile) | (1 << CParser.Atomic))) != 0):
                    self.state = 552
                    self.typeQualifier()
                    self.state = 557
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 558
                self.assignmentExpression()
                self.state = 559
                self.match(CParser.RightBracket)
                pass

            elif la_ == 4:
                self.state = 561
                self.match(CParser.LeftBracket)
                self.state = 565
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CParser.Const) | (1 << CParser.Restrict) | (1 << CParser.Volatile) | (1 << CParser.Atomic))) != 0):
                    self.state = 562
                    self.typeQualifier()
                    self.state = 567
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 568
                self.match(CParser.Static)
                self.state = 569
                self.assignmentExpression()
                self.state = 570
                self.match(CParser.RightBracket)
                pass

            elif la_ == 5:
                self.state = 572
                self.match(CParser.LeftBracket)
                self.state = 573
                self.match(CParser.Star)
                self.state = 574
                self.match(CParser.RightBracket)
                pass

            elif la_ == 6:
                self.state = 575
                self.match(CParser.LeftParen)
                self.state = 577
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CParser.T__0) | (1 << CParser.T__1) | (1 << CParser.T__2) | (1 << CParser.T__3) | (1 << CParser.T__4) | (1 << CParser.T__5) | (1 << CParser.Auto) | (1 << CParser.Char) | (1 << CParser.Const) | (1 << CParser.Double) | (1 << CParser.Enum) | (1 << CParser.Extern) | (1 << CParser.Float) | (1 << CParser.Inline) | (1 << CParser.Int) | (1 << CParser.Long) | (1 << CParser.Register) | (1 << CParser.Restrict) | (1 << CParser.Short) | (1 << CParser.Signed) | (1 << CParser.Static) | (1 << CParser.Struct) | (1 << CParser.Typedef) | (1 << CParser.Union) | (1 << CParser.Unsigned) | (1 << CParser.Void) | (1 << CParser.Volatile) | (1 << CParser.Alignas) | (1 << CParser.Atomic) | (1 << CParser.Bool) | (1 << CParser.Complex) | (1 << CParser.Noreturn) | (1 << CParser.ThreadLocal))) != 0) or _la==CParser.Identifier:
                    self.state = 576
                    self.parameterTypeList()


                self.state = 579
                self.match(CParser.RightParen)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 629
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,71,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 627
                    la_ = self._interp.adaptivePredict(self._input,70,self._ctx)
                    if la_ == 1:
                        localctx = CParser.DirectAbstractDeclaratorContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_directAbstractDeclarator)
                        self.state = 582
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 583
                        self.match(CParser.LeftBracket)
                        self.state = 587
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CParser.Const) | (1 << CParser.Restrict) | (1 << CParser.Volatile) | (1 << CParser.Atomic))) != 0):
                            self.state = 584
                            self.typeQualifier()
                            self.state = 589
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)

                        self.state = 591
                        _la = self._input.LA(1)
                        if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CParser.Sizeof) | (1 << CParser.Alignof) | (1 << CParser.LeftParen) | (1 << CParser.Plus))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (CParser.PlusPlus - 64)) | (1 << (CParser.Minus - 64)) | (1 << (CParser.MinusMinus - 64)) | (1 << (CParser.Star - 64)) | (1 << (CParser.And - 64)) | (1 << (CParser.Not - 64)) | (1 << (CParser.Tilde - 64)) | (1 << (CParser.Identifier - 64)) | (1 << (CParser.Constant - 64)) | (1 << (CParser.StringLiteral - 64)))) != 0):
                            self.state = 590
                            self.assignmentExpression()


                        self.state = 593
                        self.match(CParser.RightBracket)
                        pass

                    elif la_ == 2:
                        localctx = CParser.DirectAbstractDeclaratorContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_directAbstractDeclarator)
                        self.state = 594
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 595
                        self.match(CParser.LeftBracket)
                        self.state = 596
                        self.match(CParser.Static)
                        self.state = 600
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CParser.Const) | (1 << CParser.Restrict) | (1 << CParser.Volatile) | (1 << CParser.Atomic))) != 0):
                            self.state = 597
                            self.typeQualifier()
                            self.state = 602
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)

                        self.state = 603
                        self.assignmentExpression()
                        self.state = 604
                        self.match(CParser.RightBracket)
                        pass

                    elif la_ == 3:
                        localctx = CParser.DirectAbstractDeclaratorContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_directAbstractDeclarator)
                        self.state = 606
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 607
                        self.match(CParser.LeftBracket)
                        self.state = 609 
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        while True:
                            self.state = 608
                            self.typeQualifier()
                            self.state = 611 
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)
                            if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CParser.Const) | (1 << CParser.Restrict) | (1 << CParser.Volatile) | (1 << CParser.Atomic))) != 0)):
                                break

                        self.state = 613
                        self.match(CParser.Static)
                        self.state = 614
                        self.assignmentExpression()
                        self.state = 615
                        self.match(CParser.RightBracket)
                        pass

                    elif la_ == 4:
                        localctx = CParser.DirectAbstractDeclaratorContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_directAbstractDeclarator)
                        self.state = 617
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 618
                        self.match(CParser.LeftBracket)
                        self.state = 619
                        self.match(CParser.Star)
                        self.state = 620
                        self.match(CParser.RightBracket)
                        pass

                    elif la_ == 5:
                        localctx = CParser.DirectAbstractDeclaratorContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_directAbstractDeclarator)
                        self.state = 621
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 622
                        self.match(CParser.LeftParen)
                        self.state = 624
                        _la = self._input.LA(1)
                        if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CParser.T__0) | (1 << CParser.T__1) | (1 << CParser.T__2) | (1 << CParser.T__3) | (1 << CParser.T__4) | (1 << CParser.T__5) | (1 << CParser.Auto) | (1 << CParser.Char) | (1 << CParser.Const) | (1 << CParser.Double) | (1 << CParser.Enum) | (1 << CParser.Extern) | (1 << CParser.Float) | (1 << CParser.Inline) | (1 << CParser.Int) | (1 << CParser.Long) | (1 << CParser.Register) | (1 << CParser.Restrict) | (1 << CParser.Short) | (1 << CParser.Signed) | (1 << CParser.Static) | (1 << CParser.Struct) | (1 << CParser.Typedef) | (1 << CParser.Union) | (1 << CParser.Unsigned) | (1 << CParser.Void) | (1 << CParser.Volatile) | (1 << CParser.Alignas) | (1 << CParser.Atomic) | (1 << CParser.Bool) | (1 << CParser.Complex) | (1 << CParser.Noreturn) | (1 << CParser.ThreadLocal))) != 0) or _la==CParser.Identifier:
                            self.state = 623
                            self.parameterTypeList()


                        self.state = 626
                        self.match(CParser.RightParen)
                        pass

             
                self.state = 631
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,71,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class TypedefNameContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(CParser.TypedefNameContext, self).__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(CParser.Identifier, 0)

        def getRuleIndex(self):
            return CParser.RULE_typedefName

        def enterRule(self, listener):
            if isinstance( listener, CListener ):
                listener.enterTypedefName(self)

        def exitRule(self, listener):
            if isinstance( listener, CListener ):
                listener.exitTypedefName(self)

        def accept(self, visitor):
            if isinstance( visitor, CVisitor ):
                return visitor.visitTypedefName(self)
            else:
                return visitor.visitChildren(self)




    def typedefName(self):

        localctx = CParser.TypedefNameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_typedefName)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 632
            self.match(CParser.Identifier)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class InitializerContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(CParser.InitializerContext, self).__init__(parent, invokingState)
            self.parser = parser

        def assignmentExpression(self):
            return self.getTypedRuleContext(CParser.AssignmentExpressionContext,0)


        def initializerList(self):
            return self.getTypedRuleContext(CParser.InitializerListContext,0)


        def getRuleIndex(self):
            return CParser.RULE_initializer

        def enterRule(self, listener):
            if isinstance( listener, CListener ):
                listener.enterInitializer(self)

        def exitRule(self, listener):
            if isinstance( listener, CListener ):
                listener.exitInitializer(self)

        def accept(self, visitor):
            if isinstance( visitor, CVisitor ):
                return visitor.visitInitializer(self)
            else:
                return visitor.visitChildren(self)




    def initializer(self):

        localctx = CParser.InitializerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_initializer)
        self._la = 0 # Token type
        try:
            self.state = 642
            token = self._input.LA(1)
            if token in [CParser.Sizeof, CParser.Alignof, CParser.LeftParen, CParser.Plus, CParser.PlusPlus, CParser.Minus, CParser.MinusMinus, CParser.Star, CParser.And, CParser.Not, CParser.Tilde, CParser.Identifier, CParser.Constant, CParser.StringLiteral]:
                self.enterOuterAlt(localctx, 1)
                self.state = 634
                self.assignmentExpression()

            elif token in [CParser.LeftBrace]:
                self.enterOuterAlt(localctx, 2)
                self.state = 635
                self.match(CParser.LeftBrace)
                self.state = 636
                self.initializerList(0)
                self.state = 638
                _la = self._input.LA(1)
                if _la==CParser.Comma:
                    self.state = 637
                    self.match(CParser.Comma)


                self.state = 640
                self.match(CParser.RightBrace)

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class InitializerListContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(CParser.InitializerListContext, self).__init__(parent, invokingState)
            self.parser = parser

        def initializer(self):
            return self.getTypedRuleContext(CParser.InitializerContext,0)


        def designation(self):
            return self.getTypedRuleContext(CParser.DesignationContext,0)


        def initializerList(self):
            return self.getTypedRuleContext(CParser.InitializerListContext,0)


        def getRuleIndex(self):
            return CParser.RULE_initializerList

        def enterRule(self, listener):
            if isinstance( listener, CListener ):
                listener.enterInitializerList(self)

        def exitRule(self, listener):
            if isinstance( listener, CListener ):
                listener.exitInitializerList(self)

        def accept(self, visitor):
            if isinstance( visitor, CVisitor ):
                return visitor.visitInitializerList(self)
            else:
                return visitor.visitChildren(self)



    def initializerList(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CParser.InitializerListContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 76
        self.enterRecursionRule(localctx, 76, self.RULE_initializerList, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 646
            _la = self._input.LA(1)
            if _la==CParser.LeftBracket or _la==CParser.Dot:
                self.state = 645
                self.designation()


            self.state = 648
            self.initializer()
            self._ctx.stop = self._input.LT(-1)
            self.state = 658
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,76,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CParser.InitializerListContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_initializerList)
                    self.state = 650
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 651
                    self.match(CParser.Comma)
                    self.state = 653
                    _la = self._input.LA(1)
                    if _la==CParser.LeftBracket or _la==CParser.Dot:
                        self.state = 652
                        self.designation()


                    self.state = 655
                    self.initializer() 
                self.state = 660
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,76,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class DesignationContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(CParser.DesignationContext, self).__init__(parent, invokingState)
            self.parser = parser

        def designator(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(CParser.DesignatorContext)
            else:
                return self.getTypedRuleContext(CParser.DesignatorContext,i)


        def getRuleIndex(self):
            return CParser.RULE_designation

        def enterRule(self, listener):
            if isinstance( listener, CListener ):
                listener.enterDesignation(self)

        def exitRule(self, listener):
            if isinstance( listener, CListener ):
                listener.exitDesignation(self)

        def accept(self, visitor):
            if isinstance( visitor, CVisitor ):
                return visitor.visitDesignation(self)
            else:
                return visitor.visitChildren(self)




    def designation(self):

        localctx = CParser.DesignationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_designation)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 662 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 661
                self.designator()
                self.state = 664 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==CParser.LeftBracket or _la==CParser.Dot):
                    break

            self.state = 666
            self.match(CParser.Assign)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class DesignatorContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(CParser.DesignatorContext, self).__init__(parent, invokingState)
            self.parser = parser

        def constantExpression(self):
            return self.getTypedRuleContext(CParser.ConstantExpressionContext,0)


        def Identifier(self):
            return self.getToken(CParser.Identifier, 0)

        def getRuleIndex(self):
            return CParser.RULE_designator

        def enterRule(self, listener):
            if isinstance( listener, CListener ):
                listener.enterDesignator(self)

        def exitRule(self, listener):
            if isinstance( listener, CListener ):
                listener.exitDesignator(self)

        def accept(self, visitor):
            if isinstance( visitor, CVisitor ):
                return visitor.visitDesignator(self)
            else:
                return visitor.visitChildren(self)




    def designator(self):

        localctx = CParser.DesignatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_designator)
        try:
            self.state = 674
            token = self._input.LA(1)
            if token in [CParser.LeftBracket]:
                self.enterOuterAlt(localctx, 1)
                self.state = 668
                self.match(CParser.LeftBracket)
                self.state = 669
                self.constantExpression()
                self.state = 670
                self.match(CParser.RightBracket)

            elif token in [CParser.Dot]:
                self.enterOuterAlt(localctx, 2)
                self.state = 672
                self.match(CParser.Dot)
                self.state = 673
                self.match(CParser.Identifier)

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class StaticAssertDeclarationContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(CParser.StaticAssertDeclarationContext, self).__init__(parent, invokingState)
            self.parser = parser

        def constantExpression(self):
            return self.getTypedRuleContext(CParser.ConstantExpressionContext,0)


        def StringLiteral(self, i=None):
            if i is None:
                return self.getTokens(CParser.StringLiteral)
            else:
                return self.getToken(CParser.StringLiteral, i)

        def getRuleIndex(self):
            return CParser.RULE_staticAssertDeclaration

        def enterRule(self, listener):
            if isinstance( listener, CListener ):
                listener.enterStaticAssertDeclaration(self)

        def exitRule(self, listener):
            if isinstance( listener, CListener ):
                listener.exitStaticAssertDeclaration(self)

        def accept(self, visitor):
            if isinstance( visitor, CVisitor ):
                return visitor.visitStaticAssertDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def staticAssertDeclaration(self):

        localctx = CParser.StaticAssertDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_staticAssertDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 676
            self.match(CParser.StaticAssert)
            self.state = 677
            self.match(CParser.LeftParen)
            self.state = 678
            self.constantExpression()
            self.state = 679
            self.match(CParser.Comma)
            self.state = 681 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 680
                self.match(CParser.StringLiteral)
                self.state = 683 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==CParser.StringLiteral):
                    break

            self.state = 685
            self.match(CParser.RightParen)
            self.state = 686
            self.match(CParser.Semi)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class StatementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(CParser.StatementContext, self).__init__(parent, invokingState)
            self.parser = parser

        def labeledStatement(self):
            return self.getTypedRuleContext(CParser.LabeledStatementContext,0)


        def compoundStatement(self):
            return self.getTypedRuleContext(CParser.CompoundStatementContext,0)


        def expressionStatement(self):
            return self.getTypedRuleContext(CParser.ExpressionStatementContext,0)


        def selectionStatement(self):
            return self.getTypedRuleContext(CParser.SelectionStatementContext,0)


        def iterationStatement(self):
            return self.getTypedRuleContext(CParser.IterationStatementContext,0)


        def jumpStatement(self):
            return self.getTypedRuleContext(CParser.JumpStatementContext,0)


        def getRuleIndex(self):
            return CParser.RULE_statement

        def enterRule(self, listener):
            if isinstance( listener, CListener ):
                listener.enterStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, CListener ):
                listener.exitStatement(self)

        def accept(self, visitor):
            if isinstance( visitor, CVisitor ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = CParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_statement)
        try:
            self.state = 694
            la_ = self._interp.adaptivePredict(self._input,80,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 688
                self.labeledStatement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 689
                self.compoundStatement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 690
                self.expressionStatement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 691
                self.selectionStatement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 692
                self.iterationStatement()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 693
                self.jumpStatement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class LabeledStatementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(CParser.LabeledStatementContext, self).__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(CParser.Identifier, 0)

        def statement(self):
            return self.getTypedRuleContext(CParser.StatementContext,0)


        def constantExpression(self):
            return self.getTypedRuleContext(CParser.ConstantExpressionContext,0)


        def getRuleIndex(self):
            return CParser.RULE_labeledStatement

        def enterRule(self, listener):
            if isinstance( listener, CListener ):
                listener.enterLabeledStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, CListener ):
                listener.exitLabeledStatement(self)

        def accept(self, visitor):
            if isinstance( visitor, CVisitor ):
                return visitor.visitLabeledStatement(self)
            else:
                return visitor.visitChildren(self)




    def labeledStatement(self):

        localctx = CParser.LabeledStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_labeledStatement)
        try:
            self.state = 707
            token = self._input.LA(1)
            if token in [CParser.Identifier]:
                self.enterOuterAlt(localctx, 1)
                self.state = 696
                self.match(CParser.Identifier)
                self.state = 697
                self.match(CParser.Colon)
                self.state = 698
                self.statement()

            elif token in [CParser.Case]:
                self.enterOuterAlt(localctx, 2)
                self.state = 699
                self.match(CParser.Case)
                self.state = 700
                self.constantExpression()
                self.state = 701
                self.match(CParser.Colon)
                self.state = 702
                self.statement()

            elif token in [CParser.Default]:
                self.enterOuterAlt(localctx, 3)
                self.state = 704
                self.match(CParser.Default)
                self.state = 705
                self.match(CParser.Colon)
                self.state = 706
                self.statement()

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class CompoundStatementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(CParser.CompoundStatementContext, self).__init__(parent, invokingState)
            self.parser = parser

        def blockItem(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(CParser.BlockItemContext)
            else:
                return self.getTypedRuleContext(CParser.BlockItemContext,i)


        def getRuleIndex(self):
            return CParser.RULE_compoundStatement

        def enterRule(self, listener):
            if isinstance( listener, CListener ):
                listener.enterCompoundStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, CListener ):
                listener.exitCompoundStatement(self)

        def accept(self, visitor):
            if isinstance( visitor, CVisitor ):
                return visitor.visitCompoundStatement(self)
            else:
                return visitor.visitChildren(self)




    def compoundStatement(self):

        localctx = CParser.CompoundStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_compoundStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 709
            self.match(CParser.LeftBrace)
            self.state = 713
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CParser.T__0) | (1 << CParser.T__1) | (1 << CParser.T__2) | (1 << CParser.T__3) | (1 << CParser.T__4) | (1 << CParser.T__5) | (1 << CParser.Auto) | (1 << CParser.Break) | (1 << CParser.Case) | (1 << CParser.Char) | (1 << CParser.Const) | (1 << CParser.Continue) | (1 << CParser.Default) | (1 << CParser.Do) | (1 << CParser.Double) | (1 << CParser.Enum) | (1 << CParser.Extern) | (1 << CParser.Float) | (1 << CParser.For) | (1 << CParser.Goto) | (1 << CParser.If) | (1 << CParser.Inline) | (1 << CParser.Int) | (1 << CParser.Long) | (1 << CParser.Register) | (1 << CParser.Restrict) | (1 << CParser.Return) | (1 << CParser.Short) | (1 << CParser.Signed) | (1 << CParser.Sizeof) | (1 << CParser.Static) | (1 << CParser.Struct) | (1 << CParser.Switch) | (1 << CParser.Typedef) | (1 << CParser.Union) | (1 << CParser.Unsigned) | (1 << CParser.Void) | (1 << CParser.Volatile) | (1 << CParser.While) | (1 << CParser.Alignas) | (1 << CParser.Alignof) | (1 << CParser.Atomic) | (1 << CParser.Bool) | (1 << CParser.Complex) | (1 << CParser.Noreturn) | (1 << CParser.StaticAssert) | (1 << CParser.ThreadLocal) | (1 << CParser.LeftParen) | (1 << CParser.LeftBrace) | (1 << CParser.Plus))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (CParser.PlusPlus - 64)) | (1 << (CParser.Minus - 64)) | (1 << (CParser.MinusMinus - 64)) | (1 << (CParser.Star - 64)) | (1 << (CParser.And - 64)) | (1 << (CParser.Not - 64)) | (1 << (CParser.Tilde - 64)) | (1 << (CParser.Semi - 64)) | (1 << (CParser.Identifier - 64)) | (1 << (CParser.Constant - 64)) | (1 << (CParser.StringLiteral - 64)))) != 0):
                self.state = 710
                self.blockItem()
                self.state = 715
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 716
            self.match(CParser.RightBrace)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class BlockItemContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(CParser.BlockItemContext, self).__init__(parent, invokingState)
            self.parser = parser

        def declaration(self):
            return self.getTypedRuleContext(CParser.DeclarationContext,0)


        def statement(self):
            return self.getTypedRuleContext(CParser.StatementContext,0)


        def getRuleIndex(self):
            return CParser.RULE_blockItem

        def enterRule(self, listener):
            if isinstance( listener, CListener ):
                listener.enterBlockItem(self)

        def exitRule(self, listener):
            if isinstance( listener, CListener ):
                listener.exitBlockItem(self)

        def accept(self, visitor):
            if isinstance( visitor, CVisitor ):
                return visitor.visitBlockItem(self)
            else:
                return visitor.visitChildren(self)




    def blockItem(self):

        localctx = CParser.BlockItemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_blockItem)
        try:
            self.state = 720
            la_ = self._interp.adaptivePredict(self._input,83,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 718
                self.declaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 719
                self.statement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ExpressionStatementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(CParser.ExpressionStatementContext, self).__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(CParser.ExpressionContext,0)


        def getRuleIndex(self):
            return CParser.RULE_expressionStatement

        def enterRule(self, listener):
            if isinstance( listener, CListener ):
                listener.enterExpressionStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, CListener ):
                listener.exitExpressionStatement(self)

        def accept(self, visitor):
            if isinstance( visitor, CVisitor ):
                return visitor.visitExpressionStatement(self)
            else:
                return visitor.visitChildren(self)




    def expressionStatement(self):

        localctx = CParser.ExpressionStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_expressionStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 723
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CParser.Sizeof) | (1 << CParser.Alignof) | (1 << CParser.LeftParen) | (1 << CParser.Plus))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (CParser.PlusPlus - 64)) | (1 << (CParser.Minus - 64)) | (1 << (CParser.MinusMinus - 64)) | (1 << (CParser.Star - 64)) | (1 << (CParser.And - 64)) | (1 << (CParser.Not - 64)) | (1 << (CParser.Tilde - 64)) | (1 << (CParser.Identifier - 64)) | (1 << (CParser.Constant - 64)) | (1 << (CParser.StringLiteral - 64)))) != 0):
                self.state = 722
                self.expression()


            self.state = 725
            self.match(CParser.Semi)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class SelectionStatementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(CParser.SelectionStatementContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CParser.RULE_selectionStatement

     
        def copyFrom(self, ctx):
            super(CParser.SelectionStatementContext, self).copyFrom(ctx)



    class IfStatementContext(SelectionStatementContext):

        def __init__(self, parser, ctx): # actually a CParser.SelectionStatementContext)
            super(CParser.IfStatementContext, self).__init__(parser)
            self.copyFrom(ctx)

        def expression(self):
            return self.getTypedRuleContext(CParser.ExpressionContext,0)

        def statement(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(CParser.StatementContext)
            else:
                return self.getTypedRuleContext(CParser.StatementContext,i)


        def enterRule(self, listener):
            if isinstance( listener, CListener ):
                listener.enterIfStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, CListener ):
                listener.exitIfStatement(self)

        def accept(self, visitor):
            if isinstance( visitor, CVisitor ):
                return visitor.visitIfStatement(self)
            else:
                return visitor.visitChildren(self)


    class SwitchStatementContext(SelectionStatementContext):

        def __init__(self, parser, ctx): # actually a CParser.SelectionStatementContext)
            super(CParser.SwitchStatementContext, self).__init__(parser)
            self.copyFrom(ctx)

        def expression(self):
            return self.getTypedRuleContext(CParser.ExpressionContext,0)

        def statement(self):
            return self.getTypedRuleContext(CParser.StatementContext,0)


        def enterRule(self, listener):
            if isinstance( listener, CListener ):
                listener.enterSwitchStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, CListener ):
                listener.exitSwitchStatement(self)

        def accept(self, visitor):
            if isinstance( visitor, CVisitor ):
                return visitor.visitSwitchStatement(self)
            else:
                return visitor.visitChildren(self)



    def selectionStatement(self):

        localctx = CParser.SelectionStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_selectionStatement)
        try:
            self.state = 742
            token = self._input.LA(1)
            if token in [CParser.If]:
                localctx = CParser.IfStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 727
                self.match(CParser.If)
                self.state = 728
                self.match(CParser.LeftParen)
                self.state = 729
                self.expression()
                self.state = 730
                self.match(CParser.RightParen)
                self.state = 731
                self.statement()
                self.state = 734
                la_ = self._interp.adaptivePredict(self._input,85,self._ctx)
                if la_ == 1:
                    self.state = 732
                    self.match(CParser.Else)
                    self.state = 733
                    self.statement()



            elif token in [CParser.Switch]:
                localctx = CParser.SwitchStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 736
                self.match(CParser.Switch)
                self.state = 737
                self.match(CParser.LeftParen)
                self.state = 738
                self.expression()
                self.state = 739
                self.match(CParser.RightParen)
                self.state = 740
                self.statement()

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class IterationStatementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(CParser.IterationStatementContext, self).__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(CParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(CParser.ExpressionContext,i)


        def statement(self):
            return self.getTypedRuleContext(CParser.StatementContext,0)


        def declaration(self):
            return self.getTypedRuleContext(CParser.DeclarationContext,0)


        def getRuleIndex(self):
            return CParser.RULE_iterationStatement

        def enterRule(self, listener):
            if isinstance( listener, CListener ):
                listener.enterIterationStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, CListener ):
                listener.exitIterationStatement(self)

        def accept(self, visitor):
            if isinstance( visitor, CVisitor ):
                return visitor.visitIterationStatement(self)
            else:
                return visitor.visitChildren(self)




    def iterationStatement(self):

        localctx = CParser.IterationStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_iterationStatement)
        self._la = 0 # Token type
        try:
            self.state = 786
            la_ = self._interp.adaptivePredict(self._input,92,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 744
                self.match(CParser.While)
                self.state = 745
                self.match(CParser.LeftParen)
                self.state = 746
                self.expression()
                self.state = 747
                self.match(CParser.RightParen)
                self.state = 748
                self.statement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 750
                self.match(CParser.Do)
                self.state = 751
                self.statement()
                self.state = 752
                self.match(CParser.While)
                self.state = 753
                self.match(CParser.LeftParen)
                self.state = 754
                self.expression()
                self.state = 755
                self.match(CParser.RightParen)
                self.state = 756
                self.match(CParser.Semi)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 758
                self.match(CParser.For)
                self.state = 759
                self.match(CParser.LeftParen)
                self.state = 761
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CParser.Sizeof) | (1 << CParser.Alignof) | (1 << CParser.LeftParen) | (1 << CParser.Plus))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (CParser.PlusPlus - 64)) | (1 << (CParser.Minus - 64)) | (1 << (CParser.MinusMinus - 64)) | (1 << (CParser.Star - 64)) | (1 << (CParser.And - 64)) | (1 << (CParser.Not - 64)) | (1 << (CParser.Tilde - 64)) | (1 << (CParser.Identifier - 64)) | (1 << (CParser.Constant - 64)) | (1 << (CParser.StringLiteral - 64)))) != 0):
                    self.state = 760
                    self.expression()


                self.state = 763
                self.match(CParser.Semi)
                self.state = 765
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CParser.Sizeof) | (1 << CParser.Alignof) | (1 << CParser.LeftParen) | (1 << CParser.Plus))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (CParser.PlusPlus - 64)) | (1 << (CParser.Minus - 64)) | (1 << (CParser.MinusMinus - 64)) | (1 << (CParser.Star - 64)) | (1 << (CParser.And - 64)) | (1 << (CParser.Not - 64)) | (1 << (CParser.Tilde - 64)) | (1 << (CParser.Identifier - 64)) | (1 << (CParser.Constant - 64)) | (1 << (CParser.StringLiteral - 64)))) != 0):
                    self.state = 764
                    self.expression()


                self.state = 767
                self.match(CParser.Semi)
                self.state = 769
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CParser.Sizeof) | (1 << CParser.Alignof) | (1 << CParser.LeftParen) | (1 << CParser.Plus))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (CParser.PlusPlus - 64)) | (1 << (CParser.Minus - 64)) | (1 << (CParser.MinusMinus - 64)) | (1 << (CParser.Star - 64)) | (1 << (CParser.And - 64)) | (1 << (CParser.Not - 64)) | (1 << (CParser.Tilde - 64)) | (1 << (CParser.Identifier - 64)) | (1 << (CParser.Constant - 64)) | (1 << (CParser.StringLiteral - 64)))) != 0):
                    self.state = 768
                    self.expression()


                self.state = 771
                self.match(CParser.RightParen)
                self.state = 772
                self.statement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 773
                self.match(CParser.For)
                self.state = 774
                self.match(CParser.LeftParen)
                self.state = 775
                self.declaration()
                self.state = 777
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CParser.Sizeof) | (1 << CParser.Alignof) | (1 << CParser.LeftParen) | (1 << CParser.Plus))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (CParser.PlusPlus - 64)) | (1 << (CParser.Minus - 64)) | (1 << (CParser.MinusMinus - 64)) | (1 << (CParser.Star - 64)) | (1 << (CParser.And - 64)) | (1 << (CParser.Not - 64)) | (1 << (CParser.Tilde - 64)) | (1 << (CParser.Identifier - 64)) | (1 << (CParser.Constant - 64)) | (1 << (CParser.StringLiteral - 64)))) != 0):
                    self.state = 776
                    self.expression()


                self.state = 779
                self.match(CParser.Semi)
                self.state = 781
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CParser.Sizeof) | (1 << CParser.Alignof) | (1 << CParser.LeftParen) | (1 << CParser.Plus))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (CParser.PlusPlus - 64)) | (1 << (CParser.Minus - 64)) | (1 << (CParser.MinusMinus - 64)) | (1 << (CParser.Star - 64)) | (1 << (CParser.And - 64)) | (1 << (CParser.Not - 64)) | (1 << (CParser.Tilde - 64)) | (1 << (CParser.Identifier - 64)) | (1 << (CParser.Constant - 64)) | (1 << (CParser.StringLiteral - 64)))) != 0):
                    self.state = 780
                    self.expression()


                self.state = 783
                self.match(CParser.RightParen)
                self.state = 784
                self.statement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class JumpStatementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(CParser.JumpStatementContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CParser.RULE_jumpStatement

     
        def copyFrom(self, ctx):
            super(CParser.JumpStatementContext, self).copyFrom(ctx)



    class ContinueStatementContext(JumpStatementContext):

        def __init__(self, parser, ctx): # actually a CParser.JumpStatementContext)
            super(CParser.ContinueStatementContext, self).__init__(parser)
            self.copyFrom(ctx)


        def enterRule(self, listener):
            if isinstance( listener, CListener ):
                listener.enterContinueStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, CListener ):
                listener.exitContinueStatement(self)

        def accept(self, visitor):
            if isinstance( visitor, CVisitor ):
                return visitor.visitContinueStatement(self)
            else:
                return visitor.visitChildren(self)


    class GotoStatementContext(JumpStatementContext):

        def __init__(self, parser, ctx): # actually a CParser.JumpStatementContext)
            super(CParser.GotoStatementContext, self).__init__(parser)
            self.copyFrom(ctx)

        def Identifier(self):
            return self.getToken(CParser.Identifier, 0)

        def enterRule(self, listener):
            if isinstance( listener, CListener ):
                listener.enterGotoStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, CListener ):
                listener.exitGotoStatement(self)

        def accept(self, visitor):
            if isinstance( visitor, CVisitor ):
                return visitor.visitGotoStatement(self)
            else:
                return visitor.visitChildren(self)


    class ReturnStatementContext(JumpStatementContext):

        def __init__(self, parser, ctx): # actually a CParser.JumpStatementContext)
            super(CParser.ReturnStatementContext, self).__init__(parser)
            self.copyFrom(ctx)

        def expression(self):
            return self.getTypedRuleContext(CParser.ExpressionContext,0)


        def enterRule(self, listener):
            if isinstance( listener, CListener ):
                listener.enterReturnStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, CListener ):
                listener.exitReturnStatement(self)

        def accept(self, visitor):
            if isinstance( visitor, CVisitor ):
                return visitor.visitReturnStatement(self)
            else:
                return visitor.visitChildren(self)


    class BreakStatementContext(JumpStatementContext):

        def __init__(self, parser, ctx): # actually a CParser.JumpStatementContext)
            super(CParser.BreakStatementContext, self).__init__(parser)
            self.copyFrom(ctx)


        def enterRule(self, listener):
            if isinstance( listener, CListener ):
                listener.enterBreakStatement(self)

        def exitRule(self, listener):
            if isinstance( listener, CListener ):
                listener.exitBreakStatement(self)

        def accept(self, visitor):
            if isinstance( visitor, CVisitor ):
                return visitor.visitBreakStatement(self)
            else:
                return visitor.visitChildren(self)



    def jumpStatement(self):

        localctx = CParser.JumpStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_jumpStatement)
        self._la = 0 # Token type
        try:
            self.state = 800
            token = self._input.LA(1)
            if token in [CParser.Goto]:
                localctx = CParser.GotoStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 788
                self.match(CParser.Goto)
                self.state = 789
                self.match(CParser.Identifier)
                self.state = 790
                self.match(CParser.Semi)

            elif token in [CParser.Continue]:
                localctx = CParser.ContinueStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 791
                self.match(CParser.Continue)
                self.state = 792
                self.match(CParser.Semi)

            elif token in [CParser.Break]:
                localctx = CParser.BreakStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 793
                self.match(CParser.Break)
                self.state = 794
                self.match(CParser.Semi)

            elif token in [CParser.Return]:
                localctx = CParser.ReturnStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 795
                self.match(CParser.Return)
                self.state = 797
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CParser.Sizeof) | (1 << CParser.Alignof) | (1 << CParser.LeftParen) | (1 << CParser.Plus))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (CParser.PlusPlus - 64)) | (1 << (CParser.Minus - 64)) | (1 << (CParser.MinusMinus - 64)) | (1 << (CParser.Star - 64)) | (1 << (CParser.And - 64)) | (1 << (CParser.Not - 64)) | (1 << (CParser.Tilde - 64)) | (1 << (CParser.Identifier - 64)) | (1 << (CParser.Constant - 64)) | (1 << (CParser.StringLiteral - 64)))) != 0):
                    self.state = 796
                    self.expression()


                self.state = 799
                self.match(CParser.Semi)

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class CompilationUnitContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(CParser.CompilationUnitContext, self).__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(CParser.EOF, 0)

        def externalDeclaration(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(CParser.ExternalDeclarationContext)
            else:
                return self.getTypedRuleContext(CParser.ExternalDeclarationContext,i)


        def getRuleIndex(self):
            return CParser.RULE_compilationUnit

        def enterRule(self, listener):
            if isinstance( listener, CListener ):
                listener.enterCompilationUnit(self)

        def exitRule(self, listener):
            if isinstance( listener, CListener ):
                listener.exitCompilationUnit(self)

        def accept(self, visitor):
            if isinstance( visitor, CVisitor ):
                return visitor.visitCompilationUnit(self)
            else:
                return visitor.visitChildren(self)




    def compilationUnit(self):

        localctx = CParser.CompilationUnitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_compilationUnit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 805
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CParser.T__0) | (1 << CParser.T__1) | (1 << CParser.T__2) | (1 << CParser.T__3) | (1 << CParser.T__4) | (1 << CParser.T__5) | (1 << CParser.Auto) | (1 << CParser.Char) | (1 << CParser.Const) | (1 << CParser.Double) | (1 << CParser.Enum) | (1 << CParser.Extern) | (1 << CParser.Float) | (1 << CParser.Inline) | (1 << CParser.Int) | (1 << CParser.Long) | (1 << CParser.Register) | (1 << CParser.Restrict) | (1 << CParser.Short) | (1 << CParser.Signed) | (1 << CParser.Static) | (1 << CParser.Struct) | (1 << CParser.Typedef) | (1 << CParser.Union) | (1 << CParser.Unsigned) | (1 << CParser.Void) | (1 << CParser.Volatile) | (1 << CParser.Alignas) | (1 << CParser.Atomic) | (1 << CParser.Bool) | (1 << CParser.Complex) | (1 << CParser.Noreturn) | (1 << CParser.StaticAssert) | (1 << CParser.ThreadLocal) | (1 << CParser.LeftParen))) != 0) or ((((_la - 67)) & ~0x3f) == 0 and ((1 << (_la - 67)) & ((1 << (CParser.Star - 67)) | (1 << (CParser.Semi - 67)) | (1 << (CParser.Identifier - 67)))) != 0):
                self.state = 802
                self.externalDeclaration()
                self.state = 807
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 808
            self.match(CParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ExternalDeclarationContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(CParser.ExternalDeclarationContext, self).__init__(parent, invokingState)
            self.parser = parser

        def functionDefinition(self):
            return self.getTypedRuleContext(CParser.FunctionDefinitionContext,0)


        def declaration(self):
            return self.getTypedRuleContext(CParser.DeclarationContext,0)


        def getRuleIndex(self):
            return CParser.RULE_externalDeclaration

        def enterRule(self, listener):
            if isinstance( listener, CListener ):
                listener.enterExternalDeclaration(self)

        def exitRule(self, listener):
            if isinstance( listener, CListener ):
                listener.exitExternalDeclaration(self)

        def accept(self, visitor):
            if isinstance( visitor, CVisitor ):
                return visitor.visitExternalDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def externalDeclaration(self):

        localctx = CParser.ExternalDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_externalDeclaration)
        try:
            self.state = 813
            la_ = self._interp.adaptivePredict(self._input,96,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 810
                self.functionDefinition()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 811
                self.declaration()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 812
                self.match(CParser.Semi)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class FunctionDefinitionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(CParser.FunctionDefinitionContext, self).__init__(parent, invokingState)
            self.parser = parser

        def declarator(self):
            return self.getTypedRuleContext(CParser.DeclaratorContext,0)


        def compoundStatement(self):
            return self.getTypedRuleContext(CParser.CompoundStatementContext,0)


        def declarationSpecifier(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(CParser.DeclarationSpecifierContext)
            else:
                return self.getTypedRuleContext(CParser.DeclarationSpecifierContext,i)


        def declaration(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(CParser.DeclarationContext)
            else:
                return self.getTypedRuleContext(CParser.DeclarationContext,i)


        def getRuleIndex(self):
            return CParser.RULE_functionDefinition

        def enterRule(self, listener):
            if isinstance( listener, CListener ):
                listener.enterFunctionDefinition(self)

        def exitRule(self, listener):
            if isinstance( listener, CListener ):
                listener.exitFunctionDefinition(self)

        def accept(self, visitor):
            if isinstance( visitor, CVisitor ):
                return visitor.visitFunctionDefinition(self)
            else:
                return visitor.visitChildren(self)




    def functionDefinition(self):

        localctx = CParser.FunctionDefinitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_functionDefinition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 818
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,97,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 815
                    self.declarationSpecifier() 
                self.state = 820
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,97,self._ctx)

            self.state = 821
            self.declarator()
            self.state = 825
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CParser.T__0) | (1 << CParser.T__1) | (1 << CParser.T__2) | (1 << CParser.T__3) | (1 << CParser.T__4) | (1 << CParser.T__5) | (1 << CParser.Auto) | (1 << CParser.Char) | (1 << CParser.Const) | (1 << CParser.Double) | (1 << CParser.Enum) | (1 << CParser.Extern) | (1 << CParser.Float) | (1 << CParser.Inline) | (1 << CParser.Int) | (1 << CParser.Long) | (1 << CParser.Register) | (1 << CParser.Restrict) | (1 << CParser.Short) | (1 << CParser.Signed) | (1 << CParser.Static) | (1 << CParser.Struct) | (1 << CParser.Typedef) | (1 << CParser.Union) | (1 << CParser.Unsigned) | (1 << CParser.Void) | (1 << CParser.Volatile) | (1 << CParser.Alignas) | (1 << CParser.Atomic) | (1 << CParser.Bool) | (1 << CParser.Complex) | (1 << CParser.Noreturn) | (1 << CParser.StaticAssert) | (1 << CParser.ThreadLocal))) != 0) or _la==CParser.Identifier:
                self.state = 822
                self.declaration()
                self.state = 827
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 828
            self.compoundStatement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx, ruleIndex, predIndex):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[0] = self.unaryExpression_sempred
        self._predicates[3] = self.logicalOrExpression_sempred
        self._predicates[28] = self.directDeclarator_sempred
        self._predicates[35] = self.directAbstractDeclarator_sempred
        self._predicates[38] = self.initializerList_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def unaryExpression_sempred(self, localctx, predIndex):
            if predIndex == 0:
                return self.precpred(self._ctx, 10)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 6)
         

    def logicalOrExpression_sempred(self, localctx, predIndex):
            if predIndex == 4:
                return self.precpred(self._ctx, 10)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 9)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 7:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 8:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 9:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 10:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 11:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 12:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 13:
                return self.precpred(self._ctx, 1)
         

    def directDeclarator_sempred(self, localctx, predIndex):
            if predIndex == 14:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 15:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 16:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 17:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 18:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 19:
                return self.precpred(self._ctx, 1)
         

    def directAbstractDeclarator_sempred(self, localctx, predIndex):
            if predIndex == 20:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 21:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 22:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 23:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 24:
                return self.precpred(self._ctx, 1)
         

    def initializerList_sempred(self, localctx, predIndex):
            if predIndex == 25:
                return self.precpred(self._ctx, 1)
         



