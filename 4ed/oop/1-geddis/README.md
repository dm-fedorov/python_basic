
Программа рисует окно в ООП стиле:

#oop_tkinter_01.py
import tkinter

class SimpleGUI:
    def __init__(self):
        # создаем корневое окно
        self.window = tkinter.Tk()
        tkinter.mainloop()

# создаем экземпляр класса MyGUI
simple_gui = SimpleGUI()


Программа рисует окно с текстом в ООП стиле:

#oop_tkinter_02.py
import tkinter

class SimpleGUI:
    def __init__(self):

        self.window = tkinter.Tk()
        self.label = tkinter.Label(self.window,
                                   text='Привет, мир!')
        self.label.pack()
        tkinter.mainloop()

# Создать экземпляр класса MyGUI.
simple_gui = SimpleGUI() 

Нажатие на кнопку приводит к появлению информационного диалогового окна.

#oop_tkinter_03.py
import tkinter
import tkinter.messagebox

class SimpleGUI:
    def __init__(self):
        self.window = tkinter.Tk()

        # В момент нажатия на кнопку, 
        # исполняется метод click
        self.button = tkinter.Button(self.window,
                                     text='Нажми меня!',
                                     command=self.click)
        self.button.pack()
        tkinter.mainloop()

    def click(self):
        # информационное диалоговое окно.
        tkinter.messagebox.showinfo('Информационное окно',
                                    'Спасибо, что нажали на меня!')

simple_gui = SimpleGUI()


Реализация примера с помощью ООП.

#oop_tkinter_04.py
import tkinter

class ConverterGUI:
    def __init__(self):
        self.window = tkinter.Tk()

        self.label_1 = tkinter.Label(self.window,
                                   text='Введите число:')
        self.label_1.pack()

        self.entry = tkinter.Entry(self.window)
        self.entry.pack()
        
        self.label_2 = tkinter.Label(self.window,
                                         text='Преобразовано:')
        self.label_2.pack()

        self.value = tkinter.StringVar()

        self.label_3 = tkinter.Label(self.window,
                                         textvariable=self.value)
        self.label_3.pack()    
                
        self.button = tkinter.Button(self.window,
                                          text='Преобразовать',
                                          command=self.convert)
        self.button.pack()

        self.quit_button = tkinter.Button(self.window,
                                          text='Выйти',
                                          command=self.window.destroy)
        self.quit_button.pack()

        tkinter.mainloop()

    def convert(self):

        try:            
            # Преобразованное значение из виджета self.entry
            # помещаем в переменную self.value,
            # автоматически обновляется self.label_3 из-за
            # привязки к переменной self.value.
            self.value.set(float(self.entry.get()) * 3.14)
        except Exception:
            self.value.set("Ошибка ввода")
            
convert = ConverterGUI()
