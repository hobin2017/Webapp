"""
  The fundamental database interactive object used by the ORM is called the `Session`. The Session object has a Connection
object internally which it uses to emit SQL.

Reference:
  - https://docs.sqlalchemy.org/en/14/tutorial/dbapi_transactions.html#executing-with-an-orm-session
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy import text


driver2db = create_engine(url="sqlite+pysqlite:///:memory:", echo=True, future=True)

with Session(driver2db) as sess2db:
    # The Session can be used in the manner similar to the Connection object.
    cursor_result = sess2db.execute(text('select "hello world"'))
    sql_result = cursor_result.all()
    print(sql_result)

