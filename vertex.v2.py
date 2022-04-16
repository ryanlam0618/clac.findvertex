from fractions import Fraction
from tkinter import *


def t():
    A = int(inpA.get())
    B = int(inpB.get())
    C = int(inpC.get())
    if A == 0:
        ans = Label(text='invalid', font='微軟正黑體 28')  # ans.config
        ans.place(anchor=NW, x=200, y=245, width='400', height='35')  # show ans
    D = B ** 2 - 4 * A * C
    h = (-B / (2 * A))
    h = Fraction(h)
    k = (C - (A * (h ** 2)))
    k = Fraction(k)
    if A > 0:
        if C and B > 0:
            chg = str(A) + 'x²+' + str(B) + 'x+' + str(C)
        if B < 0 and C > 0:
            chg = str(A) + 'x²' + str(B) + 'x+' + str(C)
        if C < 0 and B > 0:
            chg = str(A) + 'x²+' + str(B) + 'x' + str(C)
        if B < 0 and C < 0:
            chg = str(A) + 'x²' + str(B) + 'x' + str(C)
    VT = ('vertex=', '(', h, ",", k, ')')  # change fomu code
    ans = Label(text=VT, font='微軟正黑體 28')  # ans.config
    ans.place(anchor=NW, x=200, y=245, width='400', height='35')  # show ans
    fomu.config(text=chg)  # change label


win = Tk()  # main window
win.title('find vertex')  # title
win.minsize(width=800, height=400)
win.maxsize(width=1920, height=1080)
win.geometry("800x400")  # first size
win.config(bg='sky blue')  # background

hkfm = Label(text='# h=-b/2a', bg='white', font='微軟正黑體 28')
hkfm.place(anchor=NE, x=800, y=55, width=300, height=40)
hkfm = Label(text='# k=c-a(h²)', bg='white', font='微軟正黑體 28')
hkfm.place(anchor=NE, x=800, y=110, width=300, height=40)
title = Label(text='find vertex', font='微軟正黑體 28', bg='sky blue')
title.place(anchor=NW, x=300, y=0)
fomu = Label(text='ax²+bx+c', font='微軟正黑體 28', bg='sky blue')
fomu.place(anchor=NW, x=140, y=195)
inpAx = Label(bg='sky blue', font='微軟正黑體 20', text='a=')
inpAx.place(anchor=NW, x=140, y=55, width='50', height='40')
inpA = Entry(font='微軟正黑體 20')
inpA.place(anchor=NW, x=180, y=55, width='100', height='40')
inpBx = Label(bg='sky blue', font='微軟正黑體 20', text='b=')
inpBx.place(anchor=NW, x=140, y=100, width='50', height='40')
inpB = Entry(font='微軟正黑體 20', bg='white')
inpB.place(anchor=NW, x=180, y=100, width='100', height='40')
inpCx = Label(bg='sky blue', font='微軟正黑體 20', text='c=')
inpCx.place(anchor=NW, x=140, y=145, width='50', height='40')
inpC = Entry(bg='white', font='微軟正黑體 20')
inpC.place(anchor=NW, x=180, y=145, width='100', height='40')
btn = Button(text='計算', font='微軟正黑體 14', command=t)
btn.place(anchor=N, x=400, y=100, width='60', height='50')
win.mainloop()  # show window
