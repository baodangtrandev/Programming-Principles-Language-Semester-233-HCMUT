"""
 * Initial code for Assignment
 * Programming Language Principles
 * Author: Võ Tiến
 * Link FB : https://www.facebook.com/profile.php?id=100056605580171
 * Link Group : https://www.facebook.com/groups/211867931379013
 * Date: 06.19.2024
"""
from Emitter import Emitter
from functools import reduce

from Frame import Frame
from abc import ABC
from Visitor import *
from AST import *
from Utils import *
from CodeGenError import *



class CodeGenerator:
    
    def gen(self, ast, path):
        gc = CodeGenVisitor(ast, path)
        gc.visit(ast, None)
        
class CodeGenVisitor(Visitor):
    def __init__(self, astTree, path):
        self.astTree = astTree
        self.emit = Emitter(path + "/MT22.j")

        
    def visitProgram(self, ast:Program, o):
        
        self.emit.printout("""

; MT22.j

.bytecode 61.0
.source MT22.java
.class public MT22
.super java/lang/Object

.method public <init>()V
  .limit stack 1
  .limit locals 1
  .line 6
  0: aload_0
  1: invokespecial java/lang/Object/<init>()V
  4: return
.end method

.method public static main([Ljava/lang/String;)V
  .limit stack 2
  .limit locals 1
  .line 8
  0: getstatic java/lang/System/err Ljava/io/PrintStream;
  3: ldc "MT22"
  5: invokestatic io/writeString(Ljava/lang/String;)V
  .line 9
  8: return
.end method
                           """)
        
        
        self.emit.emitEPILOG()
    
