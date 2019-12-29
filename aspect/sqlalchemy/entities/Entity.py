#
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base() # Always do this in order to derive subclasses
#
import datetime
from sqlalchemy import Column, Integer, String, DateTime
#
class Entity(Base):
    __tablename__ = 'entity'
    #
    id              = Column(Integer, primary_key=True, autoincrement=True)
    name            = Column(String(512))
    description     = Column(String(512))
    hash            = Column(String(512))
    #
    creation_date   = Column(DateTime)
    update_date     = Column(DateTime)
    created_by      = Column(String(64))
    updated_by      = Column(String(64))
    #
    # type          = ???