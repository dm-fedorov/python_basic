import tkinter
import tkinter.messagebox as messagebox
from PIL import Image, ImageTk
import requests
from io import BytesIO


# Класс, который хранит данные текущего заказа
class Cart:
    def __init__(self):
        self.cart = {}

    def get_number(self, pizza_name):
        if pizza_name in self.cart:
            return self.cart[pizza_name]
        else:
            return 0

    def get_pizzas(self):
        result = []
        for name in list(self.cart.keys()):
            result.append([name, self.cart[name]])

        return result

    def add_pizza(self, pizza_name):
        if pizza_name in self.cart:
            self.cart[pizza_name] += 1
        else:
            self.cart[pizza_name] = 1


# Класс, позволяющий осуществлять навигацию в приложении
class MainLayoutManager:

    def __init__(self, main_container, cart_container, cart_page):
        self.pages = {
            "menu": main_container,
            "cart": cart_container
        }

        self.cart_page = cart_page

        self.chosen_page = "main"
        main_container.tkraise()

    def navigate_to(self, name):
        if name == "Меню":
            page = self.pages["menu"]
            page.tkraise()

        elif name == "Корзина":
            page = self.pages["cart"]
            page.tkraise()

            # Добавляет актуальные данные на страницу
            self.cart_page.render()


# Класс, отвечающий за боковое меню и навигацию в нем
class SideBar(tkinter.Frame):
    def __init__(self, master, main_layout, font_color="black", bg_color="white"):
        tkinter.Frame.__init__(self, master, bg=bg_color)

        self.bg_color = bg_color
        self.font_color = font_color

        self.main_layout = main_layout
        self.navigation = ["Меню", "Корзина", ]

        self.buttons = {}

    def draw(self):
        self.grid(row=0, column=0, sticky='nw')
        count = 0

        for nav in self.navigation:
            if count == 0:
                bg_color = "#B0DDF5"
            else:
                bg_color = self.bg_color

            btn = tkinter.Label(self, text=nav, bg=bg_color, width=8,
                                foreground=self.font_color, anchor="nw", font=("Arial", 14), cursor="hand2")
            btn.grid(row=count, column=0, sticky='nw', padx=(10, 10), pady=(5, 5))
            count += 1
            btn.bind('<Button-1>', self.set_navigation(nav))
            self.buttons[nav] = btn

    def set_navigation(self, name):
        def _navigate_to(arg):
            self.main_layout.navigate_to(name)
            for button_name in list(self.buttons.keys()):
                if button_name == name:
                    self.buttons[button_name].config(bg="#B0DDF5")
                else:
                    self.buttons[button_name].config(bg="white")

        return _navigate_to


# Виджеты с информацией о пицце
class PizzaWidget(tkinter.Frame):
    rows_count = 0

    def __init__(self, master, name, price, size, description, image, cart,
                 bg_color="black", font_color="yellow",
                 button_bg="green", button_font="red"):
        tkinter.Frame.__init__(self, master, bg=bg_color, width=550)

        self.name = name
        self.price = price
        self.size = size
        self.description = description
        self.image = image
        self.columns_count = 0
        self.cart = cart
        self.bg_color = bg_color
        self.font_color = font_color
        self.button_bg = button_bg
        self.button_font = button_font

    def draw(self):
        self.grid(row=PizzaWidget.rows_count, column=0, sticky="new", padx=(25, 40), pady=(5, 5))
        PizzaWidget.rows_count += 1

        pic_path = self.image

        response = requests.get(pic_path, stream=True)
        pizza_pic = Image.open(BytesIO(response.content))
        pic = ImageTk.PhotoImage(pizza_pic)

        pizza_pic_label = tkinter.Label(self, image=pic, bg=self.bg_color, width=150)
        pizza_pic_label.image = pic
        pizza_pic_label.grid(row=0, column=0)

        pizza_content = tkinter.Frame(self, bg=self.bg_color, width=400)
        pizza_content.grid(row=0, column=1, sticky="nw")

        pizza_header = tkinter.Label(pizza_content, text=self.name, bg=self.bg_color, wraplength=400,
                                     foreground=self.font_color, anchor="nw", font=("Arial", 14))
        pizza_header.grid(row=0, column=0, padx=(10, 0), sticky="nw")

        pizza_price = tkinter.Label(pizza_content, text=f"{self.size} см - {self.price}руб.",
                                    bg=self.bg_color, wraplength=400,
                                    foreground=self.font_color, anchor="nw", font=("Arial", 12))
        pizza_price.grid(row=1, column=0, padx=(10, 0), pady=(5, 5), sticky="nw")

        pizza_description = tkinter.Label(pizza_content, text=self.description, bg=self.bg_color,
                                          foreground=self.font_color, anchor="nw", font=("Arial", 12),
                                          wraplength=400)
        pizza_description.grid(row=2, column=0, padx=(10, 0), pady=(5, 5), sticky="nw")

        pizza_order_btn = tkinter.Label(pizza_content, text="Добавить в корзину", cursor="hand2",
                                        height=2, width=30,
                                        bg=self.button_bg, foreground=self.button_font, font=("Arial", 12))
        pizza_order_btn.grid(row=3, column=0, padx=(10, 0), pady=(5, 0), sticky="nw")

        pizzas_count_label = tkinter.Label(pizza_content, text=f"В корзине {self.cart.get_number(self.name)}",
                                           bg=self.bg_color, foreground=self.font_color, font=("Arial", 10))
        pizzas_count_label.grid(row=4, column=0, padx=(10, 0), pady=(0, 0), sticky="nw")

        def add_pizza_to_cart(arg):
            self.cart.add_pizza(self.name)
            pizzas_count_label.config(text=f"В корзине {self.cart.get_number(self.name)}")

        pizza_order_btn.bind('<Button-1>', add_pizza_to_cart)


