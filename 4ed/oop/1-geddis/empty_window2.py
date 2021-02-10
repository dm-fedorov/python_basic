# Эта программа показывает пустое окно.

import tkinter

class SimpleGUI:
    def __init__(self):
        # создаем корневое окно
        self.main_window = tkinter.Tk()

        tkinter.mainloop()

# создаем экземпляр класса MyGUI
simple_gui = SimpleGUI()
