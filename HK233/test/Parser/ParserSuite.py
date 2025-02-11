"""
 * Initial code for Assignment
 * Programming Language Principles
 * Author: Võ Tiến
 * Link FB : https://www.facebook.com/profile.php?id=100056605580171
 * Link Group : https://www.facebook.com/groups/211867931379013
 * Date: 06.19.2024
"""

import unittest
import inspect
from TestUtils import TestParser


class ParserSuite(unittest.TestCase):
    def test_001(self):
        """test Variable and type"""
        input = """
            a : integer;  
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, inspect.stack()[0].function))

    def test_002(self):
        """test Variable and type"""
        input = """
            a, b, c : integer; 
            a : integer 
        """
        expect = "Error on line 4 col 8: <EOF>"
        self.assertTrue(TestParser.test(input, expect, inspect.stack()[0].function))
               
    def test_003(self):
        """test Variable and type"""
        input = """
            a,  : integer; 
        """
        expect = "Error on line 2 col 16: :"
        self.assertTrue(TestParser.test(input, expect, inspect.stack()[0].function))
               
    def test_004(self):
        """test Variable and type"""
        input = """
            a : float;
            b : boolean;
            c : string;
            d : auto;
            e, h : auto;
            f : array [1] of integer;
            g : array [1, 2] of float;
            h, h, h : array [1, 3] of boolean;
            j : array [1, 3] of integer;
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, inspect.stack()[0].function))
             
    def test_005(self):
        """test Variable and type"""
        input = """
            f : array [1] of auto;
        """
        expect = "Error on line 2 col 29: auto"
        self.assertTrue(TestParser.test(input, expect, inspect.stack()[0].function))  
        
    def test_006(self):
        """test Variable and type"""
        input = """
            f : array [1] of auto;
        """
        expect = "Error on line 2 col 29: auto"
        self.assertTrue(TestParser.test(input, expect, inspect.stack()[0].function)) 
        
    def test_007(self):
        """test Variable and type"""
        input = """
            f : array [] of float;
        """
        expect = "Error on line 2 col 23: ]"
        self.assertTrue(TestParser.test(input, expect, inspect.stack()[0].function)) 
        
    def test_008(self):
        """test Variable and type"""
        input = """
            f : array [,] of float;
        """
        expect = "Error on line 2 col 23: ,"
        self.assertTrue(TestParser.test(input, expect, inspect.stack()[0].function)) 
        
    def test_009(self):
        """test Variable and type"""
        input = """
            f : array [1.2] of float;
        """
        expect = "Error on line 2 col 23: 1.2"
        self.assertTrue(TestParser.test(input, expect, inspect.stack()[0].function)) 
        
    def test_010(self):
        """test Variable and type"""
        input = """
            f : array [true] of float;
        """
        expect = "Error on line 2 col 23: true"
        self.assertTrue(TestParser.test(input, expect, inspect.stack()[0].function)) 
        
    def test_011(self):
        """test Variable and type"""
        input = """
            f : array [1+1] of float;
        """
        expect = "Error on line 2 col 24: +"
        self.assertTrue(TestParser.test(input, expect, inspect.stack()[0].function)) 

    def test_012(self):
        """test Variable and type"""
        input = """
            f : integer = 1;
            a, b : integer = 1, 2;
            a, b, c, d : array [1] of float  = 1, 2, 3, 4;
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, inspect.stack()[0].function)) 
                
    def test_013(self):
        """test Variable and type"""
        input = """
            a, b : integer = 1;
        """
        expect = "Error on line 2 col 30: ;"
        self.assertTrue(TestParser.test(input, expect, inspect.stack()[0].function)) 
                
    def test_014(self):
        """test Variable and type"""
        input = """
            a, b : integer = 1, 2, 3;
        """
        expect = "Error on line 2 col 33: ,"
        self.assertTrue(TestParser.test(input, expect, inspect.stack()[0].function)) 

    def test_015(self):
        """test Variable and type"""
        input = """
            for : auto = 1;
        """
        expect = "Error on line 2 col 12: for"
        self.assertTrue(TestParser.test(input, expect, inspect.stack()[0].function)) 

    def test_016(self):
        """test Variable and type"""
        input = """
            a : auto = for;
        """
        expect = "Error on line 2 col 23: for"
        self.assertTrue(TestParser.test(input, expect, inspect.stack()[0].function)) 
                                                
    def test_017(self):
        """test Variable and type"""
        input = """
            a : integer = ;
        """
        expect = "Error on line 2 col 26: ;"
        self.assertTrue(TestParser.test(input, expect, inspect.stack()[0].function)) 

    def test_018(self):
        """test function"""
        input = """
            foo : function auto (inherit out id : auto, inherit out id : auto) inherit foo1 {}
            foo : function array [1] of integer () {}
            foo : function integer (inherit id : float, out id : boolean, id : array [1] of integer) {}
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, inspect.stack()[0].function)) 
        
    def test_019(self):
        """test function"""
        input = """
            function : function auto (inherit out id : auto, inherit out id : auto) inherit foo1 {}
        """
        expect = "Error on line 2 col 12: function"
        self.assertTrue(TestParser.test(input, expect, inspect.stack()[0].function)) 
        
    def test_020(self):
        """test function"""
        input = """
            foo : function auto (out inherit id : auto, inherit out id : auto) inherit foo1 {}
        """
        expect = "Error on line 2 col 37: inherit"
        self.assertTrue(TestParser.test(input, expect, inspect.stack()[0].function)) 
        
    def test_021(self):
        """test function"""
        input = """
            foo : function auto (inherit out id : auto, ) inherit foo1 {}
        """
        expect = "Error on line 2 col 56: )"
        self.assertTrue(TestParser.test(input, expect, inspect.stack()[0].function)) 
        
    def test_022(self):
        """test function"""
        input = """
            foo : function auto (inherit out id : auto) inherit out foo1 {}
        """
        expect = "Error on line 2 col 64: out"
        self.assertTrue(TestParser.test(input, expect, inspect.stack()[0].function)) 
        
    def test_023(self):
        """test function"""
        input = """
            foo : function (inherit out id : auto) {}
        """
        expect = "Error on line 2 col 27: ("
        self.assertTrue(TestParser.test(input, expect, inspect.stack()[0].function)) 
        
    def test_024(self):
        """test function"""
        input = """
            foo : function auto (inherit out id : auto) foo1 {}
        """
        expect = "Error on line 2 col 56: foo1"
        self.assertTrue(TestParser.test(input, expect, inspect.stack()[0].function)) 
        
    def test_025(self):
        """test Expression"""
        input = """
            id : auto = a :: 1;
            id : auto = a > b ;
            id : auto = a >= b;
            id : auto = a < b;
            id : auto = a <= b;
            id : auto = a == b;
            id : auto = a != b;
            id : auto = a && b || c ;
            id : auto = a + b - c;
            id : auto = a * b / c % d;
            id : auto = - a;
            id : auto = ! a;
            id : auto = a[1,2,3];
            id : auto = id[2,3] + id[2];
            id : auto = 1 + 1.0 - "1" + true - false - {1} + {1,2,3};
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, inspect.stack()[0].function)) 
                                                                               
                                                                               
    def test_026(self):
        """test Expression"""
        input = """
            id : auto = "a" :: 1 :: "b";
        """
        expect = "Error on line 2 col 33: ::"
        self.assertTrue(TestParser.test(input, expect, inspect.stack()[0].function)) 
                                                                               
    def test_027(self):
        """test Expression"""
        input = """
            id : auto = ("a" :: 1) :: "b";
            id : auto = "a" :: (a[2] :: "b");
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, inspect.stack()[0].function)) 

    def test_028(self):
        """test Expression"""
        input = """
            id : auto = a >= b < c;
        """
        expect = "Error on line 2 col 31: <"
        self.assertTrue(TestParser.test(input, expect, inspect.stack()[0].function)) 
                   
    def test_029(self):
        """test Expression"""
        input = """
            id : auto = a != b <= c;
        """
        expect = "Error on line 2 col 31: <="
        self.assertTrue(TestParser.test(input, expect, inspect.stack()[0].function)) 

    def test_030(self):
        """test Expression"""
        input = """
            id : integer = (a != b) <= c;
            id : float = a != (b <= c);
            id : string = a > b :: c < d;
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, inspect.stack()[0].function)) 
                                    
    def test_031(self):
        """test Expression"""
        input = """
            id : string = (a :: b) > c :: d;
            id : string = (a :: b) > (c :: d);
            id : string = a :: b > c :: d;
        """
        expect = "Error on line 4 col 37: ::"
        self.assertTrue(TestParser.test(input, expect, inspect.stack()[0].function)) 
                                    
    def test_032(self):
        """test Expression"""
        input = """
            id : string = a && b && c;
            id : string = a || b || c;
            id : string = true || false && "true" || d[1];
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, inspect.stack()[0].function)) 

    def test_033(self):
        """test Expression"""
        input = """
            id : array [2] of integer = (a > b) && (d < c);
            id : string = a > b && d < c;
        """
        expect = "Error on line 3 col 37: <"
        self.assertTrue(TestParser.test(input, expect, inspect.stack()[0].function)) 
                                       
    def test_034(self):
        """test Expression"""
        input = """
            id : string = a > b && d < c;
        """
        expect = "Error on line 2 col 37: <"
        self.assertTrue(TestParser.test(input, expect, inspect.stack()[0].function)) 

    def test_035(self):
        """test Expression"""
        input = """
            id : string = a + b * 2 / b % c;
            id : string = a + b + c * "2" / b % c;
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, inspect.stack()[0].function)) 

    def test_036(self):
        """test Expression"""
        input = """
            id : float = - b;
            id : float = ---- b;
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, inspect.stack()[0].function)) 

    def test_037(self):
        """test Expression"""
        input = """
            id : float = ! b;
            id : float = ! ! ! b;
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, inspect.stack()[0].function)) 

    def test_038(self):
        """test Expression"""
        input = """
            id : float = !! -- b;
            id : float = -- !! b;
        """
        expect = "Error on line 3 col 28: !"
        self.assertTrue(TestParser.test(input, expect, inspect.stack()[0].function)) 

    def test_039(self):
        """test Expression"""
        input = """
            id : float = a[1+2, 7 :: c, "!"];
            id : float = for[1+2, 7 :: c];
        """
        expect = "Error on line 3 col 25: for"
        self.assertTrue(TestParser.test(input, expect, inspect.stack()[0].function)) 

    def test_040(self):
        """test Expression"""
        input = """
            id : float = a[];
        """
        expect = "Error on line 2 col 27: ]"
        self.assertTrue(TestParser.test(input, expect, inspect.stack()[0].function)) 

    def test_041(self):
        """test Expression"""
        input = """
            id : float = a[1][2];
        """
        expect = "Error on line 2 col 29: ["
        self.assertTrue(TestParser.test(input, expect, inspect.stack()[0].function)) 

    def test_042(self):
        """test Expression"""
        input = """
            id : float = foo()[2];
        """
        expect = "Error on line 2 col 30: ["
        self.assertTrue(TestParser.test(input, expect, inspect.stack()[0].function)) 

    def test_043(self):
        """test Expression"""
        input = """
            id : float = foo() + foo(i[2, 1+ 2], 2 + 2 * 3 :: 3, "2");
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, inspect.stack()[0].function)) 

    def test_044(self):
        """test Expression"""
        input = """
            id : float = {1,1+2,"2"::"#"} + 2;
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, inspect.stack()[0].function)) 

    def test_045(self):
        """test Expression"""
        input = """
            id : float = {};
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, inspect.stack()[0].function)) 

    def test_046(self):
        """test Statements"""
        input = """
            foo : function auto ()
            {
                
            };
        """
        expect = "Error on line 5 col 13: ;"
        self.assertTrue(TestParser.test(input, expect, inspect.stack()[0].function)) 

    def test_047(self):
        """test Statements"""
        input = """
            foo : function auto ()
            {
                id : float;
                id : float = 1;
                a, b : float = 1, 2;
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, inspect.stack()[0].function)) 

    def test_048(self):
        """test Statements"""
        input = """
            foo : function auto ()
            {
                id = 1 + 2;
                id = {2}
            }
        """
        expect = "Error on line 6 col 12: }"
        self.assertTrue(TestParser.test(input, expect, inspect.stack()[0].function)) 

    def test_049(self):
        """test Statements"""
        input = """
            foo : function auto ()
            {
                id = 1 + 2;
                id[2] = 1;
                id[1+2, 2+3] = "1";
                id[] = 1;
            }
        """
        expect = "Error on line 7 col 19: ]"
        self.assertTrue(TestParser.test(input, expect, inspect.stack()[0].function)) 

    def test_050(self):
        """test Statements"""
        input = """
            foo : function auto ()
            {
                if (1+2*3) a = 1;
                else a = 2;
                
                if (1+2*3){}
                
                if (true)
                    if (true){}
                    else {}
                    
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, inspect.stack()[0].function)) 

    def test_051(self):
        """test Statements"""
        input = """
            foo : function auto ()
            {
                if (1+2*3) a = 1;
                else a = 2  
            }
        """
        expect = "Error on line 6 col 12: }"
        self.assertTrue(TestParser.test(input, expect, inspect.stack()[0].function)) 

    def test_052(self):
        """test Statements"""
        input = """
            foo : function auto ()
            {
                if (1+2*3) ;
                else a = 2; 
            }
        """
        expect = "Error on line 4 col 27: ;"
        self.assertTrue(TestParser.test(input, expect, inspect.stack()[0].function)) 

    def test_053(self):
        """test Statements"""
        input = """
            foo : function auto ()
            {
                if 1+2*3 a = 1;
                else a = 2; 
            }
        """
        expect = "Error on line 4 col 19: 1"
        self.assertTrue(TestParser.test(input, expect, inspect.stack()[0].function)) 

    def test_054(self):
        """test Statements"""
        input = """
            foo : function auto ()
            {
                if (1+2*3) a = 1;
                else (1+2*3) a = 2; 
            }
        """
        expect = "Error on line 5 col 21: ("
        self.assertTrue(TestParser.test(input, expect, inspect.stack()[0].function)) 

    def test_055(self):
        """test Statements"""
        input = """
            foo : function auto ()
            {
                continue;
                break;
                continue;
                break;
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, inspect.stack()[0].function)) 

    def test_056(self):
        """test Statements"""
        input = """
            foo : function auto ()
            {
                continue
            }
        """
        expect = "Error on line 5 col 12: }"
        self.assertTrue(TestParser.test(input, expect, inspect.stack()[0].function)) 

    def test_057(self):
        """test Statements"""
        input = """
            foo : function auto ()
            {
                break
            }
        """
        expect = "Error on line 5 col 12: }"
        self.assertTrue(TestParser.test(input, expect, inspect.stack()[0].function)) 

    def test_058(self):
        """test Statements"""
        input = """
            foo : function auto ()
            {
                for(id = 1, i < 1, i + 1) break;
                
                for(id = 1 + 2 * 3, 1+2::3 , 1+2::3) {}
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, inspect.stack()[0].function)) 

    def test_058(self):
        """test Statements"""
        input = """
            foo : function auto ()
            {
                for(id = 1, i < 1, i + 1) break;
                
                for(id = 1 + 2 * 3, 1+2::3 , 1+2::3) {}
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, inspect.stack()[0].function)) 
        
    def test_059(self):
        """test Statements"""
        input = """
            foo : function auto ()
            {
                for(id[2] = 1, i < 1, i + 1) break;
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, inspect.stack()[0].function)) 
        
    def test_060(self):
        """test Statements"""
        input = """
            foo : function auto ()
            {
                for(id = 1, i < 1,) break;
            }
        """
        expect = "Error on line 4 col 34: )"
        self.assertTrue(TestParser.test(input, expect, inspect.stack()[0].function)) 
        
    def test_061(self):
        """test Statements"""
        input = """
            foo : function auto ()
            {
                for(id = 1, , i + 1) continue;
            }
        """
        expect = "Error on line 4 col 28: ,"
        self.assertTrue(TestParser.test(input, expect, inspect.stack()[0].function)) 
        
    def test_062(self):
        """test Statements"""
        input = """
            foo : function auto ()
            {
                for(id = 1,1 , i = i + 1) continue;
            }
        """
        expect = "Error on line 4 col 33: ="
        self.assertTrue(TestParser.test(input, expect, inspect.stack()[0].function)) 
        
    def test_063(self):
        """test Statements"""
        input = """
            foo : function auto ()
            {
                while(true) break;
                while(1+2*3) {}
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, inspect.stack()[0].function)) 
        
    def test_064(self):
        """test Statements"""
        input = """
            foo : function auto ()
            {
                while() break;
            }
        """
        expect = "Error on line 4 col 22: )"
        self.assertTrue(TestParser.test(input, expect, inspect.stack()[0].function)) 
        
    def test_065(self):
        """test Statements"""
        input = """
            foo : function auto ()
            {
                do 
                {
                   break; 
                }
                while(1+2>3);
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, inspect.stack()[0].function)) 

    def test_066(self):
        """test Statements"""
        input = """
            foo : function auto ()
            {
                do 
                {
                   break; 
                }
                while(1+2>3)
            }
        """
        expect = "Error on line 9 col 12: }"
        self.assertTrue(TestParser.test(input, expect, inspect.stack()[0].function)) 

    def test_067(self):
        """test Statements"""
        input = """
            foo : function auto ()
            {
                do 
                    if(true) break;
                while(1+2>3);
            }
        """
        expect = "Error on line 5 col 20: if"
        self.assertTrue(TestParser.test(input, expect, inspect.stack()[0].function)) 

    def test_068(self):
        """test Statements"""
        input = """
            foo : function auto ()
            {
                do 
                    {};
                while(1+2>3);
            }
        """
        expect = "Error on line 5 col 22: ;"
        self.assertTrue(TestParser.test(input, expect, inspect.stack()[0].function)) 

    def test_069(self):
        """test Statements"""
        input = """
            foo : function auto ()
            {
                do 
                    {}
                while();
            }
        """
        expect = "Error on line 6 col 22: )"
        self.assertTrue(TestParser.test(input, expect, inspect.stack()[0].function)) 

    def test_070(self):
        """test Statements"""
        input = """
            foo : function auto ()
            {
                return 1 + 3 * 4 :: b;
                return (b > 2 :: b);
                return;
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, inspect.stack()[0].function)) 

    def test_071(self):
        """test Statements"""
        input = """
            foo : function auto ()
            {
                return
            }
        """
        expect = "Error on line 5 col 12: }"
        self.assertTrue(TestParser.test(input, expect, inspect.stack()[0].function)) 

    def test_072(self):
        """test Statements"""
        input = """
            foo : function auto ()
            {
                return 1 + 2
            }
        """
        expect = "Error on line 5 col 12: }"
        self.assertTrue(TestParser.test(input, expect, inspect.stack()[0].function)) 

    def test_073(self):
        """test Statements"""
        input = """
            foo : function auto ()
            {
                foo(1+2,3);
                foo();
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, inspect.stack()[0].function)) 

    def test_074(self):
        """test Statements"""
        input = """
            foo : function auto ()
            {
                foo(1,2)
            }
        """
        expect = "Error on line 5 col 12: }"
        self.assertTrue(TestParser.test(input, expect, inspect.stack()[0].function)) 

    def test_075(self):
        """test Statements"""
        input = """
            foo : function auto ()
            {
                {
                    
                }
                {
                    return;
                    return;
                }
                {{{return;}}}
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, inspect.stack()[0].function)) 

    def test_076(self):
        """test Statements"""
        input = """
            foo : function auto ()
            {
                {
                    
                };
            }
        """
        expect = "Error on line 6 col 17: ;"
        self.assertTrue(TestParser.test(input, expect, inspect.stack()[0].function)) 
        
        
    def test_077(self):
        """test function"""
        input = """
            foo : function void () break;
        """
        expect = "Error on line 2 col 35: break"
        self.assertTrue(TestParser.test(input, expect, inspect.stack()[0].function))        
        
    def test_078(self):
        """test function"""
        input = """
            a : void;
        """
        expect = "Error on line 2 col 16: void"
        self.assertTrue(TestParser.test(input, expect, inspect.stack()[0].function)) 
    
    def test_079(self):
        """test function"""
        input = """
            foo : function void (a : void){}
        """
        expect = "Error on line 2 col 37: void"
        self.assertTrue(TestParser.test(input, expect, inspect.stack()[0].function))          
        
    def test_080(self):
        """test function"""
        input = """
            foo : function void (){
                return {1 :: 2, 1 * 2 + 3 + a[2, 4], {1,3,4}};
                return {id} :: {3};
                return foo({1} + {3}, {4});
                id[2+3, {1}] = (2);
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, inspect.stack()[0].function))     
                                            
    def test_081(self):
        """test stmt"""
        input = """
            foo : function void (){
                a : float;
                if (1) a : float;
            }
        """
        expect = "Error on line 4 col 25: :"
        self.assertTrue(TestParser.test(input, expect, inspect.stack()[0].function))     

                                            
    def test_082(self):
        """test stmt"""
        input = """
            foo : function void (){
                a : float;
                if (1) return;
                else a : float;
            }
        """
        expect = "Error on line 5 col 23: :"
        self.assertTrue(TestParser.test(input, expect, inspect.stack()[0].function))     

    def test_083(self):
        """test stmt"""
        input = """
            foo : function void (){
                for (i[2+3 :: 4, fc(1,2)]=1,1,1)  a, b : float = 1,2;
            }
        """
        expect = "Error on line 3 col 51: ,"
        self.assertTrue(TestParser.test(input, expect, inspect.stack()[0].function))     

    def test_084(self):
        """test stmt"""
        input = """
            foo : function void (){
                while(1)  a, b : float;
            }
        """
        expect = "Error on line 3 col 27: ,"
        self.assertTrue(TestParser.test(input, expect, inspect.stack()[0].function))     

    def test_085(self):
        """test stmt"""
        input = """
        foo : function void (){
            a : string;
            return ;
            a, b : boolean = 1, 2;
            return ;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, inspect.stack()[0].function))     
                                                                                                                                                                                                                                                                                                                                                                                                                                                        