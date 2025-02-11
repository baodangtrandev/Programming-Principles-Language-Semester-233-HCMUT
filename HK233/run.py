

import sys
import os
import glob
import subprocess
import unittest
import shutil
import platform
from antlr4 import *

for path in ['./test/', './test/Lexer/', './test/Parser/', './test/ASTGen/',  './test/Check/', './test/CodeGen/',  './main/']:
    sys.path.append(path)
ANTLR_JAR = os.environ.get('ANTLR_JAR')
TARGET_DIR = 'target/main'
GENERATE_DIR = 'main/parser'
ARGV = ""
def main(argv):

    if len(argv) < 1:
        printUsage()
    elif argv[0] == 'gen':
        # java -jar ../libs/antlr/antlr-4.9.2-complete.jar -o target -no-listener -visitor main/MT22.g4
        subprocess.run(["java", "-jar", ANTLR_JAR, "-o", "target",
                       "-no-listener", "-visitor", "main/MT22.g4"])
    elif argv[0] == 'clear':
        folders = ["ASTGen/input", "ASTGen/output",
                  "Check/input", "Check/output", 
                  "CodeGen/input", "CodeGen/output",
                  "Lexer/input", "Lexer/output", 
                  "Parser/input", "Parser/output"]
        
        folder_pycache = ["main", "target/main", "target", "test", 'test/Lexer/', 'test/Parser/', 'test/ASTGen/',  'test/Check/', 'test/CodeGen/']
        for folder in folder_pycache:
            folder_path = folder + "/__pycache__"
            if os.path.exists(folder_path):
                shutil.rmtree(folder_path)  


        for folder in folders:
            folder_path = "test/" + folder

            if not os.path.exists(folder_path):
                os.makedirs(folder_path)
            else:
                files = os.listdir(folder_path)
                for file in files:
                    file_path = os.path.join(folder_path, file)
                    try:
                        if os.path.isfile(file_path) or os.path.islink(file_path):
                            os.unlink(file_path)
                        elif os.path.isdir(file_path):
                            shutil.rmtree(file_path)
                    except Exception as e:
                        print(f'Failed to delete {file_path}. Reason: {e}') 
        
        print("Clear full file input/ouput in test")



                              
    elif argv[0] == 'test':
        if not os.path.isdir(TARGET_DIR):
            subprocess.run(["java", "-jar", ANTLR_JAR, "-o", "target",
                        "-no-listener", "-visitor", "main/MT22.g4"])
        if not (TARGET_DIR) in sys.path:
            sys.path.append(TARGET_DIR)
            sys.path.append("target")
        if len(argv) < 2:
            printUsage()
        if len(argv) == 2:
            if argv[1] == 'LexerSuite':
                from LexerSuite import LexerSuite
                getAndTest(argv[1], LexerSuite)
            elif argv[1] == 'ParserSuite':
                from ParserSuite import ParserSuite
                getAndTest(argv[1], ParserSuite)
            elif argv[1] == 'ASTGenSuite':
                from ASTGenSuite import ASTGenSuite
                getAndTest(argv[1], ASTGenSuite)
            elif argv[1] == 'CheckerSuite':
                from CheckerSuite import CheckerSuite
                getAndTest(argv[1], CheckerSuite)
            elif argv[1] == 'CodeGenSuite':
                from CodeGenSuite import CheckCodeGenSuite
                getAndTest(argv[1], CheckCodeGenSuite)
            else:
                printUsage()
        else:
            if argv[1] == 'LexerSuite':
                from LexerSuite import LexerSuite
                getAndTestFucntion(argv[1] + " - " + argv[2], LexerSuite, argv[2])
            elif argv[1] == 'ParserSuite':
                from ParserSuite import ParserSuite
                getAndTestFucntion(argv[1] + " - " + argv[2], ParserSuite, argv[2])
            elif argv[1] == 'ASTGenSuite':
                from ASTGenSuite import ASTGenSuite
                getAndTestFucntion(argv[1] + " - " + argv[2], ASTGenSuite, argv[2])
            elif argv[1] == 'CheckerSuite':
                from CheckSuite import CheckSuite
                getAndTestFucntion(argv[1] + " - " + argv[2], CheckSuite, argv[2])
            elif argv[1] == 'CodeGenSuite':
                from CodeGenSuite import CheckCodeGenSuite
                getAndTestFucntion(argv[1] + " - " + argv[2], CheckCodeGenSuite, argv[2])
            else:
                printUsage()
    else:
        printUsage()


def getAndTest(argv, cls):
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(cls)
    test(argv, suite)

def getAndTestFucntion(argv, cls, nameFunction):
    suite = unittest.TestSuite()
    suite.addTest(cls(nameFunction))
    test(argv, suite)

def generate_repeating_sequence(size):
    base_sequence = "1234567890"
    repeated_sequence = (base_sequence * ((size // len(base_sequence)) + 1))[:size]
    return repeated_sequence

def printMT22(argv, stream, result):
    # print(f'{argv} - Assignment - PPL - HK233 - VO TIEN')
    # print("Vo Tien : https://www.facebook.com/profile.php?id=100056605580171")
    print('Tests run ', result.testsRun)
    stream.seek(0)
    expect = stream.readline()
    print(generate_repeating_sequence(len(expect) - 1))
    print(expect , end='')
    listErrors = []
    listFailures = []
    for i in range(1, len(expect)):
        if expect[i - 1] == 'E' : listErrors += [i]
        if expect[i - 1] == 'F' : listFailures += [i]
    
    # Convert lists to comma-separated strings
    errors_str = ", ".join(map(str, listErrors))
    failures_str = ", ".join(map(str, listFailures))

    # Print the lists in the desired format
    if len(listFailures) + len(listErrors) :
        Pass =  100.0 *( 1 - (len(listFailures) + len(listErrors)) * 1.0 / (len(expect) - 1))
        print(f"Pass     : {Pass} %")
        print(f"Errors   : {errors_str}")
        print(f"Failures : {failures_str}")
    else :
        print(f"Pass full 10.")
    

def test(argv, suite):
    from pprint import pprint
    from io import StringIO
    stream = StringIO()
    runner = unittest.TextTestRunner(stream=stream)
    result = runner.run(suite)
    print('Tests run ', result.testsRun)
    print('Errors ', result.errors)
    pprint(result.failures)
    stream.seek(0)
    print('Test output\n', stream.read())
    printMT22(argv, stream, result)


def printUsage():
    print("python3/python run.py gen")
    print("python3/python run.py test LexerSuite")
    print("python3/python run.py test ParserSuite")
    print("python3/python run.py test ASTGenSuite")
    print("python3/python run.py test CheckerSuite")
    print("python3/python run.py test CodeGenSuite")


if __name__ == "__main__":
    main(sys.argv[1:])
