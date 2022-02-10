"""
Software developed by: Psmotta

Version 0.1

This software was developed for better understanding Python language
and its an open source code for all students lern more about it.

Date of criation: 02/05/2022
"""

from cgitb import text
from lib2to3.pgen2.token import NUMBER
import random
from symtable import Symbol
from textwrap import fill
from tkinter import *


def password_generator():

    low = "abcdefghijklmnopqrstuvwxyz"
    up = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    NUMBER = "0123456789"
    Symbol = "[]{}%#()*/"

    all = low + up + NUMBER + Symbol
    length = 15
    password = "".join(random.sample(all, length))

    password_text["text"] = password


window = Tk()
window.title("Random Password Genarator")
window.geometry("400x150")

principal_text = Label(window, text="Click to generate your random password")
principal_text.grid(column=0, row=0, padx=90, pady=10)

button = Button(window, text="Generate your password", command=password_generator)
button.grid(column=0, row=3, padx=100, pady=10)

password_text = Label(window, text="")
password_text.grid(column=0, row=2, padx=90, pady=10)


window.mainloop()
