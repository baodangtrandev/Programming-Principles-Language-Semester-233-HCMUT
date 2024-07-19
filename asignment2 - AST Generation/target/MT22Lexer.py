# Generated from main/mt22/parser/MT22.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *
# Trần Đăng Bảo - 2210270



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\29")
        buf.write("\u01ef\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\3\2\3\2\3\2\3\2\7\2\u0094\n")
        buf.write("\2\f\2\16\2\u0097\13\2\3\3\3\3\3\3\3\3\7\3\u009d\n\3\f")
        buf.write("\3\16\3\u00a0\13\3\3\3\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3\6")
        buf.write("\3\7\3\7\3\7\7\7\u00ae\n\7\f\7\16\7\u00b1\13\7\3\7\3\7")
        buf.write("\6\7\u00b5\n\7\r\7\16\7\u00b6\7\7\u00b9\n\7\f\7\16\7\u00bc")
        buf.write("\13\7\5\7\u00be\n\7\3\b\3\b\7\b\u00c2\n\b\f\b\16\b\u00c5")
        buf.write("\13\b\3\t\3\t\3\n\3\n\5\n\u00cb\n\n\3\n\6\n\u00ce\n\n")
        buf.write("\r\n\16\n\u00cf\3\13\3\13\3\13\3\f\3\f\5\f\u00d7\n\f\3")
        buf.write("\r\3\r\3\r\3\r\5\r\u00dd\n\r\3\16\3\16\3\17\3\17\3\17")
        buf.write("\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21")
        buf.write("\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\23\3\23\3\23")
        buf.write("\3\23\3\23\3\24\3\24\3\24\3\24\3\24\3\24\3\25\3\25\3\25")
        buf.write("\3\25\3\25\3\25\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\27")
        buf.write("\3\27\3\27\3\27\3\27\3\27\3\30\3\30\3\30\3\31\3\31\3\31")
        buf.write("\3\31\3\31\3\31\3\31\3\31\3\32\3\32\3\32\3\32\3\32\3\32")
        buf.write("\3\32\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\34\3\34\3\34")
        buf.write("\3\34\3\34\3\35\3\35\3\35\3\35\3\35\3\35\3\36\3\36\3\36")
        buf.write("\3\36\3\36\3\37\3\37\3\37\3\37\3 \3 \3 \3 \3 \3 \3 \3")
        buf.write(" \3 \3!\3!\3!\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3#\3#\3")
        buf.write("#\3#\3#\3#\3$\3$\3%\3%\3&\3&\3\'\3\'\3(\3(\3)\3)\3*\3")
        buf.write("*\3*\3+\3+\3+\3,\3,\3,\3-\3-\3-\3.\3.\3/\3/\3/\3\60\3")
        buf.write("\60\3\61\3\61\3\61\3\62\3\62\3\62\3\63\3\63\3\64\3\64")
        buf.write("\3\65\3\65\3\66\3\66\3\67\3\67\38\38\39\39\3:\3:\3;\3")
        buf.write(";\3<\3<\3=\3=\3>\3>\3>\3?\3?\3?\5?\u019d\n?\3?\3?\3?\3")
        buf.write("?\3?\3?\5?\u01a5\n?\3?\3?\3@\3@\5@\u01ab\n@\3A\3A\7A\u01af")
        buf.write("\nA\fA\16A\u01b2\13A\3A\3A\3A\3B\3B\5B\u01b9\nB\3B\3B")
        buf.write("\3B\7B\u01be\nB\fB\16B\u01c1\13B\3C\3C\5C\u01c5\nC\3C")
        buf.write("\3C\3D\6D\u01ca\nD\rD\16D\u01cb\3D\3D\3E\3E\3E\7E\u01d3")
        buf.write("\nE\fE\16E\u01d6\13E\3E\3E\3E\5E\u01db\nE\3E\3E\3F\3F")
        buf.write("\3F\7F\u01e2\nF\fF\16F\u01e5\13F\3F\3F\5F\u01e9\nF\3F")
        buf.write("\3F\3G\3G\3G\4\u009e\u01b0\2H\3\2\5\2\7\2\t\2\13\2\r\2")
        buf.write("\17\2\21\2\23\2\25\2\27\2\31\2\33\2\35\3\37\4!\5#\6%\7")
        buf.write("\'\2)\b+\t-\n/\13\61\f\63\r\65\16\67\29\17;\20=\21?\22")
        buf.write("A\23C\24E\25G\26I\27K\30M\31O\32Q\33S\34U\35W\36Y\37[")
        buf.write(" ]!_\"a#c$e%g&i\'k(m)o*q+s,u-w.y/{\60}\61\177\62\u0081")
        buf.write("\63\u0083\64\u0085\65\u0087\66\u0089\67\u008b8\u008d9")
        buf.write("\3\2\16\4\2\f\f\17\17\4\2C\\c|\3\2\62;\3\2\63;\4\2--/")
        buf.write("/\4\2GGgg\n\2$$))^^ddhhppttvv\5\2\f\f$$^^\5\2\n\f\16\17")
        buf.write("\"\"\6\2\f\f\17\17$$^^\3\3\f\f\3\2\17\17\2\u01fb\2\35")
        buf.write("\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2")
        buf.write("\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2")
        buf.write("\2\2\2\63\3\2\2\2\2\65\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2")
        buf.write("=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2")
        buf.write("\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2")
        buf.write("\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2")
        buf.write("\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3")
        buf.write("\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m")
        buf.write("\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2")
        buf.write("w\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2\2}\3\2\2\2\2\177\3\2\2")
        buf.write("\2\2\u0081\3\2\2\2\2\u0083\3\2\2\2\2\u0085\3\2\2\2\2\u0087")
        buf.write("\3\2\2\2\2\u0089\3\2\2\2\2\u008b\3\2\2\2\2\u008d\3\2\2")
        buf.write("\2\3\u008f\3\2\2\2\5\u0098\3\2\2\2\7\u00a4\3\2\2\2\t\u00a6")
        buf.write("\3\2\2\2\13\u00a8\3\2\2\2\r\u00bd\3\2\2\2\17\u00bf\3\2")
        buf.write("\2\2\21\u00c6\3\2\2\2\23\u00c8\3\2\2\2\25\u00d1\3\2\2")
        buf.write("\2\27\u00d6\3\2\2\2\31\u00dc\3\2\2\2\33\u00de\3\2\2\2")
        buf.write("\35\u00e0\3\2\2\2\37\u00e5\3\2\2\2!\u00eb\3\2\2\2#\u00f3")
        buf.write("\3\2\2\2%\u00f6\3\2\2\2\'\u00fb\3\2\2\2)\u0101\3\2\2\2")
        buf.write("+\u0107\3\2\2\2-\u010b\3\2\2\2/\u0114\3\2\2\2\61\u0117")
        buf.write("\3\2\2\2\63\u011f\3\2\2\2\65\u0126\3\2\2\2\67\u012d\3")
        buf.write("\2\2\29\u0132\3\2\2\2;\u0138\3\2\2\2=\u013d\3\2\2\2?\u0141")
        buf.write("\3\2\2\2A\u014a\3\2\2\2C\u014d\3\2\2\2E\u0155\3\2\2\2")
        buf.write("G\u015b\3\2\2\2I\u015d\3\2\2\2K\u015f\3\2\2\2M\u0161\3")
        buf.write("\2\2\2O\u0163\3\2\2\2Q\u0165\3\2\2\2S\u0167\3\2\2\2U\u016a")
        buf.write("\3\2\2\2W\u016d\3\2\2\2Y\u0170\3\2\2\2[\u0173\3\2\2\2")
        buf.write("]\u0175\3\2\2\2_\u0178\3\2\2\2a\u017a\3\2\2\2c\u017d\3")
        buf.write("\2\2\2e\u0180\3\2\2\2g\u0182\3\2\2\2i\u0184\3\2\2\2k\u0186")
        buf.write("\3\2\2\2m\u0188\3\2\2\2o\u018a\3\2\2\2q\u018c\3\2\2\2")
        buf.write("s\u018e\3\2\2\2u\u0190\3\2\2\2w\u0192\3\2\2\2y\u0194\3")
        buf.write("\2\2\2{\u0196\3\2\2\2}\u01a4\3\2\2\2\177\u01aa\3\2\2\2")
        buf.write("\u0081\u01ac\3\2\2\2\u0083\u01b8\3\2\2\2\u0085\u01c4\3")
        buf.write("\2\2\2\u0087\u01c9\3\2\2\2\u0089\u01cf\3\2\2\2\u008b\u01de")
        buf.write("\3\2\2\2\u008d\u01ec\3\2\2\2\u008f\u0090\7\61\2\2\u0090")
        buf.write("\u0091\7\61\2\2\u0091\u0095\3\2\2\2\u0092\u0094\n\2\2")
        buf.write("\2\u0093\u0092\3\2\2\2\u0094\u0097\3\2\2\2\u0095\u0093")
        buf.write("\3\2\2\2\u0095\u0096\3\2\2\2\u0096\4\3\2\2\2\u0097\u0095")
        buf.write("\3\2\2\2\u0098\u0099\7\61\2\2\u0099\u009a\7,\2\2\u009a")
        buf.write("\u009e\3\2\2\2\u009b\u009d\13\2\2\2\u009c\u009b\3\2\2")
        buf.write("\2\u009d\u00a0\3\2\2\2\u009e\u009f\3\2\2\2\u009e\u009c")
        buf.write("\3\2\2\2\u009f\u00a1\3\2\2\2\u00a0\u009e\3\2\2\2\u00a1")
        buf.write("\u00a2\7,\2\2\u00a2\u00a3\7\61\2\2\u00a3\6\3\2\2\2\u00a4")
        buf.write("\u00a5\t\3\2\2\u00a5\b\3\2\2\2\u00a6\u00a7\t\4\2\2\u00a7")
        buf.write("\n\3\2\2\2\u00a8\u00a9\7a\2\2\u00a9\f\3\2\2\2\u00aa\u00be")
        buf.write("\7\62\2\2\u00ab\u00af\t\5\2\2\u00ac\u00ae\5\t\5\2\u00ad")
        buf.write("\u00ac\3\2\2\2\u00ae\u00b1\3\2\2\2\u00af\u00ad\3\2\2\2")
        buf.write("\u00af\u00b0\3\2\2\2\u00b0\u00ba\3\2\2\2\u00b1\u00af\3")
        buf.write("\2\2\2\u00b2\u00b4\5\13\6\2\u00b3\u00b5\5\t\5\2\u00b4")
        buf.write("\u00b3\3\2\2\2\u00b5\u00b6\3\2\2\2\u00b6\u00b4\3\2\2\2")
        buf.write("\u00b6\u00b7\3\2\2\2\u00b7\u00b9\3\2\2\2\u00b8\u00b2\3")
        buf.write("\2\2\2\u00b9\u00bc\3\2\2\2\u00ba\u00b8\3\2\2\2\u00ba\u00bb")
        buf.write("\3\2\2\2\u00bb\u00be\3\2\2\2\u00bc\u00ba\3\2\2\2\u00bd")
        buf.write("\u00aa\3\2\2\2\u00bd\u00ab\3\2\2\2\u00be\16\3\2\2\2\u00bf")
        buf.write("\u00c3\7\60\2\2\u00c0\u00c2\5\t\5\2\u00c1\u00c0\3\2\2")
        buf.write("\2\u00c2\u00c5\3\2\2\2\u00c3\u00c1\3\2\2\2\u00c3\u00c4")
        buf.write("\3\2\2\2\u00c4\20\3\2\2\2\u00c5\u00c3\3\2\2\2\u00c6\u00c7")
        buf.write("\t\6\2\2\u00c7\22\3\2\2\2\u00c8\u00ca\t\7\2\2\u00c9\u00cb")
        buf.write("\5\21\t\2\u00ca\u00c9\3\2\2\2\u00ca\u00cb\3\2\2\2\u00cb")
        buf.write("\u00cd\3\2\2\2\u00cc\u00ce\5\t\5\2\u00cd\u00cc\3\2\2\2")
        buf.write("\u00ce\u00cf\3\2\2\2\u00cf\u00cd\3\2\2\2\u00cf\u00d0\3")
        buf.write("\2\2\2\u00d0\24\3\2\2\2\u00d1\u00d2\7^\2\2\u00d2\u00d3")
        buf.write("\n\b\2\2\u00d3\26\3\2\2\2\u00d4\u00d7\n\t\2\2\u00d5\u00d7")
        buf.write("\5\31\r\2\u00d6\u00d4\3\2\2\2\u00d6\u00d5\3\2\2\2\u00d7")
        buf.write("\30\3\2\2\2\u00d8\u00d9\7^\2\2\u00d9\u00dd\t\b\2\2\u00da")
        buf.write("\u00db\7)\2\2\u00db\u00dd\7$\2\2\u00dc\u00d8\3\2\2\2\u00dc")
        buf.write("\u00da\3\2\2\2\u00dd\32\3\2\2\2\u00de\u00df\7$\2\2\u00df")
        buf.write("\34\3\2\2\2\u00e0\u00e1\7c\2\2\u00e1\u00e2\7w\2\2\u00e2")
        buf.write("\u00e3\7v\2\2\u00e3\u00e4\7q\2\2\u00e4\36\3\2\2\2\u00e5")
        buf.write("\u00e6\7d\2\2\u00e6\u00e7\7t\2\2\u00e7\u00e8\7g\2\2\u00e8")
        buf.write("\u00e9\7c\2\2\u00e9\u00ea\7m\2\2\u00ea \3\2\2\2\u00eb")
        buf.write("\u00ec\7d\2\2\u00ec\u00ed\7q\2\2\u00ed\u00ee\7q\2\2\u00ee")
        buf.write("\u00ef\7n\2\2\u00ef\u00f0\7g\2\2\u00f0\u00f1\7c\2\2\u00f1")
        buf.write("\u00f2\7p\2\2\u00f2\"\3\2\2\2\u00f3\u00f4\7f\2\2\u00f4")
        buf.write("\u00f5\7q\2\2\u00f5$\3\2\2\2\u00f6\u00f7\7g\2\2\u00f7")
        buf.write("\u00f8\7n\2\2\u00f8\u00f9\7u\2\2\u00f9\u00fa\7g\2\2\u00fa")
        buf.write("&\3\2\2\2\u00fb\u00fc\7h\2\2\u00fc\u00fd\7c\2\2\u00fd")
        buf.write("\u00fe\7n\2\2\u00fe\u00ff\7u\2\2\u00ff\u0100\7g\2\2\u0100")
        buf.write("(\3\2\2\2\u0101\u0102\7h\2\2\u0102\u0103\7n\2\2\u0103")
        buf.write("\u0104\7q\2\2\u0104\u0105\7c\2\2\u0105\u0106\7v\2\2\u0106")
        buf.write("*\3\2\2\2\u0107\u0108\7h\2\2\u0108\u0109\7q\2\2\u0109")
        buf.write("\u010a\7t\2\2\u010a,\3\2\2\2\u010b\u010c\7h\2\2\u010c")
        buf.write("\u010d\7w\2\2\u010d\u010e\7p\2\2\u010e\u010f\7e\2\2\u010f")
        buf.write("\u0110\7v\2\2\u0110\u0111\7k\2\2\u0111\u0112\7q\2\2\u0112")
        buf.write("\u0113\7p\2\2\u0113.\3\2\2\2\u0114\u0115\7k\2\2\u0115")
        buf.write("\u0116\7h\2\2\u0116\60\3\2\2\2\u0117\u0118\7k\2\2\u0118")
        buf.write("\u0119\7p\2\2\u0119\u011a\7v\2\2\u011a\u011b\7g\2\2\u011b")
        buf.write("\u011c\7i\2\2\u011c\u011d\7g\2\2\u011d\u011e\7t\2\2\u011e")
        buf.write("\62\3\2\2\2\u011f\u0120\7t\2\2\u0120\u0121\7g\2\2\u0121")
        buf.write("\u0122\7v\2\2\u0122\u0123\7w\2\2\u0123\u0124\7t\2\2\u0124")
        buf.write("\u0125\7p\2\2\u0125\64\3\2\2\2\u0126\u0127\7u\2\2\u0127")
        buf.write("\u0128\7v\2\2\u0128\u0129\7t\2\2\u0129\u012a\7k\2\2\u012a")
        buf.write("\u012b\7p\2\2\u012b\u012c\7i\2\2\u012c\66\3\2\2\2\u012d")
        buf.write("\u012e\7v\2\2\u012e\u012f\7t\2\2\u012f\u0130\7w\2\2\u0130")
        buf.write("\u0131\7g\2\2\u01318\3\2\2\2\u0132\u0133\7y\2\2\u0133")
        buf.write("\u0134\7j\2\2\u0134\u0135\7k\2\2\u0135\u0136\7n\2\2\u0136")
        buf.write("\u0137\7g\2\2\u0137:\3\2\2\2\u0138\u0139\7x\2\2\u0139")
        buf.write("\u013a\7q\2\2\u013a\u013b\7k\2\2\u013b\u013c\7f\2\2\u013c")
        buf.write("<\3\2\2\2\u013d\u013e\7q\2\2\u013e\u013f\7w\2\2\u013f")
        buf.write("\u0140\7v\2\2\u0140>\3\2\2\2\u0141\u0142\7e\2\2\u0142")
        buf.write("\u0143\7q\2\2\u0143\u0144\7p\2\2\u0144\u0145\7v\2\2\u0145")
        buf.write("\u0146\7k\2\2\u0146\u0147\7p\2\2\u0147\u0148\7w\2\2\u0148")
        buf.write("\u0149\7g\2\2\u0149@\3\2\2\2\u014a\u014b\7q\2\2\u014b")
        buf.write("\u014c\7h\2\2\u014cB\3\2\2\2\u014d\u014e\7k\2\2\u014e")
        buf.write("\u014f\7p\2\2\u014f\u0150\7j\2\2\u0150\u0151\7g\2\2\u0151")
        buf.write("\u0152\7t\2\2\u0152\u0153\7k\2\2\u0153\u0154\7v\2\2\u0154")
        buf.write("D\3\2\2\2\u0155\u0156\7c\2\2\u0156\u0157\7t\2\2\u0157")
        buf.write("\u0158\7t\2\2\u0158\u0159\7c\2\2\u0159\u015a\7{\2\2\u015a")
        buf.write("F\3\2\2\2\u015b\u015c\7-\2\2\u015cH\3\2\2\2\u015d\u015e")
        buf.write("\7/\2\2\u015eJ\3\2\2\2\u015f\u0160\7,\2\2\u0160L\3\2\2")
        buf.write("\2\u0161\u0162\7\61\2\2\u0162N\3\2\2\2\u0163\u0164\7\'")
        buf.write("\2\2\u0164P\3\2\2\2\u0165\u0166\7#\2\2\u0166R\3\2\2\2")
        buf.write("\u0167\u0168\7(\2\2\u0168\u0169\7(\2\2\u0169T\3\2\2\2")
        buf.write("\u016a\u016b\7~\2\2\u016b\u016c\7~\2\2\u016cV\3\2\2\2")
        buf.write("\u016d\u016e\7?\2\2\u016e\u016f\7?\2\2\u016fX\3\2\2\2")
        buf.write("\u0170\u0171\7#\2\2\u0171\u0172\7?\2\2\u0172Z\3\2\2\2")
        buf.write("\u0173\u0174\7>\2\2\u0174\\\3\2\2\2\u0175\u0176\7>\2\2")
        buf.write("\u0176\u0177\7?\2\2\u0177^\3\2\2\2\u0178\u0179\7@\2\2")
        buf.write("\u0179`\3\2\2\2\u017a\u017b\7@\2\2\u017b\u017c\7?\2\2")
        buf.write("\u017cb\3\2\2\2\u017d\u017e\7<\2\2\u017e\u017f\7<\2\2")
        buf.write("\u017fd\3\2\2\2\u0180\u0181\7*\2\2\u0181f\3\2\2\2\u0182")
        buf.write("\u0183\7+\2\2\u0183h\3\2\2\2\u0184\u0185\7]\2\2\u0185")
        buf.write("j\3\2\2\2\u0186\u0187\7_\2\2\u0187l\3\2\2\2\u0188\u0189")
        buf.write("\7\60\2\2\u0189n\3\2\2\2\u018a\u018b\7.\2\2\u018bp\3\2")
        buf.write("\2\2\u018c\u018d\7=\2\2\u018dr\3\2\2\2\u018e\u018f\7<")
        buf.write("\2\2\u018ft\3\2\2\2\u0190\u0191\7}\2\2\u0191v\3\2\2\2")
        buf.write("\u0192\u0193\7\177\2\2\u0193x\3\2\2\2\u0194\u0195\7?\2")
        buf.write("\2\u0195z\3\2\2\2\u0196\u0197\5\r\7\2\u0197\u0198\b>\2")
        buf.write("\2\u0198|\3\2\2\2\u0199\u019a\5\r\7\2\u019a\u019c\5\17")
        buf.write("\b\2\u019b\u019d\5\23\n\2\u019c\u019b\3\2\2\2\u019c\u019d")
        buf.write("\3\2\2\2\u019d\u01a5\3\2\2\2\u019e\u019f\5\r\7\2\u019f")
        buf.write("\u01a0\5\23\n\2\u01a0\u01a5\3\2\2\2\u01a1\u01a2\5\17\b")
        buf.write("\2\u01a2\u01a3\5\23\n\2\u01a3\u01a5\3\2\2\2\u01a4\u0199")
        buf.write("\3\2\2\2\u01a4\u019e\3\2\2\2\u01a4\u01a1\3\2\2\2\u01a5")
        buf.write("\u01a6\3\2\2\2\u01a6\u01a7\b?\3\2\u01a7~\3\2\2\2\u01a8")
        buf.write("\u01ab\5\67\34\2\u01a9\u01ab\5\'\24\2\u01aa\u01a8\3\2")
        buf.write("\2\2\u01aa\u01a9\3\2\2\2\u01ab\u0080\3\2\2\2\u01ac\u01b0")
        buf.write("\5\33\16\2\u01ad\u01af\5\27\f\2\u01ae\u01ad\3\2\2\2\u01af")
        buf.write("\u01b2\3\2\2\2\u01b0\u01b1\3\2\2\2\u01b0\u01ae\3\2\2\2")
        buf.write("\u01b1\u01b3\3\2\2\2\u01b2\u01b0\3\2\2\2\u01b3\u01b4\5")
        buf.write("\33\16\2\u01b4\u01b5\bA\4\2\u01b5\u0082\3\2\2\2\u01b6")
        buf.write("\u01b9\5\7\4\2\u01b7\u01b9\5\13\6\2\u01b8\u01b6\3\2\2")
        buf.write("\2\u01b8\u01b7\3\2\2\2\u01b9\u01bf\3\2\2\2\u01ba\u01be")
        buf.write("\5\7\4\2\u01bb\u01be\5\13\6\2\u01bc\u01be\5\t\5\2\u01bd")
        buf.write("\u01ba\3\2\2\2\u01bd\u01bb\3\2\2\2\u01bd\u01bc\3\2\2\2")
        buf.write("\u01be\u01c1\3\2\2\2\u01bf\u01bd\3\2\2\2\u01bf\u01c0\3")
        buf.write("\2\2\2\u01c0\u0084\3\2\2\2\u01c1\u01bf\3\2\2\2\u01c2\u01c5")
        buf.write("\5\3\2\2\u01c3\u01c5\5\5\3\2\u01c4\u01c2\3\2\2\2\u01c4")
        buf.write("\u01c3\3\2\2\2\u01c5\u01c6\3\2\2\2\u01c6\u01c7\bC\5\2")
        buf.write("\u01c7\u0086\3\2\2\2\u01c8\u01ca\t\n\2\2\u01c9\u01c8\3")
        buf.write("\2\2\2\u01ca\u01cb\3\2\2\2\u01cb\u01c9\3\2\2\2\u01cb\u01cc")
        buf.write("\3\2\2\2\u01cc\u01cd\3\2\2\2\u01cd\u01ce\bD\5\2\u01ce")
        buf.write("\u0088\3\2\2\2\u01cf\u01d4\5\33\16\2\u01d0\u01d3\n\13")
        buf.write("\2\2\u01d1\u01d3\5\31\r\2\u01d2\u01d0\3\2\2\2\u01d2\u01d1")
        buf.write("\3\2\2\2\u01d3\u01d6\3\2\2\2\u01d4\u01d2\3\2\2\2\u01d4")
        buf.write("\u01d5\3\2\2\2\u01d5\u01da\3\2\2\2\u01d6\u01d4\3\2\2\2")
        buf.write("\u01d7\u01d8\7\17\2\2\u01d8\u01db\7\f\2\2\u01d9\u01db")
        buf.write("\t\f\2\2\u01da\u01d7\3\2\2\2\u01da\u01d9\3\2\2\2\u01db")
        buf.write("\u01dc\3\2\2\2\u01dc\u01dd\bE\6\2\u01dd\u008a\3\2\2\2")
        buf.write("\u01de\u01e3\5\33\16\2\u01df\u01e2\n\13\2\2\u01e0\u01e2")
        buf.write("\5\31\r\2\u01e1\u01df\3\2\2\2\u01e1\u01e0\3\2\2\2\u01e2")
        buf.write("\u01e5\3\2\2\2\u01e3\u01e1\3\2\2\2\u01e3\u01e4\3\2\2\2")
        buf.write("\u01e4\u01e8\3\2\2\2\u01e5\u01e3\3\2\2\2\u01e6\u01e9\t")
        buf.write("\r\2\2\u01e7\u01e9\5\25\13\2\u01e8\u01e6\3\2\2\2\u01e8")
        buf.write("\u01e7\3\2\2\2\u01e9\u01ea\3\2\2\2\u01ea\u01eb\bF\7\2")
        buf.write("\u01eb\u008c\3\2\2\2\u01ec\u01ed\13\2\2\2\u01ed\u01ee")
        buf.write("\bG\b\2\u01ee\u008e\3\2\2\2\35\2\u0095\u009e\u00af\u00b6")
        buf.write("\u00ba\u00bd\u00c3\u00ca\u00cf\u00d6\u00dc\u019c\u01a4")
        buf.write("\u01aa\u01b0\u01b8\u01bd\u01bf\u01c4\u01cb\u01d2\u01d4")
        buf.write("\u01da\u01e1\u01e3\u01e8\t\3>\2\3?\3\3A\4\b\2\2\3E\5\3")
        buf.write("F\6\3G\7")
        return buf.getvalue()


