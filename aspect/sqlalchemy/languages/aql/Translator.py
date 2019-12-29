#
from aspect.core.languages.aql.AqlParser import AqlParser
from aspect.core.languages.aql.AqlVisitor import AqlVisitor
from aspect.core.languages.aql.SymbolTable import SymbolTable
#
from aspect.sqlalchemy.languages.aql.commands.BoolCommand import BoolCommand

#
class Translator(AqlVisitor):
    #
    def __init__(self, symbol_table=None):
        super().__init__()
        self.symbol_table = symbol_table
        self.command = None
        self.add_standard_functions()
        self.visited = False

    # TODO load dynamically all the commands
    def add_standard_functions(self):
        st = self.symbol_table
        #st.set_function('position', PositionCommand)

    # TODO test
    def setup_command(self, command, context):
        if command == None: return
        command.symbol_table = self.symbol_table
        command.context = context
        self.command = command
        return command

    #
    def visitQueryExpression(self, ctx:AqlParser.QueryExpressionContext):
        self.visited = True
        return self.visitExpression(ctx.children[0])

    # 
    def visitExpression(self, ctx:AqlParser.ExpressionContext):
        return self.visitNavigateExpression(ctx.children[0])

    # # TODO
    # def visitNavigateExpression(self, ctx:AqlParser.NavigateExpressionContext):
    #     return self.visitChildren(ctx)

    # TODO
    def visitAtomExpression(self, ctx:AqlParser.AtomExpressionContext):
        command = None
        if ctx.children[0].getText() == 'true':
            command = BoolCommand(True)
            return self.setup_command(command, ctx)
        else: 
            return self.visitChildren(ctx)
