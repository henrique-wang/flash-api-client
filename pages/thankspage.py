import tkinter as tk
from tkinter import ttk

LARGEFONT = ("Verdana", 35)
MEDIUMFONT = ("Verdana", 20)

class Shopping_4(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        # First Line
        label_1 = ttk.Label(self, text="Muito obrigado pela compra :D",
                            font=MEDIUMFONT)
        label_1.place(relx=0.5, rely=0.4, anchor='center')

        # Second Line
        label_2 = ttk.Label(self, text="Volte sempre!!!",
                            font=MEDIUMFONT)
        label_2.place(relx=0.5, rely=0.5, anchor='center')

        button_newShopping = tk.Button(self, text="Iniciar nova compra",
                                  command=lambda: self.go_to_home(controller), bg='#ffb3fe')
        button_newShopping.place(relx=0.9, rely=0.8, anchor='se')

    def go_to_home(self, controller):
        controller.cart = None
        controller.show_frame("HomeClient")