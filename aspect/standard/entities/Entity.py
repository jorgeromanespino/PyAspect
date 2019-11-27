#
from aspect.core.entities.Entity import Entity as CoreEntity

#
class Entity(CoreEntity):
    # Static properties. Class metadata
    class meta:
        type = 'entity'
        name = 'entity'
        model = {}
        addToModel = True

    #
    def __init__(self, args={}):
        super().__init__(args)
