This tutorial is from the [official website](https://docs.sqlalchemy.org/en/14/)

# test
- test_orm01.py: create a new table
- test_orm02.py: table reflection
- test_orm03.py: insert, update, select

# concept
- [instance of table class](https://docs.sqlalchemy.org/en/14/tutorial/orm_data_manipulation.html#instances-of-classes-represent-rows)
> An instance of the table class represents a row. 
- [cte](https://docs.sqlalchemy.org/en/14/tutorial/data_select.html#orm-entity-subqueries-ctes)
> One advantage is the generated table can be used more than once.
```sql
WITH t1 AS (
  SELECT * FROM table01
)
```
