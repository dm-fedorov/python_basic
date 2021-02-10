Удалим файл с базой данных и запустим программу.
Возникнет ошибка, т.к. таблица users не создана (базы данных нет):

Traceback (most recent call last):
sqlite3.OperationalError: no such table: users

Рассмотрим процесс обработки ошибок внутри инструкции with.
Здесь необходимо снова вернуться к теме обработки исключений.

Функция exc_info из стандартного модуля sys позволяет получить данные об исключении.
Запустим программу sys_info.py.

#sys_info.py
import sys

try:
    1/0
except:
    err = sys.exc_info()
    print(err)

В результате вернулся кортеж, который содержит тип исключения, значение исключения и объект трассировки:

(<class 'ZeroDivisionError'>, ZeroDivisionError('division by zero'), <traceback object at 0x7facd8b9c580>)

С этими значениями связаны параметры exc_type, exc_value, exc_trace метода __exit__.

Если исключение возникло в __enter__, то тело with и блок __exit__ выполняться не будут. 

Перечень возможных исключений в SQLite3:
https://docs.python.org/3/library/sqlite3.html#exceptions

Если исключение возникнет внутри тела инструкции with, то информация о нем будет передана 
методу __exit__ в виде трех аргументов. 

