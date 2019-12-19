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
    # TODO Refactor to a dictionary
    DEFAULT_PERSISTANCE_ENGINE = 'sql.sqlite'
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

    # TODO initialize
    def initialize(self, persistance_engine):
        try:
            pass
        except expression as identifier:
            pass

    # TODO clone
    # TODO translate
    # TODO generate_code
    # TODO add_entity_by_query
    # TODO get_variable
    # TODO set_variable
    # TODO get_function
    # TODO set_function
    # TODO function_by_query_entity_type
    # TODO set_function_by_query

    # TODO translate_aspect_filter
    # TODO generate_code_for_aspect_filter

    # TODO load_context_symbols
    # TODO build_builtin_types
    # TODO instance_code_generator_and_interpreter
    # TODO new_object_by_property_name
    # TODO check_object_by_name
    # TODO translate_raw_aql_to_expression
    # TODO translate_aql_to_expression
    # TODO translate_aql_filter_to_expression
