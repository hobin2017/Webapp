"""
  aim: create a new table
  A Table may be declared, which means we explicitly spell out in source code what the table looks like.
  A Table may be reflected, which means we generate the object based on what’s already present in a particular database.

Reference:
  - https://docs.sqlalchemy.org/en/14/tutorial/metadata.html
"""
from sqlalchemy import create_engine
from sqlalchemy import MetaData, Table, Column, Integer, String
from sqlalchemy.orm import declarative_base


# https://docs.sqlalchemy.org/en/14/tutorial/metadata.html#setting-up-metadata-with-table-objects
# Having a single MetaData object for an entire application is the most common case.
metadata = MetaData()
# Once we have a MetaData object, we can declare some Table objects.
user_table = Table(
    "user_account01",
    metadata,  # MetaData object
    Column('id', Integer, primary_key=True),
    Column('name', String(30)),
    Column('fullname', String)
)


# https://docs.sqlalchemy.org/en/14/tutorial/metadata.html#setting-up-the-registry
Base = declarative_base()  # sqlalchemy.orm.decl_api.DeclarativeMeta


class User(Base):
    __tablename__ = 'user_account02'
    id = Column(Integer, primary_key=True)
    name = Column(String(30))
    fullname = Column(String)


if __name__ == '__main__':
    print(user_table.columns.keys())
    print(user_table.primary_key)
    print('---------1st way---------')
    # https://docs.sqlalchemy.org/en/14/tutorial/metadata.html#emitting-ddl-to-the-database
    driver2db = create_engine(url="sqlite+pysqlite:///:memory:", echo=True, future=True)
    metadata.create_all(bind=driver2db, tables=[user_table])  # create tables
    metadata.drop_all(bind=driver2db, tables=[user_table])  # delete tables

    print('---------2nd way---------')
    Base.metadata.create_all(bind=driver2db)
    Base.metadata.drop_all(bind=driver2db)

