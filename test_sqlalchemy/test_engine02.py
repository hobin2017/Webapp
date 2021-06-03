"""

Reference:
  - https://docs.sqlalchemy.org/en/14/tutorial/dbapi_transactions.html
"""
from sqlalchemy import create_engine
from sqlalchemy import text


driver2db = create_engine("sqlite+pysqlite:///:memory:", echo=True, future=True)

# https://docs.sqlalchemy.org/en/14/tutorial/dbapi_transactions.html#committing-changes
with driver2db.connect() as cnx2db:
    cnx2db.execute(text("CREATE TABLE table01 (x int, y int)"))
    # the text() construct use the colon format for parameters
    cnx2db.execute(text("INSERT INTO table01 (x, y) VALUES (:x, :y)"),
        [{"x": 1, "y": 1}, {"x": 2, "y": 4}]
    )
    # The transaction is not committed automatically
    cnx2db.commit()

print('---------')
# https://docs.sqlalchemy.org/en/14/tutorial/dbapi_transactions.html#fetching-rows
with driver2db.connect() as cnx2db02:
    cursor_result = cnx2db02.execute(text('SELECT * FROM table01'))  # The result can be consumed only once
    # The Row objects are intended to act like Python named tuples.
    for row_obj in cursor_result:
        print(row_obj.x, row_obj.y)

    cursor_result = cnx2db02.execute(text('SELECT * FROM table01'))
    # The RowMapping objects act like Python dictionary.
    for row_obj in cursor_result.mappings():
        print(row_obj.get('x'), row_obj.get('y'))