class MT22Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    AUTO = 1
    BREAK = 2
    BOOLEAN = 3
    DO = 4
    ELSE = 5
    FLOAT = 6
    FOR = 7
    FUNCTION = 8
    IF = 9
    INTEGER = 10
    RETURN = 11
    STRING = 12
    WHILE = 13
    VOID = 14
    OUT = 15
    CONTINUE = 16
    OF = 17
    INHERIT = 18
    ARRAY = 19
    ADD = 20
    MINUS = 21
    MUL = 22
    DIV = 23
    MOD = 24
    NOT = 25
    AND = 26
    OR = 27
    EQUAL = 28
    NOT_EQUAL = 29
    LESS_THAN = 30
    LESS_EQUAL = 31
    GREATER_THAN = 32
    GREATER_EQUAL = 33
    TWO_COLON = 34
    LP = 35
    RP = 36
    LSB = 37
    RSB = 38
    DOT = 39
    COMMA = 40
    SEMI = 41
    COLON = 42
    LB = 43
    RB = 44
    ASSIGN = 45
    INTLIT = 46
    FLOATLIT = 47
    BOOLEAN_LIT = 48
    STRING_LIT = 49
    IDENTIFIER = 50
    COMMENT = 51
    WS = 52
    UNCLOSE_STRING = 53
    ILLEGAL_ESCAPE = 54
    ERROR_CHAR = 55

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'auto'", "'break'", "'boolean'", "'do'", "'else'", "'float'", 
            "'for'", "'function'", "'if'", "'integer'", "'return'", "'string'", 
            "'while'", "'void'", "'out'", "'continue'", "'of'", "'inherit'", 
            "'array'", "'+'", "'-'", "'*'", "'/'", "'%'", "'!'", "'&&'", 
            "'||'", "'=='", "'!='", "'<'", "'<='", "'>'", "'>='", "'::'", 
            "'('", "')'", "'['", "']'", "'.'", "','", "';'", "':'", "'{'", 
            "'}'", "'='" ]

    symbolicNames = [ "<INVALID>",
            "AUTO", "BREAK", "BOOLEAN", "DO", "ELSE", "FLOAT", "FOR", "FUNCTION", 
            "IF", "INTEGER", "RETURN", "STRING", "WHILE", "VOID", "OUT", 
            "CONTINUE", "OF", "INHERIT", "ARRAY", "ADD", "MINUS", "MUL", 
            "DIV", "MOD", "NOT", "AND", "OR", "EQUAL", "NOT_EQUAL", "LESS_THAN", 
            "LESS_EQUAL", "GREATER_THAN", "GREATER_EQUAL", "TWO_COLON", 
            "LP", "RP", "LSB", "RSB", "DOT", "COMMA", "SEMI", "COLON", "LB", 
            "RB", "ASSIGN", "INTLIT", "FLOATLIT", "BOOLEAN_LIT", "STRING_LIT", 
            "IDENTIFIER", "COMMENT", "WS", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
            "ERROR_CHAR" ]

    ruleNames = [ "CPPCOMMENT", "CCOMMENT", "LETTER", "DIGIT", "UNDERSCORE", 
                  "INTPART", "FRACPART", "SIGN", "EXPPART", "NESCAPE", "STR", 
                  "ESCAPE", "TWO_QUOTE", "AUTO", "BREAK", "BOOLEAN", "DO", 
                  "ELSE", "FALSE", "FLOAT", "FOR", "FUNCTION", "IF", "INTEGER", 
                  "RETURN", "STRING", "TRUE", "WHILE", "VOID", "OUT", "CONTINUE", 
                  "OF", "INHERIT", "ARRAY", "ADD", "MINUS", "MUL", "DIV", 
                  "MOD", "NOT", "AND", "OR", "EQUAL", "NOT_EQUAL", "LESS_THAN", 
                  "LESS_EQUAL", "GREATER_THAN", "GREATER_EQUAL", "TWO_COLON", 
                  "LP", "RP", "LSB", "RSB", "DOT", "COMMA", "SEMI", "COLON", 
                  "LB", "RB", "ASSIGN", "INTLIT", "FLOATLIT", "BOOLEAN_LIT", 
                  "STRING_LIT", "IDENTIFIER", "COMMENT", "WS", "UNCLOSE_STRING", 
                  "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    grammarFileName = "MT22.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[60] = self.INTLIT_action 
            actions[61] = self.FLOATLIT_action 
            actions[63] = self.STRING_LIT_action 
            actions[67] = self.UNCLOSE_STRING_action 
            actions[68] = self.ILLEGAL_ESCAPE_action 
            actions[69] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def INTLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.text = self.text.replace("_","")
     

    def FLOATLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            self.text = self.text.replace("_","")
     

    def STRING_LIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:
            self.text = str(self.text[1:-1])
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:

                if len(self.text) >= 2 and self.text[-1] == '\n' and self.text[-2] == '\r':
                    raise UncloseString(self.text[1:-2])
                elif (self.text[-1] == '\n'):
                    raise UncloseString(self.text[1:-1])
                else:
                    raise UncloseString(self.text[1:])

     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:

                raise IllegalEscape(self.text[1:])

     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 5:
            raise ErrorToken(self.text)
     


