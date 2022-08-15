# -*- coding: utf-8 -*-
"""
Created on Mon Aug 15 17:35:42 2022

@author: PC_RC
"""

from tkinter import *
import random


root = Tk()
root.title("Password Changer")
root.geometry("400x400")

guessed_password = Entry(root)
show_guessed_password = Label(root)
generated_password = Label(root)

array_3d = [[['!', '@', '#', '$', '%', '^'], ["Good", "Bad", "Awesome", "Average", "Worst"], ['12', '23', '34', '45', '56', '67', '78']]]


def new_password():
    show_guessed_password["text"] = "Guessed Password: " + guessed_password.get()
    
    random_no_1 = random.randint(0, 5)
    random_no_2 = random.randint(0, 1)
    random_no_3 = random.randint(0, 7)
    
    letter1 = str(array_3d[0][0][random_no_1])
    letter2 = (array_3d[0][1][random_no_2])
    letter3 = (array_3d[0][2][random_no_3])
    generated_password["text"] = "Generated Password: " + letter1 + "" + letter2 + "" + letter3
    
btn = Button(root, text = "New Password", command = new_password)
guessed_password.place(relx = 0.5, rely = 0.5, anchor = CENTER)
show_guessed_password.place(relx = 0.5, rely = 0.6, anchor = CENTER)
btn.place(relx = 0.5, rely = 0.7, anchor = CENTER)
generated_password.place(relx = 0.5, rely = 0.8, anchor = CENTER)


root.mainloop()