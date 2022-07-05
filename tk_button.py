from tkinter import *

myWindow = Tk()

def myClick():
    myLabel2 = Label(myWindow, text = "Choose A Topic")
    myLabel2.pack()

myLabel = Label(myWindow, text = "Welcome to Caroline's Quiz")
myButton = Button(myWindow, text = "Start Quiz", padx = 40, pady = 10, command = myClick, bg = 'red')

myLabel.pack()
myButton.pack()

myWindow.mainloop()