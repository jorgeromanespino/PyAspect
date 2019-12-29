#
from aspect.core.languages.aql.AqlEngine import AqlEngine as CoreAqlEngine
from aspect.sqlalchemy.languages.aql.Translator import Translator as SqlAlchemyTranslator

#
class AqlEngine(CoreAqlEngine):
    #
    def __init__(self):
        super().__init__()

    # TODO translate
    def translate(self, ast):
        new_symbol_table = self.symbol_table.clone()
        translator = SqlAlchemyTranslator(symbol_table=new_symbol_table)
        translator.visit(ast)
        return translator

    # TODO clone
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
