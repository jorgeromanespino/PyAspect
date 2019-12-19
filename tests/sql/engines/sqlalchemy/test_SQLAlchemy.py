#
import pytest
#
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
# Always do this
Base = declarative_base() 
from sqlalchemy.orm import sessionmaker

#
import datetime
from sqlalchemy import Column, Integer, String, DateTime

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
    # type            =

# class Type(Entity):
#     __tablename__ = 'type'
#     #
#     local_name      = Column(String(512))
#     local_namespace = Column(String(512))

#
def create_engine_and_session():
    engine = sqlalchemy.create_engine('mysql+pymysql://aspectuserdb:aspectuserpassword2015p@localhost:3306/aspectdb')
    Base.metadata.create_all(engine)
    session = sessionmaker(bind=engine)()
    return (engine, session)
#
def test_db_connection_write_and_read_entity():
    #
    engine, session = create_engine_and_session()
    #
    e1 = Entity(name='John')
    session.add(e1)
    session.commit()
    #
    e1_read = session.query(Entity).filter_by(name='John').first()
    #
    session.delete(e1)
    session.commit()
    #
    assert e1_read.name == 'John'

# #
# def test_db_connection_write_and_read_type():
#     t1 = Type(id=1)
