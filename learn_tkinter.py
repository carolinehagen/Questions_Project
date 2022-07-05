from tkinter import *

root = Tk()

# Create a label widget
myLabel1 = Label(root, text = "Welcome to Caroline's Quiz!")
myLabel2 = Label(root, text = "My name is Caroline")

# Shoving it onto the window
myLabel1.grid(row =0, column =0)
myLabel2.grid(row =1, column =5)

root.mainloop()