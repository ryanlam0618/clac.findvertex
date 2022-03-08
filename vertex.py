from fractions import Fraction
from tkinter import *


def t():
    A = int(inpA.get())
    B = int(inpB.get())
    C = int(inpC.get())
    D = B ** 2 - 4 * A * C
    h = (-B / (2 * A))
    h = Fraction(h)
    k = (C - (A * (h ** 2)))
    k = Fraction(k)
    VT = ('vertex=', '(', h, ",", k, ')')
    VTx = Label(text=VT, font='微軟正黑體 28')  # ans.config
    VTx.place(anchor=NW, x=0, y=150, width='500', height='35')  # show ans
    input()

win = Tk()  # main window
win.title('find vertex')  # title
win.minsize(width=800, height=400)
win.maxsize(width=1920, height=1080)
win.geometry("800x400")  # first size
win.config(bg='sky blue')  # background

Ep = Label(text='ax²+bx+c', font='微軟正黑體 28', bg='sky blue')  # base formula
Ep.grid(row=0, column=0)  # show the lb
inpA = Entry(bg='white', font='微軟正黑體 28')  # a entry
inpA.place(anchor=NW, x=0, y=55, width='50', height='40')  # show (a) entry
inpAx = Label(text='x²+', font='微軟正黑體 28')  # a str
inpAx.place(anchor=NW, x=40, y=55, width='55', height='40')  # show a str
inpB = Entry(bg='white', font='微軟正黑體 28')  # b entry
inpB.place(anchor=NW, x=90, y=55, width='50', height='40')  # show b entry
inpBx = Label(text='x+', font='微軟正黑體 28')  # b str
inpBx.place(anchor=NW, x=135, y=55, width='45', height='40')  # show b str
inpC = Entry(bg='white', font='微軟正黑體 28')  # c
inpC.place(anchor=NW, x=180, y=55, width='50', height='40')  # show C
hkfm = Label(text='# h=-b/2a', bg='skyblue', font='微軟正黑體 28')
hkfm.place(anchor=NE, x=700, y=55, width=400, height=40)
hkfm = Label(text='# k=c-(a*h²)', bg='skyblue', font='微軟正黑體 28')
hkfm.place(anchor=NE, x=700, y=20, width=400, height=40)
btn = Button(text='計算', font='微軟正黑體 14', command=t)
btn.place(anchor=NW, x=0, y=100, width='60', height='35')
win.mainloop()
