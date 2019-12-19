#
from antlr4 import *
from aspect.core.languages.aql.AqlLexer import AqlLexer
from aspect.core.languages.aql.AqlParser import AqlParser
from aspect.core.languages.aql.AqlVisitor import AqlVisitor
from aspect.core.languages.aql.SymbolTable import SymbolTable

#
class AqlEngine:
    #
    def __init__(self):
        self.symbol_table = SymbolTable()

    #
    def parse(self, q):
        input = InputStream(q)
        lexer = AqlLexer(input)
        stream = CommonTokenStream(lexer)
        parser = AqlParser(stream)
        parser.buildParseTrees = True
        tree = parser.queryExpression()   
        return tree   


    # TODO clone
    # TODO translate
    # TODO generate_code
    # TODO add_entity_by_query
    # TODO get_variable
    # TODO set_variable
    # TODO get_function
    # TODO set_function

    # TODO translate_aspect_filter
    # TODO generate_code_for_aspect_filter

    # TODO initialize
    # TODO load_context_symbols
    # TODO build_builtin_types
    # TODO instance_code_generator_and_interpreter
    # TODO new_object_by_property_name
    # TODO check_object_by_name
    # TODO translate_raw_aql_to_expression
    # TODO translate_aql_to_expression
    # TODO translate_aql_filter_to_expression
