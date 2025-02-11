"""
 * Initial code for Assignment
 * Programming Language Principles
 * Author: Võ Tiến
 * Link FB : https://www.facebook.com/profile.php?id=100056605580171
 * Link Group : https://www.facebook.com/groups/211867931379013
 * Date: 06.19.2024
"""
import unittest
from TestUtils import TestCodeGen
from AST import *


class CheckCodeGenSuite(unittest.TestCase):
    
    def test1(self):
        input = """
            int a = 1;
        """
        expect = "VoTien\n"
        self.assertTrue(TestCodeGen.test(input, expect, 1))    
        
    def test2(self):
        input = """
            int a = 1;
        """
        expect = "VoTien1"
        self.assertTrue(TestCodeGen.test(input, expect, 2))    
