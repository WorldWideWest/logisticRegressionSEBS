from tkinter import *
from tkinter import messagebox

# CREATING THE WIDGETS
## Info widgets
root = Tk(className=' SEBS admission test ')
infoLabel = Label(text = 'Please input the number of points in the range (0 - 100): ')

## Entery widget and function's
box = Entry(root, width = 50)
box.insert(0, 'Enter the number of points')
def CheckValue():
    try:
        float(box.get())
        if(float(box.get()) < 1 or float(box.get()) > 100):
            messagebox.showerror('Error', 'Value out of range!')
        elif(float(box.get()) >= 1 or float(box.get()) <= 100):
            messagebox.showinfo('Info', 'You have passed the exam')
    except Exception:
        messagebox.showerror('Error', 'Syntax Error - the value could not be parsed!')

blank = Label(text = "             ", bg = "#D6CED5")

## Button proporties
applyButton = Button(root, text = 'Calculate', padx = 50, pady = 10, command = CheckValue)

# APPLYING THE WIDGETS
infoLabel.grid(row = 0, column = 0)
box.grid(row = 1, column = 0)
blank.grid(row = 2, column = 0)
blank.grid(row = 3, column = 0) 
applyButton.grid(row = 4, column = 0)

# WINDOW
root.geometry("306x150")
root.configure(bg = '#D6CED5')
root.mainloop()