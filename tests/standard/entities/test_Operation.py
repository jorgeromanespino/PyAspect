#
import pytest
from aspect.standard.entities.Operation import Operation


@pytest.fixture
def operation():
    return Operation()

#
def test_operation_instantiation(operation):
    assert operation.id == 0 and operation.name == "" \
        and operation.created_by == 'defaultUser' and operation.updated_by == 'defaultUser' \
        and operation.date_created != None and operation.last_update != None \
        and operation.signature == "" and operation.local_namespace == "" \
        and operation.local_name == ""
