from MT22Visitor import MT22Visitor
from MT22Parser import MT22Parser
from AST import *

class ASTGeneration(MT22Visitor):
#type_: BOOLEAN | INTEGER | FLOAT | STRING | AUTO | array_type; int a = 5 integer type -> object IntegerType()
    def visitType_(self, ctx: MT22Parser.Type_Context):
        if ctx.INTEGER():
            return IntegerType()
        elif ctx.FLOAT():
            return FloatType()
        elif ctx.BOOLEAN():
            return BooleanType()
        elif ctx.STRING():
            return StringType()
        elif ctx.AUTO():
            return AutoType()
        else:
            return self.visit(ctx.array_type())

#type_n_auto: BOOLEAN | INTEGER | FLOAT | STRING;
    def visitType_n_auto(self, ctx: MT22Parser.Type_n_autoContext):
        if ctx.INTEGER():
            return IntegerType()
        elif ctx.FLOAT():
            return FloatType()
        elif ctx.BOOLEAN():
            return BooleanType()
        else:
            return StringType()

#array_type: ARRAY LSB dimensions RSB OF type_n_auto;
    def visitArray_type(self, ctx: MT22Parser.Array_typeContext):
        return ArrayType(self.visit(ctx.dimensions()), self.visit(ctx.type_n_auto()))

#dimensions: INTLIT COMMA dimensions | INTLIT;
    def visitDimensions(self, ctx: MT22Parser.DimensionsContext):
        if ctx.getChildCount() == 1:
            return [int(ctx.INTLIT().getText())]
        return [int(ctx.INTLIT().getText())] + self.visit(ctx.dimensions())

    # Expression
#factor: INTLIT | FLOATLIT | BOOLEAN_LIT| STRING_LIT | IDENTIFIER
#| function_call | array_literal;
    def visitFactor(self, ctx: MT22Parser.FactorContext):
        if ctx.IDENTIFIER():
            return Id(ctx.IDENTIFIER().getText())
        elif ctx.INTLIT():
            return IntegerLit(int(ctx.INTLIT().getText()))
        elif ctx.FLOATLIT():
            return FloatLit(float(ctx.FLOATLIT().getText()))
        elif ctx.BOOLEAN_LIT():
            return BooleanLit(ctx.BOOLEAN_LIT().getText() == "true")
        elif ctx.STRING_LIT():
            return StringLit(ctx.STRING_LIT().getText())
        elif ctx.function_call():
            return self.visit(ctx.function_call())
        else:
            return self.visit(ctx.array_literal())

#expression8: LP expression RP | factor;
    def visitExpression8(self, ctx: MT22Parser.Expression8Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.factor())
        return self.visit(ctx.expression())

#expression7: index_operator | expression8;
    def visitExpression7(self, ctx: MT22Parser.Expression7Context):
        if ctx.index_operator():
            return self.visit(ctx.index_operator())
        return self.visit(ctx.expression8())

#expression6: (MINUS | ADD) expression6 | expression7;
    def visitExpression6(self, ctx: MT22Parser.Expression6Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expression7())
        else:
            return UnExpr(ctx.getChild(0).getText(), self.visit(ctx.expression6()))

#expression5: NOT expression5 | expression6;
    def visitExpression5(self, ctx: MT22Parser.Expression5Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expression6())
        return UnExpr(ctx.getChild(0).getText(), self.visit(ctx.expression5()))

#expression4: expression4 (MUL | DIV | MOD) expression5 | expression5;
    def visitExpression4(self, ctx: MT22Parser.Expression4Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expression5())
        return BinExpr(ctx.getChild(1).getText(), self.visit(ctx.expression4()), self.visit(ctx.expression5()))

#expression3: expression3 (ADD | MINUS) expression4 | expression4;
    def visitExpression3(self, ctx: MT22Parser.Expression3Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expression4())
        return BinExpr(ctx.getChild(1).getText(), self.visit(ctx.expression3()), self.visit(ctx.expression4()))

