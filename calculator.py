from tkinter import *
win = Tk()
win.title('Calculator')

# Will hold the display of the calculator
textbox = StringVar()
textbox.set("")
value = ""
global value #initial value of variable value

def buttonClicked(event):
    global value #calling value of value into local function
    button = event.widget
    value = value + button.cget("text") # cget recognizes the text of the button, and + allows us to make multi-digit numbers
    textbox.set(value)
    return value

def functionClicked(event):
    button = event.widget
    item = button.cget("text")
    textbox.set(item)
    var1 = value
    value = ""
    global value #clears previous entry






    
    
buttons = []  # holds all buttons
for buttonNum in range(0,10):
    # creates a new button with that number
    button = Button(win, text=str(buttonNum))
    button.pack()
    button.bind("<Button-1>", buttonClicked)
    # binds function to event
    buttons.append(button)
    button.grid(row=int(buttonNum/3)+1 , column=buttonNum % 3) 


funclist = ["%","*","-","+","="]
functions = []
for operator in range(0,5):
    button = Button(win, text=str(funclist[operator]))
    button.pack()
    button.bind("<Button-1>", functionClicked)
    functions.append(button)
    button.grid(row=int(operator+1) , column=4)
    
#want to create a dictionary to hold previous values, which can then be accessed as a whole with operator(s)when equal sign is pressed
#need to def funcs for all operators

    

l = Label(win, textvariable=textbox)
l.grid(row=0, column=2)

win.mainloop()

