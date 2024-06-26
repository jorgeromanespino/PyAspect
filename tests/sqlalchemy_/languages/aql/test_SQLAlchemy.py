#
import pytest
import sqlalchemy
from aspect.sqlalchemy.entities.Entity import Entity, Base

#
def create_engine_and_session():
    engine = sqlalchemy.create_engine('mysql+pymysql://pyaspectuserdb:aspectuserpassword2020p@localhost:3306/pyaspectdb')
    Base.metadata.create_all(engine)
    session = sqlalchemy.orm.sessionmaker(bind=engine)()
    return (engine, session)

#
engine, session = create_engine_and_session()
 
#
def test_db_connection_write_and_read_entity():
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