#expression2: expression2 (AND | OR) expression3 | expression3;
    def visitExpression2(self, ctx: MT22Parser.Expression2Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expression3())
        return BinExpr(ctx.getChild(1).getText(), self.visit(ctx.expression2()), self.visit(ctx.expression3()))

#expression1: expression2 (EQUAL | NOT_EQUAL | LESS_THAN | GREATER_THAN | LESS_EQUAL | GREATER_EQUAL) expression2 | expression2;
    def visitExpression1(self, ctx: MT22Parser.Expression1Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expression2(0))
        return BinExpr(ctx.getChild(1).getText(), self.visit(ctx.expression2(0)), self.visit(ctx.expression2(1)))
    
#expression: expression1 TWO_COLON expression1 | expression1;
    def visitExpression(self, ctx: MT22Parser.ExpressionContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expression1(0))
        return BinExpr(ctx.getChild(1).getText(), self.visit(ctx.expression1(0)), self.visit(ctx.expression1(1)))

#array_literal: LB exp_list RB;
    def visitArray_literal(self, ctx: MT22Parser.Array_literalContext):
        return ArrayLit(self.visit(ctx.exp_list()))

#exp_list: exp_prime | ;
    def visitExp_list(self, ctx: MT22Parser.Exp_listContext):
        if ctx.exp_prime():
            return self.visit(ctx.exp_prime())
        else:
            return []

#exp_prime: expression COMMA exp_prime | expression;
    def visitExp_prime(self, ctx: MT22Parser.Exp_primeContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.expression())]
        return [self.visit(ctx.expression())] + self.visit(ctx.exp_prime())

#index_operator: IDENTIFIER LSB (exp_prime) RSB;
    def visitIndex_operator(self, ctx: MT22Parser.Index_operatorContext):
        return ArrayCell(ctx.IDENTIFIER().getText(), self.visit(ctx.exp_prime()))

    # Statement
#function_call: IDENTIFIER LP exp_list RP;
    def visitFunction_call(self, ctx: MT22Parser.Function_callContext):
        return FuncCall(ctx.IDENTIFIER().getText(), self.visit(ctx.exp_list()))

#call_statement: function_call SEMI;
    def visitCall_statement(self, ctx: MT22Parser.Call_statementContext):
        return CallStmt(ctx.IDENTIFIER().getText(), self.visit(ctx.exp_list()))

#return_statement: RETURN expression? SEMI;
    def visitReturn_statement(self, ctx: MT22Parser.Return_statementContext):
        if ctx.expression():
            return ReturnStmt(self.visit(ctx.expression()))
        return ReturnStmt(None)

#continue_statement: CONTINUE SEMI;
    def visitContinue_statement(self, ctx: MT22Parser.Continue_statementContext):
        return ContinueStmt()

#break_statement: BREAK SEMI;
    def visitBreak_statement(self, ctx: MT22Parser.Break_statementContext):
        return BreakStmt()

#dowhile_statement: DO block_statement WHILE LP expression RP SEMI;
    def visitDowhile_statement(self, ctx: MT22Parser.Dowhile_statementContext):
        return DoWhileStmt(self.visit(ctx.expression()), self.visit(ctx.block_statement()))

#while_statement: WHILE LP expression RP statement;
    def visitWhile_statement(self, ctx: MT22Parser.While_statementContext):
        return WhileStmt(self.visit(ctx.expression()), self.visit(ctx.statement()))

#for_statement: FOR LP assign_statement COMMA expression COMMA  expression RP statement;
    def visitFor_statement(self, ctx: MT22Parser.For_statementContext):
        assignStmt = AssignStmt(self.visit(ctx.lhs()), self.visit(ctx.expression(0)))
        return ForStmt(assignStmt, self.visit(ctx.expression(1)), self.visit(ctx.expression(2)), self.visit(ctx.statement()))
    

#if_statement: IF LP expression RP statement (ELSE statement)?;
    def visitIf_statement(self, ctx: MT22Parser.If_statementContext):
        if ctx.ELSE():
            return IfStmt(self.visit(ctx.expression()), self.visit(ctx.statement(0)), self.visit(ctx.statement(1)))
        return IfStmt(self.visit(ctx.expression()), self.visit(ctx.statement(0)))

