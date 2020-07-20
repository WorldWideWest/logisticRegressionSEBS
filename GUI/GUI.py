from tkinter import *
from tkinter import messagebox

# CREATING THE WIDGETS
## Info widgets
root = Tk(className=' SEBS admission test ')
infoLabel = Label(text = 'Please input the number of points in the range (0 - 100): ')

## Entery widget and function's
form = Entry(root, width = 50)
blank = Label(text = "             ", bg = "#D6CED5")

## Button proporties
applyButton = Button(root, text = 'Calculate', padx = 50, pady = 10)

# APPLYING THE WIDGETS
infoLabel.grid(row = 0, column = 0)
form.grid(row = 1, column = 0)
blank.grid(row = 2, column = 0)
blank.grid(row = 3, column = 0) 
applyButton.grid(row = 4, column = 0)

# WINDOW
root.geometry("306x150")
root.configure(bg = '#D6CED5')
root.mainloop()