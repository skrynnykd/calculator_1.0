from tkinter import *
from tkinter import Button

root = Tk()
root.geometry("395x170")
root.title("Calculator 1.0")
root.config(background="Green")

expression = ""



result = StringVar()
expression_field = Entry(textvariable=result)
expression_field.grid(columnspan=4, ipadx=100)

def press_num(num):
    global expression
    expression += str(num)
    result.set(expression)
def equelpress():
    try:
        global expression
        total = str(eval(expression))
        result.set(total)
        expression = total
    except:
        result.set("error")
        expression = ""
def reset():
    global expression
    total = ""
    result.set(total)
    expression = total


button1 = Button(text = "1", background="Red", height=1, width=7, command=lambda: press_num(1))
button1.grid(row=5, column=0)

button2 = Button(text = "2", height=1, width=7, command=lambda: press_num(2))
button2.grid(row=5, column=1)

button3 = Button(text = "3", height=1, width=7, command=lambda: press_num(3))
button3.grid(row=5, column=2)

button4 = Button(text = "4", height=1, width=7, command=lambda: press_num(4))
button4.grid(row=4, column=0)

button5 = Button(text = "5", height=1, width=7, command=lambda: press_num(5))
button5.grid(row=4, column=1)

button6 = Button(text = "6", height=1, width=7, command=lambda: press_num(6))
button6.grid(row=4, column=2)

button7= Button(text = "7", height=1, width=7, command=lambda: press_num(7))
button7.grid(row=3, column=0)

button8 = Button(text = "8", height=1, width=7, command=lambda: press_num(8))
button8.grid(row=3, column=1)

button9 = Button(text = "9", height=1, width=7, command=lambda: press_num(9))
button9.grid(row=3, column=2)

plus = Button(text = "+", height=1, width=7, command=lambda: press_num("+"))
plus.grid(row=5, column=3)

button0 = Button(text = "0", height=1, width=7, command=lambda: press_num(0))
button0.grid(row=6, column=0)

minus = Button(text = "-", height=1, width=7, command=lambda: press_num("-"))
minus.grid(row=4, column=3)

equal = Button(text = "=", height=1, width=7, command=equelpress)
equal.grid(row=6, column=3)

umn = Button(text = "*", height=1, width=7, command=lambda: press_num("*"))
umn.grid(row=3, column=3)

dele = Button(text = "/", height=1, width=7, command=lambda: press_num("/"))
dele.grid(row=2, column=3)

reset = Button(text = "C", height=1, width=7, command=reset)
reset.grid(row=2, column=0)


root.mainloop()


