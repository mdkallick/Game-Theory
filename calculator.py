win = Tk()
win.title('Calculator')
tvar = ""

def beenClicked():
    l.configure(text=Button(win)) #this doesn't work yet, want it to show any button depending on which was clicked                                                                
def configfunc(button, tvar):
    tvar = tvar + button
    l.configure(text=tvar)
    return tvar

b1.configure(command=configfunc("1", tvar))
b2.configure(command=configfunc("2", tvar))
#b3.configure(command=b3func)                                                                                                                                                      
#b4.configure(command=b4func)                                                                                                                                                      
#b5.configure(command=b5func)                                                                                                                                                      
#b6.configure(command=b6func)                                                                                                                                                      
#b7.configure(command=b7func)                                                                                                                                                      
#b8.configure(command=b8func)                                                                                                                                                      
#b9.configure(command=b9func)                                                                                                                                                      
#b0.configure(command=b0func)                                                                                                                                                      
#bdiv.configure(command=bdivfunc)                                                                                                                                                  
#bmul.configure(command=bmulfunc)                                                                                                                                                  
#badd.configure(command=baddfunc)                                                                                                                                                  
#bsub.configure(command=bsubfunc)                                                                                                                                                  
#bequ.configure(command=bequfunc)                                                                                                                                                  
#bclr.configure(command=clear) 




from tkinter import *
win = Tk()
win.title('Calculator')
tvar = ""

def beenClicked():
    l.configure(text=Button(win)) #this doesn't work yet, want it to show any button depending on which was clicked
def configfunc(button):
    tvar = tvar + "button"
    l.configure(text=tvar)
    return tvar











b1 = Button(win, text="1")
b2 = Button(win, text="2")
b3 = Button(win, text="3")
b4 = Button(win, text="4")
b5 = Button(win, text="5")
b6 = Button(win, text="6")
b7 = Button(win, text="7")
b8 = Button(win, text="8")
b9 = Button(win, text="9")
b0 = Button(win, text="0")
bdiv = Button(win, text="/")
bmul = Button(win, text="*")
badd = Button(win, text="+")
bsub = Button(win, text="-")
bequ = Button(win, text="=")
bclr = Button(win, text='c')
b1.grid(row=3, column=1)
b2.grid(row=3, column=2)
b3.grid(row=3, column=3)
b4.grid(row=2, column=1)
b5.grid(row=2, column=2)
b6.grid(row=2, column=3)
b7.grid(row=1, column=1)
b8.grid(row=1, column=2)
b9.grid(row=1, column=3)
b0.grid(row=4, column=1)
bdiv.grid(row=1, column=4)
bmul.grid(row=2, column=4)
badd.grid(row=4, column=4)
bsub.grid(row=3, column=4)
bequ.grid(row=4, column=3)
bclr.grid(row=4, column=2)
l = Label(win, text="")
l.grid(row=0, column=2)

textbox = StringVar()
textbox.set(None)


b1.configure(command=configfunc("1"))
b2.configure(command=configfunc("2"))
b3.configure(command=b3func)
b4.configure(command=b4func)
b5.configure(command=b5func)
b6.configure(command=b6func)
b7.configure(command=b7func)
b8.configure(command=b8func)
b9.configure(command=b9func)
b0.configure(command=b0func)
bdiv.configure(command=bdivfunc)
bmul.configure(command=bmulfunc)
badd.configure(command=baddfunc)
bsub.configure(command=bsubfunc)
bequ.configure(command=bequfunc)
bclr.configure(command=clear)


win.mainloop()

