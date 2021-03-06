#
from datetime import datetime
import copy

#
class AspectException(BaseException):
    pass

#
class Entity:
    # Static properties. Class metadata
    class Meta:
        type = 'entity'
        name = 'entity'
        model = {}
        addToModel = False

    #
    def __init__(self, args={}):
        self.id = args.id if hasattr(args, 'id') else 0
        self.name = args.name if hasattr(args, 'name') else ''
        self.date_created = args.date_created if hasattr(args, 'date_created') else datetime.now()
        self.last_update = args.last_update if hasattr(args, 'last_update') else datetime.now()
        self.created_by = args.created_by if hasattr(args, 'created_by') else 'defaultUser'
        self.updated_by = args.updated_by if hasattr(args, 'updated_by') else 'defaultUser'
        #
        #if Entity.meta['addToModel']: 
        #    Entity.meta.model[self)] = this

    def __hash__(self):
        return self.id

    #
    @staticmethod
    def copy_properties(source, target, deep=False):
        source = source if isinstance(source, dict) else source
        d = copy.deepcopy(source) if deep else copy.copy(source)
        for k, v in d.items():
            target.__dict__[k] = v