import os
import pymysql
from dotenv import load_dotenv
import pandas as pd
from daebakai import db
load_dotenv()

rows = None

class chat_Database():
    def a():
        return "1"
    def show_table(name):
        db1 = os.getenv("DB")
        sql = f'''
        SELECT 1 FROM Information_schema.tables
        WHERE table_schema = '{db1}'
        AND table_name = '{name}'
        '''
        cursor = db.get_db().cursor()
        execute_sql = cursor.execute(sql)
        print(execute_sql,"테스트테스트")
        rows = cursor.fetchall()
        cursor.close()
        return execute_sql
    def create_table(name):
        pw = os.getenv("PASSWORD")
        user = os.getenv("USER_USER")
        db = os.getenv("DB")
        connection = None
        rows = None
        try:
            connection = pymysql.connect(host='tusiworks.iptime.org',
                                     user= user,
                                     password= pw,
                                     db=db,
                                     port=3308,
                                     charset='utf8mb4',
                                     cursorclass=pymysql.cursors.DictCursor)
            if connection:
                with connection.cursor() as cursor:
                    sql = f'''
                        CREATE TABLE {name}(
                            id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
                            c_id INT NOT NULL,
                            name VARCHAR(30) NOT NULL,
                            message TEXT NOT NULL,
                            time VARCHAR(100) NOT NULL,
                            YMH VARCHAR(100) NOT NULL,
                            FOREIGN KEY(c_id) REFERENCES user(id)
                        )ENGINE=InnoDB DEFAULT CHARSET=utf8mb4
                    '''
                    cursor.execute(sql)
                rows = cursor.fetchall()
                connection.commit()
        except Exception as e:
            print('->', e)
            rows = None
        finally:
            if connection:
                connection.close()
        return rows
    def insert_message(c_number, c_name, message, c_time, c_YMH, name):
        sql = f'''
        INSERT INTO {name}(c_id, name, message, time, YMH)
        values({c_number},'{c_name}', '{message}', '{c_time}', '{c_YMH}')
        '''
        cursor = db.get_db().cursor()
        cursor.execute(sql)
        db.get_db().commit()
        cursor.close()
        return rows
    def select_keyword():
        sql = f'''
        SELECT name from chatbot_keyword
        '''
        cursor = db.get_db().cursor()
        execute_sql = cursor.execute(sql)
        rows = cursor.fetchall()
        cursor.close()
        return rows

class bot_Database():
    def a():
        return "1"
    def show_table(name):
        db1 = os.getenv("DB")
        sql = f'''
        SELECT 1 FROM Information_schema.tables
        WHERE table_schema = '{db1}'
        AND table_name = '{name}'
        '''
        cursor = db.get_db().cursor()
        execute_sql = cursor.execute(sql)
        print(execute_sql,"테스트테스트")
        rows = cursor.fetchall()
        cursor.close()
        return execute_sql

    def select_basic_bot():
        sql = f'''
        SELECT * from daebak_bot
        where id = "1"
        '''
        cursor = db.get_db().cursor()
        execute_sql = cursor.execute(sql)
        rows = cursor.fetchall()
        cursor.close()
        return rows
    def select_content(cont):
        sql = f'''
        SELECT * from daebak_bot
        where base_keyword = "{cont}"
        '''
        cursor = db.get_db().cursor()
        execute_sql = cursor.execute(sql)
        rows = cursor.fetchall()
        cursor.close()
        return rows
    def test():
        sql = f'''
        select base_keyword from daebak_bot
        '''
        cursor = db.get_db().cursor()
        execute_sql = cursor.execute(sql)
        rows = cursor.fetchall()
        cursor.close()
        return rows



class Database():
    rows = None
    def read_table(name, my_id):
        sql = f'''
        SELECT * from {name}
        WHERE c_id = '{my_id}'
        '''
        cursor = db.get_db().cursor()
        execute_sql = cursor.execute(sql)
        rows = cursor.fetchall()
        cursor.close()
        print(rows)
        return rows
