#
# https://tomassetti.me/antlr-mega-tutorial/#starting-with-python
#
from antlr4 import *
from aspect.core.languages.aql.AqlLexer import AqlLexer
from aspect.core.languages.aql.AqlParser import AqlParser
from aspect.core.languages.aql.AqlVisitor import AqlVisitor

#
def test_antlr_objects():
    assert AqlVisitor != None and AqlParser != None and AqlVisitor != None

#
def test_atom_expression():
    input = 'entity'
    input = InputStream(input)
    lexer = AqlLexer(input)
    stream = CommonTokenStream(lexer)
    parser = AqlParser(stream)
    parser.buildParseTrees = True
    tree = parser.atomExpression()

    assert input != None and lexer != None and stream != None
    assert parser != None and tree != None
    assert tree.getText() == 'entity'
    assert tree.children[0].getText() == 'entity'

#
predicate_visited = False
def predicate_visitor_func(self, ctx):
    predicate_visited = True
    return self.visitChildren(ctx);

#
class MyAqlVisitor(AqlVisitor):
    # Static
    predicate_visited = False
    #
    def visitPredicateExpression(self, ctx:AqlParser.PredicateExpressionContext):
        MyAqlVisitor.predicate_visited = True
        return self.visitChildren(ctx)

#
def test_aql_visitor():
    input = 'entity'
    input = InputStream(input)
    lexer = AqlLexer(input)
    stream = CommonTokenStream(lexer)
    parser = AqlParser(stream)
    visitor = MyAqlVisitor()#AqlVisitor()

    parser.buildParseTrees = True
    tree = parser.queryExpression()

    assert input != None and lexer != None and stream != None
    assert parser != None and visitor != None and tree != None
    assert tree.getText() == 'entity'
    assert tree.children[0].getText() == 'entity'

    #
    MyAqlVisitor.predicate_visited = False
    visitor.visit(tree)

    #
    assert MyAqlVisitor.predicate_visited == True