# Страница с заказом
class CartPage(tkinter.Frame):
    def __init__(self, master, cart, pizzas_data, font_color="black",
                 bg_color="white", button_bg="blue", button_font="white"):
        tkinter.Frame.__init__(self, master, bg=bg_color)

        self.cart = cart
        self.font_color = font_color
        self.bg_color = bg_color
        self.button_bg = button_bg
        self.button_font = button_font
        self.pizzas_data = pizzas_data
        self.layouts = []

    def draw(self):
        self.grid(row=0, column=0, sticky="nw", padx=(25, 10), pady=(5, 5))

        empty_layout = tkinter.Frame(self, bg=self.bg_color, width=519, height=550)
        empty_layout.grid(row=0, column=0, sticky="ns")
        not_empty_layout = tkinter.Frame(self, bg=self.bg_color, width=519, height=550)
        not_empty_layout.grid(row=0, column=0, sticky="ns")
        empty_layout.tkraise()

        border = tkinter.Frame(self, bg=self.bg_color, width=1, height=550)
        border.grid(row=0, column=1, sticky="ns")

        self.layouts = [empty_layout, not_empty_layout]

        text = tkinter.Label(empty_layout, text="Корзина пуста! Вернитесь в меню, чтобы добавить товары",
                             bg=self.bg_color, wraplength=519,
                             foreground=self.font_color, anchor="nw", font=("Arial", 14))
        text.grid(row=0, column=0, padx=(10, 0), sticky="nw")

        self.render()
        empty_layout.tkraise()

    def render(self):
        orders = self.cart.get_pizzas()
        if len(orders) == 0:
            self.layouts[0].tkraise()
        else:
            self.layouts[1].tkraise()

            for widgets in self.layouts[1].winfo_children():
                widgets.destroy()

            text = tkinter.Label(self.layouts[1], text="Ваш заказ",
                                 bg=self.bg_color, foreground=self.font_color, anchor="nw", font=("Arial", 16))
            text.grid(row=0, column=0, padx=(10, 0), sticky="nw")

            border1 = tkinter.Frame(self.layouts[1], width=519, height=4, bg=self.button_bg)
            border1.grid(row=1, column=0, padx=(5, 5), sticky="we")

            table = tkinter.Frame(self.layouts[1], bg=self.bg_color, width=519)
            table.grid(row=2, column=0, sticky="nw", pady=(20, 30))

            count = 0
            for name in ["Название", "Количество", "Стоимость"]:
                text = tkinter.Label(table, text=name,
                                     bg=self.bg_color, foreground=self.font_color, anchor="nw", font=("Arial", 14))
                text.grid(row=0, column=count, padx=(10, 0), pady=(5, 15), sticky="nw")
                count += 1

            for i in range(len(orders)):
                price = int()
                for pizza in self.pizzas_data:
                    if pizza["name"] == orders[i][0]:
                        price = pizza["price"]
                orders[i].append(int(price) * int(orders[i][1]))

            count_y = 1
            for order in orders:
                count_x = 0
                for pos in order:

                    text = tkinter.Label(table, text=pos,
                                         bg=self.bg_color,
                                         foreground=self.font_color, anchor="nw", font=("Arial", 12))
                    text.grid(row=count_y, column=count_x, padx=(10, 5), sticky="nw")
                    count_x += 1

                count_y += 1

            border2 = tkinter.Frame(self.layouts[1], width=519, height=4, bg=self.button_bg)
            border2.grid(row=3, column=0, padx=(5, 5), sticky="we")

            text = tkinter.Label(self.layouts[1], text="Чтобы сделать заказ, введите ваш адрес в форму ниже",
                                 wraplength=520,
                                 bg=self.bg_color, foreground=self.font_color, anchor="nw", font=("Arial", 14))
            text.grid(row=4, column=0, padx=(10, 0), pady=(15, 5), sticky="nw")

            address_field = tkinter.Entry(self.layouts[1], bg=self.bg_color,
                                          foreground=self.font_color, font=("Arial", 12))
            address_field.grid(row=5, column=0, padx=(10, 10), pady=(15, 25), sticky="new")

            order_btn = tkinter.Label(self.layouts[1], text="Заказать", cursor="hand2",
                                      height=2, width=30,
                                      bg=self.button_bg, foreground=self.button_font, font=("Arial", 12))
            order_btn.grid(row=6, column=0, padx=(10, 0), pady=(5, 20), sticky="se")

            order_btn.bind('<Button-1>', self.show_message(f"Ваш заказ принят! Ожидайте доставки в течение 40 минут."))

    def show_message(self, info):
        def _show_message(args):
            messagebox.showinfo(message=info)

        return _show_message


