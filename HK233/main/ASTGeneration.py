"""
 * Initial code for Assignment
 * Programming Language Principles
 * Author: Võ Tiến
 * Link FB : https://www.facebook.com/profile.php?id=100056605580171
 * Link Group : https://www.facebook.com/groups/211867931379013
 * Date: 06.23.2024
"""
from MT22Visitor import MT22Visitor
from MT22Parser import MT22Parser
from AST import *
from functools import reduce

class ASTGeneration(MT22Visitor):


    # Visit a parse tree produced by MT22Parser#program.
    #* program: list_declared EOF;
    def visitProgram(self, ctx:MT22Parser.ProgramContext):
        return Program(self.visit(ctx.list_declared()))


    # Visit a parse tree produced by MT22Parser#list_declared.
    #* list_declared:  declared list_declared |  declared;
    def visitList_declared(self, ctx:MT22Parser.List_declaredContext):
        if ctx.getChildCount() == 1: 
            return self.visit(ctx.declared())
        return self.visit(ctx.declared()) + self.visit(ctx.list_declared())


    # Visit a parse tree produced by MT22Parser#declared.
    #* declared: function | variables SC;
    def visitDeclared(self, ctx:MT22Parser.DeclaredContext):
        if ctx.function():
            return [self.visit(ctx.function())]
        return self.visit(ctx.variables())
    

    # Visit a parse tree produced by MT22Parser#variables.
    #* variables:  variables_initialization | list_identifier COL all_types;
    def visitVariables(self, ctx:MT22Parser.VariablesContext):
        if ctx.variables_initialization():
            variables_initialization = self.visit(ctx.variables_initialization())
            mid_index = len(variables_initialization) // 2
            first_part = variables_initialization[:mid_index]
            middle_part = variables_initialization[mid_index:mid_index+1]
            last_part = variables_initialization[mid_index+1:]
            return [VarDecl(first_part[i], middle_part[0], last_part[i]) for i in range(0, mid_index)]
        return [VarDecl(name, self.visit(ctx.all_types())) for name in self.visit(ctx.list_identifier())]


    # Visit a parse tree produced by MT22Parser#variables_initialization.
    #* variables_initialization: ID CM  variables_initialization CM expression | ID COL all_types ASSIGNINIT expression;
    def visitVariables_initialization(self, ctx:MT22Parser.Variables_initializationContext):
        if ctx.ASSIGNINIT():
            return [ctx.ID().getText()] + [self.visit(ctx.all_types())] + [self.visit(ctx.expression())]
        return [ctx.ID().getText()] + self.visit(ctx.variables_initialization()) + [self.visit(ctx.expression())]
        


    # Visit a parse tree produced by MT22Parser#list_identifier.
    #* list_identifier : ID CM list_identifier | ID;
    def visitList_identifier(self, ctx:MT22Parser.List_identifierContext):
        if ctx.getChildCount() == 1:
            return [ctx.ID().getText()]
        return [ctx.ID().getText()] + self.visit(ctx.list_identifier())


    # Visit a parse tree produced by MT22Parser#all_types.
    #* all_types: atomic_type | array_type | AUTO;
    def visitAll_types(self, ctx:MT22Parser.All_typesContext):
        if ctx.atomic_type():
            return self.visit(ctx.atomic_type())
        elif ctx.array_type():
            return self.visit(ctx.array_type())
        return AutoType()
            


    # Visit a parse tree produced by MT22Parser#atomic_type.
    #* atomic_type:  INTEGER | FLOAT | BOOLEAN | STRING;
    def visitAtomic_type(self, ctx:MT22Parser.Atomic_typeContext):
        if ctx.INTEGER():
            return IntegerType()
        elif ctx.FLOAT():
            return FloatType()
        elif ctx.BOOLEAN():
            return BooleanType()
        return StringType()


    # Visit a parse tree produced by MT22Parser#array_type.
    #* array_type: ARRAY LSB dimensions RSB OF atomic_type;
    def visitArray_type(self, ctx:MT22Parser.Array_typeContext):
        return ArrayType(self.visit(ctx.dimensions()), self.visit(ctx.atomic_type()))


    # Visit a parse tree produced by MT22Parser#dimensions.
    #* dimensions: INT_LIT CM dimensions | INT_LIT;
    def visitDimensions(self, ctx:MT22Parser.DimensionsContext):
        if ctx.getChildCount() == 1:
            return [int(ctx.INT_LIT().getText())]
        return [int(ctx.INT_LIT().getText())] + self.visit(ctx.dimensions())


    # Visit a parse tree produced by MT22Parser#function.
    #* function: ID COL FUNCTION (all_types  | VOID) LP prameters_list? RP (INHERIT ID)? block_statement; 
    def visitFunction(self, ctx:MT22Parser.FunctionContext):
        prameters = self.visit(ctx.prameters_list()) if ctx.prameters_list() else []
        inherit = ctx.ID()[1].getText() if ctx.INHERIT() else None
        _type = VoidType() if ctx.VOID() else self.visit(ctx.all_types())
        return FuncDecl(ctx.ID()[0].getText(), _type, prameters, inherit, self.visit(ctx.block_statement()))


    # Visit a parse tree produced by MT22Parser#prameters_list.
    #* prameters_list: prameter CM prameters_list | prameter; 
    def visitPrameters_list(self, ctx:MT22Parser.Prameters_listContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.prameter())]
        return [self.visit(ctx.prameter())] + self.visit(ctx.prameters_list())


    # Visit a parse tree produced by MT22Parser#prameter.
    #* prameter: INHERIT? OUT? ID COL all_types;
    def visitPrameter(self, ctx:MT22Parser.PrameterContext):
        inherit = False
        out = False
        if ctx.INHERIT():
            inherit = True
        if ctx.OUT():
            out = True
        return ParamDecl(ctx.ID().getText(),self.visit(ctx.all_types()),out,inherit)

    # Visit a parse tree produced by MT22Parser#list_expression.
    #* list_expression: expression CM list_expression | expression;
    def visitList_expression(self, ctx:MT22Parser.List_expressionContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.expression())]
        return [self.visit(ctx.expression())] + self.visit(ctx.list_expression())


    # Visit a parse tree produced by MT22Parser#expression.
    #* expression: expression1 CONCAT expression1 | expression1;
    def visitExpression(self, ctx:MT22Parser.ExpressionContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expression1()[0])
        
        op = ctx.CONCAT().getText()
        left = self.visit(ctx.expression1()[0])
        right = self.visit(ctx.expression1()[1])
        return BinExpr(op, left, right)



    # Visit a parse tree produced by MT22Parser#expression1.
    #* expression1: expression2 (EQUAL | NOT_EQUAL | LT | GT | LE | GE) expression2 | expression2;
    def visitExpression1(self, ctx:MT22Parser.Expression1Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expression2()[0])
        
        op = ''
        if ctx.EQUAL():
            op = ctx.EQUAL().getText()
        elif ctx.NOT_EQUAL():
            op = ctx.NOT_EQUAL().getText()
        elif ctx.LT():
            op = ctx.LT().getText()
        elif ctx.GT():
            op = ctx.GT().getText()
        elif ctx.LE():
            op = ctx.LE().getText()
        elif ctx.GE():
            op = ctx.GE().getText()

        left = self.visit(ctx.expression2()[0])
        right = self.visit(ctx.expression2()[1])
        return BinExpr(op, left, right)


    # Visit a parse tree produced by MT22Parser#expression2.
    #* expression2: expression2 (AND | OR) expression3 | expression3;
    def visitExpression2(self, ctx:MT22Parser.Expression2Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expression3())
        
        op = ''
        if ctx.AND():
            op = ctx.AND().getText()
        elif ctx.OR():
            op = ctx.OR().getText()

        left = self.visit(ctx.expression2())
        right = self.visit(ctx.expression3())
        return BinExpr(op, left, right)


    # Visit a parse tree produced by MT22Parser#expression3.
    #* expression3: expression3 (ADD | SUB) expression4 | expression4;
    def visitExpression3(self, ctx:MT22Parser.Expression3Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expression4())
        
        op = ''
        if ctx.ADD():
            op = ctx.ADD().getText()
        elif ctx.SUB():
            op = ctx.SUB().getText()

        left = self.visit(ctx.expression3())
        right = self.visit(ctx.expression4())
        return BinExpr(op, left, right)


    # Visit a parse tree produced by MT22Parser#expression4.
    #* expression4: expression4 (MUL | DIV | MOD) expression5 | expression5;
    def visitExpression4(self, ctx:MT22Parser.Expression4Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expression5())
        
        op = ''
        if ctx.MUL():
            op = ctx.MUL().getText()
        elif ctx.DIV():
            op = ctx.DIV().getText()
        elif ctx.MOD():
            op = ctx.MOD().getText()

        left = self.visit(ctx.expression4())
        right = self.visit(ctx.expression5())
        return BinExpr(op, left, right)


    # Visit a parse tree produced by MT22Parser#expression5.
    #* expression5: (NOT) expression5 | expression6;
    def visitExpression5(self, ctx:MT22Parser.Expression5Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expression6())
        return UnExpr('!', self.visit(ctx.expression5()))

    # Visit a parse tree produced by MT22Parser#expression6.
    #* expression6: SUB expression6 | expression7;
    def visitExpression6(self, ctx:MT22Parser.Expression6Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expression7())
        return UnExpr('-', self.visit(ctx.expression6()))


    # Visit a parse tree produced by MT22Parser#expression7.
    #* expression7: ID LSB list_expression RSB | expression8;
    def visitExpression7(self, ctx:MT22Parser.Expression7Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expression8())
        return ArrayCell(ctx.ID().getText(), self.visit(ctx.list_expression()))


    # Visit a parse tree produced by MT22Parser#expression8.
    #* expression8: ID | literal | LP expression RP | ID LP list_expression? RP;
    def visitExpression8(self, ctx:MT22Parser.Expression8Context):
        if ctx.literal():
            return self.visit(ctx.literal())
        elif ctx.expression():
            return self.visit(ctx.expression())
        elif ctx.getChildCount() == 1:
            return Id(ctx.ID().getText())
        return FuncCall(ctx.ID().getText(), self.visit(ctx.list_expression()) if ctx.list_expression() else [])


    # Visit a parse tree produced by MT22Parser#literal.
    #* literal: INT_LIT | FLOAT_LIT | STRING_LIT | TRUE | FALSE | array_literal;
    def visitLiteral(self, ctx:MT22Parser.LiteralContext):
        if ctx.INT_LIT():
            return IntegerLit(int(ctx.INT_LIT().getText()))
        elif ctx.FLOAT_LIT():
            return FloatLit(float(ctx.FLOAT_LIT().getText()))
        elif ctx.STRING_LIT():
            return StringLit(ctx.STRING_LIT().getText())
        elif ctx.TRUE():
            return BooleanLit(True)
        elif ctx.FALSE():
            return BooleanLit(False)
        return self.visit(ctx.array_literal())


    # Visit a parse tree produced by MT22Parser#array_literal.
    #* array_literal: LCB list_expression RCB;
    def visitArray_literal(self, ctx:MT22Parser.Array_literalContext):
        return ArrayLit(self.visit(ctx.list_expression()))


    # Visit a parse tree produced by MT22Parser#statement.
    #* statement: ( assignment_statement 
    #*             | if_statement | for_statement 
    #*             | break_statement | continue_statement 
    #*             | return_statement  | call_statement 
    #*             | block_statement | while_statement | do_while_statement);
    def visitStatement(self, ctx:MT22Parser.StatementContext):
        return self.visitChildren(ctx) #! return self.visit(ctx.getChild(0))


    # Visit a parse tree produced by MT22Parser#declaration_statement.
    #* declaration_statement: variables SC;
    def visitDeclaration_statement(self, ctx:MT22Parser.Declaration_statementContext):
        return self.visit(ctx.variables())


    # Visit a parse tree produced by MT22Parser#assignment_statement.
    #* assignment_statement: lhs ASSIGNINIT expression SC;
    def visitAssignment_statement(self, ctx:MT22Parser.Assignment_statementContext):
        return AssignStmt(self.visit(ctx.lhs()), self.visit(ctx.expression()))


    # Visit a parse tree produced by MT22Parser#lhs.
    #* lhs: ID | ID LSB list_expression RSB;
    def visitLhs(self, ctx:MT22Parser.LhsContext):
        if ctx.getChildCount() == 1:
            return Id(ctx.ID().getText())
        return ArrayCell(ctx.ID().getText(), self.visit(ctx.list_expression()))


    # Visit a parse tree produced by MT22Parser#if_statement.
    #* if_statement: IF LP expression RP statement (ELSE statement)?;
    def visitIf_statement(self, ctx:MT22Parser.If_statementContext):
        return IfStmt(self.visit(ctx.expression()), self.visit(ctx.statement()[0]), self.visit(ctx.statement()[1]) if ctx.ELSE()  else None)


    # Visit a parse tree produced by MT22Parser#for_statement.
    #* for_statement: FOR LP lhs ASSIGNINIT expression CM expression CM expression RP statement;
    def visitFor_statement(self, ctx:MT22Parser.For_statementContext):
        return ForStmt(AssignStmt(self.visit(ctx.lhs()), self.visit(ctx.expression()[0])), self.visit(ctx.expression()[1]), self.visit(ctx.expression()[2]), self.visit(ctx.statement()))


    # Visit a parse tree produced by MT22Parser#while_statement.
    #* while_statement: WHILE  LP expression RP statement;
    def visitWhile_statement(self, ctx:MT22Parser.While_statementContext):
        return WhileStmt(self.visit(ctx.expression()), self.visit(ctx.statement()))


    # Visit a parse tree produced by MT22Parser#do_while_statement.
    #* do_while_statement: DO block_statement WHILE LP expression RP SC;
    def visitDo_while_statement(self, ctx:MT22Parser.Do_while_statementContext):
        return DoWhileStmt(self.visit(ctx.expression()), self.visit(ctx.block_statement()))


    # Visit a parse tree produced by MT22Parser#break_statement.
    #* break_statement: BREAK SC;
    def visitBreak_statement(self, ctx:MT22Parser.Break_statementContext):
        return BreakStmt()


    # Visit a parse tree produced by MT22Parser#continue_statement.
    #* continue_statement: CONTINUE SC;
    def visitContinue_statement(self, ctx:MT22Parser.Continue_statementContext):
        return ContinueStmt()


    # Visit a parse tree produced by MT22Parser#return_statement.
    #* return_statement: RETURN expression? SC;
    def visitReturn_statement(self, ctx:MT22Parser.Return_statementContext):
        return ReturnStmt(self.visit(ctx.expression()) if ctx.expression() else None)


    # Visit a parse tree produced by MT22Parser#call_statement.
    #* call_statement: ID LP list_expression? RP SC;
    def visitCall_statement(self, ctx:MT22Parser.Call_statementContext):
        return CallStmt(ctx.ID().getText(), self.visit(ctx.list_expression()) if ctx.list_expression() else [])


    # Visit a parse tree produced by MT22Parser#block_statement.
    #* block_statement: LCB list_statement? RCB; 
    def visitBlock_statement(self, ctx:MT22Parser.Block_statementContext):
        return BlockStmt(self.visit(ctx.list_statement()) if ctx.list_statement() else [])


    # Visit a parse tree produced by MT22Parser#list_statement.
    #* list_statement: (statement | declaration_statement) list_statement | statement | declaration_statement;
    def visitList_statement(self, ctx:MT22Parser.List_statementContext):
        #* statement : object | declaration_statement : list<object>
        stmt = self.visit(ctx.getChild(0))
        if ctx.getChildCount() == 1:
            if ctx.statement() : return [stmt]
            return stmt
        if ctx.statement() : return [stmt] + self.visit(ctx.list_statement())
        return stmt + self.visit(ctx.list_statement())

