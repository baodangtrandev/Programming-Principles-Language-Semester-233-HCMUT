"""
 * Initial code for Assignment
 * Programming Language Principles
 * Author: Võ Tiến
 * Link FB : https://www.facebook.com/profile.php?id=100056605580171
 * Link Group : https://www.facebook.com/groups/211867931379013
 * Date: 06.22.2024
"""
import sys
import os
import unittest
import inspect
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from TestUtils import TestLexer

"""
 * python3 run.py test LexerSuite or python run.py test LexerSuite 
 * Description test case
"""
class LexerSuite(unittest.TestCase):
      
    def test_001(self):
        """test SKIP"""
        input = """ \t\r\f\b\n \t \r \f \b \n
        
        """
        expect = "<EOF>"
        self.assertTrue(TestLexer.test(input, expect, inspect.stack()[0].function))

    def test_002(self):
        """test SKIP"""
        input = """
            // Comment Vo Tien
            \t \r // Vo Tien
            // Vo Tien // // Vo Tien
        """
        expect = "<EOF>"
        self.assertTrue(TestLexer.test(input, expect, inspect.stack()[0].function))
        
    def test_003(self):
        """test SKIP"""
        input = """
           /* 123 */
           /* // 123 */
        """
        expect = "<EOF>"
        self.assertTrue(TestLexer.test(input, expect, inspect.stack()[0].function))
        
    def test_004(self):
        """test SKIP"""
        input = """
           /* (1) */ // */
        """
        expect = "<EOF>"
        self.assertTrue(TestLexer.test(input, expect, inspect.stack()[0].function))
        
    def test_005(self):
        """test SKIP"""
        input = """
           /* /* (1) * / */ */
        """
        expect = "*,/,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, inspect.stack()[0].function))
        
    def test_006(self):
        """test KeyWord"""
        input = """
           auto float integer string void array // type
           break do else for function return while out continue of inherit // keyword
           false true // literal boolean
        """
        expect = "auto,float,integer,string,void,array,break,do,else,for,function,return,while,out,continue,of,inherit,false,true,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, inspect.stack()[0].function))

    def test_007(self):
        """test Operators"""
        input = """
           + - * / % !
           && || != < > <= >= ::
        """
        expect = "+,-,*,/,%,!,&&,||,!=,<,>,<=,>=,::,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, inspect.stack()[0].function))

    def test_008(self):
        """test Separators"""
        input = """
           [] {} () , . ; :
        """
        expect = "[,],{,},(,),,,.,;,:,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, inspect.stack()[0].function))

    def test_009(self):
        """test Identifiers"""
        input = """
           a1b A1b _1b b B _ __ a_1_b
        """
        expect = "a1b,A1b,_1b,b,B,_,__,a_1_b,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, inspect.stack()[0].function))

    def test_010(self):
        """test Identifiers"""
        input = """
           1b
        """
        expect = "1,b,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, inspect.stack()[0].function))

    def test_011(self):
        """test Identifiers"""
        input = """
           $a
        """
        expect = "Error Token $"
        self.assertTrue(TestLexer.test(input, expect, inspect.stack()[0].function))

    def test_012(self):
        """test Identifiers"""
        input = """
           a~b
        """
        expect = "a,Error Token ~"
        self.assertTrue(TestLexer.test(input, expect, inspect.stack()[0].function))

    def test_013(self):
        """test Identifiers"""
        input = """
           a~b
        """
        expect = "a,Error Token ~"
        self.assertTrue(TestLexer.test(input, expect, inspect.stack()[0].function))

    def test_014(self):
        """test INT Literal"""
        input = """
           0 10 1_2_301 1_2 1_0_0 1_0 9_01_000 1_0_0_00_000_0000
        """
        expect = "0,10,12301,12,100,10,901000,100000000000,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, inspect.stack()[0].function))
        
    def test_015(self):
        """test INT Literal"""
        input = """
           0010
        """
        expect = "0,0,10,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, inspect.stack()[0].function))
        
    def test_016(self):
        """test INT Literal"""
        input = """
           0_01
        """
        expect = "0,_01,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, inspect.stack()[0].function))
        
    def test_017(self):
        """test INT Literal"""
        input = """
           01_2
        """
        expect = "0,12,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, inspect.stack()[0].function))
        
    def test_018(self):
        """test INT Literal"""
        input = """
           1__2
        """
        expect = "1,__2,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, inspect.stack()[0].function))

    def test_019(self):
        """test INT Literal"""
        input = """
           1__
        """
        expect = "1,__,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, inspect.stack()[0].function))
        
    def test_019(self):
        """test INT Literal"""
        input = """
           1_00_
        """
        expect = "100,_,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, inspect.stack()[0].function))
        
    def test_020(self):
        """test FLOAT Literal"""
        input = """
           1_00_
        """
        expect = "100,_,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, inspect.stack()[0].function))
        
    def test_021(self):
        """test FLOAT Literal"""
        input = """
           0.01e+0 0.01e-000 1_0.e-0 1_0.10e+1 1_0.e-1 1_2e-10 1_0e+10 1_0.
        """
        expect = "0.01e+0,0.01e-000,10.e-0,10.10e+1,10.e-1,12e-10,10e+10,10.,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, inspect.stack()[0].function))

    def test_022(self):
        """test FLOAT Literal"""
        input = """
           e-1 e0 e+1 .01 .02 .
        """
        expect = "e,-,1,e0,e,+,1,.,0,1,.,0,2,.,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, inspect.stack()[0].function))
        
    def test_023(self):
        """test FLOAT Literal"""
        input = """
           1_0.1_2
        """
        expect = "10.1,_2,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, inspect.stack()[0].function))
        
    def test_024(self):
        """test FLOAT Literal"""
        input = """
           1_0.e1_1
        """
        expect = "10.e1,_1,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, inspect.stack()[0].function))
        
    def test_025(self):
        """test FLOAT Literal"""
        input = """
           1_0.e1_1
        """
        expect = "10.e1,_1,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, inspect.stack()[0].function))
        
    def test_026(self):
        """test FLOAT Literal"""
        input = """
           1_0.e1_1
        """
        expect = "10.e1,_1,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, inspect.stack()[0].function))

    def test_027(self):
        """test FLOAT Literal"""
        input = """
           1_0.e1_1
        """
        expect = "10.e1,_1,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, inspect.stack()[0].function))
        
    def test_028(self):
        """test String Literal"""
        input = """
           "abc ' \b \f \t \\b \\f \\r \\n \\t \\' \\" \\\\ $%^&*#@!~()1:<>;?{]}["
        """
        expect = "abc ' \b \f \t \\b \\f \\r \\n \\t \\' \\\" \\\\ $%^&*#@!~()1:<>;?{]}[,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, inspect.stack()[0].function))

    def test_029(self):
        """test UNCLOSE_STRING"""
        input = """
           " abc \n"
        """
        expect = "Unclosed String:  abc "
        self.assertTrue(TestLexer.test(input, expect, inspect.stack()[0].function))
        
    def test_030(self):
        """test UNCLOSE_STRING"""
        input = """
           " abc \n ab \n \n"
        """
        expect = "Unclosed String:  abc "
        self.assertTrue(TestLexer.test(input, expect, inspect.stack()[0].function))

    def test_031(self):
        """test UNCLOSE_STRING"""
        input = """
           " abc 
           123 "
        """
        expect = "Unclosed String:  abc "
        self.assertTrue(TestLexer.test(input, expect, inspect.stack()[0].function))

    def test_032(self):
        """test UNCLOSE_STRING"""
        input = """
           " abc \n\r"
        """
        expect = "Unclosed String:  abc "
        self.assertTrue(TestLexer.test(input, expect, inspect.stack()[0].function))
              
    def test_033(self):
        """test ILLEGAL_ESCAPE"""
        input = """
           " abc \\1"
        """
        expect = "Illegal Escape In String:  abc \\1"
        self.assertTrue(TestLexer.test(input, expect, inspect.stack()[0].function))
       
    def test_034(self):
        """test ILLEGAL_ESCAPE"""
        input = """
           " abc \\ "
        """
        expect = "Illegal Escape In String:  abc \\ "
        self.assertTrue(TestLexer.test(input, expect, inspect.stack()[0].function))

    def test_035(self):
        """test UNCLOSE_STRING"""
        input = """" abc """
        expect = "Unclosed String:  abc "
        self.assertTrue(TestLexer.test(input, expect, inspect.stack()[0].function))
                                         
    def test_036(self):
        """test ILLEGAL_ESCAPE"""
        input = """\"abc\\\""""
        expect = "Unclosed String: abc\\\""
        self.assertTrue(TestLexer.test(input, expect, inspect.stack()[0].function))

    def test_037(self):
        """test float"""
        input = """.123"""
        expect = ".,123,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, inspect.stack()[0].function))

    def test_038(self):
        """test float"""
        input = """.00123"""
        expect = ".,0,0,123,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, inspect.stack()[0].function))

    def test_039(self):
        """test float"""
        input = """12."""
        expect = "12.,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, inspect.stack()[0].function))

    def test_040(self):
        """test float"""
        input = """#"""
        expect = "Error Token #"
        self.assertTrue(TestLexer.test(input, expect, inspect.stack()[0].function))

    def test_040(self):
        """test error"""
        input = """#"""
        expect = "Error Token #"
        self.assertTrue(TestLexer.test(input, expect, inspect.stack()[0].function))

    def test_040(self):
        """test string"""
        input = """
            "' '""
        
        """
        expect = "' ',Unclosed String: "
        self.assertTrue(TestLexer.test(input, expect, inspect.stack()[0].function))

    def test_041(self):
        """test error"""
        input = """
            @
        
        """
        expect = "Error Token @"
        self.assertTrue(TestLexer.test(input, expect, inspect.stack()[0].function))

    def test_042(self):
        """test error"""
        input = """
            / /
        
        """
        expect = "/,/,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, inspect.stack()[0].function))
