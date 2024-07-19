# Generated from main/mt22/parser/MT22.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MT22Parser import MT22Parser
else:
    from MT22Parser import MT22Parser

# This class defines a complete generic visitor for a parse tree produced by MT22Parser.

class MT22Visitor(ParseTreeVisitor):

    # Visit a parse tree produced by MT22Parser#program.
    def visitProgram(self, ctx:MT22Parser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#list_declared.
    def visitList_declared(self, ctx:MT22Parser.List_declaredContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#declaration.
    def visitDeclaration(self, ctx:MT22Parser.DeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#list_var_declaration.
    def visitList_var_declaration(self, ctx:MT22Parser.List_var_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#list_var_declaration_prime.
    def visitList_var_declaration_prime(self, ctx:MT22Parser.List_var_declaration_primeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#var_declaration.
    def visitVar_declaration(self, ctx:MT22Parser.Var_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#var_decl_non_assign.
    def visitVar_decl_non_assign(self, ctx:MT22Parser.Var_decl_non_assignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#var_decl_assign.
    def visitVar_decl_assign(self, ctx:MT22Parser.Var_decl_assignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#identifier_list.
    def visitIdentifier_list(self, ctx:MT22Parser.Identifier_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#type_.
    def visitType_(self, ctx:MT22Parser.Type_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#type_n_auto.
    def visitType_n_auto(self, ctx:MT22Parser.Type_n_autoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#array_type.
    def visitArray_type(self, ctx:MT22Parser.Array_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#dimensions.
    def visitDimensions(self, ctx:MT22Parser.DimensionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#parameter_list.
    def visitParameter_list(self, ctx:MT22Parser.Parameter_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#parameter_prime.
    def visitParameter_prime(self, ctx:MT22Parser.Parameter_primeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#parameter.
    def visitParameter(self, ctx:MT22Parser.ParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#function_declaration.
    def visitFunction_declaration(self, ctx:MT22Parser.Function_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#return_type.
    def visitReturn_type(self, ctx:MT22Parser.Return_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#inherit_function.
    def visitInherit_function(self, ctx:MT22Parser.Inherit_functionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expression.
    def visitExpression(self, ctx:MT22Parser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expression1.
    def visitExpression1(self, ctx:MT22Parser.Expression1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expression2.
    def visitExpression2(self, ctx:MT22Parser.Expression2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expression3.
    def visitExpression3(self, ctx:MT22Parser.Expression3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expression4.
    def visitExpression4(self, ctx:MT22Parser.Expression4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expression5.
    def visitExpression5(self, ctx:MT22Parser.Expression5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expression6.
    def visitExpression6(self, ctx:MT22Parser.Expression6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expression7.
    def visitExpression7(self, ctx:MT22Parser.Expression7Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expression8.
    def visitExpression8(self, ctx:MT22Parser.Expression8Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#factor.
    def visitFactor(self, ctx:MT22Parser.FactorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#array_literal.
    def visitArray_literal(self, ctx:MT22Parser.Array_literalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#exp_list.
    def visitExp_list(self, ctx:MT22Parser.Exp_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#exp_prime.
    def visitExp_prime(self, ctx:MT22Parser.Exp_primeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#index_operator.
    def visitIndex_operator(self, ctx:MT22Parser.Index_operatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#statement.
    def visitStatement(self, ctx:MT22Parser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#assign_statement.
    def visitAssign_statement(self, ctx:MT22Parser.Assign_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#lhs.
    def visitLhs(self, ctx:MT22Parser.LhsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#if_statement.
    def visitIf_statement(self, ctx:MT22Parser.If_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#for_statement.
    def visitFor_statement(self, ctx:MT22Parser.For_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#while_statement.
    def visitWhile_statement(self, ctx:MT22Parser.While_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#dowhile_statement.
    def visitDowhile_statement(self, ctx:MT22Parser.Dowhile_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#break_statement.
    def visitBreak_statement(self, ctx:MT22Parser.Break_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#continue_statement.
    def visitContinue_statement(self, ctx:MT22Parser.Continue_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#return_statement.
    def visitReturn_statement(self, ctx:MT22Parser.Return_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#call_statement.
    def visitCall_statement(self, ctx:MT22Parser.Call_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#function_call.
    def visitFunction_call(self, ctx:MT22Parser.Function_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#block_statement.
    def visitBlock_statement(self, ctx:MT22Parser.Block_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#blk_items.
    def visitBlk_items(self, ctx:MT22Parser.Blk_itemsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#blk_item.
    def visitBlk_item(self, ctx:MT22Parser.Blk_itemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#statement_list.
    def visitStatement_list(self, ctx:MT22Parser.Statement_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#statement_prime.
    def visitStatement_prime(self, ctx:MT22Parser.Statement_primeContext):
        return self.visitChildren(ctx)



del MT22Parser