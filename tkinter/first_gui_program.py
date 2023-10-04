from tkinter import *

# creating a GUI Screen
screen = Tk()

# A label that contains text
label = Label(screen, text = "Hello world!", padx = 10, pady = 20)

# Packing the label into the GUI screen
label.pack()

# Running the mainloop function to display the GUI screen continuously in the screen
screen.mainloop()