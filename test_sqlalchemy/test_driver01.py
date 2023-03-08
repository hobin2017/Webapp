"""

Reference:
  - [psycopg2](https://docs.sqlalchemy.org/en/20/dialects/postgresql.html#module-sqlalchemy.dialects.postgresql.psycopg2)
"""
from sqlalchemy import create_engine


# psycopg2
# pip install psycopg2
# format: postgresql+psycopg2://user:password@host:port/dbname[?key=value&key=value...]
url = "postgresql+psycopg2://postgres:password01@127.0.0.1:5432/database01"

#
driver2db = create_engine(url=url)
