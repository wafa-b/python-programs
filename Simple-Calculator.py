from tkinter import *

def btnClick(numbers):
    global operater
    operater = operater + str(numbers)
    text_input.set(operater)

def btnClear():
    global operater
    operater = ""
    text_input.set("")

def btnResult():
    global operater
    try:
        result = str(eval(operater))
        text_input.set(result)
        operater = ""
    except ZeroDivisionError:
        text_input.set("ERROR")
        operater = ""


top = Tk()
top.title('Calculator')
top.resizable(0, 0)
top.bg="gray"
# top.minsize(300,300)
top.configure(background="light gray")

operater = ""
text_input = StringVar()

txtDesplay = Entry(top,textvariable=text_input,bd=10,bg="light blue",width=32).grid(columnspan=4)

btn7 = Button(top,text="7",padx=16,pady=16,bd=10, highlightbackground='light blue', height=1, width=5,command=lambda:btnClick(7)).grid(row=1,column=0)

btn8 = Button(top,text="8",padx=16,pady=16,bd=10,highlightbackground='light blue', height=1, width=5,command=lambda:btnClick(8)).grid(row=1,column=1)

btn9 = Button(top,text="9",padx=16,pady=16,bd=10,highlightbackground='light blue', height=1, width=5,command=lambda:btnClick(9)).grid(row=1,column=2)

btndiv = Button(top,text="/",padx=16,pady=16,bd=10,highlightbackground='light blue', height=1, width=5,command=lambda:btnClick("/")).grid(row=1,column=3)

btn4 = Button(top,text="4",padx=16,pady=16,bd=10,highlightbackground='light blue', height=1, width=5,command=lambda:btnClick(4)).grid(row=2,column=0)

btn5 = Button(top,text="5",padx=16,pady=16,bd=10,highlightbackground="light blue", height=1, width=5,command=lambda:btnClick(5)).grid(row=2,column=1)

btn6 = Button(top,text="6",padx=16,pady=16,bd=10,highlightbackground="light blue", height=1, width=5,command=lambda:btnClick(6)).grid(row=2,column=2)

btnmul = Button(top,text="X",padx=16,pady=16,bd=10,highlightbackground="light blue", height=1, width=5,command=lambda:btnClick("*")).grid(row=2,column=3)

btn1 = Button(top,text="1",padx=16,pady=16,bd=10,highlightbackground="light blue", height=1, width=5,command=lambda:btnClick(1)).grid(row=3,column=0)

btn2 = Button(top,text="2",padx=16,pady=16,bd=10,highlightbackground="light blue", height=1, width=5,command=lambda:btnClick(2)).grid(row=3,column=1)

btn3 = Button(top,text="3",padx=16,pady=16,bd=10,highlightbackground="light blue", height=1, width=5,command=lambda:btnClick(3)).grid(row=3,column=2)

btnsub = Button(top,text="-",padx=16,pady=16,bd=10,highlightbackground="light blue", height=1, width=5,command=lambda:btnClick("-")).grid(row=3,column=3)

btnadd = Button(top,text="+",padx=16,pady=16,bd=10,highlightbackground="light blue", height=1, width=5,command=lambda:btnClick("+")).grid(row=3,column=3)

btn0 = Button(top,text="0",padx=16,pady=16,bd=10,highlightbackground="light blue", height=1, width=5,command=lambda:btnClick(0)).grid(row=4,column=0)

btnnumdot = Button(top,text=".",padx=16,pady=16,bd=10,highlightbackground="light blue", height=1, width=5,command=lambda:btnClick(".")).grid(row=4,column=1)

btnnumclear = Button(top,text="C",padx=16,pady=16,bd=10,highlightbackground="light blue", height=1, width=5,command=btnClear).grid(row=4,column=2)

btnresult = Button(top,text="=",padx=16,pady=16,bd=10,highlightbackground="light blue", height=1, width=5,command=btnResult).grid(row=4,column=3)

top.mainloop()

