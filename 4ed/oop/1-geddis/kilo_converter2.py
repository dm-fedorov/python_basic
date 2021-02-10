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
