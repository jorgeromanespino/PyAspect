#
import pytest
#
from aspect.sqlalchemy.languages.aql.Command import Command

#
def test_command_instantiation():
    cmd = Command()
    assert cmd != None and cmd.parent == {} and cmd.children == []
