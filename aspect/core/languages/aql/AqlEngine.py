#
from antlr4 import *
from aspect.core.languages.aql.AqlLexer import AqlLexer
from aspect.core.languages.aql.AqlParser import AqlParser
from aspect.core.languages.aql.AqlVisitor import AqlVisitor
from aspect.core.languages.aql.SymbolTable import SymbolTable

# TODO Refactor
class AqlContext:
    pass

#
class AqlEngine:
    #
    DEFAULT_PERSISTANCE_ENGINE = 'default'
    
    #
    def __init__(self):
        self.symbol_table = SymbolTable()
        self.aql_context = AqlContext()
        self.code_generator = None
        self.interpreter = None
        self.add_builtin_types = True

    #
    def parse(self, q):
        input = InputStream(q)
        lexer = AqlLexer(input)
        stream = CommonTokenStream(lexer)
        parser = AqlParser(stream)
        parser.buildParseTrees = True
        tree = parser.queryExpression()   
        return tree   

