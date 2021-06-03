"""

Reference:
  - https://docs.sqlalchemy.org/en/14/tutorial/engine.html#tutorial-engine
  - https://docs.sqlalchemy.org/en/14/tutorial/dbapi_transactions.html
"""
from sqlalchemy import create_engine
from sqlalchemy import text

# url parameter:
# sqlite represents the database type
# pysqlite represents the database driver
# /:memory: represents the database location
#
# future parameter: Use the 2.0 style
driver2db = create_engine(url="sqlite+pysqlite:///:memory:", echo=True, future=True)

with driver2db.connect() as cnx2db:
    # sql_result = cnx2db.execute('select "hello world"')  # sqlalchemy.exc.ObjectNotExecutableError
    cursor_result = cnx2db.execute(text('select "hello world"'))
    sql_result = cursor_result.all()
    print(sql_result)

