from tkinter import *
from tkinter import messagebox
import numpy as np
import pandas as pd
import statsmodels.api as sm
import sys
sys.setrecursionlimit(100000)


## LOGISTIC REGRESSION

# importing the data
rawDataPass = pd.read_excel('source\\convertedData\\rawDataCleaned\\XLSX/Passed.xlsx')
rawDataPass['Admitted'] = 1

rawDataFail = pd.read_excel('source\\convertedData\\rawDataCleaned\\XLSX/Failed.xlsx')
rawDataFail['Admitted'] = 0

data = pd.concat([rawDataPass, rawDataFail])

# building the regression

y = data['Admitted'] # dependent variable
x1 = data['Points'] # independent variable

x = sm.add_constant(x1)
regLog = sm.Logit(y,x)
resultsLog = regLog.fit()
resultsLog.predict()


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

            ## creating the prediction
            num = float(box.get())
            testData = pd.DataFrame({"Points": [num]})
            testData = sm.add_constant(testData, has_constant="add")
            predValue = resultsLog.predict(testData)
            value = predValue[0]
            if(float(value) < 0.5):
                output = "We are sorry but you have not passed the exam :("
                messagebox.showinfo('Info', str(output))
            elif(float(value) >= 0.5):
                output = "Congratulations you have passed the exam :)"
                messagebox.showinfo('Info', str(output))
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