"""
  aim: reflect an existing table to the Table object
  A Table may be reflected, which means we generate the object based on what’s already present in a particular database.

Reference:
  - https://docs.sqlalchemy.org/en/14/tutorial/metadata.html#table-reflection
"""
from sqlalchemy import create_engine
from sqlalchemy import MetaData, Table, text


driver2db = create_engine(url="sqlite+pysqlite:///:memory:", echo=False, future=True)
table_name = 'table01'
# table setup from test_engine02.py
with driver2db.connect() as cnx2db:
    cnx2db.execute(text("CREATE TABLE %s (x int, y int)" % table_name))
    cnx2db.commit()

# table reflection
print('------table reflection------')
metadata = MetaData()
existed_table = Table(table_name, metadata, autoload_with=driver2db)
print(existed_table.columns.keys())

