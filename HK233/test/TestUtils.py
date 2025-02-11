"""
 * Initial code for Assignment
 * file : testunile.py
 * Programming Language Principles
 * Author: Võ Tiến
 * Link FB : https://www.facebook.com/profile.php?id=100056605580171
 * Link Group : https://www.facebook.com/groups/211867931379013
 * Date: 06.19.2024
"""


import sys
import os
from antlr4 import *
from antlr4.error.ErrorListener import ConsoleErrorListener, ErrorListener
if not './main/' in sys.path:
    sys.path.append('./main/')
if os.path.isdir('./target/') and not './target/' in sys.path:
    sys.path.append('./target/')
from MT22Lexer import MT22Lexer
from MT22Parser import MT22Parser
from lexererr import *
from ASTGeneration import ASTGeneration
from StaticChecker import StaticChecker
from StaticError import *
from CodeGenerator import CodeGenerator
import subprocess

JASMIN_JAR = "./test/CodeGen/external/jasmin.jar"
TEST_DIR = "./test/testcases/"
SOL_DIR = "./test/"
Lexer = MT22Lexer
Parser = MT22Parser


class TestUtil:
    @staticmethod
    def makeSource(inputStr, inputfile):
        file = open(inputfile, "w")
        file.write(inputStr)
        file.close()
        return FileStream(inputfile)

class TestLexer:
    _DIR = './test/Lexer/'
    
    @staticmethod
    def test(input, expect, num):
        inputfile = TestUtil.makeSource(input, TestLexer._DIR + 'input/' + str(num) + ".txt")
        TestLexer.check(TestLexer._DIR + 'output/' + str(num) + ".txt", inputfile)
        dest = open(TestLexer._DIR + 'output/' + str(num) + ".txt", "r")
        line = dest.read()
        return line == expect

    @staticmethod
    def check(soldir, inputfile):
        dest = open(soldir, "w")
        lexer = Lexer(inputfile)
        try:
            TestLexer.printLexeme(dest, lexer)
        except (ErrorToken, UncloseString, IllegalEscape) as err:
            dest.write(err.message)
        finally:
            dest.close()

    @staticmethod
    def printLexeme(dest, lexer):
        tok = lexer.nextToken()
        if tok.type != Token.EOF:
            dest.write(tok.text+",")
            TestLexer.printLexeme(dest, lexer)
        else:
            dest.write("<EOF>")

class NewErrorListener(ConsoleErrorListener):
    INSTANCE = None

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        raise SyntaxException("Error on line " + str(line) +
                              " col " + str(column) + ": " + offendingSymbol.text)

NewErrorListener.INSTANCE = NewErrorListener()

class SyntaxException(Exception):
    def __init__(self, msg):
        self.message = msg

class TestParser:
    
    _DIR = './test/Parser/'
    
    @staticmethod
    def createErrorListener():
        return NewErrorListener.INSTANCE

    @staticmethod
    def test(input, expect, num):
        inputfile = TestUtil.makeSource(input, TestParser._DIR + 'input/' + str(num) + ".txt")
        TestParser.check(TestParser._DIR + 'output/' + str(num) + ".txt", inputfile)
        dest = open(TestParser._DIR + 'output/' + str(num) + ".txt", "r")
        line = dest.read()
        return line == expect
        
    @staticmethod
    def check(soldir, inputfile):
        dest = open(soldir, "w")
        lexer = Lexer(inputfile)
        listener = TestParser.createErrorListener()
        tokens = CommonTokenStream(lexer)
        parser = Parser(tokens)
        parser.removeErrorListeners()
        parser.addErrorListener(listener)
        try:
            parser.program()
            dest.write("successful")
        except SyntaxException as f:
            dest.write(f.message)
        except Exception as e:
            dest.write(str(e))
        finally:
            dest.close()

class TestAST:
    _DIR = './test/ASTGen/'
    
    @staticmethod
    def test(input, expect, num):
        inputfile = TestUtil.makeSource(input, TestAST._DIR + 'input/' + str(num) + ".txt")
        TestAST.check(TestAST._DIR + 'output/' + str(num) + ".txt", inputfile)
        dest = open(TestAST._DIR + 'output/' + str(num) + ".txt", "r")
        line = dest.read()
        return line == expect

    @staticmethod
    def check(soldir, inputfile):
        dest = open(soldir, "w")
        lexer = Lexer(inputfile)
        tokens = CommonTokenStream(lexer)
        parser = Parser(tokens)
        tree = parser.program()
        asttree = ASTGeneration().visit(tree)
        dest.write(str(asttree))
        dest.close()

class TestChecker:
    _DIR = './test/Check/'
    
    @staticmethod
    def test(input, expect, num):
        if type(input) is str:
            inputfile = TestUtil.makeSource(input, TestChecker._DIR + 'input/' + str(num) + ".txt")
            lexer = Lexer(inputfile)
            tokens = CommonTokenStream(lexer)
            parser = Parser(tokens)
            tree = parser.program()
            asttree = ASTGeneration().visit(tree)
        else:
            inputfile = TestUtil.makeSource(str(input), TestChecker._DIR + 'input/' + str(num) + ".txt")
            asttree = input
            
        TestChecker.check(TestChecker._DIR + 'output/' + str(num) + ".txt", asttree, num)
        dest = open(TestChecker._DIR + 'output/' + str(num) + ".txt", "r")
        line = dest.read()
        return line == expect

    @staticmethod
    def check(soldir, asttree, num):
        dest = open(soldir, "w")
        checker = StaticChecker(asttree)
        try:
            res = checker.check()
            dest.write(str(res) if res else "")
        except StaticError as e:
            dest.write(str(e))
        finally:
            dest.close()
        

class TestCodeGen():
    _DIR = './test/CodeGen/'
    
    @staticmethod
    def test(input, expect, num):
        if type(input) is str:
            inputfile = TestUtil.makeSource(input, TestCodeGen._DIR + 'input/' + str(num) + ".txt")
            lexer = Lexer(inputfile)
            tokens = CommonTokenStream(lexer)
            parser = Parser(tokens)
            tree = parser.program()
            asttree = ASTGeneration().visit(tree)
           
        else:
            inputfile = TestUtil.makeSource(str(input), TestCodeGen._DIR + 'input/' + str(num) + ".txt")
            asttree = input

        TestCodeGen.check(asttree, num)

        dest = open(TestCodeGen._DIR + 'output/' + str(num) + ".txt", "r")
        line = dest.read()
        return line == expect

    @staticmethod
    def check(asttree, num):
        codeGen = CodeGenerator()
        path = TestCodeGen._DIR + "file_j/input" +  str(num)
        if not os.path.isdir(path):
            os.mkdir(path)
            
        f = open(TestCodeGen._DIR + 'output/' + str(num) + ".txt", "w")
        try:
            codeGen.gen(asttree, path)

            subprocess.call("java -jar ./test/CodeGen/external/jasmin.jar -d ./test/CodeGen/file_j/input" + str(num) + " ./test/CodeGen/file_j/input" + str(num) + "/MT22.j", shell=True, stderr=subprocess.STDOUT)

            subprocess.run("cd test/CodeGen/file_j/input" + str(num) + " && java -cp ../../lib;. MT22", shell=True, stdout=f, timeout=10)
        except StaticError as e:
            f.write(str(e))
        except subprocess.TimeoutExpired:
            f.write("Time out\n")
        except subprocess.CalledProcessError as e:
            raise RuntimeError("command '{}' return with error (code {}): {}".format(
                e.cmd, e.returncode, e.output))
        finally:
            f.close()


