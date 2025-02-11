import unittest
from TestUtils import TestChecker
from AST import *
class CheckerSuite(unittest.TestCase):

    def test_001(self):
        input = """
            x : integer;
            b : float;
            x : string;

            main : function void(){}
        """
        expect = "Redeclared Variable: x"
        self.assertTrue(TestChecker.test(input, expect, 100))

    def test_002(self):
        input = """
            a, b, a : integer;
            main : function void(){}
        """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input, expect, 101))
    
    def test_003(self):
        input = """
            hihi : function void () {}
            hihi : function void () {}
            main : function void(){}
        """
        expect = "Redeclared Function: hihi"
        self.assertTrue(TestChecker.test(input, expect, 102))

    def test_004(self):
        input = """
            q : function void () {}
            q : function void (q : string) {}
            main : function void(){}
        """
        expect = "Redeclared Function: q"
        self.assertTrue(TestChecker.test(input, expect, 103))

    def test_005(self):
        input = """
            readInteger : function integer (e : integer){ 
                return 1;
            }
            main : function void(){}
        """
        expect = "Redeclared Function: readInteger"
        self.assertTrue(TestChecker.test(input, expect, 104))

    def test_006(self):
        input = """
            readInteger : integer;
            main : function void(){}
        """
        expect = "Redeclared Variable: readInteger"
        self.assertTrue(TestChecker.test(input, expect, 105))

    def test_007(self):
        input = """
            a : integer;
            a : function void (){}
            main : function void(){}
        """
        expect = "Redeclared Function: a"
        self.assertTrue(TestChecker.test(input, expect, 106))

    def test_008(self):
        input = """
            a : function void (){}
            a : float;
            main : function void(){}
        """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input, expect, 107))

    def test_009(self):
        input = """
            a : function void (a : integer) inherit lala{preventDefault();}
            main : function void(){}
        """
        expect = "Undeclared Function: lala"
        self.assertTrue(TestChecker.test(input, expect, 108))

    def test_010(self):
        input = """
            a : function void (a : integer) inherit c{preventDefault();}
            b : function void (b : integer){}
            c : function void () inherit b{}
            d : function void () inherit parentb{}
            main : function void(){}
        """
        expect = "Undeclared Function: parentb"
        self.assertTrue(TestChecker.test(input, expect, 109))

    def test_011(self):
        input = """
            function_a : integer;
            x : function void (a : integer) inherit printInteger{preventDefault();}
            y : function void (b : integer){}
            z : function void () inherit main{}
            w : function void () inherit function_a{}
            main : function void(){}
        """
        expect = "Undeclared Function: function_a"
        self.assertTrue(TestChecker.test(input, expect, 110))

    def test_012(self):
        input = """
            my_function : function integer(){}
        """
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input, expect, 111))

    def test_013(self):
        input = """
            main : function string(){
                return "HelloPPL";
            }
        """
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input, expect, 112))

    def test_014(self):
        input = """
            main : function void(x : string){
            }
        """
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input, expect, 113))

    def test_015(self):
        input = """
            my_function: function void(){}
            main : function auto() inherit my_function{}
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 114))

    def test_016(self):
        input = """
            main : string;
        """
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input, expect, 115))

    def test_017(self):
        input = """
            foo_a : function integer (a : auto) {
                b : boolean = a && true || foo_b();
                c : boolean = 1.0 && true;
                return 1;
            }
            
            main : function void() {}
            foo_b : function auto (){return true;}
        """
        expect = """Type mismatch in expression: BinExpr("&&", FloatLit(1.0), BooleanLit(True))"""
        self.assertTrue(TestChecker.test(input, expect, 116))

    def test_018(self):
        input = """
            a : integer;
            foo_x : function void(a : integer) inherit foo_y{preventDefault();}
            foo_y : function void (a : integer, foo_y : string) {}
            foo_z : function void (a : integer, a : string) {}
            main : function void(){}
        """
        expect = "Redeclared Parameter: a"
        self.assertTrue(TestChecker.test(input, expect, 117))

    def test_018(self):
        input = """
            a : integer;
            foo_x : function string (a : integer, b : string) {
                a : integer;
                {
                    a : integer;
                }
                a : string;
            }

            main : function void(){}
        """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input, expect, 118))

    def test_019(self):
        input = """
            a : integer;
            foo_x : function void (c : integer, b : string) {
                {
                    a : integer;
                }
                a : integer;
                {
                    b, a, b : integer;
                }
            }

            main : function void(){}
        """
        expect = "Redeclared Variable: b"
        self.assertTrue(TestChecker.test(input, expect, 119))

    def test_020(self):
        input = """
            x : auto;
            main : function void(){}
        """
        expect = "Invalid Variable: x"
        self.assertTrue(TestChecker.test(input, expect, 120))

    def test_021(self):
        input = """
            main : function void(){
                my_var : auto;
            }
        """
        expect = "Invalid Variable: my_var"
        self.assertTrue(TestChecker.test(input, expect, 121))

    def test_022(self):
        input = """
            a : auto = 5;
            main : function void(){
                b : string = 2;
            }
        """
        expect = """Type mismatch in Variable Declaration: VarDecl("b", StringType(), IntegerLit(2))"""
        self.assertTrue(TestChecker.test(input, expect, 122))

    def test_023(self):
        input = """
            a : integer = 10;
            b : string = true;
            main : function integer(){}
        """
        expect = """Type mismatch in Variable Declaration: VarDecl("b", StringType(), BooleanLit(True))"""
        self.assertTrue(TestChecker.test(input, expect, 123))

    def test_024(self):
        input = """  
            foo : function auto (a : integer) {
                {  
                    return 1;
                    {
                        return "B";
                    }
                    return "B";
                }
                return "A";
            }
        """
        expect = """Type mismatch in statement: ReturnStmt(StringLit("A"))"""
        self.assertTrue(TestChecker.test(input, expect, 124))

    def test_025(self):
        input = """
            foo_x: function void(inherit b : auto){}
            foo_y: function void(b : auto) inherit foo_x{preventDefault();}

            main : function auto() {}
        """
        expect = "Invalid Parameter: b"
        self.assertTrue(TestChecker.test(input, expect, 125))

    def test_026(self):
        input = """
            foo_x: function void() inherit foo_y{preventDefault();}
            foo_y: function void(inherit b : auto){}
            foo_z: function void(inherit b : auto) inherit foo_x{preventDefault();}            

            main : function void() {}
        """
        expect = "Invalid Parameter: b"
        self.assertTrue(TestChecker.test(input, expect, 126))

    def test_027(self):
        input = """
            foo_x: function void(inherit b : integer) inherit foo_y{preventDefault();}
            foo_y: function void(b : integer){}
            foo_z: function void(b : integer) inherit foo_x{preventDefault();}            

            main : function void() {}
        """
        expect = "Invalid Parameter: b"
        self.assertTrue(TestChecker.test(input, expect, 127))

    def test_028(self):
        input = """
            foo_x: function void(){}
            foo_y: function void(a : auto)  inherit foo_x{}
            foo_z: function void() inherit foo_y{}            

            main : function void() {}
        """
        expect = "Invalid statement in function: foo_z"
        self.assertTrue(TestChecker.test(input, expect, 128))

    def test_029(self):
        input = """
            foo_a: function void(){}
            foo_b: function void(a : auto)  inherit foo_a{}
            foo_c: function void() inherit foo_b{ super(1); }
            foo_d: function void()  inherit foo_a{preventDefault();}              
            foo_e: function void(a : auto)  inherit foo_d{super();} 
            main : function void() {}
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 129))
    
    def test_030(self):
        input = """
            foo_a: function void(){}
            foo_b: function void(a : auto)  inherit foo_a{}
            foo_c: function void() inherit foo_b{ a, b : string; }            

            main : function void() {}
        """
        expect = "Invalid statement in function: foo_c"
        self.assertTrue(TestChecker.test(input, expect, 130))

    def test_031(self):
        input = """
            foo_x: function void(){}
            foo_y: function void(a : auto)  inherit foo_x{}
            foo_z: function void() inherit foo_y{}            

            main : function void() {}
        """
        expect = "Invalid statement in function: foo_z"
        self.assertTrue(TestChecker.test(input, expect, 131))

    def test_032(self):
        input = """
            foo_a: function void(){}
            foo_b: function void(a : integer)  inherit foo_a{
                preventDefault(1, 10);
            }          

            main : function void() {}
        """
        expect = "Type mismatch in expression: IntegerLit(1)"
        self.assertTrue(TestChecker.test(input, expect, 132))

    def test_033(self):
        input = """
            foo_a: function void(){}
            foo_b: function void(a : integer)  inherit foo_a{
                super("M");
            }          

            main : function void() {}
        """
        expect = """Type mismatch in expression: StringLit("M")"""
        self.assertTrue(TestChecker.test(input, expect, 133))

    def test_034(self):
        input = """
            foo_a: function void(a : integer){}
            foo_b: function void()  inherit foo_a{
                super();
            }          

            main : function void() {}
        """
        expect = "Type mismatch in expression: "
        self.assertTrue(TestChecker.test(input, expect, 134))

    def test_035(self):
        input = """
            foo_a: function void(b : float, a : float){}
            foo_b: function void()  inherit foo_a{
                super(1, 2.0);
            }          
            foo_c: function void()  inherit foo_a{
                super(1,false);
            }       
            main : function void() {}
        """
        expect = "Type mismatch in expression: BooleanLit(False)"
        self.assertTrue(TestChecker.test(input, expect, 135))

    def test_036(self):
        input = """
            a : integer = 100;
            y : integer = c;
            main : function void(){}
        """
        expect = "Undeclared Identifier: c"
        self.assertTrue(TestChecker.test(input, expect, 136))

    def test_037(self):
        input = """
            a : integer = 100;
            foo_a : function void (e : integer){
                b : integer = a;
                {
                    c : integer = b;
                    b : integer = a;
                    e : integer = e;
                }
                d : integer = c;
            }

            main : function void(){}
        """
        expect = "Undeclared Identifier: c"
        self.assertTrue(TestChecker.test(input, expect, 137))

    def test_038(self):
        input = """
            a : integer = 100;
            foo_a : function void (e : integer){
                {
                    b : integer = m;
                }
                d : integer = c;
            }
            m : integer = a;
            main : function void(){}
        """
        expect = "Undeclared Identifier: m"
        self.assertTrue(TestChecker.test(input, expect, 138))

    def test_039(self):
        input = """
            foo_x: function void(inherit c : integer) inherit foo_y{preventDefault();}
            foo_y: function void(inherit b : integer){}
            foo_z: function integer() inherit foo_x{
                preventDefault();
                a, d : integer = b, c;
            }            

            main : function auto() {}
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 139))

    def test_040(self):
        input = """
            foo_x: function void(inherit c : integer) inherit foo_y{preventDefault();}
            foo_y: function void( b : integer){}
            foo_z: function integer() inherit foo_x{
                preventDefault();
                a, d : integer = b, c;
            }            

            main : function auto() {}
        """
        expect = "Undeclared Identifier: b"
        self.assertTrue(TestChecker.test(input, expect, 140))


    def test_041(self):
        input = """
            foo_x: function void(inherit c : integer, inherit b : integer) inherit foo_y{preventDefault();}
            foo_y: function void( b : integer){}
            foo_z: function integer() inherit foo_x{
                preventDefault();
                a, d : integer = b, c;
            }            

            main : function auto() {}
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 141))

    def test_042(self):
        input = """
            foo_x: function void(inherit c : integer, inherit b : integer) inherit foo_y{preventDefault();}
            foo_y: function void( b : integer){
                a, d : integer = b, c;
            }
            foo_z: function integer() inherit foo_x{
                preventDefault();
                a, d : integer = b, c;
            }            

            main : function auto() {}
        """
        expect = "Undeclared Identifier: c"
        self.assertTrue(TestChecker.test(input, expect, 142))

    def test_043(self):
        input = """
            foo_x: function void(b : auto) {
                a : integer = b;
                d : integer = b;
                c : string = b;
            }
                   
            main : function auto() {}
        """
        expect = """Type mismatch in Variable Declaration: VarDecl("c", StringType(), Id("b"))"""
        self.assertTrue(TestChecker.test(input, expect, 143))

    def test_044(self):
        input = """
            foo_x: function void(inherit c : auto) inherit foo_y{preventDefault();}
            foo_y: function void(inherit b : auto){}
            foo_z: function integer() inherit foo_x{
                preventDefault();
                a, d : integer = b, c;
                e : boolean = b;
            }            

            main : function auto() {}
        """
        expect = """Type mismatch in Variable Declaration: VarDecl("e", BooleanType(), Id("b"))"""
        self.assertTrue(TestChecker.test(input, expect, 144))

    def test_045(self):
        input = """
            foo_x: function void(inherit c : auto) inherit foo_y{preventDefault();}
            foo_y: function void(inherit b : auto){}
            foo_z: function integer() inherit foo_x{
                preventDefault();
                a : float = b;
                d : integer = d;
                e : float = d;
                k : string = d;
            }            

            main : function auto() {}
        """
        expect = """Type mismatch in Variable Declaration: VarDecl("k", StringType(), Id("d"))"""
        self.assertTrue(TestChecker.test(input, expect, 145))

    def test_046(self):
        input = """
            foo_x: function void(inherit c : integer) {}
            foo_y: function integer(inherit b : float){return 1;}
            foo_z: function integer(){return 1;}            

            main : function auto() {
                a : integer = foo_z();
                b : integer = foo_y(1.0);
                d : integer = foo_d();
            }
        """
        expect = """Undeclared Function: foo_d"""
        self.assertTrue(TestChecker.test(input, expect, 146))


    def test_047(self):
        input = """
            a : integer = foo_c();
            b : integer = foo_b(2.0);
            foo_a: function void(inherit c : integer) {}
            foo_b: function integer(inherit b : float){return 1;}
            foo_c: function integer(){return 1;}  
            d : integer = foo_d();   

            main : function auto() {

            }
        """
        expect = """Undeclared Function: foo_d"""
        self.assertTrue(TestChecker.test(input, expect, 147))


    def test_048(self):
        input = """
            foo_x: function integer(inherit c : integer) {return 1;}
            foo_y: function void(inherit b : integer){}
            foo_z: function integer(){return 2;}  

            main : function auto() {
                a : integer = foo_z(1);
            }
        """
        expect = """Type mismatch in expression: FuncCall("foo_z", [IntegerLit(1)])"""
        self.assertTrue(TestChecker.test(input, expect, 148))

    def test_049(self):
        input = """
            foo_x: function integer(inherit c : integer) {return 1;}
            foo_y: function void(inherit b : integer){}
            foo_z: function integer(){return 1;}  

            main : function auto() {
                a : integer = foo_x();
            }
        """
        expect = """Type mismatch in expression: FuncCall("foo_x", [])"""
        self.assertTrue(TestChecker.test(input, expect, 148))

    def test_050(self):
        input = """
            foo_x: function integer(inherit c : integer) {return 1;}
            foo_y: function void(inherit b : integer){}
            foo_z: function integer(){return 1;}  

            main : function auto() {
                a : integer = foo_z("a");
            }
        """
        expect = """Type mismatch in expression: FuncCall("foo_z", [StringLit("a")])"""
        self.assertTrue(TestChecker.test(input, expect, 149))

    def test_051(self):
        input = """
            foo_x: function integer(inherit c : integer) {return 1;}
            foo_y: function void(inherit b : integer){}
            foo_z: function integer(){return 1;}  

            main : function auto() {
                a : integer = foo_y(10);
            }
        """
        expect = """Type mismatch in expression: FuncCall("foo_y", [IntegerLit(10)])"""
        self.assertTrue(TestChecker.test(input, expect, 150))

    def test_052(self):
        input = """
            foo_x: function integer(c : auto) {
                b : string = c;
            }

            main : function auto() {
                a : integer = foo_x(2);
            }
        """
        expect = """Type mismatch in expression: FuncCall("foo_x", [IntegerLit(2)])"""
        self.assertTrue(TestChecker.test(input, expect, 151))

    def test_053(self):
        input = """
            main : function auto() {
                a : integer = foo_x(2);
            }

            foo_x: function integer(c : auto) {
                b : string = c;
            }
        """
        expect = """Type mismatch in Variable Declaration: VarDecl("b", StringType(), Id("c"))"""
        self.assertTrue(TestChecker.test(input, expect, 152))

    def test_054(self):
        input = """
            main : function auto() {
                a : integer = foo_x(2);
            }

            foo_x: function auto(c : auto) {
                a : string = foo_x(2);
            }
        """
        expect = """Type mismatch in Variable Declaration: VarDecl("a", StringType(), FuncCall("foo_x", [IntegerLit(2)]))"""
        self.assertTrue(TestChecker.test(input, expect, 153))

    def test_055(self):
        input = """
            foo_x: function integer(inherit c : float) {return 1;}
            foo_y: function void(inherit b : float){}
            foo_z: function void(){}            

            main : function auto() {
                foo_x(1.0);
                foo_y(1.0);
                foo_z();
                foo_m();
            }
        """
        expect = """Undeclared Function: foo_m"""
        self.assertTrue(TestChecker.test(input, expect, 154))


    def test_056(self):
        input = """
            foo_a: function void(inherit c : integer) {
                foo_c();
                foo_m();
            }
            foo_b: function integer(inherit b : integer){return 1;}
            foo_c: function integer(){return 1;}   

            main : function auto() {

            }
        """
        expect = """Undeclared Function: foo_m"""
        self.assertTrue(TestChecker.test(input, expect, 155))

    def test_057(self):
        input = """
            foo_x: function void(){preventDefault();}      

            main : function void() {}
        """
        expect = "Undeclared Function: preventDefault"
        self.assertTrue(TestChecker.test(input, expect, 156))

    def test_058(self):
        input = """
            foo_x: function void(){}

            foo_y: function void(a : auto)  inherit foo_x{}

            foo_z: function void() inherit foo_y{
                preventDefault();
                super(1);
            }            

            main : function void() {}
        """
        expect = "Undeclared Function: super"
        self.assertTrue(TestChecker.test(input, expect, 157))
   
    def test_059(self):
        input = """
            foo_x: function integer(inherit c : integer) {return 1;}
            foo_y: function void(inherit b : integer){}
            foo_z: function integer(){return 1;}  

            main : function auto() {
                foo_z(1);
            }
        """
        expect = """Type mismatch in statement: CallStmt("foo_z",[IntegerLit(1)])"""
        self.assertTrue(TestChecker.test(input, expect, 158))

    def test_060(self):
        input = """
            foo_x: function integer(inherit c : integer) {return 1;}
            foo_y: function void(inherit b : integer){}
            foo_z: function integer(){return 1;}  

            main : function auto() {
                foo_x();
            }
        """
        expect = """Type mismatch in statement: CallStmt("foo_x",[])"""
        self.assertTrue(TestChecker.test(input, expect, 159))

    def test_061(self):
        input = """
            foo_x: function integer(inherit c : integer) {return 1;}
            foo_y: function void(inherit b : integer){}
            foo_z: function integer(){return 1;}  

            main : function auto() {
                foo_z("a");
            }
        """
        expect = """Type mismatch in statement: CallStmt("foo_z",[StringLit("a")])"""
        self.assertTrue(TestChecker.test(input, expect, 160))

    def test_062(self):
        input = """
            foo_x: function integer(c : auto) {
                b : string = c;
            }

            main : function auto() {
                foo_x(2);
            }
        """
        expect = """Type mismatch in statement: CallStmt("foo_x",[IntegerLit(2)])"""
        self.assertTrue(TestChecker.test(input, expect, 161))

    def test_063(self):
        input = """
            main : function auto() {
                a : integer = foo_x(2);
            }
            foo_x: function integer(c : auto) {
                b : string = c;
            }
        """
        expect = """Type mismatch in Variable Declaration: VarDecl("b", StringType(), Id("c"))"""
        self.assertTrue(TestChecker.test(input, expect, 162))

    def test_064(self):
        input = """
            main : function auto() {
                foo_x(2);
            }

            foo_x: function auto(c : auto) {
                foo_x(2);
            }
        """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 163))

    def test_065(self):
        input = """
            main : function void() {
                x : auto = 1; // integer;
                y : auto = 2.0; // float;
                z : auto = "a"; // string;
                t : auto = true; // boolean;
                m : array [1] of integer;
                n : array [1] of float;
                p :  array [1] of string;
                q :  array [2] of integer;
                k :  array [1,2] of integer;

                y = x;
            }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 164))

    def test_066(self):
        input = """
            main : function void() {
                x : auto = 1; // integer;
                y : auto = 2.0; // float;
                z : auto = "a"; // string;
                t : auto = true; // boolean;
                m : array [1] of integer;
                n : array [1] of float;
                p :  array [1] of string;
                q :  array [2] of integer;
                k :  array [1,2] of integer;

                x = z;
            }
        """
        expect = """Type mismatch in statement: AssignStmt(Id("x"), Id("z"))"""
        self.assertTrue(TestChecker.test(input, expect, 165))

    def test_067(self):
        input = """
            main : function void() {
                x : auto = 1; // integer;
                y : auto = 2.0; // float;
                z : auto = "a"; // string;
                t : auto = true; // boolean;
                m : array [1] of integer;
                n : array [1] of float;
                p :  array [1] of string;
                q :  array [2] of integer;
                k :  array [1,2] of integer;

                y = t;
            }
        """
        expect = """Type mismatch in statement: AssignStmt(Id("y"), Id("t"))"""
        self.assertTrue(TestChecker.test(input, expect, 166))

    def test_068(self):
        input = """
            main : function void() {
                x : auto = 1; // integer;
                y : auto = 2.0; // float;
                z : auto = "a"; // string;
                t : auto = true; // boolean;
                m : array [1] of integer;
                n : array [1] of float;
                p :  array [1] of string;
                q :  array [2] of integer;
                k :  array [1,2] of integer;

                x = m;
            }
        """
        expect = """Type mismatch in statement: AssignStmt(Id("x"), Id("m"))"""
        self.assertTrue(TestChecker.test(input, expect, 167))

    def test_069(self):
        input = """
            main : function void() {
                x : auto = 1; // integer;
                y : auto = 2.0; // float;
                z : auto = "a"; // string;
                t : auto = true; // boolean;
                m : array [1] of integer;
                n : array [1] of float;
                p :  array [1] of string;
                q :  array [2] of integer;
                k :  array [1,2] of integer;

                m = p;
            }
        """
        expect = """Type mismatch in statement: AssignStmt(Id("m"), Id("p"))"""
        self.assertTrue(TestChecker.test(input, expect, 168))

    def test_070(self):
        input = """
            main : function void() {
                x : auto = 1; // integer;
                y : auto = 2.0; // float;
                z : auto = "a"; // string;
                t : auto = true; // boolean;
                m : array [1] of integer;
                n : array [1] of float;
                p :  array [1] of string;
                q :  array [2] of integer;
                k :  array [1,2] of integer;

                m = q;
            }
        """
        expect = """Type mismatch in statement: AssignStmt(Id("m"), Id("q"))"""
        self.assertTrue(TestChecker.test(input, expect, 169))

    def test_071(self):
        input = """
            main : function void() {
                x : auto = 1; // integer;
                y : auto = 2.0; // float;
                z : auto = "a"; // string;
                t : auto = true; // boolean;
                m : array [1] of integer;
                n : array [1] of float;
                p :  array [1] of string;
                q :  array [2] of integer;
                k :  array [1,2] of integer;

                q = k;
            }
        """
        expect = """Type mismatch in statement: AssignStmt(Id("q"), Id("k"))"""
        self.assertTrue(TestChecker.test(input, expect, 170))

    def test_072(self):
        input = """
            main : function void() {
                a : auto = 1; // integer;
                b : auto = 2.0; // float;
                c : auto = "a"; // string;
                d : auto = true; // boolean;
                e : array [1] of integer;
                f : array [1] of float;
                j :  array [1] of string;
                k :  array [2] of integer;
                h :  array [1,2] of integer;

                a = a;
                b = b;
                c = c;
                d = d;
                e = e;
                f = f;
                j = j;
                k = k;
                h = h;
                e = f;
            }
        """
        expect = """Type mismatch in statement: AssignStmt(Id("e"), Id("f"))"""
        self.assertTrue(TestChecker.test(input, expect, 171))


    def test_073(self):
        input = """
            foo_a : function integer (b : auto){
                b = 2.0;
                b = 2;
                b = "@";
            }

            main : function void() {}
        """
        expect = """Type mismatch in statement: AssignStmt(Id("b"), StringLit("@"))"""
        self.assertTrue(TestChecker.test(input, expect, 172))

    def test_074(self):
        input = """
            main : function void() {
                if(true){
                    a : auto = 10;
                } 
                else {
                    a : auto = 100;
                }
            }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 173))

    def test_075(self):
        input = """
            main : function void() {
                if(1){
                    a : auto = 100;
                } 
                else {
                    a : auto = 100;
                }
            }
        """
        expect = """Type mismatch in statement: IfStmt(IntegerLit(1), BlockStmt([VarDecl("a", AutoType(), IntegerLit(100))]), BlockStmt([VarDecl("a", AutoType(), IntegerLit(100))]))"""
        self.assertTrue(TestChecker.test(input, expect, 174))

    def test_076(self):
        input = """
            main : function void() {
                if(foo_a()){
                    a : auto = 1;
                } 
                else {
                    a : auto = 1;
                }
            }

            foo_a : function void(){
            }
        """
        expect = """Type mismatch in expression: FuncCall("foo_a", [])"""
        self.assertTrue(TestChecker.test(input, expect, 175))

    def test_077(self):
        input = """
            main : function void() {
                if(foo_a()){
                    a : auto = 100;
                } 
                else {
                    a : auto = 100;
                }
            }

            foo_a : function auto(){
                return;
            }
        """
        expect = """Type mismatch in statement: ReturnStmt()"""
        self.assertTrue(TestChecker.test(input, expect, 176))

    def test_078(self):
        input = """
            main : function void() {
                if(foo_a()){
                    a : auto = 1000;
                } 
            }

            foo_a : function auto(){
                return true;
            }
        """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 177))

    def test_079(self):
        input = """
            main : function void() {}

            foo_a : function auto(a : auto){
                if(foo_a(100)){
                    
                }
                c : boolean = foo_a(100);
                b : string = foo_a(100);
            }
        """
        expect = """Type mismatch in Variable Declaration: VarDecl("b", StringType(), FuncCall("foo_a", [IntegerLit(100)]))"""
        self.assertTrue(TestChecker.test(input, expect, 178))

    def test_080(self):
        input = """
            main : function void() {
                id : auto = 10;
                for(id = 1, true, id)
                {
                    return;
                }
            }

            foo_a : function auto(){
                return 100;
            }
        """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 179))

    def test_081(self):
        input = """
            main : function void() {
                id : auto = "0001";
                for(id = 1, true, id)
                {
                    return;
                }
            }

            foo_a : function auto(){
                return 1;
            }
        """
        expect = """Type mismatch in statement: ForStmt(AssignStmt(Id("id"), IntegerLit(1)), BooleanLit(True), Id("id"), BlockStmt([ReturnStmt()]))"""
        self.assertTrue(TestChecker.test(input, expect, 180))

    def test_082(self):
        input = """
            main : function void() {
                id : auto = 2.0;
                for(id = 1, true, id)
                {
                    return;
                }
            }

            foo_a : function auto(){
                return 1;
            }
        """
        expect = """Type mismatch in statement: ForStmt(AssignStmt(Id("id"), IntegerLit(1)), BooleanLit(True), Id("id"), BlockStmt([ReturnStmt()]))"""
        self.assertTrue(TestChecker.test(input, expect, 181))


    def test_083(self):
        input = """
            main : function void() {
                id : auto = 1;
                for(id = "1001", true, id)
                {
                    return;
                }
            }

            foo_a : function auto(){
                return 1;
            }
        """
        expect = """Type mismatch in statement: ForStmt(AssignStmt(Id("id"), StringLit("1001")), BooleanLit(True), Id("id"), BlockStmt([ReturnStmt()]))"""
        self.assertTrue(TestChecker.test(input, expect, 182))

    def test_084(self):
        input = """
            main : function void() {
                id : auto = 1;
                for(id = 2, foo_a(), id)
                {
                    return;
                }
            }

            foo_a : function auto(){
                return 101;
            }
        """
        expect = """Type mismatch in statement: ReturnStmt(IntegerLit(101))"""
        self.assertTrue(TestChecker.test(input, expect, 183))

    def test_085(self):
        input = """
            main : function void() {
                id : auto = 1;
                for(id = 1, foo_a(), id)
                {
                    return;
                }
            }

            foo_a : function integer(){
                return 1;
            }
        """
        expect = """Type mismatch in statement: ForStmt(AssignStmt(Id("id"), IntegerLit(1)), FuncCall("foo_a", []), Id("id"), BlockStmt([ReturnStmt()]))"""
        self.assertTrue(TestChecker.test(input, expect, 184))

    def test_086(self):
        input = """
            main : function void() {
                id : auto = 1000;
                for(id = 1, true, true)
                {
                    return;
                }
            }

            foo_a : function integer(){
                return 1;
            }
        """
        expect = """Type mismatch in statement: ForStmt(AssignStmt(Id("id"), IntegerLit(1)), BooleanLit(True), BooleanLit(True), BlockStmt([ReturnStmt()]))"""
        self.assertTrue(TestChecker.test(input, expect, 185))

    def test_087(self):
        input = """
            main : function void() {
                id : auto = 1010;
                for(id = foo_a(), true, 1)
                {
                    return;
                }
            }

            foo_a : function auto(){
                return true;
            }
        """
        expect = """Type mismatch in statement: ReturnStmt(BooleanLit(True))"""
        self.assertTrue(TestChecker.test(input, expect, 186))

    def test_088(self):
        input = """
            main : function void() {

            }

            foo_a : function auto(id : auto){
                for(id = 1, true, 1)
                {
                    return;
                }
                foo_a("aaaa");
            }
        """
        expect = """Type mismatch in statement: CallStmt("foo_a",[StringLit("aaaa")])"""
        self.assertTrue(TestChecker.test(input, expect, 187))

    def test_089(self):
        input = """
            main : function void() {
                a : auto = 1;
                while(true){
                    a : auto = 1;
                    return;
                }
                while(true) return;
                while(1) return;
            }

            foo_a : function auto(){
                return false;
            }
        """
        expect = """Type mismatch in statement: WhileStmt(IntegerLit(1), ReturnStmt())"""
        self.assertTrue(TestChecker.test(input, expect, 188))


    def test_090(self):
        input = """
            main : function void() {
                while(foo_a()) return;
            }

            foo_a : function auto(){
                return false;
            }
        """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 189))

    def test_091(self):
        input = """
            main : function void() {
                while(foo_a()) return;
            }

            foo_a : function string(){
                return "1001";
            }
        """
        expect = """Type mismatch in statement: WhileStmt(FuncCall("foo_a", []), ReturnStmt())"""
        self.assertTrue(TestChecker.test(input, expect, 190))

    def test_092(self):
        input = """
            main : function void() {
                while(foo_a()) return;
            }

            foo_a : function auto(){
                return false;
            }
        """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 191))

    def test_093(self):
        input = """
            main : function void() {
                break;
            }
        """
        expect = """Must in loop: BreakStmt()"""
        self.assertTrue(TestChecker.test(input, expect, 192))

    def test_094(self):
        input = """
            main : function void() {
                continue;
            }
        """
        expect = """Must in loop: ContinueStmt()"""
        self.assertTrue(TestChecker.test(input, expect, 193))

    def test_095(self):
        input = """
            main : function void() {
                while(true)
                {
                    a : auto = 1;
                    for (a=1,true,1) break;
                    break;
                    continue;
                    do{
                        {
                            break;
                            continue;
                        }
                    }while(true);
                    break;
                    continue;
                    for (a=1,true,1) continue;
                }
            }
        """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 194))

        
    def test_096(self):
        input = """
            main : function void() {
                while(true)
                {
                    a : auto = 1;
                    for (a=1,true,1) break;
                    break;
                    continue;
                    do{
                        {
                            break;
                            continue;
                        }
                    }while(true);
                    break;
                    continue;
                    for (a=1,true,1) continue;
                }
                break;
            }
        """
        expect = """Must in loop: BreakStmt()"""
        self.assertTrue(TestChecker.test(input, expect, 195))

    def test_097(self):
        input = """
            main : function void() {
                while(true)
                {
                    a : auto = 1;
                    for (a=1,true,1) break;
                    break;
                    continue;
                    do{
                        {
                            break;
                            continue;
                        }
                    }while(true);
                    break;
                    continue;
                    for (a=1,true,1) continue;
                }
                continue;
            }
        """
        expect = """Must in loop: ContinueStmt()"""
        self.assertTrue(TestChecker.test(input, expect, 196))

    def test_098(self):
        input = """
            foo : function float() {
                return 1;
                return "a";
            }
            main : function auto() {}
        """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 197))

    def test_099(self):
        input = """
            foo : function float() {
                return 1.1;
                return "a";
                {
                    return "a";
                }
            }
            main : function void() {}
        """
        expect = """"""
        self.assertTrue(TestChecker.test(input, expect, 198))

    def test_100(self):
        input = """
            foo : function integer() {
                return foo_a();
            }
            foo_a : function auto() {
                return "string";
            }
            main : function void() {}
        """
        expect = """Type mismatch in statement: ReturnStmt(StringLit("string"))"""
        self.assertTrue(TestChecker.test(input, expect, 199))