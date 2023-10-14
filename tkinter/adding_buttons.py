
from tkinter import *

#this command adds a label in the screen
def click():
    global screen
    lbl = Label(screen, text = "You clicked the button")
    lbl.pack()
    return

screen = Tk()

#setting screen dimensions
screen.geometry("400x400")

#changing the bacground color
screen.config(bg = "#ff0120") 

#Adding button
btn = Button(screen, text = "Click Me!", bg="#ffff00", command = click) #click function is invoked when the button is clicked

#packing the button in the screen
btn.pack()

screen.mainloop()