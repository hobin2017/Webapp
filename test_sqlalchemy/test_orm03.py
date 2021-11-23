"""
  aim: execute select/insert/update with table-class

Reference:
  - https://docs.sqlalchemy.org/en/14/tutorial/orm_data_manipulation.html
  - [Update class](https://docs.sqlalchemy.org/en/14/core/dml.html#sqlalchemy.sql.expression.Update)
"""
from sqlalchemy import create_engine
from sqlalchemy import MetaData, Table, Column, Integer, String
from sqlalchemy.orm import declarative_base, Session, aliased
from sqlalchemy import insert, select, update


Base = declarative_base()  # sqlalchemy.orm.decl_api.DeclarativeMeta


class User(Base):
    __tablename__ = 'user_account'
    id = Column(Integer, primary_key=True)
    name = Column(String(30))
    fullname = Column(String)

    def __repr__(self):
        return f"""User(id={self.id!r}, name={self.name!r}, fullname={self.fullname!r})"""


driver2db = create_engine(url="sqlite+pysqlite:///:memory:", echo=False, future=True)
# new tables
Base.metadata.create_all(driver2db)


print('------insert------')
# https://docs.sqlalchemy.org/en/14/tutorial/orm_data_manipulation.html#instances-of-classes-represent-rows
user01 = User(name='1', fullname='01')  # the instance of table-class represents a row
user02 = User(name='2', fullname='02')
#
sess2db = Session(driver2db)
sess2db.add(user01)
sess2db.add(user02)
#
sess2db.flush()  # send the pending changes to database
sess2db.commit()
sess2db.close()

print('------update------')
with Session(driver2db) as sess2db:
    sess2db.execute(
        update(User).where(  # where-clause
            User.name == '1',
            User.fullname == '01',  # and logic
        ).values(  # set-clause
            # User.fullname == '-1',  # wrong style
            fullname='-1',
        )
    )
    sess2db.commit()

print('------select------')
with Session(driver2db) as sess2db:
    result = sess2db.execute(select(User))
    # https://docs.sqlalchemy.org/en/14/orm/queryguide.html#selecting-orm-entities-and-attributes
    # the scalars function skip the generation of Row object
    for user_obj in result.scalars():
        print(user_obj)  # instance of the `User` class