#lhs: IDENTIFIER LSB exp_prime RSB | IDENTIFIER;
    def visitLhs(self, ctx: MT22Parser.LhsContext):
        if ctx.getChildCount() == 1:
            return Id(ctx.IDENTIFIER().getText())
        return ArrayCell(ctx.IDENTIFIER().getText(), self.visit(ctx.exp_prime()))

#assign_statement: lhs ASSIGN expression SEMI;
    def visitAssign_statement(self, ctx: MT22Parser.Assign_statementContext):
        return AssignStmt(self.visit(ctx.lhs()), self.visit(ctx.expression()))

#statement_prime: statement statement_prime | statement;
    def visitStatement_prime(self, ctx: MT22Parser.Statement_primeContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.statement())]
        return [self.visit(ctx.statement())] + self.visit(ctx.statement_prime())

#statement_list: statement_prime | ;
    def visitStatement_list(self, ctx: MT22Parser.Statement_listContext):
        if ctx.getChildCount() == 0:
            return []
        return self.visit(ctx.statement_prime())
    
#blk_item: (var_declaration | statement)
    def visitBlk_item(self, ctx: MT22Parser.Blk_itemContext):
        if ctx.var_declaration():
            return self.visit(ctx.var_declaration())
        return [self.visit(ctx.statement())]

#blk_items: blk_item blk_items | ;
    def visitBlk_items(self, ctx: MT22Parser.Blk_itemsContext):
        if ctx.blk_items():
            return self.visit(ctx.blk_item()) + self.visit(ctx.blk_items())
        return []

#block_statement: LB blk_items RB;
    def visitBlock_statement(self, ctx: MT22Parser.Block_statementContext):
        return BlockStmt(self.visit(ctx.blk_items()))

#statement: var_declaration | assign_statement | if_statement | for_statement | while_statement | dowhile_statement 
#| break_statement | continue_statement | return_statement | call_statement | block_statement;
    def visitStatement(self, ctx: MT22Parser.StatementContext):
        return self.visit(ctx.getChild(0))

    # Parameter vs Function
#inherit_function: INHERIT IDENTIFIER;
    def visitInherit_function(self, ctx: MT22Parser.Inherit_functionContext):
        return ctx.IDENTIFIER().getText()

#return_type: BOOLEAN | INTEGER | FLOAT | STRING | VOID | AUTO | array_type;
    def visitReturn_type(self, ctx: MT22Parser.Return_typeContext):
        if ctx.INTEGER():
            return IntegerType()
        elif ctx.FLOAT():
            return FloatType()
        elif ctx.BOOLEAN():
            return BooleanType()
        elif ctx.STRING():
            return StringType()
        elif ctx.AUTO():
            return AutoType()
        elif ctx.array_type():
            return self.visit(ctx.array_type())
        else:
            return VoidType()
        

    # Return list a function declaration
#function_declaration: IDENTIFIER COLON FUNCTION return_type LP parameter_list RP inherit_function? block_statement;
    def visitFunction_declaration(self, ctx: MT22Parser.Function_declarationContext):
       # print("-----------------------------------------------")
        if ctx.inherit_function():
            return [FuncDecl(ctx.IDENTIFIER().getText(), self.visit(ctx.return_type()), self.visit(ctx.parameter_list()), self.visit(ctx.inherit_function()), self.visit(ctx.block_statement()))]
        return [FuncDecl(ctx.IDENTIFIER().getText(), self.visit(ctx.return_type()), self.visit(ctx.parameter_list()), None , self.visit(ctx.block_statement()))]

    # Return a list parameter declaration
