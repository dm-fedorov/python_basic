
Пример создания базы данных:

>>> from sqlite3 import connect
>>> conn = connect("my_database.sqlite")

Создание курсора:

>>> c = conn.cursor()
>>> c.execute("""
CREATE TABLE users (id, first_name, last_name)
""")
<sqlite3.Cursor object at 0x7f61d6385030>
>>> c.execute("""
INSERT INTO users (id, first_name, last_name) VALUES (1, "Ivan", "Petrov");
""")
<sqlite3.Cursor object at 0x7f61d6385030>
>>> c.execute("""
INSERT INTO users (id, first_name, last_name) VALUES (2, "Mark", "Ivanov");
""")
<sqlite3.Cursor object at 0x7f61d6385030>
>>> c.execute("""
SELECT * FROM users;
""").fetchall()
[(1, 'Ivan', 'Petrov'), (2, 'Mark', 'Ivanov')]
>>> conn.commit()
>>> conn.close()
>>> 