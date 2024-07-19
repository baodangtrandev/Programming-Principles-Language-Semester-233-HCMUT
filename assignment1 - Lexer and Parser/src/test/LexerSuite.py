import unittest
from TestUtils import TestLexer


class LexerSuite(unittest.TestCase):

    def test_001(self):
        """test SKIP"""
        input = """ \t\r\f\b\n \t \r \f \b \n
        
        """
        expect = "<EOF>"
        self.assertTrue(TestLexer.test(input, expect, "001"))

    def test_002(self):
        """test SKIP"""
        input = """
            // Comment Vo Tien
            \t \r // Vo Tien
            // Vo Tien // // Vo Tien
        """
        expect = "<EOF>"
        self.assertTrue(TestLexer.test(input, expect, "002"))
        
    def test_003(self):
        """test SKIP"""
        input = """
           /* 123 */
           /* // 123 */
        """
        expect = "<EOF>"
        self.assertTrue(TestLexer.test(input, expect, "003"))
        
    def test_004(self):
        """test SKIP"""
        input = """
           /* (1) */ // */
        """
        expect = "<EOF>"
        self.assertTrue(TestLexer.test(input, expect, "004"))
        
    def test_005(self):
        """test SKIP"""
        input = """
           /* /* (1) * / */ */
        """
        expect = "*,/,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, "005"))
        
    def test_006(self):
        """test KeyWord"""
        input = """
           auto float integer string void array // type
           break do else for function return while out continue of inherit // keyword
           false true // literal boolean
        """
        expect = "auto,float,integer,string,void,array,break,do,else,for,function,return,while,out,continue,of,inherit,false,true,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, "006"))

    def test_007(self):
        """test Operators"""
        input = """
           + - * / % !
           && || != < > <= >= ::
        """
        expect = "+,-,*,/,%,!,&&,||,!=,<,>,<=,>=,::,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, "007"))

    def test_008(self):
        """test Separators"""
        input = """
           [] {} () , . ; :
        """
        expect = "[,],{,},(,),,,.,;,:,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, "008"))

    def test_009(self):
        """test Identifiers"""
        input = """
           a1b A1b _1b b B _ __ a_1_b
        """
        expect = "a1b,A1b,_1b,b,B,_,__,a_1_b,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, "009"))

    def test_010(self):
        """test Identifiers"""
        input = """
           1b
        """
        expect = "1,b,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, "010"))

    def test_011(self):
        """test Identifiers"""
        input = """
           $a
        """
        expect = "Error Token $"
        self.assertTrue(TestLexer.test(input, expect, "011"))

    def test_012(self):
        """test Identifiers"""
        input = """
           a~b
        """
        expect = "a,Error Token ~"
        self.assertTrue(TestLexer.test(input, expect, "012"))

    def test_013(self):
        """test Identifiers"""
        input = """
           a~b
        """
        expect = "a,Error Token ~"
        self.assertTrue(TestLexer.test(input, expect, "013"))

    def test_014(self):
        """test INT Literal"""
        input = """
           0 10 1_2_301 1_2 1_0_0 1_0 9_01_000 1_0_0_00_000_0000
        """
        expect = "0,10,12301,12,100,10,901000,100000000000,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, "014"))
        
    def test_015(self):
        """test INT Literal"""
        input = """
           0010
        """
        expect = "0,0,10,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, "015"))
        
    def test_016(self):
        """test INT Literal"""
        input = """
           0_01
        """
        expect = "0,_01,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, "016"))
        
    def test_017(self):
        """test INT Literal"""
        input = """
           01_2
        """
        expect = "0,12,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, "017"))
        
    def test_018(self):
        """test INT Literal"""
        input = """
           1__2
        """
        expect = "1,__2,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, "018"))

    def test_019(self):
        """test INT Literal"""
        input = """
           1__
        """
        expect = "1,__,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, "019"))
        
    def test_020(self):
        """test INT Literal"""
        input = """
           1_00_
        """
        expect = "100,_,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, "020"))
        
    def test_021(self):
        """test FLOAT Literal"""
        input = """
           0.01e+0 0.01e-000 1_0.e-0 1_0.10e+1 1_0.e-1 1_2e-10 1_0e+10 1_0.
        """
        expect = "0.01e+0,0.01e-000,10.e-0,10.10e+1,10.e-1,12e-10,10e+10,10.,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, "021"))

    def test_022(self):
        """test FLOAT Literal"""
        input = """
           e-1 e0 e+1 .01 .02 .
        """
        expect = "e,-,1,e0,e,+,1,.,0,1,.,0,2,.,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, "022"))
        
    def test_023(self):
        """test FLOAT Literal"""
        input = """
           1_0.1_2
        """
        expect = "10.1,_2,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, "023"))
        
    def test_024(self):
        """test FLOAT Literal"""
        input = """
           1_0.e1_1
        """
        expect = "10.e1,_1,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, "024"))

    def test_025(self):
        """test FLOAT Literal"""
        input = """
           1_0.e1_1
        """
        expect = "10.e1,_1,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, "025"))

    def test_026(self):
        """test FLOAT Literal"""
        input = """
           1_0.e1_1
        """
        expect = "10.e1,_1,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, "026"))

    def test_027(self):
        """test FLOAT Literal"""
        input = """
           1_0.e1_1
        """
        expect = "10.e1,_1,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, "027"))
        
    def test_028(self):
        """test String Literal"""
        input = """
           "abc ' \b \f \t \\b \\f \\r \\n \\t \\' \\" \\\\ $%^&*#@!~()1:<>;?{]}["
        """
        expect = "abc ' \b \f \t \\b \\f \\r \\n \\t \\' \\\" \\\\ $%^&*#@!~()1:<>;?{]}[,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, "028"))

    def test_029(self):
        """test UNCLOSE_STRING"""
        input = """
           " abc \n"
        """
        expect = "Unclosed String:  abc "
        self.assertTrue(TestLexer.test(input, expect, "029"))
        
    def test_030(self):
        """test UNCLOSE_STRING"""
        input = """
           " abc \n ab \n \n"
        """
        expect = "Unclosed String:  abc "
        self.assertTrue(TestLexer.test(input, expect, "030"))

    def test_031(self):
        """test UNCLOSE_STRING"""
        input = """
           " abc 
           123 "
        """
        expect = "Unclosed String:  abc "
        self.assertTrue(TestLexer.test(input, expect, "031"))

    def test_032(self):
        """test UNCLOSE_STRING"""
        input = """
           " abc \n\r"
        """
        expect = "Unclosed String:  abc "
        self.assertTrue(TestLexer.test(input, expect, "032"))
              
    def test_033(self):
        """test ILLEGAL_ESCAPE"""
        input = """
           " abc \\1"
        """
        expect = "Illegal Escape In String:  abc \\1"
        self.assertTrue(TestLexer.test(input, expect, "033"))
       
    def test_034(self):
        """test ILLEGAL_ESCAPE"""
        input = """
           " abc \\ "
        """
        expect = "Illegal Escape In String:  abc \\ "
        self.assertTrue(TestLexer.test(input, expect, "034"))

    def test_035(self):
        """test UNCLOSE_STRING"""
        input = """" abc """
        expect = "Unclosed String:  abc "
        self.assertTrue(TestLexer.test(input, expect, "035"))
                                         
    def test_036(self):
        """test ILLEGAL_ESCAPE"""
        input = """\"abc\\\""""
        expect = "Unclosed String: abc\\\""
        self.assertTrue(TestLexer.test(input, expect, "036"))

    def test_037(self):
        """test float"""
        input = """.123"""
        expect = ".,123,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, "037"))

    def test_038(self):
        """test float"""
        input = """.00123"""
        expect = ".,0,0,123,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, "038"))

    def test_039(self):
        """test float"""
        input = """12."""
        expect = "12.,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, "039"))

    def test_040(self):
        """test error"""
        input = """#"""
        expect = "Error Token #"
        self.assertTrue(TestLexer.test(input, expect, "040"))

    def test_041(self):
        """test error"""
        input = """
            @
        
        """
        expect = "Error Token @"
        self.assertTrue(TestLexer.test(input, expect, "041"))

    def test_042(self):
        """test error"""
        input = """
            / /
        
        """
        expect = "/,/,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, "042"))

    def test_043(self):
        """test float"""
        input = """123.456"""
        expect = "123.456,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, "043"))

    def test_044(self):
        """test float"""
        input = """0.456"""
        expect = "0.456,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, "044"))

    def test_045(self):
        """test float"""
        input = """123e-10"""
        expect = "123e-10,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, "045"))

    def test_046(self):
        """test float"""
        input = """456.78e+9"""
        expect = "456.78e+9,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, "046"))

    def test_047(self):
        """test identifier"""
        input = """_validIdentifier"""
        expect = "_validIdentifier,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, "047"))

    def test_048(self):
        """test identifier"""
        input = """validIdentifier123"""
        expect = "validIdentifier123,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, "048"))

    def test_049(self):
        """test string literal"""
        input = """ "Valid String Literal" """
        expect = "Valid String Literal,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, "049"))

    def test_050(self):
        """test string literal"""
        input = """ "String with escape \\n" """
        expect = "String with escape \\n,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, "050"))

    def test_051(self):
        """test string literal"""
        input = """ "String with special chars !@#$%^&*()_+{}:" """
        expect = "String with special chars !@#$%^&*()_+{}:,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, "051"))

    def test_052(self):
        """test invalid char"""
        input = """ ` """
        expect = "Error Token `"
        self.assertTrue(TestLexer.test(input, expect, "052"))

    def test_053(self):
        """test invalid char"""
        input = """ ~ """
        expect = "Error Token ~"
        self.assertTrue(TestLexer.test(input, expect, "053"))

    def test_054(self):
        """test keyword"""
        input = """ function """
        expect = "function,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, "054"))

    def test_055(self):
        """test keyword"""
        input = """ auto """
        expect = "auto,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, "055"))

    def test_056(self):
        """test keyword"""
        input = """ return """
        expect = "return,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, "056"))

    def test_057(self):
        """test keyword"""
        input = """ break """
        expect = "break,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, "057"))

    def test_058(self):
        """test boolean literal"""
        input = """ true """
        expect = "true,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, "058"))

    def test_059(self):
        """test boolean literal"""
        input = """ false """
        expect = "false,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, "059"))

    def test_060(self):
        """test operator"""
        input = """ + """
        expect = "+,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, "060"))

    def test_061(self):
        """test operator"""
        input = """ - """
        expect = "-,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, "061"))

    def test_062(self):
        """test operator"""
        input = """ * """
        expect = "*,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, "062"))

    def test_063(self):
        """test operator"""
        input = """ / """
        expect = "/,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, "063"))

    def test_064(self):
        """test operator"""
        input = """ % """
        expect = "%,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, "064"))

    def test_065(self):
        """test operator"""
        input = """ ! """
        expect = "!,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, "065"))

    def test_066(self):
        """test operator"""
        input = """ && """
        expect = "&&,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, "066"))

    def test_067(self):
        """test operator"""
        input = """ || """
        expect = "||,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, "067"))

    def test_068(self):
        """test operator"""
        input = """ != """
        expect = "!=,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, "068"))

    def test_069(self):
        """test operator"""
        input = """ < """
        expect = "<,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, "069"))

    def test_070(self):
        """test operator"""
        input = """ > """
        expect = ">,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, "070"))

    def test_071(self):
        """test operator"""
        input = """ <= """
        expect = "<=,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, "071"))

    def test_072(self):
        """test operator"""
        input = """ >= """
        expect = ">=,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, "072"))

    def test_073(self):
        """test operator"""
        input = """ :: """
        expect = "::,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, "073"))

    def test_074(self):
        """test separator"""
        input = """ [] """
        expect = "[,],<EOF>"
        self.assertTrue(TestLexer.test(input, expect, "074"))

    def test_075(self):
        """test separator"""
        input = """ {} """
        expect = "{,},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, "075"))

    def test_076(self):
        """test separator"""
        input = """ () """
        expect = "(,),<EOF>"
        self.assertTrue(TestLexer.test(input, expect, "076"))

    def test_077(self):
        """test separator"""
        input = """ , """
        expect = ",,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, "077"))

    def test_078(self):
        """test separator"""
        input = """ . """
        expect = ".,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, "078"))

    def test_079(self):
        """test separator"""
        input = """ ; """
        expect = ";,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, "079"))

    def test_080(self):
        """test separator"""
        input = """ : """
        expect = ":,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, "080"))

    def test_081(self):
        """test integer literal"""
        input = """ 123 """
        expect = "123,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, "081"))

    def test_082(self):
        """test integer literal"""
        input = """ 0 """
        expect = "0,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, "082"))

    def test_083(self):
        """test integer literal"""
        input = """ 999999 """
        expect = "999999,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, "083"))

    def test_084(self):
        """test integer literal"""
        input = """ 1001 """
        expect = "1001,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, "084"))

    def test_085(self):
        """test integer literal"""
        input = """ 1234567890 """
        expect = "1234567890,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, "085"))

    def test_086(self):
        """test integer literal"""
        input = """ 2147483647 """
        expect = "2147483647,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, "086"))

    def test_087(self):
        """test integer literal"""
        input = """ 0x123 """
        expect = "0,x123,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, "087"))

    def test_088(self):
        """test integer literal"""
        input = """ 0XABC """
        expect = "0,XABC,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, "088"))

    def test_089(self):
        """test integer literal"""
        input = """ 0123 """
        expect = "0,123,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, "089"))

    def test_090(self):
        """test float literal"""
        input = """ 0.123 """
        expect = "0.123,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, "090"))

    def test_091(self):
        """test float literal"""
        input = """ 123.456 """
        expect = "123.456,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, "091"))

    def test_092(self):
        """test float literal"""
        input = """ 0e10 """
        expect = "0e10,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, "092"))

    def test_093(self):
        """test float literal"""
        input = """ 1.23e+4 """
        expect = "1.23e+4,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, "093"))

    def test_094(self):
        """test float literal"""
        input = """ 1.23e-4 """
        expect = "1.23e-4,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, "094"))

    def test_095(self):
        """test float literal"""
        input = """ 1e10 """
        expect = "1e10,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, "095"))

    def test_096(self):
        """test float literal"""
        input = """ 123e-4 """
        expect = "123e-4,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, "096"))

    def test_097(self):
        """test float literal"""
        input = """ 123e+4 """
        expect = "123e+4,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, "097"))

    def test_098(self):
        """test string literal"""
        input = """ "This is a test string" """
        expect = "This is a test string,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, "098"))

    def test_099(self):
        """test string literal"""
        input = """ "Another test string" """
        expect = "Another test string,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, "099"))

    def test_100(self):
        """test unclose string"""
        input = """ "Unclosed string literal """
        expect = "Unclosed String: Unclosed string literal "
        self.assertTrue(TestLexer.test(input, expect, "100"))
