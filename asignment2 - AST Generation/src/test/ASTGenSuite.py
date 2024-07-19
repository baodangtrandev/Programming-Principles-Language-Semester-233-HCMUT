import unittest
from TestUtils import TestAST
from AST import *


class ASTGenSuite(unittest.TestCase):
    def test_001(self):
        """test Variable and type"""
        input = """
            a : integer;  
        """
        expect = """Program([
	VarDecl(a, IntegerType)
])"""
        self.assertTrue(TestAST.test(input, str(expect), 1))

    def test_002(self):
        """test Variable and type"""
        input = """
            a, b : float;  
        """
        expect = """Program([
	VarDecl(a, FloatType)
	VarDecl(b, FloatType)
])"""
        self.assertTrue(TestAST.test(input, str(expect), 2 ))

    def test_003(self):
        """test Variable and type"""
        input = """
            a, b : string;
            c : auto;  
        """
        expect = """Program([
	VarDecl(a, StringType)
	VarDecl(b, StringType)
	VarDecl(c, AutoType)
])"""
        self.assertTrue(TestAST.test(input, str(expect), 3))

    def test_004(self):
        """test Variable and type"""
        input = """
            a : auto;
            c, d : auto;  
            e : boolean;
        """
        expect = """Program([
	VarDecl(a, AutoType)
	VarDecl(c, AutoType)
	VarDecl(d, AutoType)
	VarDecl(e, BooleanType)
])"""
        self.assertTrue(TestAST.test(input, str(expect), 4))

    def test_005(self):
        """test Variable and type"""
        input = """
            a, b, c : array [2,2] of integer;
        """
        expect = """Program([
	VarDecl(a, ArrayType([2, 2], IntegerType))
	VarDecl(b, ArrayType([2, 2], IntegerType))
	VarDecl(c, ArrayType([2, 2], IntegerType))
])"""
        self.assertTrue(TestAST.test(input, str(expect), 5))

    def test_006(self):
        """test Variable and type"""
        input = """
            a : array [2,2,3] of float;
            a : array [2] of string;
            a : array [2] of boolean;
        """
        expect = """Program([
	VarDecl(a, ArrayType([2, 2, 3], FloatType))
	VarDecl(a, ArrayType([2], StringType))
	VarDecl(a, ArrayType([2], BooleanType))
])"""
        self.assertTrue(TestAST.test(input, str(expect), 6))

    def test_007(self):
        """test Variable and type"""
        input = """
            a : integer = 1;
        """
        expect = """Program([
	VarDecl(a, IntegerType, IntegerLit(1))
])"""
        self.assertTrue(TestAST.test(input, str(expect), 7))

    def test_008(self):
        """test Variable and type"""
        input = """
            a, b : string = 1, 2;
        """
        expect = """Program([
	VarDecl(a, StringType, IntegerLit(1))
	VarDecl(b, StringType, IntegerLit(2))
])"""
        self.assertTrue(TestAST.test(input, str(expect), 8))

    def test_009(self):
        """test Variable and type"""
        input = """
            a, b : boolean = 1, 2;
            c : float = 3;
            d, e, g : auto = 1, 2, 3;
        """
        expect = """Program([
	VarDecl(a, BooleanType, IntegerLit(1))
	VarDecl(b, BooleanType, IntegerLit(2))
	VarDecl(c, FloatType, IntegerLit(3))
	VarDecl(d, AutoType, IntegerLit(1))
	VarDecl(e, AutoType, IntegerLit(2))
	VarDecl(g, AutoType, IntegerLit(3))
])"""
        self.assertTrue(TestAST.test(input, str(expect),9 ))

    def test_010(self):
        """test function"""
        input = """
            foo : function void () inherit foo1 {}
            foo : function auto (inherit out id : float, out id : auto, inherit id : integer) inherit foo1 {}
            foo : function array [1] of integer (inherit out id : array [1] of integer) {}
        """
        expect = """Program([
	FuncDecl(foo, VoidType, [], foo1, BlockStmt([]))
	FuncDecl(foo, AutoType, [InheritOutParam(id, FloatType), OutParam(id, AutoType), InheritParam(id, IntegerType)], foo1, BlockStmt([]))
	FuncDecl(foo, ArrayType([1], IntegerType), [InheritOutParam(id, ArrayType([1], IntegerType))], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, str(expect), 10))

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
        expect = """Program([
	VarDecl(id, IntegerType, BinExpr(>, IntegerLit(1), IntegerLit(2)))
	VarDecl(id, IntegerType, BinExpr(>=, IntegerLit(1), IntegerLit(2)))
	VarDecl(id, IntegerType, BinExpr(<, IntegerLit(1), BooleanLit(True)))
	VarDecl(id, IntegerType, BinExpr(<=, IntegerLit(1), StringLit(2a)))
	VarDecl(id, IntegerType, BinExpr(==, IntegerLit(1), FloatLit(2.0)))
	VarDecl(id, IntegerType, BinExpr(!=, FloatLit(1.0), IntegerLit(2)))
])"""
        self.assertTrue(TestAST.test(input, str(expect), 11))
        
    def test_012(self):
        """test expression"""
        input = """
            id : integer = 1 > 2 :: "2" == 2.0003;
        """
        expect = """Program([
	VarDecl(id, IntegerType, BinExpr(::, BinExpr(>, IntegerLit(1), IntegerLit(2)), BinExpr(==, StringLit(2), FloatLit(2.0003))))
])"""
        self.assertTrue(TestAST.test(input, str(expect),12 ))
        
    def test_013(self):
        """test expression"""
        input = """
            id : integer = 1 && 2 || id;
        """
        expect = """Program([
	VarDecl(id, IntegerType, BinExpr(||, BinExpr(&&, IntegerLit(1), IntegerLit(2)), Id(id)))
])"""
        self.assertTrue(TestAST.test(input, str(expect),13 ))

    def test_014(self):
        """test expression"""
        input = """
            id : integer = 1 + 2 - 3;
        """
        expect = """Program([
	VarDecl(id, IntegerType, BinExpr(-, BinExpr(+, IntegerLit(1), IntegerLit(2)), IntegerLit(3)))
])"""
        self.assertTrue(TestAST.test(input, str(expect), 14))

    def test_015(self):
        """test expression"""
        input = """
            id : integer = 1 * 2 / 3 % 2.0;
        """
        expect = """Program([
	VarDecl(id, IntegerType, BinExpr(%, BinExpr(/, BinExpr(*, IntegerLit(1), IntegerLit(2)), IntegerLit(3)), FloatLit(2.0)))
])"""
        self.assertTrue(TestAST.test(input, str(expect), 15))


    def test_016(self):
        """test expression"""
        input = """
            id : integer = !1 + !!!1;
        """
        expect = """Program([
	VarDecl(id, IntegerType, BinExpr(+, UnExpr(!, IntegerLit(1)), UnExpr(!, UnExpr(!, UnExpr(!, IntegerLit(1))))))
])"""
        self.assertTrue(TestAST.test(input, str(expect), 16))

    def test_017(self):
        """test expression"""
        input = """
            id : integer = -1 + ---1;
        """
        expect = """Program([
	VarDecl(id, IntegerType, BinExpr(+, UnExpr(-, IntegerLit(1)), UnExpr(-, UnExpr(-, UnExpr(-, IntegerLit(1))))))
])"""
        self.assertTrue(TestAST.test(input, str(expect), 17))

    def test_018(self):
        """test expression"""
        input = """
            id : integer = a[1+2] + a[2, 3];
            id : integer = a[1+2, a[2, 3]];
        """
        expect = """Program([
	VarDecl(id, IntegerType, BinExpr(+, ArrayCell(a, [BinExpr(+, IntegerLit(1), IntegerLit(2))]), ArrayCell(a, [IntegerLit(2), IntegerLit(3)])))
	VarDecl(id, IntegerType, ArrayCell(a, [BinExpr(+, IntegerLit(1), IntegerLit(2)), ArrayCell(a, [IntegerLit(2), IntegerLit(3)])]))
])"""
        self.assertTrue(TestAST.test(input, str(expect), 18))

    def test_019(self):
        """test expression"""
        input = """
            id : float = (a > b + id(1+2, 3)) * id();
        """
        expect = """Program([
	VarDecl(id, FloatType, BinExpr(*, BinExpr(>, Id(a), BinExpr(+, Id(b), FuncCall(id, [BinExpr(+, IntegerLit(1), IntegerLit(2)), IntegerLit(3)]))), FuncCall(id, [])))
])"""
        self.assertTrue(TestAST.test(input, str(expect), 19))

    def test_020(self):
        """test expression"""
        input = """
            id : float = {1+2, foo(), {1,2}};
        """
        expect = """Program([
	VarDecl(id, FloatType, ArrayLit([BinExpr(+, IntegerLit(1), IntegerLit(2)), FuncCall(foo, []), ArrayLit([IntegerLit(1), IntegerLit(2)])]))
])"""
        self.assertTrue(TestAST.test(input, str(expect), 20))

    def test_021(self):
        """test expression"""
        input = """
            id : float = 1 * 2 + 3 > 4 / 5 :: 6 < !! --4;
        """
        expect = """Program([
	VarDecl(id, FloatType, BinExpr(::, BinExpr(>, BinExpr(+, BinExpr(*, IntegerLit(1), IntegerLit(2)), IntegerLit(3)), BinExpr(/, IntegerLit(4), IntegerLit(5))), BinExpr(<, IntegerLit(6), UnExpr(!, UnExpr(!, UnExpr(-, UnExpr(-, IntegerLit(4))))))))
])"""
        self.assertTrue(TestAST.test(input, str(expect), 21))

    def test_022(self):
        """test Statement"""
        input = """
            a, b : integer = 1, 2;
            foo : function void () {
                
            }
        """
        expect = """Program([
	VarDecl(a, IntegerType, IntegerLit(1))
	VarDecl(b, IntegerType, IntegerLit(2))
	FuncDecl(foo, VoidType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, str(expect), 22))
        
    def test_023(self):
        """test Statement"""
        input = """
            foo : function void () {
                a, b : integer = 1, 2;
                c, d : float;
            }
        """
        expect = """Program([
	FuncDecl(foo, VoidType, [], None, BlockStmt([VarDecl(a, IntegerType, IntegerLit(1)), VarDecl(b, IntegerType, IntegerLit(2)), VarDecl(c, FloatType), VarDecl(d, FloatType)]))
])"""
        self.assertTrue(TestAST.test(input, str(expect), 23))

    def test_024(self):
        """test Statement"""
        input = """
            foo : function void () {
                a = 1;
                a[1.0] = 1;
                a[1,2] = "!";
            }
        """
        expect = """Program([
	FuncDecl(foo, VoidType, [], None, BlockStmt([AssignStmt(Id(a), IntegerLit(1)), AssignStmt(ArrayCell(a, [FloatLit(1.0)]), IntegerLit(1)), AssignStmt(ArrayCell(a, [IntegerLit(1), IntegerLit(2)]), StringLit(!))]))
])"""
        self.assertTrue(TestAST.test(input, str(expect), 24))

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
        expect = """Program([
	FuncDecl(foo, VoidType, [], None, BlockStmt([IfStmt(BooleanLit(True), BreakStmt(), BlockStmt([])), IfStmt(BooleanLit(True), IfStmt(BooleanLit(True), ReturnStmt(), ReturnStmt()))]))
])"""
        self.assertTrue(TestAST.test(input, str(expect), 25))
        
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
        expect = """Program([
	FuncDecl(foo, VoidType, [], None, BlockStmt([IfStmt(BooleanLit(True), IfStmt(BooleanLit(True), ReturnStmt(), ContinueStmt()), BreakStmt())]))
])"""
        self.assertTrue(TestAST.test(input, str(expect), 26))
        
    def test_027(self):
        """test Statement"""
        input = """
            foo : function void () {  
                if (true) return;
            }
        """
        expect = """Program([
	FuncDecl(foo, VoidType, [], None, BlockStmt([IfStmt(BooleanLit(True), ReturnStmt())]))
])"""
        self.assertTrue(TestAST.test(input, str(expect),27 ))

    def test_028(self):
        """test Statement"""
        input = """
            foo : function void () {  
                return;
                return 1 + 2;
            }
        """
        expect = """Program([
	FuncDecl(foo, VoidType, [], None, BlockStmt([ReturnStmt(), ReturnStmt(BinExpr(+, IntegerLit(1), IntegerLit(2)))]))
])"""
        self.assertTrue(TestAST.test(input, str(expect), 28))
        
    def test_029(self):
        """test Statement"""
        input = """
            foo : function void () {  
                foo();
                foo(1+2, 3);
            }
        """
        expect = """Program([
	FuncDecl(foo, VoidType, [], None, BlockStmt([CallStmt(foo, ), CallStmt(foo, BinExpr(+, IntegerLit(1), IntegerLit(2)), IntegerLit(3))]))
])"""
        self.assertTrue(TestAST.test(input, str(expect), 29))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
        
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
        expect = """Program([
	FuncDecl(foo, VoidType, [], None, BlockStmt([BlockStmt([BreakStmt(), ContinueStmt(), BlockStmt([BlockStmt([BlockStmt([])])])])]))
])"""
        self.assertTrue(TestAST.test(input, str(expect),30 ))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
        
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
        expect = """Program([
	FuncDecl(foo, VoidType, [], None, BlockStmt([BlockStmt([VarDecl(a, FloatType), VarDecl(b, FloatType), VarDecl(c, FloatType, IntegerLit(1)), VarDecl(d, FloatType, IntegerLit(2)), VarDecl(e, StringType, StringLit(@))])]))
])"""
        self.assertTrue(TestAST.test(input, str(expect),31 ))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
        
    def test_032(self):
        """test Statement"""
        input = """
            foo : function void () {  
                for (i = 1, i < 10, i + 1) {
                    writeInt(i);
                }
            }

        """
        expect = """Program([
	FuncDecl(foo, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([CallStmt(writeInt, Id(i))]))]))
])"""
        self.assertTrue(TestAST.test(input, str(expect), 32))         

    def test_033(self):
        """test Statement"""
        input = """
            foo : function void () {  
                for (i = 1, i < 10, i + 1) break;
            }

        """
        expect = """Program([
	FuncDecl(foo, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(1)), BreakStmt())]))
])"""
        self.assertTrue(TestAST.test(input, str(expect), 33))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
        

    def test_034(self):
        """test Statement"""
        input = """
            foo : function void () {  
                while (true) break;
                while (false) {}
            }
        """
        expect = """Program([
	FuncDecl(foo, VoidType, [], None, BlockStmt([WhileStmt(BooleanLit(True), BreakStmt()), WhileStmt(BooleanLit(False), BlockStmt([]))]))
])"""
        self.assertTrue(TestAST.test(input, str(expect), 34))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
        
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
        expect = """Program([
	FuncDecl(foo, VoidType, [], None, BlockStmt([DoWhileStmt(FloatLit(1.0), BlockStmt([BreakStmt()]))]))
])"""
        self.assertTrue(TestAST.test(input, str(expect), 35))        
        

    def test_036(self):
        """test Statement"""
        input = """
            foo : function void () {  
                for (i[1+1] = 1, i < 10, i + 1) return;
            }
        """
        expect = """Program([
	FuncDecl(foo, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(ArrayCell(i, [BinExpr(+, IntegerLit(1), IntegerLit(1))]), IntegerLit(1)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(1)), ReturnStmt())]))
])"""
        self.assertTrue(TestAST.test(input, str(expect), 36)) 
    def test_037(self):
        """test Variable and type"""
        input = """
            x, y, z : integer;
        """
        expect = """Program([
	VarDecl(x, IntegerType)
	VarDecl(y, IntegerType)
	VarDecl(z, IntegerType)
])"""
        self.assertTrue(TestAST.test(input, str(expect), 37))

    def test_038(self):
        """test Variable and type"""
        input = """
            a, b : boolean;
        """
        expect = """Program([
	VarDecl(a, BooleanType)
	VarDecl(b, BooleanType)
])"""
        self.assertTrue(TestAST.test(input, str(expect), 38))

    def test_039(self):
        """test Variable and type"""
        input = """
            m, n : auto;
        """
        expect = """Program([
	VarDecl(m, AutoType)
	VarDecl(n, AutoType)
])"""
        self.assertTrue(TestAST.test(input, str(expect), 39))

    def test_040(self):
        """test Variable and type"""
        input = """
            a : string = "hello";
        """
        expect = """Program([
	VarDecl(a, StringType, StringLit(hello))
])"""
        self.assertTrue(TestAST.test(input, str(expect), 40))

    def test_041(self):
        """test Variable and type"""
        input = """
            b : boolean = true;
        """
        expect = """Program([
	VarDecl(b, BooleanType, BooleanLit(True))
])"""
        self.assertTrue(TestAST.test(input, str(expect), 41))

    def test_042(self):
        """test Variable and type"""
        input = """
            x : integer = 10;
        """
        expect = """Program([
	VarDecl(x, IntegerType, IntegerLit(10))
])"""
        self.assertTrue(TestAST.test(input, str(expect), 42))

    def test_043(self):
        """test Variable and type"""
        input = """
            x : float = 3.14;
        """
        expect = """Program([
	VarDecl(x, FloatType, FloatLit(3.14))
])"""
        self.assertTrue(TestAST.test(input, str(expect), 43))

    def test_044(self):
        """test Variable and type"""
        input = """
            a, b, c : array [5] of integer;
        """
        expect = """Program([
	VarDecl(a, ArrayType([5], IntegerType))
	VarDecl(b, ArrayType([5], IntegerType))
	VarDecl(c, ArrayType([5], IntegerType))
])"""
        self.assertTrue(TestAST.test(input, str(expect), 44))

    def test_045(self):
        """test Variable and type"""
        input = """
            y : auto = 10;
        """
        expect = """Program([
	VarDecl(y, AutoType, IntegerLit(10))
])"""
        self.assertTrue(TestAST.test(input, str(expect), 45))

    def test_046(self):
        """test Variable and type"""
        input = """
            y : auto = 2.5;
        """
        expect = """Program([
	VarDecl(y, AutoType, FloatLit(2.5))
])"""
        self.assertTrue(TestAST.test(input, str(expect), 46))

    def test_047(self):
        """test Variable and type"""
        input = """
            a, b, c : array [3, 3] of float;
        """
        expect = """Program([
	VarDecl(a, ArrayType([3, 3], FloatType))
	VarDecl(b, ArrayType([3, 3], FloatType))
	VarDecl(c, ArrayType([3, 3], FloatType))
])"""
        self.assertTrue(TestAST.test(input, str(expect), 47))

    def test_048(self):
        """test Variable and type"""
        input = """
            a : array [3, 3] of integer = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};
        """
        expect = """Program([
	VarDecl(a, ArrayType([3, 3], IntegerType), ArrayLit([ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3)]), ArrayLit([IntegerLit(4), IntegerLit(5), IntegerLit(6)]), ArrayLit([IntegerLit(7), IntegerLit(8), IntegerLit(9)])]))
])"""
        self.assertTrue(TestAST.test(input, str(expect), 48))

    def test_049(self):
        """test Variable and type"""
        input = """
            s : string = "test";
        """
        expect = """Program([
	VarDecl(s, StringType, StringLit(test))
])"""
        self.assertTrue(TestAST.test(input, str(expect), 49))

    def test_050(self):
        """test function"""
        input = """
            foo : function void () {}
        """
        expect = """Program([
	FuncDecl(foo, VoidType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, str(expect), 50))

    def test_051(self):
        """test function"""
        input = """
            foo : function integer (x : integer) {}
        """
        expect = """Program([
	FuncDecl(foo, IntegerType, [Param(x, IntegerType)], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, str(expect), 51))

    def test_052(self):
        """test function"""
        input = """
            foo : function float (x : integer, y : float) {}
        """
        expect = """Program([
	FuncDecl(foo, FloatType, [Param(x, IntegerType), Param(y, FloatType)], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, str(expect), 52))

    def test_053(self):
        """test function"""
        input = """
            bar : function void () inherit foo {}
        """
        expect = """Program([
	FuncDecl(bar, VoidType, [], foo, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, str(expect), 53))

    def test_054(self):
        """test function"""
        input = """
            bar : function auto (x : integer) inherit foo {}
        """
        expect = """Program([
	FuncDecl(bar, AutoType, [Param(x, IntegerType)], foo, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, str(expect), 54))

    def test_055(self):
        """test expression"""
        input = """
            x : integer = 1 + 2;
        """
        expect = """Program([
	VarDecl(x, IntegerType, BinExpr(+, IntegerLit(1), IntegerLit(2)))
])"""
        self.assertTrue(TestAST.test(input, str(expect), 55))

    def test_056(self):
        """test expression"""
        input = """
            y : float = 3.5 - 2.1;
        """
        expect = """Program([
	VarDecl(y, FloatType, BinExpr(-, FloatLit(3.5), FloatLit(2.1)))
])"""
        self.assertTrue(TestAST.test(input, str(expect), 56))

    def test_057(self):
        """test expression"""
        input = """
            z : boolean = true && false;
        """
        expect = """Program([
	VarDecl(z, BooleanType, BinExpr(&&, BooleanLit(True), BooleanLit(False)))
])"""
        self.assertTrue(TestAST.test(input, str(expect), 57))

    def test_058(self):
        """test expression"""
        input = """
            s : string = "a" :: "b";
        """
        expect = """Program([
	VarDecl(s, StringType, BinExpr(::, StringLit(a), StringLit(b)))
])"""
        self.assertTrue(TestAST.test(input, str(expect), 58))

    def test_059(self):
        """test expression"""
        input = """
            r : boolean = 1 > 2;
        """
        expect = """Program([
	VarDecl(r, BooleanType, BinExpr(>, IntegerLit(1), IntegerLit(2)))
])"""
        self.assertTrue(TestAST.test(input, str(expect), 59))

    def test_060(self):
        """test expression"""
        input = """
            r : boolean = 1 <= 2;
        """
        expect = """Program([
	VarDecl(r, BooleanType, BinExpr(<=, IntegerLit(1), IntegerLit(2)))
])"""
        self.assertTrue(TestAST.test(input, str(expect), 60))

    def test_061(self):
        """test expression"""
        input = """
            r : boolean = "abc" == "def";
        """
        expect = """Program([
	VarDecl(r, BooleanType, BinExpr(==, StringLit(abc), StringLit(def)))
])"""
        self.assertTrue(TestAST.test(input, str(expect), 61))

    def test_062(self):
        """test expression"""
        input = """
            r : boolean = 1 != 2;
        """
        expect = """Program([
	VarDecl(r, BooleanType, BinExpr(!=, IntegerLit(1), IntegerLit(2)))
])"""
        self.assertTrue(TestAST.test(input, str(expect), 62))

    def test_063(self):
        """test expression"""
        input = """
            r : boolean = 1 == 1;
        """
        expect = """Program([
	VarDecl(r, BooleanType, BinExpr(==, IntegerLit(1), IntegerLit(1)))
])"""
        self.assertTrue(TestAST.test(input, str(expect), 63))

    def test_064(self):
        """test expression"""
        input = """
            a : integer = 5 * 3;
        """
        expect = """Program([
	VarDecl(a, IntegerType, BinExpr(*, IntegerLit(5), IntegerLit(3)))
])"""
        self.assertTrue(TestAST.test(input, str(expect), 64))

    def test_065(self):
        """test expression"""
        input = """
            a : float = 5.2 / 2.0;
        """
        expect = """Program([
	VarDecl(a, FloatType, BinExpr(/, FloatLit(5.2), FloatLit(2.0)))
])"""
        self.assertTrue(TestAST.test(input, str(expect), 65))

    def test_066(self):
        """test expression"""
        input = """
            b : integer = 5 % 2;
        """
        expect = """Program([
	VarDecl(b, IntegerType, BinExpr(%, IntegerLit(5), IntegerLit(2)))
])"""
        self.assertTrue(TestAST.test(input, str(expect), 66))

    def test_067(self):
        """test expression"""
        input = """
            c : integer = -5;
        """
        expect = """Program([
	VarDecl(c, IntegerType, UnExpr(-, IntegerLit(5)))
])"""
        self.assertTrue(TestAST.test(input, str(expect), 67))

    def test_068(self):
        """test expression"""
        input = """
            d : boolean = !true;
        """
        expect = """Program([
	VarDecl(d, BooleanType, UnExpr(!, BooleanLit(True)))
])"""
        self.assertTrue(TestAST.test(input, str(expect), 68))

    def test_069(self):
        """test expression"""
        input = """
            e : float = -0.5;
        """
        expect = """Program([
	VarDecl(e, FloatType, UnExpr(-, FloatLit(0.5)))
])"""
        self.assertTrue(TestAST.test(input, str(expect), 69))

    def test_070(self):
        """test expression"""
        input = """
            f : integer = x + 1;
        """
        expect = """Program([
	VarDecl(f, IntegerType, BinExpr(+, Id(x), IntegerLit(1)))
])"""
        self.assertTrue(TestAST.test(input, str(expect), 70))

    def test_071(self):
        """test expression"""
        input = """
            g : float = y - 1.0;
        """
        expect = """Program([
	VarDecl(g, FloatType, BinExpr(-, Id(y), FloatLit(1.0)))
])"""
        self.assertTrue(TestAST.test(input, str(expect), 71))

    def test_072(self):
        """test expression"""
        input = """
            h : integer = a * b;
        """
        expect = """Program([
	VarDecl(h, IntegerType, BinExpr(*, Id(a), Id(b)))
])"""
        self.assertTrue(TestAST.test(input, str(expect), 72))

    def test_073(self):
        """test expression"""
        input = """
            i : float = c / d;
        """
        expect = """Program([
	VarDecl(i, FloatType, BinExpr(/, Id(c), Id(d)))
])"""
        self.assertTrue(TestAST.test(input, str(expect), 73))

    def test_074(self):
        """test expression"""
        input = """
            j : integer = e % f;
        """
        expect = """Program([
	VarDecl(j, IntegerType, BinExpr(%, Id(e), Id(f)))
])"""
        self.assertTrue(TestAST.test(input, str(expect), 74))

    def test_075(self):
        """test expression"""
        input = """
            k : integer = -x;
        """
        expect = """Program([
	VarDecl(k, IntegerType, UnExpr(-, Id(x)))
])"""
        self.assertTrue(TestAST.test(input, str(expect), 75))

    def test_076(self):
        """test expression"""
        input = """
            l : boolean = !y;
        """
        expect = """Program([
	VarDecl(l, BooleanType, UnExpr(!, Id(y)))
])"""
        self.assertTrue(TestAST.test(input, str(expect), 76))

    def test_077(self):
        """test expression"""
        input = """
            m : integer = n == o;
        """
        expect = """Program([
	VarDecl(m, IntegerType, BinExpr(==, Id(n), Id(o)))
])"""
        self.assertTrue(TestAST.test(input, str(expect), 77))

    def test_078(self):
        """test expression"""
        input = """
            p : boolean = q != r;
        """
        expect = """Program([
	VarDecl(p, BooleanType, BinExpr(!=, Id(q), Id(r)))
])"""
        self.assertTrue(TestAST.test(input, str(expect), 78))

    def test_079(self):
        """test expression"""
        input = """
            s : boolean = t && u;
        """
        expect = """Program([
	VarDecl(s, BooleanType, BinExpr(&&, Id(t), Id(u)))
])"""
        self.assertTrue(TestAST.test(input, str(expect), 79))

    def test_080(self):
        """test expression"""
        input = """
            v : boolean = w || x;
        """
        expect = """Program([
	VarDecl(v, BooleanType, BinExpr(||, Id(w), Id(x)))
])"""
        self.assertTrue(TestAST.test(input, str(expect), 80))

    def test_081(self):
        """test expression"""
        input = """
            y : boolean = z > a;
        """
        expect = """Program([
	VarDecl(y, BooleanType, BinExpr(>, Id(z), Id(a)))
])"""
        self.assertTrue(TestAST.test(input, str(expect), 81))

    def test_082(self):
        """test expression"""
        input = """
            b : boolean = c < d;
        """
        expect = """Program([
	VarDecl(b, BooleanType, BinExpr(<, Id(c), Id(d)))
])"""
        self.assertTrue(TestAST.test(input, str(expect), 82))

    def test_083(self):
        """test expression"""
        input = """
            e : boolean = f >= g;
        """
        expect = """Program([
	VarDecl(e, BooleanType, BinExpr(>=, Id(f), Id(g)))
])"""
        self.assertTrue(TestAST.test(input, str(expect), 83))

    def test_084(self):
        """test expression"""
        input = """
            h : boolean = i <= j;
        """
        expect = """Program([
	VarDecl(h, BooleanType, BinExpr(<=, Id(i), Id(j)))
])"""
        self.assertTrue(TestAST.test(input, str(expect), 84))

    def test_085(self):
        """test statement"""
        input = """
            foo : function void () {
                x = 5;
            }
        """
        expect = """Program([
	FuncDecl(foo, VoidType, [], None, BlockStmt([AssignStmt(Id(x), IntegerLit(5))]))
])"""
        self.assertTrue(TestAST.test(input, str(expect), 85))

    def test_086(self):
        """test statement"""
        input = """
            foo : function void () {
                y = 2.5;
            }
        """
        expect = """Program([
	FuncDecl(foo, VoidType, [], None, BlockStmt([AssignStmt(Id(y), FloatLit(2.5))]))
])"""
        self.assertTrue(TestAST.test(input, str(expect), 86))

    def test_087(self):
        """test statement"""
        input = """
            foo : function void () {
                z = true;
            }
        """
        expect = """Program([
	FuncDecl(foo, VoidType, [], None, BlockStmt([AssignStmt(Id(z), BooleanLit(True))]))
])"""
        self.assertTrue(TestAST.test(input, str(expect), 87))

    def test_088(self):
        """test statement"""
        input = """
            foo : function void () {
                s = "hello";
            }
        """
        expect = """Program([
	FuncDecl(foo, VoidType, [], None, BlockStmt([AssignStmt(Id(s), StringLit(hello))]))
])"""
        self.assertTrue(TestAST.test(input, str(expect), 88))

    def test_089(self):
        """test statement"""
        input = """
            foo : function void () {
                a[5] = 10;
            }
        """
        expect = """Program([
	FuncDecl(foo, VoidType, [], None, BlockStmt([AssignStmt(ArrayCell(a, [IntegerLit(5)]), IntegerLit(10))]))
])"""
        self.assertTrue(TestAST.test(input, str(expect), 89))

    def test_090(self):
        """test statement"""
        input = """
            foo : function void () {
                b[1] = "test";
            }
        """
        expect = """Program([
	FuncDecl(foo, VoidType, [], None, BlockStmt([AssignStmt(ArrayCell(b, [IntegerLit(1)]), StringLit(test))]))
])"""
        self.assertTrue(TestAST.test(input, str(expect), 90))

    def test_091(self):
        """test statement"""
        input = """
            foo : function void () {
                c[2] = false;
            }
        """
        expect = """Program([
	FuncDecl(foo, VoidType, [], None, BlockStmt([AssignStmt(ArrayCell(c, [IntegerLit(2)]), BooleanLit(False))]))
])"""
        self.assertTrue(TestAST.test(input, str(expect), 91))

    def test_092(self):
        """test statement"""
        input = """
            foo : function void () {
                d = 5 + 3;
            }
        """
        expect = """Program([
	FuncDecl(foo, VoidType, [], None, BlockStmt([AssignStmt(Id(d), BinExpr(+, IntegerLit(5), IntegerLit(3)))]))
])"""
        self.assertTrue(TestAST.test(input, str(expect), 92))

    def test_093(self):
        """test statement"""
        input = """
            foo : function void () {
                e = 2.5 - 1.0;
            }
        """
        expect = """Program([
	FuncDecl(foo, VoidType, [], None, BlockStmt([AssignStmt(Id(e), BinExpr(-, FloatLit(2.5), FloatLit(1.0)))]))
])"""
        self.assertTrue(TestAST.test(input, str(expect), 93))

    def test_094(self):
        """test statement"""
        input = """
            foo : function void () {
                f = a * b;
            }
        """
        expect = """Program([
	FuncDecl(foo, VoidType, [], None, BlockStmt([AssignStmt(Id(f), BinExpr(*, Id(a), Id(b)))]))
])"""
        self.assertTrue(TestAST.test(input, str(expect), 94))

    def test_095(self):
        """test statement"""
        input = """
            foo : function void () {
                g = c / d;
            }
        """
        expect = """Program([
	FuncDecl(foo, VoidType, [], None, BlockStmt([AssignStmt(Id(g), BinExpr(/, Id(c), Id(d)))]))
])"""
        self.assertTrue(TestAST.test(input, str(expect), 95))

    def test_096(self):
        """test statement"""
        input = """
            foo : function void () {
                h = e % f;
            }
        """
        expect = """Program([
	FuncDecl(foo, VoidType, [], None, BlockStmt([AssignStmt(Id(h), BinExpr(%, Id(e), Id(f)))]))
])"""
        self.assertTrue(TestAST.test(input, str(expect), 96))

    def test_097(self):
        """test statement"""
        input = """
            foo : function void () {
                i = -g;
            }
        """
        expect = """Program([
	FuncDecl(foo, VoidType, [], None, BlockStmt([AssignStmt(Id(i), UnExpr(-, Id(g)))]))
])"""
        self.assertTrue(TestAST.test(input, str(expect), 97))

    def test_098(self):
        """test statement"""
        input = """
            foo : function void () {
                j = !h;
            }
        """
        expect = """Program([
	FuncDecl(foo, VoidType, [], None, BlockStmt([AssignStmt(Id(j), UnExpr(!, Id(h)))]))
])"""
        self.assertTrue(TestAST.test(input, str(expect), 98))

    def test_099(self):
        """test statement"""
        input = """
            foo : function void () {
                k = l == m;
            }
        """
        expect = """Program([
	FuncDecl(foo, VoidType, [], None, BlockStmt([AssignStmt(Id(k), BinExpr(==, Id(l), Id(m)))]))
])"""
        self.assertTrue(TestAST.test(input, str(expect), 99))

    def test_100(self):
        """test statement"""
        input = """
            foo : function void () {
                n = o != p;
            }
        """
        expect = """Program([
	FuncDecl(foo, VoidType, [], None, BlockStmt([AssignStmt(Id(n), BinExpr(!=, Id(o), Id(p)))]))
])"""
        self.assertTrue(TestAST.test(input, str(expect), 100))  