#parameter: INHERIT? OUT? IDENTIFIER COLON type_;
    def visitParameter(self, ctx: MT22Parser.ParameterContext):
        if ctx.OUT() and ctx.INHERIT():
            return [ParamDecl(ctx.IDENTIFIER().getText(), self.visit(ctx.type_()), True, True)]
        elif ctx.OUT():
            return [ParamDecl(ctx.IDENTIFIER().getText(), self.visit(ctx.type_()), True, False)]
        elif ctx.INHERIT():
            return [ParamDecl(ctx.IDENTIFIER().getText(), self.visit(ctx.type_()), False, True)]
        else:
            return [ParamDecl(ctx.IDENTIFIER().getText(), self.visit(ctx.type_()), False, False)]

#parameter_prime: parameter COMMA parameter_prime | parameter;
    def visitParameter_prime(self, ctx: MT22Parser.Parameter_primeContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.parameter())
        return self.visit(ctx.parameter()) + self.visit(ctx.parameter_prime())

#parameter_list: parameter_prime | ;
    def visitParameter_list(self, ctx: MT22Parser.Parameter_listContext):
        if ctx.getChildCount() == 0:
            return []
        return self.visit(ctx.parameter_prime())

    # Variable Declaration
#identifier_list: IDENTIFIER COMMA identifier_list | IDENTIFIER;
    def visitIdentifier_list(self, ctx: MT22Parser.Identifier_listContext):
        if ctx.getChildCount() == 1:
            return [ctx.IDENTIFIER().getText()]
        return [ctx.IDENTIFIER().getText()] + self.visit(ctx.identifier_list())

#var_decl_non_assign: identifier_list COLON type_;
    def visitVar_decl_non_assign(self, ctx: MT22Parser.Var_decl_non_assignContext):
        return [VarDecl(name, self.visit(ctx.type_())) for name in self.visit(ctx.identifier_list())]
    
#var_decl_assign: IDENTIFIER COMMA var_decl_assign COMMA expression | IDENTIFIER COLON type_ ASSIGN expression;
    def visitVar_decl_assign(self, ctx: MT22Parser.Var_decl_assignContext):
        if ctx.var_decl_assign():
            return [ctx.IDENTIFIER().getText()] + self.visit(ctx.var_decl_assign()) + [self.visit(ctx.expression())]
        return [ctx.IDENTIFIER().getText()]+ [self.visit(ctx.type_())] + [self.visit(ctx.expression())]
        
#return List[VarDecl]   
#var_declaration: (var_decl_non_assign | var_decl_assign) SEMI;
    def visitVar_declaration(self, ctx: MT22Parser.Var_declarationContext):
        if ctx.var_decl_non_assign():
            return self.visit(ctx.var_decl_non_assign())
        else:
            list_var_decl = self.visit(ctx.var_decl_assign())
            mid_index = len(list_var_decl) // 2
            ids = list_var_decl[:mid_index]
            exps = list_var_decl[mid_index + 1:]
            typ = list_var_decl[mid_index]
            return [VarDecl(id, typ, exp) for id, exp in zip(ids, exps)]

#list_var_declaration_prime: var_declaration list_var_declaration_prime | var_declaration; 
    def visitList_var_declaration_prime(self, ctx: MT22Parser.List_var_declaration_primeContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.var_declaration())
        return self.visit(ctx.var_declaration()) + self.visit(ctx.list_var_declaration_prime())

#list_var_declaration: list_var_declaration_prime | ;
    def visitList_var_declaration(self, ctx: MT22Parser.List_var_declarationContext):
        if ctx.getChildCount() == 0:
            return []
        return self.visit(ctx.list_var_declaration_prime())

# Declaration 
#return a list of declaration
#declaration: var_declaration | function_declaration | parameter ;
    def visitDeclaration(self, ctx: MT22Parser.DeclarationContext):
        return self.visit(ctx.getChild(0))

#list_declared: declaration list_declared | declaration;   
    def visitList_declared(self, ctx: MT22Parser.List_declaredContext):
        if ctx.list_declared():
            return self.visit(ctx.declaration()) + self.visit(ctx.list_declared())
        return self.visit(ctx.declaration())

#program: list_declared EOF;
    def visitProgram(self, ctx: MT22Parser.ProgramContext):
        return Program(self.visit(ctx.list_declared()))