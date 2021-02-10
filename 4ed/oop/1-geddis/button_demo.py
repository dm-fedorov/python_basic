# Эта программа демонстрирует элемент интерфейса Button.
# Когда пользователь нажимает кнопку Button, 
# на экран выводится информационное диалоговое окно.

import tkinter
import tkinter.messagebox

class SimpleGUI:
    
    def __init__(self):
        self.window = tkinter.Tk()

        # Когда пользователь нажимает кнопку, 
        # должен быть исполнен метод click.
        self.button = tkinter.Button(self.window,
                                        text='Нажми меня!',
                                        command=self.click)

        self.button.pack()

        # Войти в главный цикл tkinter.
        tkinter.mainloop()

    def click(self):
        # Показать информационное диалоговое окно.
        tkinter.messagebox.showinfo('Информационное окно',
                                    'Спасибо, что нажали на меня!')

simple_gui = SimpleGUI()
