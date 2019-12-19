#
import pytest
#
from aspect.core.languages.aql.translators.Command import Command

#
def test_command_instantiation():
    cmd = Command()
    assert cmd != None and cmd.parent == {} and cmd.children == []
