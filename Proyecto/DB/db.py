from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine('sqlite:///database.sqlite3',convert_unicode = True)
db_session = scoped_session(sessionmaker(autocommit = False, autoflush = False, bind = engine))

Base = declarative_base()
Base.query = db_session.query_property()

def init_db():
    from models import Department, Employee, Role #importar aqui todos los modulos a utilizar
    Base.metadata.drop_all(bind = engine)
    Base.metadata.create_all(bind = engine)

    #crear fixtures
    engineering = Department(name = 'Engineering')
    db_session.add(engineering)
    hr = Department(name = 'Human Resources')
    db_session.add(hr)

    manager = Role(name = 'manager')
    db_session.add(manager)
    engineer = Role(name = 'engineer')
    db_session.add(engineer)

    peter = Employee(name = 'Peter', department = engineering, role = engineer)
    db_session.add(peter)
    roy = Employee(name = 'Roy', department = engineering, role = engineer)
    db_session.add(roy)
    tracy = Employee(name = 'Tracy', department = hr, role = manager)
    db_session.add(tracy)

    db_session.commit()
