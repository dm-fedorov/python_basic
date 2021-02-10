from sqlite3 import connect

class DBSQLite_context:
    # выполняется в самом начале
    def __init__(self, name_db):        
        self.name_db = name_db
        
     # выполняется перед блоком with
    def __enter__(self):
        self.conn = connect(self.name_db)
        self.c = self.conn.cursor()
        return self.c
        
    # выполняется после блока with,
    # параметры понадобятся позже
    # для обработки исключений
    def __exit__(self, exc_type, exc_value, exc_trace): 
         self.conn.commit()
         self.c.close()
         self.conn.close() 
         
with DBSQLite_context("my_database.sqlite") as cursor:
    sql = """SELECT * FROM users;"""
    data = cursor.execute(sql).fetchall()

print(data)
        
