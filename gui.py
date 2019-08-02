from tkinter import *

top = Tk()
top.title("Calculator")
top.minsize(300,300)

number1Label = Label(text="First Number")
number1Label.pack()
number1Box = Entry()
number1Box.pack()

number2Label = Label(text="Second Number")
number2Label.pack()
number2Box =Entry()
number2Box.pack()

def addNumbers():
    number1 = float(number1Box.get())
    number2 = float(number2Box.get())
    result =  number1 + number2
    resultLabel = Label(text="The result is "+ str(result))
    resultLabel.pack()


btn = Button(text="Add",command=addNumbers)
btn.pack()

top.mainloop()
