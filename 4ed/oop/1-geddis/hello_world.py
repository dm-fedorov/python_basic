import tkinter

class SimpleGUI:
    def __init__(self):

        self.main_window = tkinter.Tk()
        self.label = tkinter.Label(self.main_window,
                                   text='Привет, мир!')
        self.label.pack()
        tkinter.mainloop()

# Создать экземпляр класса MyGUI.
simple_gui = SimpleGUI() 
