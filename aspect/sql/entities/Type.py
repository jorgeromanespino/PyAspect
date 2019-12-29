#
from aspect.sql.entities.Entity import Entity
#
import datetime
from sqlalchemy import Column, Integer, String, DateTime
#
class Type(Entity):
    __tablename__ = 'type'
    #
    local_name      = Column(String(512))
    local_namespace = Column(String(512))