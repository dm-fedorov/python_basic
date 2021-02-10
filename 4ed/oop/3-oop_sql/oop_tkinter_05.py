#oop_tkinter_05.py
import tkinter
from sqlite3 import connect

class DBSQLite:
    def __init__(self, name_db):        
        self.conn = connect(name_db)
        self.c = self.conn.cursor()
        
    def select(self):
        self.date = self.c.execute("""SELECT * FROM users;""").fetchall()
        return self.date

    def execute(self, sql):
        self.date = self.c.execute(sql).fetchall()
        self.conn.commit()
        return self.date

    # при уничтожении объекта закрываем соединение
    def __del__(self):        
        self.c.close()
        self.conn.close()
        
class ConverterGUI:
    def __init__(self):
        self.window = tkinter.Tk()

        self.label_2 = tkinter.Label(self.window,
                                                    text='Получено:')
        self.label_2.pack()

        self.label_3 = tkinter.Label(self.window)
        self.label_3.pack()    
                
        self.button = tkinter.Button(self.window,
                                                     text='Загрузить!',
                                                     command=self.click)
        self.button.pack()

        self.quit_button = tkinter.Button(self.window,
                                                              text='Выйти',
                                                              command=self.window.destroy)
        self.quit_button.pack()

        tkinter.mainloop()

    def click(self):
        try:

            db_conn = DBSQLite("my_database.sqlite")            
            self.label_3.config(text=str(db_conn.select()))
        except Exception as err:
            self.label_3.config(text=err)
            
convert = ConverterGUI()
