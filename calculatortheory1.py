from tkinter import *
win = Tk()
win.title('Calculator')

# Will hold the display of the calculator
textbox = StringVar()
textbox.set("")
#global value
value = ""
global value #initial value of variable value
valuetwo = ""
global valuetwo
binary = 0
global binary
addi = 0
mult = 0
divi = 0
subt = 0
global addi
global mult
global divi
global subt

def plus(number, numbertwo):
    ans = int(number) + int(numbertwo)
    print (ans)
    return ans

def buttonClicked(event):
    global binary
    if binary == 0:
        global value #calling value of value into local function
        button = event.widget
        value = value + button.cget("text") # cget recognizes the text of the button, and + allows us to make multi-digit numbers
        textbox.set(value)
        return value
    elif binary == 1:
        global valuetwo
        button = event.widget
        valuetwo = valuetwo + button.cget("text")
        textbox.set(valuetwo)
        return valuetwo

def equals():
#    print("testfunc")
#    print(addi)
    if addi == 1:
        plus(value, valuetwo)
#        print ("test")
#        print(ans)
    else :
        print ("error")
    addi = 0
    mult = 0
    divi = 0
    subt = 0
    global addi
    global mult
    global divi
    global subt
    value = ""
    valuetwo = ""
    global value
    global valuetwo
    binary = 0
    global binary


def functionClicked(event):
    binary = 1
    global binary
    button = event.widget
    item = button.cget("text")
    textbox.set(item)
#    print (item)
    if item == "+":
        addi = 1
        mult = 0
        divi = 0
        subt = 0
        global addi
        global mult
        global divi
        global subt
#        print("+")
    elif item == "*":
        addi = 0
        mult = 1
        divi = 0
        subt = 0
        global addi
        global mult
        global divi
        global subt        
    elif item == "%":
        addi = 0
        mult = 0
        divi = 1
        subt = 0
        global addi
        global mult
        global divi
        global subt
    elif item == "-":
        addi = 0
        mult = 0
        divi = 0
        subt = 1
        global addi
        global mult
        global divi
        global subt
    elif item == "=":
#        print ("test=")
        equals()
    else:
        print("error")


"""        
    var1 = value
    value = ""
    global value #clears previous entry
"""







    
    
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

