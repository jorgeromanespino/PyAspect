#
from aspect.core.languages.aql.AqlVisitor import AqlVisitor


#
class SqlAlchemyTranslator(AqlVisitor):
    # Static
    predicate_visited = False
    #
    def visitPredicateExpression(self, ctx:AqlParser.PredicateExpressionContext):
        MyAqlVisitor.predicate_visited = True
        return self.visitChildren(ctx)