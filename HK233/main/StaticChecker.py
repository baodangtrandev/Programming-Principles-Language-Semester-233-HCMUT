from AST import *
from Visitor import Visitor
from Utils import Utils
from StaticError import *

class Decleration:
    def __init__(self, name : str, typ : Type):
        self.name = name
        self.typ = typ
        
class VarDecleration(Decleration):
    def __init__(self, name : str, typ: Type):
        super().__init__(name, typ)
        
class ParamDecleration(Decleration):
    def __init__(self, name : str, typ: Type, out : bool = False, inherit : bool = False):
        super().__init__(name, typ)
        self.out = out
        self.inherit = inherit
class FuncDecleration(Decleration):
    def __init__(self, name : str, typ: Type, param, parent : None = None):
        super().__init__(name, typ)
        self.param = param
        self.parent = parent
class Storage():
    def __init__(self, symbol, inferType : Type = AutoType()):
        self.symbol = symbol 
        self.inferType = inferType
    
class StaticChecker(Visitor, Utils):
    def __init__(self,ast):
        self.ast = ast
        self.list_function = [
                FuncDecleration("readInteger", IntegerType(), []),
                FuncDecleration("readFloat", FloatType(), []),
                FuncDecleration("readBoolean", BooleanType(), []),
                FuncDecleration("readString", StringType(), []),
                FuncDecleration("printInteger", VoidType(), [ParamDecleration("printInteger", IntegerType())]),
                FuncDecleration("printFloat", VoidType(), [ParamDecleration("printFloat", FloatType())]),
                FuncDecleration("printBoolean", VoidType(), [ParamDecleration("printBoolean", BooleanType())]),
                FuncDecleration("printString", VoidType(), [ParamDecleration("printString", StringType())]),
            ]
        self.current_function = None
        self.has_return = False
        self.isReturn_block = False
        self.hasGlobalVariable = False
        self.isInNested_Block = False
        self.in_loop = 0

    def compare_Type(self, lhs : Type, rhs : Type):
        if type(lhs) is ArrayType and type(rhs) is ArrayType:
            if len(lhs.dimensions) != len(rhs.dimensions) or not self.compare_Type(lhs.typ, rhs.typ):
                return False
            for index in range(len(lhs.dimensions)):
                if lhs.dimensions[index] != rhs.dimensions[index]:
                    return False
            return True
        if type(lhs) in [FloatType] and type(rhs) in [IntegerType, FloatType]:
            return True
        return type(lhs) == type(rhs)

    def findInheritParam(self, name : str, parentFunction):
        if parentFunction is None:
            return None
        for param in parentFunction.param:
            if param.inherit == True and param.name == name:
                return param
        return self.findInheritParam(name, parentFunction.parent)
    def check(self):
        self.visit(self.ast,None)
    def visitIntegerLit(self, ast : IntegerLit, param : Storage): 
        return IntegerType()
    def visitFloatLit(self, ast : FloatLit, param : Storage): 
        return FloatType()
    def visitStringLit(self, ast : StringLit, param : Storage): 
        return StringType()
    def visitBooleanLit(self, ast : BooleanLit, param : Storage): 
        return BooleanType()

    def visitArrayLit(self, ast : ArrayLit, param : Storage):
        type_element_array = self.visit(ast.explist[0], param)
        for exp in ast.explist:
            type_element = self.visit(exp, param)
            if not self.compare_Type(type_element_array, type_element):
                raise IllegalArrayLiteral(ast)
        if type(type_element_array) is not ArrayType:
            return ArrayType([len(ast.explist)], type_element_array)
        return ArrayType([len(ast.explist)] + type_element_array.dimensions, type_element_array.typ)

    def visitId(self, ast : Id, param : Storage):
        if self.hasGlobalVariable:
            for row in param.symbol[:-1]:
                if ast.name in [var.name for var in row]:
                    id = self.lookup(ast.name, row, lambda x: x.name)
                    if type(id.typ) is AutoType:
                        id.typ = param.inferType
                    return id.typ  
        else:
            for row in param.symbol:
                if ast.name in [var.name for var in row]:
                    id = self.lookup(ast.name, row, lambda x: x.name)
                    if type(id.typ) is AutoType:
                        id.typ = param.inferType
                    return id.typ
        param_inherit = None
        if len(param.symbol) != 1:
            param_inherit = self.findInheritParam(ast.name, self.current_function.parent)
        if param_inherit is not None:
            if type(param_inherit.typ) is AutoType:
                param_inherit.typ = param.inferType
            return param_inherit.typ
        
        if self.hasGlobalVariable:
            global_variable = param.symbol[-1]
            if ast.name in [var.name for var in global_variable]:
                    id = self.lookup(ast.name, global_variable, lambda x: x.name)
                    if type(id.typ) is AutoType:
                        id.typ = param.inferType
                    return id.typ
            
        raise Undeclared(Identifier(), ast.name)

    def visitFuncCall(self, ast : FuncCall, param : Storage):
        if ast.name not in [func_decl.name for func_decl in self.list_function]:
            raise Undeclared(Function(), ast.name)
        
        func_decl = self.lookup(ast.name, self.list_function, lambda x: x.name)
        if type(func_decl.typ) is VoidType:
            raise TypeMismatchInExpression(ast)
        if len(func_decl.param) != len(ast.args):
            raise TypeMismatchInExpression(ast)
        for i in range(len(ast.args)):
            lhs_type = func_decl.param[i].typ
            rhs_type = self.visit(ast.args[i], Storage(param.symbol, lhs_type))
            if type(lhs_type) is AutoType:
                func_decl.param[i].typ = rhs_type
            elif not self.compare_Type(lhs_type, rhs_type):
                raise TypeMismatchInExpression(ast)
        if type(func_decl.typ) is AutoType:
            func_decl.typ = param.inferType
            return func_decl.typ
        else:
            return func_decl.typ

    def visitCallStmt(self, ast : CallStmt, param : Storage):
        if ast.name not in [func_decl.name for func_decl in self.list_function]:
            raise Undeclared(Function(), ast.name)
        func_decl = self.lookup(ast.name, self.list_function, lambda x: x.name)
        if len(func_decl.param) != len(ast.args):
            raise TypeMismatchInStatement(ast)
        for i in range(len(ast.args)):
            lhs_type = func_decl.param[i].typ
            rhs_type = self.visit(ast.args[i], Storage(param.symbol, lhs_type))
            if type(lhs_type) is AutoType:
                func_decl.param[i].typ = rhs_type
            elif not self.compare_Type(lhs_type, rhs_type):
                raise TypeMismatchInStatement(ast)

    def visitAssignStmt(self,ast : AssignStmt, param : Storage):
        lhs_type = self.visit(ast.lhs, param)
        rhs_type = self.visit(ast.rhs, Storage(param.symbol, lhs_type))
        if type(lhs_type) is AutoType:
            lhs_type = self.visit(ast.lhs, Storage(param.symbol, rhs_type))
        elif not self.compare_Type(lhs_type, rhs_type):
            raise TypeMismatchInStatement(ast)

    def visitBlockStmt(self, ast : BlockStmt, param : Storage):
        is_return = self.isReturn_block
        env = [[]] + param.symbol
        for item in ast.body:
            if self.isReturn_block and type(item) is ReturnStmt:
                continue
            if not is_return and type(item) is ReturnStmt:
                self.isReturn_block = True
            self.visit(item, Storage(env, AutoType()))
        self.isReturn_block = is_return

    def visitIfStmt(self, ast : IfStmt, param : Storage):
        lhs_type = BooleanType()
        rhs_type = self.visit(ast.cond, Storage(param.symbol, lhs_type))
        if not self.compare_Type(lhs_type, rhs_type):
            raise TypeMismatchInStatement(ast)
        
        self.visit(ast.tstmt, param)
        if ast.fstmt:
            self.visit(ast.fstmt, param)

    def visitForStmt(self, ast : ForStmt, param : Storage):
        self.in_loop = self.in_loop + 1
        lhs_type_init = self.visit(ast.init.lhs, Storage(param.symbol, IntegerType()))
        rhs_type_init = self.visit(ast.init.rhs, Storage(param.symbol, IntegerType()))
        if type(lhs_type_init) is not IntegerType or type(rhs_type_init) is not IntegerType:
            raise TypeMismatchInStatement(ast)
        if not self.compare_Type(lhs_type_init, rhs_type_init):
            raise TypeMismatchInStatement(ast)
        
        lhs_type_condition = BooleanType()
        rhs_type_condition = self.visit(ast.cond, Storage(param.symbol, lhs_type_condition))
        if not self.compare_Type(lhs_type_condition, rhs_type_condition):
            raise TypeMismatchInStatement(ast)
        
        lhs_type_update = self.visit(ast.upd, Storage(param.symbol, IntegerType()))
        rhs_type_update = self.visit(ast.upd, Storage(param.symbol, IntegerType()))
        if type(lhs_type_update) is not IntegerType or type(rhs_type_update) is not IntegerType:
            raise TypeMismatchInStatement(ast)
        if not self.compare_Type(lhs_type_update, rhs_type_update):
            raise TypeMismatchInStatement(ast)
        self.visit(ast.stmt, param)
        self.in_loop = self.in_loop -  1

    def visitWhileStmt(self, ast : WhileStmt, param : Storage):
        self.in_loop = self.in_loop + 1
        lhs_type_condition = BooleanType()
        rhs_type_condition = self.visit(ast.cond, Storage(param.symbol, lhs_type_condition))
        if not self.compare_Type(lhs_type_condition, rhs_type_condition):
            raise TypeMismatchInStatement(ast)

        self.visit(ast.stmt, param)
        self.in_loop = self.in_loop - 1        

    def visitDoWhileStmt(self, ast : DoWhileStmt, param : Storage):
        self.in_loop += 1
        lhs_type_condition = BooleanType()
        rhs_type_condition = self.visit(ast.cond, Storage(param.symbol, lhs_type_condition))
        if not self.compare_Type(lhs_type_condition, rhs_type_condition):
            raise TypeMismatchInStatement(ast)
        self.visit(ast.stmt, param)
        self.in_loop -= 1    

    def visitBreakStmt(self, ast : BreakStmt, param : Storage):
        if self.in_loop <= 0: raise MustInLoop(ast)

    def visitContinueStmt(self, ast : ContinueStmt, param : Storage):
        if self.in_loop <= 0: raise MustInLoop(ast)

    def visitReturnStmt(self, ast : ReturnStmt, param : Storage):
        self.has_return = True
        lhs_type_function = self.current_function.typ
        rhs_type_return = self.visit(ast.expr, Storage(param.symbol, lhs_type_function)) if ast.expr else VoidType()
        if type(lhs_type_function) is AutoType:
            lhs_type_function = rhs_type_return
            self.current_function.typ = rhs_type_return
        if not self.compare_Type(lhs_type_function, rhs_type_return):
            raise TypeMismatchInStatement(ast)

    def visitBinExpr(self, ast : BinExpr, param : Storage):
        if ast.op in ['-', '+', '*', '/']:
            infer_type = IntegerType() if type(param.inferType) is not FloatType else param.inferType

            type_left_expr = self.visit(ast.left, Storage(param.symbol, infer_type))
            type_right_expr = self.visit(ast.right, Storage(param.symbol, infer_type))

            if type(type_left_expr) is not IntegerType and type(type_left_expr) is not FloatType:
                raise TypeMismatchInExpression(ast)
            if type(type_right_expr) is not IntegerType and type(type_right_expr) is not FloatType:
                raise TypeMismatchInExpression(ast)
            
            return FloatType() if type(type_left_expr) is FloatType or type(type_right_expr) is FloatType else IntegerType()
        elif ast.op in ['&&', '||']:
            type_left_expr = self.visit(ast.left, Storage(param.symbol, BooleanType()))
            type_right_expr = self.visit(ast.right, Storage(param.symbol, BooleanType()))
            if type(type_left_expr) is not BooleanType or type(type_right_expr) is not BooleanType:
                raise TypeMismatchInExpression(ast)
            return BooleanType()
        elif ast.op in ['==', '!=']:
            infer_type = IntegerType() if type(param.inferType) is not BooleanType else param.inferType
            type_left_expr = self.visit(ast.left, Storage(param.symbol, infer_type))
            type_right_expr = self.visit(ast.right, Storage(param.symbol, infer_type))
            if type(type_left_expr) is not IntegerType and type(type_left_expr) is not BooleanType:
                raise TypeMismatchInExpression(ast)
            if type(type_right_expr) is not IntegerType and type(type_right_expr) is not BooleanType:
                raise TypeMismatchInExpression(ast)
            return BooleanType()
        elif ast.op in ['<', '<=', '>', '>=']:
            infer_type = IntegerType() if type(param.inferType) is not FloatType else param.inferType

            type_left_expr = self.visit(ast.left, Storage(param.symbol, infer_type))
            type_right_expr = self.visit(ast.right, Storage(param.symbol, infer_type))

            if type(type_left_expr) is not IntegerType and type(type_left_expr) is not FloatType:
                raise TypeMismatchInExpression(ast)
            if type(type_right_expr) is not IntegerType and type(type_right_expr) is not FloatType:
                raise TypeMismatchInExpression(ast)
            return BooleanType()
        elif ast.op in ['%']:
            type_left_expr = self.visit(ast.left, Storage(param.symbol, IntegerType()))
            type_right_expr = self.visit(ast.right, Storage(param.symbol, IntegerType()))
            if type(type_left_expr) is not IntegerType or type(type_right_expr) is not IntegerType:
                raise TypeMismatchInExpression(ast)
            return IntegerType()
        elif ast.op in ['::']:
            type_left_expr = self.visit(ast.left, Storage(param.symbol, StringType()))
            type_right_expr = self.visit(ast.right, Storage(param.symbol, StringType()))
            
            if type(type_left_expr) is not StringType or type(type_right_expr) is not StringType:
                raise TypeMismatchInExpression(ast)
            return StringType()
        else:
            raise TypeMismatchInExpression(ast)
  
    def visitUnExpr(self, ast : UnExpr, param : Storage):
        if ast.op in ['-','+']:
            infer_type = IntegerType() if type(param.inferType) is not FloatType else param.inferType
            type_val = self.visit(ast.val, Storage(param.symbol, infer_type))
            if type(type_val) is not IntegerType and type(type_val) is not FloatType:
                raise TypeMismatchInExpression(ast)
            return FloatType() if type(type_val) is FloatType else IntegerType()
        elif ast.op in ['!']:
            type_val = self.visit(ast.val, Storage(param.symbol, BooleanType()))
            if type(type_val) is not BooleanType:
                raise TypeMismatchInExpression(ast)
            return BooleanType()
        else:
            raise TypeMismatchInExpression(ast)
  
    def visitArrayCell(self, ast : ArrayCell, param : Storage):
        id_type = self.visit(Id(ast.name), param)
        if type(id_type) is not ArrayType:
            raise TypeMismatchInExpression(ast)
        for i in ast.cell:
            element_type = self.visit(i, Storage(param.symbol, IntegerType()))
            if not self.compare_Type(element_type, IntegerType()):
                raise TypeMismatchInExpression(ast)
        if len(id_type.dimensions) == len(ast.cell):
            return id_type.typ
        return ArrayType(id_type.dimensions[len(ast.cell):], id_type.typ)
   
    def visitParamDecl(self, ast : ParamDecl, list_param):
        for param in list_param:
            if param.name == ast.name:
                raise Redeclared(Parameter(), ast.name)        

        list_param.append(ParamDecleration(ast.name, ast.typ, ast.out, ast.inherit)) 

    def visitVarDecl(self, ast : VarDecl, param : Storage):
        if self.lookup(ast.name, param.symbol[0], lambda x: x.name) is not None:
            raise Redeclared(Variable(), ast.name)
        
        if self.current_function is not None and not self.isInNested_Block:
            for item in self.current_function.param:
                if item.name == ast.name:
                    raise Redeclared(Variable(), ast.name)
        
        param.symbol[0].append(VarDecleration(ast.name, ast.typ))

        if type(ast.typ) is AutoType and ast.init is None:
            raise Invalid(Variable(), ast.name)
        
        if ast.init is None:
            return
        
        typeLHS = ast.typ
        if type(typeLHS) is AutoType:
            typeRHS = self.visit(ast.init, Storage(param.symbol, typeLHS))
            for item in param.symbol[0]:
                if item.name == ast.name:
                    item.typ = typeRHS
                    break
        else: 
            typeRHS = self.visit(ast.init, Storage(param.symbol, typeLHS))
            if not self.compare_Type(typeLHS, typeRHS):
                raise TypeMismatchInVarDecl(ast)
     
    def visitFuncDecl(self, ast : FuncDecl, param : Storage):
        for item in self.list_function:
            if item.name == ast.name:
                self.current_function = item
                break      
        
        for parameter in ast.params:
            param_inherit = self.findInheritParam(parameter.name, self.current_function.parent)
            if param_inherit is not None and param_inherit.name == parameter.name:
                raise Invalid(Parameter(), parameter.name)

        list_stmt_in_block_function =  ast.body.body
        if self.current_function.parent:
            if list_stmt_in_block_function == []:
                if self.current_function.parent.param != []:
                    raise InvalidStatementInFunction(ast.name)
            else:
                if self.current_function.parent.param != []:
                    if not isinstance(list_stmt_in_block_function[0], CallStmt):
                        raise InvalidStatementInFunction(ast.name)
                    if list_stmt_in_block_function[0].name == "preventDefault" and list_stmt_in_block_function[0].args == []:
                        list_stmt_in_block_function = list_stmt_in_block_function[1:]
                    elif list_stmt_in_block_function[0].name == "super":
                        if len(self.current_function.parent.param) != len(list_stmt_in_block_function[0].args):
                            raise TypeMismatchInExpression()
                        for index in range(len(list_stmt_in_block_function[0].args)):
                            lhs = self.current_function.parent.param[index].typ
                            rhs = self.visit(list_stmt_in_block_function[0].args[index], Storage(param.symbol, lhs))
                            if type(lhs) is AutoType:
                                self.current_function.parent.param[index].typ = rhs
                            elif not self.compare_Type(lhs, rhs):
                                raise TypeMismatchInExpression(list_stmt_in_block_function[0].args[index])
                        list_stmt_in_block_function = list_stmt_in_block_function[1:]
                else: 
                    if list_stmt_in_block_function[0].name == "preventDefault" and isinstance(list_stmt_in_block_function[0], CallStmt):
                        if list_stmt_in_block_function[0].args != []:
                            raise TypeMismatchInExpression( list_stmt_in_block_function[0].args[0])
                        list_stmt_in_block_function = list_stmt_in_block_function[1:]
                    elif list_stmt_in_block_function[0].name == "super" and isinstance(list_stmt_in_block_function[0], CallStmt):
                        if len(self.current_function.parent.param) != len(list_stmt_in_block_function[0].args):
                            raise TypeMismatchInExpression( list_stmt_in_block_function[0].args[0])
                        list_stmt_in_block_function = list_stmt_in_block_function[1:]
                    
        self.has_return = False
        
        param = Storage([[]]+ [self.current_function.param] + param.symbol, AutoType())
        
        for decl_or_stmt in list_stmt_in_block_function:
            if self.isReturn_block and type(decl_or_stmt) is ReturnStmt:
                continue
            if not self.isReturn_block and type(decl_or_stmt) is ReturnStmt:
                self.isReturn_block = True
            if type(decl_or_stmt) is BlockStmt:
                self.isInNested_Block = True   
            self.visit(decl_or_stmt, param)
            self.isInNested_Block = False
            
        if not self.has_return and type(self.current_function.typ) is AutoType:
            self.current_function.typ = VoidType()
        self.current_function = None
        self.isReturn_block = False

    def visitProgram(self,ast : Program, param):
        function_names = ["readInteger", "readFloat", "readBoolean", "readString", "printInteger", "printFloat", "printBoolean", "printString"]
        for x in ast.decls:
            if x.name in function_names:
                if isinstance(x, VarDecl):
                    raise Redeclared(Variable(), x.name)
                else:
                    raise Redeclared(Function(), x.name)
            else:
                function_names += [x.name]
            
            if isinstance(x, FuncDecl):
                list_param = []
                for parameter in x.params:
                    self.visit(parameter, list_param)
                self.list_function.append(FuncDecleration(x.name, x.return_type, list_param,None))
   
        start_index = 8
        
        for decl in ast.decls:
            if isinstance(decl, FuncDecl) and decl.inherit is not None: 
                parent = self.lookup(decl.inherit, self.list_function, lambda x: x.name) 
                if parent is None:
                    raise Undeclared(Function(), decl.inherit) 
                else:
                    children = self.lookup(decl.name, self.list_function[start_index:], lambda x: x.name) #
                    children.parent = parent 
            else:
                self.hasGlobalVariable = True

        param = Storage([[]], AutoType())
        for decl in ast.decls:
            self.visit(decl, param)
        main_func = self.lookup("main", self.list_function, lambda x: x.name)
        if main_func is None or (type(main_func.typ) is not VoidType and type(main_func.typ) is not AutoType) or main_func.param != []:
            raise NoEntryPoint()