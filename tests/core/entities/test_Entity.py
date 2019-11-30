#
import pytest
from aspect.core.entities.Entity import Entity

@pytest.fixture
def entity():
    return Entity()

@pytest.fixture
def new_entity():
    e = Entity()
    e.id = 1
    return e

#
def test_entity_metadata():
    assert Entity.Meta.type == 'entity'

#
def test_entity_instantiation(entity):
    assert entity.id == 0 and entity.name == "" \
        and entity.created_by == 'defaultUser' and entity.updated_by == 'defaultUser' \
        and entity.date_created != None and entity.last_update != None

#
def test_entity_hash(new_entity):
    assert hash(new_entity) == 1
