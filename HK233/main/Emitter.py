"""
 * Initial code for Assignment
 * Programming Language Principles
 * Author: Võ Tiến
 * Link FB : https://www.facebook.com/profile.php?id=100056605580171
 * Link Group : https://www.facebook.com/groups/211867931379013
 * Date: 06.19.2024
"""
from Utils import *
# from StaticCheck import *
# from StaticError import *
# import main.CodeGenerator as cgen
from MachineCode import JasminCode
from AST import *
from main.CodeGenError import *


class Emitter():
    def __init__(self, filename):
        self.filename = filename
        self.buff = list() 
        self.jvm = JasminCode() #! gọi quá

    def printout(self, in_):
        # in_: String
        self.buff.append(in_)
        
    def emitEPILOG(self):
        file = open(self.filename, "w")
        file.write(''.join(self.buff))
        file.close()    
        
        