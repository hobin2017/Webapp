from sqlalchemy import create_engine, text
from sqlalchemy.orm import Session


def upsert(sess2db, table_name, main_info):
    """
      Do insert-statement if no id.
      Do update-statement if id has a value and exists in db.
      Do insert-statement if id has a value and does not exist in db.
    """
    main_id = main_info.get('id')
    main_jenkin_build_id = main_info.get('jenkin_build_id', '')
    if main_id:
        # try to update at first
        stmt_obj = text(f'UPDATE {table_name} SET jenkin_build_id="{main_jenkin_build_id}" WHERE id = {main_id}')
        sql_result = sess2db.execute(stmt_obj)
        _rowcount = sql_result.rowcount
        if _rowcount != 0:
            if _rowcount > 1:
                print('upsert: only one row should be updated')
                return
            elif _rowcount == 1:
                print(f'upsert: update {main_info}')
                return
        # rowcount = 0
        # insert with id
        stmt_obj = text(f"INSERT INTO {table_name} (id, jenkin_build_id) VALUES ({main_id}, '{main_jenkin_build_id}')")
        sess2db.execute(stmt_obj)
        print(f'upsert: insert {main_info}')
        return

    # insert without id
    stmt_obj = text(f"INSERT INTO {table_name} (jenkin_build_id) VALUES ('{main_jenkin_build_id}')")
    sess2db.execute(stmt_obj)
    print(f'upsert: insert {main_info}')
    return


def init_table(sess2db, table_name):
    sess2db.execute(text(f"""
    CREATE TABLE {table_name} (id INTEGER PRIMARY KEY AUTOINCREMENT, jenkin_build_id VARCHAR UNIQUE)
    """))
    sess2db.execute(text(f"INSERT INTO {table_name} (jenkin_build_id) VALUES ('1')"))


if __name__ == '__main__':
    driver2db = create_engine(url="sqlite+pysqlite:///:memory:")
    # 
    test_table = 'test01'
    with Session(driver2db) as sess:
        init_table(sess, test_table)
        # upsert=update/insert
        upsert(sess, test_table, {'id': 1, 'jenkin_build_id': '11'})
        upsert(sess, test_table, {'id': 2, 'jenkin_build_id': '2'})
        upsert(sess, test_table, {'id': 2, 'jenkin_build_id': '22'})
        upsert(sess, test_table, {'jenkin_build_id': '3'})
        
        print('---verify---')
        _val = sess.execute(text(F'SELECT * FROM {test_table}'))
        _val = _val.mappings().all()
        print(_val)
