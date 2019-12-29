#
import pytest
#
from aspect.sqlalchemy.languages.aql.Translator import Translator
from antlr4 import *
from aspect.core.languages.aql.AqlLexer import AqlLexer
from aspect.core.languages.aql.AqlParser import AqlParser
from aspect.core.languages.aql.AqlVisitor import AqlVisitor

#
def test_sqlalchemy_translator_instantiation():
    translator = Translator()
    assert translator != None

#
def build_parser(query):
    input = InputStream(query)
    lexer = AqlLexer(input)
    stream = CommonTokenStream(lexer)
    parser = AqlParser(stream)
    parser.buildParseTrees = True
    return parser

#
def test_sqlalchemy_translator_visitor():
    #
    parser = build_parser('entity')
    translator = Translator()
    tree = parser.queryExpression()
    translator.visit(tree)
    #
    assert parser != None and translator != None and tree != None
    assert tree.getText() == 'entity' and  tree.children[0].getText() == 'entity'
    assert translator.visited == True    
