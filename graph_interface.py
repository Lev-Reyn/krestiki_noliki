import tkinter

window = tkinter.Tk()

window.title('Крестики нолики')
window.geometry('600x600')

O = 'O'
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def o1():
    label1.configure(text='O')
    lst[0] = O
    print(lst)


def o2():
    label2.configure(text='O')
    lst[1] = O
    print(lst)


def o3():
    label3.configure(text='O')
    lst[2] = O
    print(lst)


def o4():
    label4.configure(text='O')
    lst[3] = O
    print(lst)


def o5():
    label5.configure(text='O')
    lst[4] = O
    print(lst)


def o6():
    label6.configure(text='O')
    lst[5] = O
    print(lst)


def o7():
    label7.configure(text='O')
    lst[6] = O
    print(lst)


def o8():
    label8.configure(text='O')
    lst[7] = O
    print(lst)


def o9():
    label9.configure(text='O')
    lst[9] = O
    print(lst)


# labels
label0 = tkinter.Label(text='Играаем в крестики нолики блин)))))', background='blue')
label0.grid(columnspan=6, column=0, row=0)

label1 = tkinter.Label(text='1', background='red', width=20, height=10, cursor='circle')
label1.grid(column=0, row=1, columnspan=2, )
# label1.pack(anchor='nw', fill='both')
label2 = tkinter.Label(text='2', background='blue', width=20, height=10)
# label2.pack(anchor='n', fill='both')
label2.grid(column=2, row=1, columnspan=2)
label3 = tkinter.Label(text='3', background='green', width=20, height=10)
# label3.pack(anchor='ne')
label3.grid(column=4, row=1, columnspan=2)
label4 = tkinter.Label(text='4', background='yellow', width=20, height=10)
# label4.pack(anchor='w')
label4.grid(column=0, row=2, columnspan=2)

label5 = tkinter.Label(text='5', background='cyan', width=20, height=10)
# label5.pack(anchor='center')
label5.grid(column=2, row=2, columnspan=2)
label6 = tkinter.Label(text='6', background='gray', width=20, height=10)
# label6.pack(anchor='e')
label6.grid(column=4, row=2, columnspan=2)
label7 = tkinter.Label(text='7', background='brown', width=20, height=10)
# label7.pack(anchor='sw')
label7.grid(column=0, row=3, columnspan=2)
label8 = tkinter.Label(text='8', background='gold', width=20, height=10)
# label8.pack(anchor='s')
label8.grid(column=2, row=3, columnspan=2)
label9 = tkinter.Label(text='9', background='white', width=20, height=10)
# label9.pack(anchor='se')
label9.grid(column=4, row=3, columnspan=2)

# buttons
btn1 = tkinter.Button(text='1', command=o1)
btn1.grid(column=0, row=4)

btn2 = tkinter.Button(text='2', command=o2)
btn2.grid(column=1, row=4)

btn3 = tkinter.Button(text='3', command=o3)
btn3.grid(column=2, row=4)

btn4 = tkinter.Button(text='4', command=o4)
btn4.grid(column=0, row=5)

btn5 = tkinter.Button(text='5', command=o5)
btn5.grid(column=1, row=5)

btn6 = tkinter.Button(text='6', command=o6)
btn6.grid(column=2, row=5)

btn7 = tkinter.Button(text='7', command=o7)
btn7.grid(column=0, row=6)

btn8 = tkinter.Button(text='8', command=o8)
btn8.grid(column=1, row=6)

btn9 = tkinter.Button(text='9', command=o9)
btn9.grid(column=2, row=6)

window.mainloop()
