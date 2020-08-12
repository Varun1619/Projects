import tkinter as tk
from tkinter import*

h = 400
w = 400

root = tk.Tk()
root.geometry("250x400+300+300")
root.resizable(0,0)
root.title('Calculator')

A = 0
val = ''
operator = ''

data = StringVar()
lbl = tk.Label(
    root,
    font = ('Verdana',22), 
    anchor = 'se',
    textvariable = data,
    background = 'white'

)
lbl.pack(expand = True,fill = 'both')

def btn_9_isclicked():
    global val
    val = val + '9'
    data.set(val)
    
def btn_8_isclicked():
    global val
    val = val + '8'
    data.set(val)

def btn_7_isclicked():
    global val
    val = val + '7'
    data.set(val)

def btn_6_isclicked():
    global val
    val = val + '6'
    data.set(val)

def btn_5_isclicked():
    global val
    val = val + '5'
    data.set(val)

def btn_4_isclicked():
    global val
    val = val + '4'
    data.set(val)

def btn_3_isclicked():
    global val
    val = val + '3'
    data.set(val)

def btn_2_isclicked():
    global val
    val = val + '2'
    data.set(val)

def btn_1_isclicked():
    global val
    val = val + '1'
    data.set(val)

def btn_0_isclicked():
    global val
    val = val + '0'
    data.set(val)
    
def btn_plus_isclicked():
    global A
    global operator
    global val
    A = int(val)
    operator = "+"
    val = val + "+"
    data.set(val)

def btn_minus_isclicked():
    global A
    global operator
    global val
    A = int(val)
    operator = "-"
    val = val + "-"
    data.set(val)

def btn_multiplication_isclicked():
    global A
    global operator
    global val
    A = int(val)
    operator = "*"
    val = val + "*"
    data.set(val)

def btn_division_isclicked():
    global A
    global operator
    global val
    A = int(val)
    operator = "/"
    val = val + "/"
    data.set(val)


def btn_result_isclicked():
    global A
    global val
    global operator
    val_2 = val
    if operator == "+":
       x = int((val_2.split("+")[1]))
       C = A + x
       val = str(C)
       data.set(val)
    if operator == "-":
       x = int((val_2.split("-")[1]))
       C = A - x
       val = str(C)
       data.set(val)
    if operator == "*":
       x = int((val_2.split("*")[1]))
       C = A * x
       val = str(C)
       data.set(val)
    if operator == "/":
        x = int((val_2.split("/")[1]))      
        C = A / x
        val = str(C)
        data.set(val)



btn_row_1 =tk.Frame(root,bg = 'black')
btn_row_1.pack(expand = True,fill = 'both')

btn_9 = tk.Button(
    btn_row_1,
    text = '9', 
    font = ('Verdana',22), 
    bd = 0,
    activebackground = "gray",
    command = btn_9_isclicked
)
btn_9.pack(side = 'left' , expand = True,fill = 'both')

btn_8 = tk.Button(
    btn_row_1,
    text = '8', 
    font = ('Verdana',22), 
    bd = 0,
    activebackground = "gray",
    command = btn_8_isclicked
)
btn_8.pack(side = 'left' , expand = True,fill = 'both')

btn_7 = tk.Button(
    btn_row_1,
    text = '7', 
    font = ('Verdana',22), 
    bd = 0,
    activebackground = "gray",
    command = btn_7_isclicked
)
btn_7.pack(side = 'left' , expand = True,fill = 'both')

btn_plus= tk.Button(
    btn_row_1,
    text = '+', 
    font = ('Verdana',22), 
    bd = 0,
    activebackground = "gray",
    command = btn_plus_isclicked
)
btn_plus.pack(side = 'left' , expand = True,fill = 'both')

btn_row_2 =tk.Frame(root)
btn_row_2.pack(expand = True,fill = 'both')

btn_6 = tk.Button(
    btn_row_2,
    text = '6', 
    font = ('Verdana',22), 
    bd = 0, 
    activebackground = "gray",
    command = btn_6_isclicked
)
btn_6.pack(side = 'left' , expand = True,fill = 'both')

btn_5 = tk.Button(
    btn_row_2,
    text = '5', 
    font = ('Verdana',22), 
    bd = 0,
    activebackground = "gray",
    command = btn_5_isclicked
)
btn_5.pack(side = 'left' ,expand = True,fill = 'both')

btn_4 = tk.Button(
    btn_row_2,
    text = '4',
    font = ('Verdana',22),
    bd = 0,
    activebackground = "gray",
    command = btn_4_isclicked
)
btn_4.pack(side = 'left' , expand = True,fill = 'both')

btn_minus= tk.Button(
    btn_row_2,
    text = ' -', 
    font = ('Verdana',22), 
    bd = 0,
    activebackground = "gray",
    command = btn_minus_isclicked
)
btn_minus.pack(side = 'left' , expand = True,fill = 'both')


btn_row_3 =tk.Frame(root,bg = 'black')
btn_row_3.pack(expand = True,fill = 'both')

btn_3 = tk.Button(
    btn_row_3,
    text = '3', 
    font = ('Verdana',22), 
    bd = 0,
    activebackground = "gray",
    command = btn_3_isclicked
)
btn_3.pack(side = 'left' , expand = True,fill = 'both')

btn_2 = tk.Button(
    btn_row_3,
    text = '2', 
    font = ('Verdana',22), 
    bd = 0,
    activebackground = "gray",
    command = btn_2_isclicked
)
btn_2.pack(side = 'left' , expand = True,fill = 'both')

btn_1 = tk.Button(
    btn_row_3,
    text = '1', 
    font = ('Verdana',22), 
    bd = 0,
    activebackground = "gray",
    command = btn_1_isclicked
)
btn_1.pack(side = 'left' , expand = True,fill = 'both')

btn_divison= tk.Button(
    btn_row_3,
    text = ' /', 
    font = ('Verdana',22), 
    bd = 0,
    activebackground = "gray",
    command = btn_division_isclicked
)
btn_divison.pack(side = 'left' , expand = True,fill = 'both')

btn_row_4 =tk.Frame(root)
btn_row_4.pack(expand = True,fill = 'both')

btn_Clear = tk.Button(
    btn_row_4,
    text = 'C', 
    font = ('Verdana',22), 
    bd = 0,
    activebackground = "gray"
)
btn_Clear.pack(side = 'left' , expand = True,fill = 'both')

btn_0 = tk.Button(
    btn_row_4,
    text = '0', 
    font = ('Verdana',22), 
    bd = 0,
    activebackground = "gray",
    command = btn_0_isclicked
)
btn_0.pack(side = 'left' , expand = True,fill = 'both')

btn_result = tk.Button(
    btn_row_4,
    text = '=', 
    font = ('Verdana',22), 
    bd = 0,
    activebackground = "gray",
    command = btn_result_isclicked
)
btn_result.pack(side = 'left' , expand = True,fill = 'both')

btn_multiplication= tk.Button(
    btn_row_4,
    text = ' *', 
    font = ('Verdana',22), 
    bd = 0,
    activebackground = "gray",
    command = btn_multiplication_isclicked
)
btn_multiplication.pack(side = 'left' , expand = True,fill = 'both')

root.mainloop()