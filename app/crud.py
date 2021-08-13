import sqlite3
import json

# 定義資料庫位置
db_file = 'fastapi_db.db'

repair_info_key_arr = ['id', 'school', 'name', 'tel', 'device_type', 'repair_description', 'start_time', 'end_time', 'status', 'repair_record']


def crud_get_repair_info_db():
    # 與 db_file 建立連結
    conn = sqlite3.connect(db_file)
    # cursor_arr = conn.execute('select * from repair_info;')
    conn.row_factory = sqlite3.Row  # This enables column access by name: row['column_name']
    db = conn.cursor()
    rows = db.execute('''
        SELECT * from repair_info
        ''').fetchall()
    conn.commit()
    conn.close()
    return rows


def crud_post_repair_info_db(post_school, post_name, post_tel, post_device_type, post_repair_description, post_start_time, post_status):
    conn = sqlite3.connect(db_file)
    school = post_school
    name = post_name
    tel = post_tel
    device_type = post_device_type
    repair_description = post_repair_description
    start_time = post_start_time
    status = post_status
    sql_str = "insert into repair_info(school, name, tel, device_type, repair_description, start_time, status) values('{}','{}','{}','{}','{}','{}','{}');".format(school, name, tel, device_type, repair_description, start_time, status)
    conn.execute(sql_str)
    conn.commit()
    conn.close()
