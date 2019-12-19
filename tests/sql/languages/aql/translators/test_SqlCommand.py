#
import pytest
#
from aspect.sql.languages.aql.translators.Command import Command

#
def test_command_instantiation():
    cmd = Command()
    assert cmd != None and cmd.parent == {} and cmd.children == []
