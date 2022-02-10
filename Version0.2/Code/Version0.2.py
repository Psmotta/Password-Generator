"""
Software developed by: Psmotta

Version 0.2

This software was developed for better understanding Python language
and its an open source code for all students lern more about it.

Date (m/d/Y)
Date of criation: 02/05/2022
Date of version: 02/10/2022

"""

from cgitb import text
from distutils import command
from lib2to3.pgen2.token import NUMBER
import random
from symtable import Symbol
from textwrap import fill
from tkinter import *
import pyperclip as pc


def password_generator():

    low = "abcdefghijklmnopqrstuvwxyz"
    up = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    NUMBER = "0123456789"
    Symbol = "[]{}%#()*/"

    all = low + up + NUMBER + Symbol
    length = int(lgt.get())
    password = "".join(random.sample(all, length))

    password_text["text"] = password


def copy_password():

    pc.copy(password_text["text"])


window = Tk()
window.title("Random Password Genarator")
window.geometry("470x220")
window.configure(bg="#000000")
window.iconbitmap('.\\key2.ico')

principal_text = Label(
    window, text="Enter your password lenght and after click the button", bg="#000000", fg="#00FF00")
principal_text.grid(column=0, row=0, padx=90, pady=10)

lgt = Entry(window)
lgt.grid(column=0, row=1, padx=95, pady=10)

button = Button(window, text="Generate your password",
                command=password_generator, bg="#4F4F4F", fg="#F8F8FF")
button.grid(column=0, row=3, padx=100, pady=10)

password_text = Label(window, text="",  bg="#000000", fg="#00FF00")
password_text.grid(column=0, row=2, padx=90, pady=10)

button_copy = Button(window, text="Copy password",
                     command=copy_password, bg="#4F4F4F", fg="#F8F8FF")
button_copy.grid(column=0, row=4, padx=100, pady=10)

window.mainloop()
