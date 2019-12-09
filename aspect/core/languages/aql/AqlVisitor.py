# Generated from ./aspect/core/languages/aql/Aql.g4 by ANTLR 4.6
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .AqlParser import AqlParser
else:
    from AqlParser import AqlParser

# This class defines a complete generic visitor for a parse tree produced by AqlParser.

class AqlVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by AqlParser#queryExpression.
    def visitQueryExpression(self, ctx:AqlParser.QueryExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AqlParser#expression.
    def visitExpression(self, ctx:AqlParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AqlParser#navigateExpression.
    def visitNavigateExpression(self, ctx:AqlParser.NavigateExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AqlParser#orExpression.
    def visitOrExpression(self, ctx:AqlParser.OrExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AqlParser#andExpression.
    def visitAndExpression(self, ctx:AqlParser.AndExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AqlParser#bitOrExpression.
    def visitBitOrExpression(self, ctx:AqlParser.BitOrExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AqlParser#bitXorExpression.
    def visitBitXorExpression(self, ctx:AqlParser.BitXorExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AqlParser#bitAndExpression.
    def visitBitAndExpression(self, ctx:AqlParser.BitAndExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AqlParser#equalsExpression.
    def visitEqualsExpression(self, ctx:AqlParser.EqualsExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AqlParser#plusExpression.
    def visitPlusExpression(self, ctx:AqlParser.PlusExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AqlParser#multiplyExpression.
    def visitMultiplyExpression(self, ctx:AqlParser.MultiplyExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AqlParser#unaryExpresion.
    def visitUnaryExpresion(self, ctx:AqlParser.UnaryExpresionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AqlParser#predicateExpression.
    def visitPredicateExpression(self, ctx:AqlParser.PredicateExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AqlParser#atomExpression.
    def visitAtomExpression(self, ctx:AqlParser.AtomExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AqlParser#propertyAccess.
    def visitPropertyAccess(self, ctx:AqlParser.PropertyAccessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AqlParser#expressionList.
    def visitExpressionList(self, ctx:AqlParser.ExpressionListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AqlParser#fieldList.
    def visitFieldList(self, ctx:AqlParser.FieldListContext):
        return self.visitChildren(ctx)



del AqlParser