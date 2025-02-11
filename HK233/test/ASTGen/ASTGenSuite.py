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
from TestUtils import TestAST
from AST import *


class ASTGenSuite(unittest.TestCase):
    def test_001(self):
        """test Variable and type"""
        input = """
            a : integer;  
        """
        expect = Program([
                VarDecl("a", IntegerType())
            ])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_002(self):
        """test Variable and type"""
        input = """
            a, b : float;  
        """
        expect = Program([
                VarDecl("a", FloatType()),
                VarDecl("b", FloatType())
            ])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_003(self):
        """test Variable and type"""
        input = """
            a, b : string;
            c : auto;  
        """
        expect = Program([
                VarDecl("a", StringType()),
                VarDecl("b", StringType()),
                VarDecl("c", AutoType())
            ])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_004(self):
        """test Variable and type"""
        input = """
            a : auto;
            c, d : auto;  
            e : boolean;
        """
        expect = Program([
                VarDecl("a", AutoType()),
                VarDecl("c", AutoType()),
                VarDecl("d", AutoType()),
                VarDecl("e", BooleanType())
            ])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_005(self):
        """test Variable and type"""
        input = """
            a, b, c : array [2,2] of integer;
        """
        expect = Program([
                VarDecl("a", ArrayType([2, 2], IntegerType())),
                VarDecl("b", ArrayType([2, 2], IntegerType())),
                VarDecl("c", ArrayType([2, 2], IntegerType()))
            ])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_006(self):
        """test Variable and type"""
        input = """
            a : array [2,2,3] of float;
            a : array [2] of string;
            a : array [2] of boolean;
        """
        expect = Program([
                VarDecl("a", ArrayType([2, 2, 3], FloatType())),
                VarDecl("a", ArrayType([2], StringType())),
                VarDecl("a", ArrayType([2], BooleanType()))
            ])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_007(self):
        """test Variable and type"""
        input = """
            a : integer = 1;
        """
        expect = Program([
                VarDecl("a", IntegerType(), IntegerLit(1))
            ])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_008(self):
        """test Variable and type"""
        input = """
            a, b : string = 1, 2;
        """
        expect = Program([
                VarDecl("a", StringType(), IntegerLit(1)),
                VarDecl("b", StringType(), IntegerLit(2))
            ])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_009(self):
        """test Variable and type"""
        input = """
            a, b : boolean = 1, 2;
            c : float = 3;
            d, e, g : auto = 1, 2, 3;
        """
        expect = Program([
                VarDecl("a", BooleanType(), IntegerLit(1)),
                VarDecl("b", BooleanType(), IntegerLit(2)),
                VarDecl("c", FloatType(), IntegerLit(3)),
                VarDecl("d", AutoType(), IntegerLit(1)),
                VarDecl("e", AutoType(), IntegerLit(2)),
                VarDecl("g", AutoType(), IntegerLit(3))
            ])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_010(self):
        """test function"""
        input = """
            foo : function void () inherit foo1 {}
            foo : function auto (inherit out id : float, out id : auto, inherit id : integer) inherit foo1 {}
            foo : function array [1] of integer (inherit out id : array [1] of integer) {}
        """
        expect = Program([
            FuncDecl("foo", VoidType(), [], "foo1", BlockStmt([])),
            FuncDecl("foo", AutoType(), [ParamDecl("id", FloatType(), out=True, inherit=True), 
                                         ParamDecl("id", AutoType(), out=True, inherit=False), 
                                         ParamDecl("id", IntegerType(), out=False, inherit=True)],
                     "foo1", BlockStmt([])),
            FuncDecl("foo", ArrayType([1], IntegerType()), [ParamDecl("id", ArrayType([1], IntegerType()), out=True, inherit=True)], "None", BlockStmt([]))
        ])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))
        
    def test_011(self):
        """test expression"""
        input = """
            id : integer = 1 :: 2;
        """
        expect = Program([
            VarDecl("id", IntegerType(), BinExpr("::", IntegerLit(1), IntegerLit(2)))
        ])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_011(self):
        """test expression"""
        input = """
            id : integer = 1 > 2;
            id : integer = 1 >= 2;
            id : integer = 1 < true;
            id : integer = 1 <= "2a";
            id : integer = 1 == 2.0;
            id : integer = 1.0 != 2;
        """
        expect = Program([
                VarDecl("id", IntegerType(), BinExpr(">", IntegerLit(1), IntegerLit(2))),
                VarDecl("id", IntegerType(), BinExpr(">=", IntegerLit(1), IntegerLit(2))),
                VarDecl("id", IntegerType(), BinExpr("<", IntegerLit(1), BooleanLit(True))),
                VarDecl("id", IntegerType(), BinExpr("<=", IntegerLit(1), StringLit("2a"))),
                VarDecl("id", IntegerType(), BinExpr("==", IntegerLit(1), FloatLit(2.0))),
                VarDecl("id", IntegerType(), BinExpr("!=", FloatLit(1.0), IntegerLit(2)))
            ])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))
        
    def test_012(self):
        """test expression"""
        input = """
            id : integer = 1 > 2 :: "2" == 2.0003;
        """
        expect = Program([
                VarDecl("id", IntegerType(), BinExpr("::", BinExpr(">", IntegerLit(1), IntegerLit(2)), BinExpr("==", StringLit("2"), FloatLit(2.0003))))
            ])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))
        
    def test_013(self):
        """test expression"""
        input = """
            id : integer = 1 && 2 || id;
        """
        expect = Program([
                VarDecl("id", IntegerType(), BinExpr("||", BinExpr("&&", IntegerLit(1), IntegerLit(2)), Id("id")))
            ])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_014(self):
        """test expression"""
        input = """
            id : integer = 1 + 2 - 3;
        """
        expect = Program([
            VarDecl("id", IntegerType(), BinExpr("-", BinExpr("+", IntegerLit(1), IntegerLit(2)), IntegerLit(3)))
        ])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_015(self):
        """test expression"""
        input = """
            id : integer = 1 * 2 / 3 % 2.0;
        """
        expect = Program([
                VarDecl("id", IntegerType(), BinExpr("%", BinExpr("/", BinExpr("*", IntegerLit(1), IntegerLit(2)), IntegerLit(3)), FloatLit(2.0)))
            ])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))


    def test_016(self):
        """test expression"""
        input = """
            id : integer = !1 + !!!1;
        """
        expect = Program([
                VarDecl("id", IntegerType(), BinExpr("+", UnExpr("!", IntegerLit(1)), UnExpr("!", UnExpr("!", UnExpr("!", IntegerLit(1))))))
            ])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_017(self):
        """test expression"""
        input = """
            id : integer = -1 + ---1;
        """
        expect = Program([
                VarDecl("id", IntegerType(), BinExpr("+", UnExpr("-", IntegerLit(1)), UnExpr("-", UnExpr("-", UnExpr("-", IntegerLit(1))))))
            ])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_018(self):
        """test expression"""
        input = """
            id : integer = a[1+2] + a[2, 3];
            id : integer = a[1+2, a[2, 3]];
        """
        expect = Program([
                VarDecl("id", IntegerType(), BinExpr("+", ArrayCell("a", [BinExpr("+", IntegerLit(1), IntegerLit(2))]), ArrayCell("a", [IntegerLit(2), IntegerLit(3)]))),
                VarDecl("id", IntegerType(), ArrayCell("a", [BinExpr("+", IntegerLit(1), IntegerLit(2)), ArrayCell("a", [IntegerLit(2), IntegerLit(3)])]))
            ])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_019(self):
        """test expression"""
        input = """
            id : float = (a > b + id(1+2, 3)) * id();
        """
        expect = Program([
                VarDecl("id", FloatType(), BinExpr("*", BinExpr(">", Id("a"), BinExpr("+", Id("b"), FuncCall("id", [BinExpr("+", IntegerLit(1), IntegerLit(2)), IntegerLit(3)]))), FuncCall("id", [])))
            ])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_020(self):
        """test expression"""
        input = """
            id : float = {1+2, foo(), {1,2}};
        """
        expect = Program([
                VarDecl("id", FloatType(), ArrayLit([BinExpr("+", IntegerLit(1), IntegerLit(2)), FuncCall("foo", []), ArrayLit([IntegerLit(1), IntegerLit(2)])]))
            ])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_021(self):
        """test expression"""
        input = """
            id : float = 1 * 2 + 3 > 4 / 5 :: 6 < !! --4;
        """
        expect = Program([
                VarDecl("id", FloatType(), BinExpr("::", BinExpr(">", BinExpr("+", BinExpr("*", IntegerLit(1), IntegerLit(2)), IntegerLit(3)), BinExpr("/", IntegerLit(4), IntegerLit(5))), BinExpr("<", IntegerLit(6), UnExpr("!", UnExpr("!", UnExpr("-", UnExpr("-", IntegerLit(4))))))))
            ])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_022(self):
        """test Statement"""
        input = """
            a, b : integer = 1, 2;
            foo : function void () {
                
            }
        """
        expect = Program([
                VarDecl("a", IntegerType(), IntegerLit(1)),
                VarDecl("b", IntegerType(), IntegerLit(2)),
                FuncDecl("foo", VoidType(), [], "None", BlockStmt([]))
            ])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))
        
    def test_023(self):
        """test Statement"""
        input = """
            foo : function void () {
                a, b : integer = 1, 2;
                c, d : float;
            }
        """
        expect = Program([
                FuncDecl("foo", VoidType(), [], "None", BlockStmt([VarDecl("a", IntegerType(), IntegerLit(1)), VarDecl("b", IntegerType(), IntegerLit(2)), VarDecl("c", FloatType()), VarDecl("d", FloatType())]))
            ])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_024(self):
        """test Statement"""
        input = """
            foo : function void () {
                a = 1;
                a[1.0] = 1;
                a[1,2] = "!";
            }
        """
        expect = Program([
                FuncDecl("foo", VoidType(), [], "None", BlockStmt([AssignStmt(Id("a"), IntegerLit(1)), AssignStmt(ArrayCell("a", [FloatLit(1.0)]), IntegerLit(1)), AssignStmt(ArrayCell("a", [IntegerLit(1), IntegerLit(2)]), StringLit("!"))]))
            ])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_025(self):
        """test Statement"""
        input = """
            foo : function void () {
                if (true) break;
                else {}
                
                if (true)
                    if(true) return;
                    else return;
                
            }
        """
        expect = Program([
            FuncDecl("foo", VoidType(), [], "None", BlockStmt([
                IfStmt(BooleanLit(True), BreakStmt(), BlockStmt([])), 
                IfStmt(BooleanLit(True), 
                       IfStmt(BooleanLit(True), ReturnStmt(), ReturnStmt())
                       )]))
        ])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))
        
    def test_026(self):
        """test Statement"""
        input = """
            foo : function void () {  
                if (true)
                    if(true) return;
                    else continue;
                else break;
            }
        """
        expect = Program([
                    FuncDecl("foo", VoidType(), [], "None", BlockStmt([
                        IfStmt(BooleanLit(True), 
                               IfStmt(BooleanLit(True), ReturnStmt(), ContinueStmt()), 
                               BreakStmt())]))
                ])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))
        
    def test_027(self):
        """test Statement"""
        input = """
            foo : function void () {  
                if (true) return;
            }
        """
        expect = Program([
                FuncDecl("foo", VoidType(), [], "None", BlockStmt([IfStmt(BooleanLit(True), ReturnStmt())]))
            ])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))

    def test_028(self):
        """test Statement"""
        input = """
            foo : function void () {  
                return;
                return 1 + 2;
            }
        """
        expect = Program([
                    FuncDecl("foo", VoidType(), [], "None", BlockStmt([ReturnStmt(), ReturnStmt(BinExpr("+", IntegerLit(1), IntegerLit(2)))]))
                ])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))
        
    def test_029(self):
        """test Statement"""
        input = """
            foo : function void () {  
                foo();
                foo(1+2, 3);
            }
        """
        expect = Program([
                FuncDecl("foo", VoidType(), [], "None", BlockStmt([CallStmt("foo",[]), CallStmt("foo",[BinExpr("+", IntegerLit(1), IntegerLit(2)), IntegerLit(3)])]))
            ])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
        
    def test_030(self):
        """test Statement"""
        input = """
            foo : function void () {  
                {
                    break;
                    continue;
                    {{{}}}
                }
            }
        """
        expect = Program([
                FuncDecl("foo", VoidType(), [], "None", BlockStmt([BlockStmt([BreakStmt(), ContinueStmt(), BlockStmt([BlockStmt([BlockStmt([])])])])]))
            ])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
        
    def test_031(self):
        """test Statement"""
        input = """
            foo : function void () {  
                {
                    a,b : float;
                    c, d : float = 1, 2;
                    e : string = "@";
                }
            }
        """
        expect = Program([
                    FuncDecl("foo", VoidType(), [], "None", BlockStmt([BlockStmt([VarDecl("a", FloatType()), VarDecl("b", FloatType()), VarDecl("c", FloatType(), IntegerLit(1)), VarDecl("d", FloatType(), IntegerLit(2)), VarDecl("e", StringType(), StringLit("@"))])]))
                ])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
        
    def test_032(self):
        """test Statement"""
        input = """
            foo : function void () {  
                for (i = 1, i < 10, i + 1) {
                    writeInt(i);
                }
            }

        """
        expect = Program([
                FuncDecl("foo", VoidType(), [], "None", BlockStmt([ForStmt(AssignStmt(Id("i"), IntegerLit(1)), BinExpr("<", Id("i"), IntegerLit(10)), BinExpr("+", Id("i"), IntegerLit(1)), BlockStmt([CallStmt("writeInt",[Id("i")])]))]))
            ])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))         

    def test_033(self):
        """test Statement"""
        input = """
            foo : function void () {  
                for (i = 1, i < 10, i + 1) break;
            }

        """
        expect = Program([
                FuncDecl("foo", VoidType(), [], "None", BlockStmt([ForStmt(AssignStmt(Id("i"), IntegerLit(1)), BinExpr("<", Id("i"), IntegerLit(10)), BinExpr("+", Id("i"), IntegerLit(1)), BreakStmt())]))
            ])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
        

    def test_034(self):
        """test Statement"""
        input = """
            foo : function void () {  
                while (true) break;
                while (false) {}
            }
        """
        expect = Program([
                FuncDecl("foo", VoidType(), [], "None", BlockStmt([WhileStmt(BooleanLit(True), BreakStmt()), WhileStmt(BooleanLit(False), BlockStmt([]))]))
            ])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
        
    def test_035(self):
        """test Statement"""
        input = """
            foo : function void () {  
                do
                {
                    break;
                }
                while(1.0);
            }
        """
        expect = Program([
                FuncDecl("foo", VoidType(), [], "None", BlockStmt([DoWhileStmt(FloatLit(1.0), BlockStmt([BreakStmt()]))]))
            ])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function))        
        

    def test_036(self):
        """test Statement"""
        input = """
            foo : function void () {  
                for (i[1+1] = 1, i < 10, i + 1) return;
            }
        """
        expect = Program([
            FuncDecl("foo", VoidType(), [], "None", BlockStmt([ForStmt(AssignStmt(ArrayCell("i", [BinExpr("+", IntegerLit(1), IntegerLit(1))]), IntegerLit(1)), BinExpr("<", Id("i"), IntegerLit(10)), BinExpr("+", Id("i"), IntegerLit(1)), ReturnStmt())]))
        ])
        self.assertTrue(TestAST.test(input, str(expect), inspect.stack()[0].function)) 
        
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              