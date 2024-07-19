import unittest
from TestUtils import TestParser


class ParserSuite(unittest.TestCase):
    def test_001(self):
        """test Variable Declaration"""
        input = """
            a : integer;
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, "001"))

    def test_002(self):
        """test Multiple Variable Declarations"""
        input = """
            a, b, c : float;
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, "002"))

    def test_003(self):
        """test Variable Initialization"""
        input = """
            a : integer = 5;
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, "003"))

    def test_004(self):
        """test Multiple Variable Initialization"""
        input = """
            x, y, z : boolean = true, false, true;
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, "004"))

    def test_005(self):
        """test String Variable"""
        input = """
            name : string = "Test";
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, "005"))

    def test_006(self):
        """test Array Declaration"""
        input = """
            arr : array [1,2] of integer;
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, "006"))

    def test_007(self):
        """test Array Initialization"""
        input = """
            arr : array [1,2] of integer = {{1, 2}, {3, 4}};
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, "007"))

    def test_008(self):
        """test Function Declaration"""
        input = """
            foo : function void () {}
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, "008"))

    def test_009(self):
        """test Function with Parameters"""
        input = """
            foo : function integer (a: integer, b: float) {
                return a + b;
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, "009"))

    def test_010(self):
        """test If Statement"""
        input = """
            foo : function void () {
                if (a > b) {
                    c := a;
                }
            }
        """
        expect = "Error on line 4 col 23: ="
        self.assertTrue(TestParser.test(input, expect, "010"))

    def test_011(self):
        """test If-Else Statement"""
        input = """
            foo : function void () {
                if (a > b) {
                    c /= a;
                } else {
                    c = b;
                }
            }
        """
        expect = "Error on line 4 col 22: /"
        self.assertTrue(TestParser.test(input, expect, "011"))

    def test_012(self):
        """test While Loop"""
        input = """
            foo : function void () {
                while (a < 10) {
                    a = a + 1;
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, "012"))

    def test_013(self):
        """test Do-While Loop"""
        input = """
            foo : function void () {
                do {
                    a = a + 1;
                } while (a < 10);
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, "013"))

    def test_014(self):
        """test For Loop"""
        input = """
            foo : function void () {
                for (i = 0, i < 10, i + 1) {
                    a = a + i
                }
            }
        """
        expect = "Error on line 5 col 16: }"
        self.assertTrue(TestParser.test(input, expect, "014"))

    def test_015(self):
        """test Nested If"""
        input = """
            foo : function void () {
                if (a > b) {
                    if (c < d) {
                        e = c;
                    }
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, "015"))

    def test_016(self):
        """test Nested Loops"""
        input = """
            foo : function void () {
                for (i = 0, i < 10, i + 1) {
                    while (j < 5) {
                        j = j + 1;
                    }
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, "016"))

    def test_017(self):
        """test Function Call"""
        input = """
            foo : function void () {
                bar();
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, "017"))

    def test_018(self):
        """test Function Call with Arguments"""
        input = """
            foo : function void () {
                bar(1, 2, 3);
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, "018"))

    def test_019(self):
        """test Return Statement"""
        input = """
            foo : function integer () {
                return 5;
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, "019"))

    def test_020(self):
        """test Break Statement"""
        input = """
            foo : function void () {
                for (i = 0, i < 10, i + 1) {
                    if (i == 5) {
                        break;
                    }
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, "020"))

    def test_021(self):
        """test Continue Statement"""
        input = """
            foo : function void () {
                for (i = 0, i < 10, i + 1) {
                    if (i == 5) {
                        continue;
                    }
                    a = a + i;
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, "021"))

    def test_022(self):
        """test Logical Operators"""
        input = """
            a : boolean = true && false || true;
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, "022"))

    def test_023(self):
        """test Arithmetic Operators"""
        input = """
            a : integer = 1 + 2 * 3 - 4 / 5 % 6;
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, "023"))

    def test_024(self):
        """test String Concatenation"""
        input = """
            a : string = "Hello, " :: "world!";
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, "024"))

    def test_025(self):
        """test Array Element Access"""
        input = """
            a : integer = arr[0, 1];
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, "025"))

    def test_026(self):
        """test Array Assignment"""
        input = """
            array [0, 1] of integer;
        """
        expect = "Error on line 2 col 12: array"
        self.assertTrue(TestParser.test(input, expect, "026"))

    def test_027(self):
        """test Compound Expression"""
        input = """
            a : integer = (1 + 2) * (3 - 4) / 5;
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, "027"))

    def test_028(self):
        """test Function Return Expression"""
        input = """
            foo : function integer () {
                return 1 + 2 * 3;
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, "028"))

    def test_029(self):
        """test Function with Array Parameter"""
        input = """
            foo : function void (arr: array [5] of integer) {}
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, "029"))

    def test_030(self):
        """test Function Returning Array"""
        input = """
            foo : function array [5] of integer () {
                return {1, 2, 3, 4, 5};
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, "030"))

    def test_031(self):
        """test Nested Function Calls"""
        input = """
            foo : function integer () {
                return bar(baz(1, 2), qux(3, 4));
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, "031"))

    def test_032(self):
        """test Function with No Return"""
        input = """
            foo : function void () {}
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, "032"))

    def test_033(self):
        """test Boolean Expression"""
        input = """
            a : boolean = (1 < 2) && (3 >= 4) || (5 != 6);
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, "033"))

    def test_034(self):
        """test Unary Operators"""
        input = """
            a : integer = -5;
            b : boolean = !true;
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, "034"))

    def test_035(self):
        """test Array Initialization"""
        input = """
            arr : array [3] of float = {1.1, 2.2, 3.3};
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, "035"))

    def test_036(self):
        """test Array Index Expression"""
        input = """
            arr[1 + 2, 3 * 4] = 5;
        """
        expect = "Error on line 2 col 15: ["
        self.assertTrue(TestParser.test(input, expect, "036"))

    def test_037(self):
        """test Nested Array Access"""
        input = """
            a : integer = 1,2,3;
        """
        expect = "Error on line 2 col 27: ,"
        self.assertTrue(TestParser.test(input, expect, "037"))

    def test_038(self):
        """test Function with Nested Scope"""
        input = """
            foo : function void () {
                {
                    a : integer;
                    a = 10;
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, "038"))

    def test_039(self):
        """test If-ElseIf Statement"""
        input = """
            foo : function void () {
                if (a > b) {
                    c = a;
                } else if (a < b) {
                    c = b;
                } else {
                    c = 0;
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, "039"))

    def test_040(self):
        """test Function with Multiple Returns"""
        input = """
            foo : function integer (a: integer) {
                if (a > 0) {
                    return 1;
                } else {
                    return -1;
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, "040"))

    def test_041(self):
        """test Global Variable"""
        input = """
            global a : integer = 10;
        """
        expect = "Error on line 2 col 19: a"
        self.assertTrue(TestParser.test(input, expect, "041"))

    def test_042(self):
        """test Local Variable"""
        input = """
            foo : function void () {
                local a : integer = 10;
            }
        """
        expect = "Error on line 3 col 22: a"
        self.assertTrue(TestParser.test(input, expect, "042"))

    def test_043(self):
        """test Function Overloading"""
        input = """
            foo : function integer (a: integer) {
                return a;
            }
            foo : function float (a: float) {
                return a;
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, "043"))

    def test_044(self):
        """test Mixed Type Array"""
        input = """
            arr : array [3] of auto = {1, "two", 3.0};
        """
        expect = "Error on line 2 col 31: auto"
        self.assertTrue(TestParser.test(input, expect, "044"))

    def test_045(self):
        """test Boolean Array"""
        input = """
            arr : array [2] of boolean = {true, false};
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, "045"))

    def test_046(self):
        """test String Array"""
        input = """
            arr : array [2] of string = {"hello", "world"};
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, "046"))

    def test_047(self):
        """test Nested Function Declarations"""
        input = """
            foo : function void () {
                bar : function void () {}
                bar();
            }
        """
        expect = "Error on line 3 col 22: function"
        self.assertTrue(TestParser.test(input, expect, "047"))

    def test_048(self):
        """test Function Returning Boolean"""
        input = """
            isEven : function boolean (a: integer) {
                return a % 2 == 0;
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, "048"))

    def test_049(self):
        """test Complex Expression"""
        input = """
            a : integer = (1 + 2) * (3 - 4) / (5 + 6);
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, "049"))

    def test_050(self):
        """test Nested If-Else Statements"""
        input = """
            foo : function void () {
                if (a > b) {
                    if (c < d) {
                        e = c;
                    } else {
                        e = d;
                    }
                } else {
                    e = b;
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, "050"))
    def test_051(self):
            """test Long Function Declaration"""
            input = """
                foo : function auto (a: integer, b: float, c: boolean, d: string) {
                    return a + b;
                }
            """
            expect = "successful"
            self.assertTrue(TestParser.test(input, expect, "051"))

    def test_052(self):
        """test Function Returning String"""
        input = """
            greet : function string () {
                return "Hello, world!";
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, "052"))

    def test_053(self):
        """test Boolean Assignment"""
        input = """
            a : boolean = true;
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, "053"))

    def test_054(self):
        """test Integer Assignment"""
        input = """
            a : integer = 123;
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, "054"))

    def test_055(self):
        """test Float Assignment"""
        input = """
            a : float = 1.23;
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, "055"))

    def test_056(self):
        """test String Assignment"""
        input = """
            a : string = "Test";
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, "056"))

    def test_057(self):
        """test Variable with Underscore"""
        input = """
            _var : integer = 5;
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, "057"))

    def test_058(self):
        """test Variable with Digits"""
        input = """
            var123 : integer = 123;
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, "058"))

    def test_059(self):
        """test Variable Reassignment"""
        input = """
            a : integer = 5;
            a = 10;
        """
        expect = "Error on line 3 col 14: ="
        self.assertTrue(TestParser.test(input, expect, "059"))

    def test_060(self):
        """test Logical Negation"""
        input = """
            a : boolean = !true;
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, "060"))

    def test_061(self):
        """test Addition Assignment"""
        input = """
            a : integer = 5
            a = a + 10;
        """
        expect = "Error on line 3 col 12: a"
        self.assertTrue(TestParser.test(input, expect, "061"))

    def test_062(self):
        """test Subtraction Assignment"""
        input = """
            a : integer = 5,6;
            a = a - 3;
        """
        expect = "Error on line 2 col 27: ,"
        self.assertTrue(TestParser.test(input, expect, "062"))

    def test_063(self):
        """test Multiplication Assignment"""
        input = """
            a : int = 5;
            a = a * 2;
        """
        expect = "Error on line 2 col 16: int"
        self.assertTrue(TestParser.test(input, expect, "063"))

    def test_064(self):
        """test Division Assignment"""
        input = """
            a : integer = 10;;
            a = a / 2;
        """
        expect = "Error on line 2 col 29: ;"
        self.assertTrue(TestParser.test(input, expect, "064"))

    def test_065(self):
        """test Modulus Assignment"""
        input = """
            for (){}
            a : integer = 10;
            a = a % 3;
        """
        expect = "Error on line 2 col 12: for"
        self.assertTrue(TestParser.test(input, expect, "065"))

    def test_066(self):
        """test Parenthesized Expression"""
        input = """
            a : integer = (1 + 2) * (3 + 4);
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, "066"))

    def test_067(self):
        """test Compound Assignment"""
        input = """
            a, b, c : integer = 1, 2, 3;
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, "067"))

    def test_068(self):
        """test Complex Function Call"""
        input = """
            foo : function integer (a: integer, b: integer) {
                return a + b;
            }
            bar : function void () {
                x = foo(1, foo(2, 3));
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, "068"))

    def test_069(self):
        """test Function with Default Parameter"""
        input = """
            foo : function integer (a: integer = 5) {
                return a;
            }
        """
        expect = "Error on line 2 col 47: ="
        self.assertTrue(TestParser.test(input, expect, "069"))

    def test_070(self):
        """test Function with Variable Length Argument"""
        input = """
            foo : function void (a: integer, ... b: integer) {}
        """
        expect = "Error on line 2 col 45: ."
        self.assertTrue(TestParser.test(input, expect, "070"))

    def test_071(self):
        """test Function with Nested Return"""
        input = """
            foo : function integer () {
                if (true) {
                    return 1;
                } else {
                    return 0;
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, "071"))

    def test_072(self):
        """test Function with Multiple Statements"""
        input = """
            foo : function integer () {
                a = 1;
                b = 2;
                return a + b;
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, "072"))

    def test_073(self):
        """test Function with Global Variable"""
        input = """
            a : integer = 5;
            foo : function integer () {
                return a;
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, "073"))

    def test_074(self):
        """test Function with Local Variable"""
        input = """
            foo : function integer () {
                a : integer = 5;
                return a;
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, "074"))

    def test_075(self):
        """test Complex If-Else Statement"""
        input = """
            foo : function void () {
                if (a > b) {
                    if (c < d) {
                        e = c;
                    } else {
                        e = d;
                    }
                } else if (a < b) {
                    f = b;
                } else {
                    g = 0;
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, "075"))

    def test_076(self):
        """test Nested While Loop"""
        input = """
            foo : function void () {
                while (a < 10) {
                    while (b < 5) {
                        b = b + 1;
                    }
                    a = a + 1;
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, "076"))

    def test_077(self):
        """test Nested Do-While Loop"""
        input = """
            foo : function void () {
                do {
                    do {
                        b = b + 1;
                    } while (b < 5);
                    a = a + 1;
                } while (a < 10);
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, "077"))

    def test_078(self):
        """test Nested For Loop"""
        input = """
            foo : function void () {
                for (i = 0, i < 10, i + 1) {
                    for (j = 0, j < 5, j + 1) {
                        a = a + i + j;
                    }
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, "078"))

    def test_079(self):
        """test Function with While Loop"""
        input = """
            foo : function void () {
                while (true) {
                    break;
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, "079"))

    def test_080(self):
        """test Function with Do-While Loop"""
        input = """
            foo : function void () {
                do {
                    continue;
                } while (false);
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, "080"))

    def test_081(self):
        """test Function with For Loop"""
        input = """
            foo : function void () {
                for (i = 0, i < 10, i + 1) {
                    a = a + i;
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, "081"))

    def test_082(self):
        """test Function with Nested Function"""
        input = """
            foo : function void () {
                bar : function void () {}
                bar();
            }
        """
        expect = "Error on line 3 col 22: function"
        self.assertTrue(TestParser.test(input, expect, "082"))

    def test_083(self):
        """test Function Returning Array"""
        input = """
            foo : function array [3] of integer () {
                return {1, 2, 3};
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, "083"))

    def test_084(self):
        """test Function Returning Boolean"""
        input = """
            foo : function boolean () {
                return true;
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, "084"))

    def test_085(self):
        """test Function with Default Arguments"""
        input = """
            foo : function void (a: integer = 5, b: integer = 10) {}
        """
        expect = "Error on line 2 col 44: ="
        self.assertTrue(TestParser.test(input, expect, "085"))

    def test_086(self):
        """test Function with Variable Length Arguments"""
        input = """
            foo : function void (... args: integer) {}
        """
        expect = "Error on line 2 col 33: ."
        self.assertTrue(TestParser.test(input, expect, "086"))

    def test_087(self):
        """test Function with Mixed Type Arguments"""
        input = """
            foo : function void (a: integer, b: float, c: string) {}
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, "087"))

    def test_088(self):
        """test Function Returning Complex Type"""
        input = """
            foo : function array [2] of string () {
                return {"hello", "world"};
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, "088"))

    def test_089(self):
        """test Function with Complex Logic"""
        input = """
            foo : function integer (a: integer, b: integer) {
                if (a > b) {
                    return a;
                } else {
                    return b;
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, "089"))

    def test_090(self):
        """test Function Calling Another Function"""
        input = """
            foo : function integer (a: integer) {
                return bar(a);
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, "090"))

    def test_091(self):
        """test Function with Array Parameters"""
        input = """
            foo : function void (arr: array [3] of integer) {}
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, "091"))

    def test_092(self):
        """test Function with Default Array Parameters"""
        input = """
            foo : function void (arr: array [3] of integer = {1, 2, 3}) {}
        """
        expect = "Error on line 2 col 59: ="
        self.assertTrue(TestParser.test(input, expect, "092"))

    def test_093(self):
        """test Function with Complex Return Type"""
        input = """
            foo : function array [2] of string () {
                return {"hello", "world"};
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, "093"))

    def test_094(self):
        """test Function with Complex Parameter Types"""
        input = """
            foo : function void (a: integer, b: array [2] of string) {}
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, "094"))

    def test_095(self):
        """test Function with Multiple Statements"""
        input = """
            foo : function void () {
                a = 1;
                b = 2;
                c = a + b;
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, "095"))

    def test_096(self):
        """test Function with Conditional Statements"""
        input = """
            foo : function void () {
                if (a > b) {
                    a = a + 1;
                } else {
                    a = a - 1;
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, "096"))

    def test_097(self):
        """test Function with Loop Statements"""
        input = """
            foo : function void () {
                for (i = 0, i < 10, i + 1) {
                    a = a + i;
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, "097"))

    def test_098(self):
        """test Function with Nested If Statements"""
        input = """
            foo : function void () {
                if (a > b) {
                    if (c > d) {
                        a = a + 1;
                    } else {
                        a = a - 1;
                    }
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, "098"))

    def test_099(self):
        """test Function with Nested Loop Statements"""
        input = """
            foo : function void () {
                for (i = 0, i < 10, i + 1) {
                    for (j = 0, j < 5, j + 1) {
                        a = a + i + j;
                    }
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, "099"))

    def test_100(self):
        """test Function with Mixed Statements"""
        input = """
            foo : function void () {
                if (a > b) {
                    for (i = 0, i < 10, i + 1) {
                        a = a + i;
                    }
                } else {
                    for (j = 0, j < 5, j + 1) {
                        a = a - j;
                    }
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, "100"))
