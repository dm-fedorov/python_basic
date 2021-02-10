#with_errors.py
from sqlite3 import connect
import sqlite3

class DBSQLite_context:
    # выполняется в самом начале
    def __init__(self, name_db):        
        self.name_db = name_db
        
     # выполняется перед блоком with
    def __enter__(self):
         self.conn = connect(self.name_db)
         self.c = self.conn.cursor()
         return self.c
        
    def __exit__(self, exc_type, exc_value, exc_trace): 
         self.conn.commit()
         self.c.close()
         self.conn.close()

# обработка исключений внтури with
try:
    with DBSQLite_context("my_database.sqlite") as cursor:
        sql = """SELECT * FROM users;"""
        data = cursor.execute(sql).fetchall()
        print(data)
    
except Exception as err:
    print("Что-то пошло не так", str(err))
    
        
