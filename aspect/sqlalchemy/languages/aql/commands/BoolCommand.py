#
from aspect.sqlalchemy.languages.aql.Command import Command

#
class BoolCommand(Command):
    #
    def __init__(self, value):
        super().__init__(value=value)
        self.result = True if value == 'true' else False

    # # TODO
    # def execute():
