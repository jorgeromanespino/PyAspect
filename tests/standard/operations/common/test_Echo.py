#
import pytest
from aspect.standard.operations.common.Echo import Echo


@pytest.fixture
def echo_operation():
    return Echo(message='hello world!')

#
def test_echo_operation_execution(echo_operation):
    r = echo_operation.handle()
    assert r == 'echo hello world!'