# Данные о пицце
pizzas = [
    {
        "name": "Четыре сыра",
        "image": "https://raw.githubusercontent.com/artemmufazalov/file_storage/master/cheesy.png",
        "description": "Почувствуй вкус лучших сыров!",
        "price": 550,
        "size": 30
    },
    {
        "name": "Гавайская",
        "image": "https://raw.githubusercontent.com/artemmufazalov/file_storage/master/hawaiian.png",
        "description": "Идеальное сочетание курицы и ананаса!",
        "price": 600,
        "size": 30
    },
    {
        "name": "Грибная",
        "image": "https://raw.githubusercontent.com/artemmufazalov/file_storage/master/mushrooms.png",
        "description": "Грибы и курица, очень вкусно и очень сытно!",
        "price": 620,
        "size": 30
    },
]

main_bg_color = "white"
main_font_color = "black"

cart = Cart()

window = tkinter.Tk()
window.title("Pizza App")
window.configure(background=main_bg_color)
window.resizable(False, False)

# Устанавливаем иконку приложения
path = "https://raw.githubusercontent.com/artemmufazalov/file_storage/master/pizza.png"
response = requests.get(path, stream=True)
ico = Image.open(BytesIO(response.content))
photo = ImageTk.PhotoImage(ico)
window.wm_iconphoto(False, photo)

# Настраиваем скелет приложения
mainFrame = tkinter.Frame(window, width=800, height=600, bg=main_bg_color)
mainFrame.grid(row=0, column=0, padx=(10, 20), pady=(20, 40))

cart_content = tkinter.Frame(mainFrame, bg=main_bg_color, width=520, height=550)
cart_content.grid(row=0, column=1, sticky='nw')

main_content = tkinter.Frame(mainFrame, bg=main_bg_color, width=520, height=550)
main_content.grid(row=0, column=1, sticky='nw')

cart_page = CartPage(cart_content, cart, pizzas,
                     font_color=main_font_color,
                     bg_color=main_bg_color,
                     button_bg="blue",
                     button_font="white")

cart_page.draw()

# Устанавливаем для страниц меню и корзины навигацию
main_layout = MainLayoutManager(main_container=main_content, cart_container=cart_content, cart_page=cart_page)

side_bar = SideBar(mainFrame, main_layout)
side_bar.draw()


for pizza in pizzas:
    pizza_widget = PizzaWidget(main_content,
                               pizza["name"], pizza["price"],
                               pizza["size"], pizza["description"],
                               pizza["image"], cart,
                               font_color=main_font_color,
                               bg_color=main_bg_color,
                               button_bg="blue",
                               button_font="white")

    pizza_widget.draw()

window.mainloop()
