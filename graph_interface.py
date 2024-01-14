from tkinter import *
from tkmacosx import Button
from button_back import *

colour_button = 'blue'  # цвет фона кнопок
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]

window = Tk()

window.title('Крестики нолики')
window.geometry('725x600')

# заголовок в игре
label_title = Label(text='\t' * 5 + 'Ходи' + '\t' * 5, background='cyan', font=('impact', 15))
label_title.grid(columnspan=6, column=0, row=0)

# поля (кнопки)
btn1 = Button(text=1, background=colour_button, font=('impact', 60), height=180, command=lambda: o(btn1, lst))
btn1.grid(columnspan=2, column=0, row=1)

btn2 = Button(text=2, background=colour_button, font=('impact', 60), height=180, command=lambda: o(btn2, lst))
btn2.grid(columnspan=2, column=2, row=1)

btn3 = Button(text=3, background=colour_button, font=('impact', 60), height=180, command=lambda: o(btn3, lst))
btn3.grid(columnspan=2, column=4, row=1)

btn4 = Button(text=4, background=colour_button, font=('impact', 60), height=180, command=lambda: o(btn4, lst))
btn4.grid(columnspan=2, column=0, row=2)

btn5 = Button(text=5, background=colour_button, font=('impact', 60), height=180, command=lambda: o(btn5, lst))
btn5.grid(columnspan=2, column=2, row=2)

btn6 = Button(text=6, background=colour_button, font=('impact', 60), height=180, command=lambda: o(btn6, lst))
btn6.grid(columnspan=2, column=4, row=2)

btn7 = Button(text=7, background=colour_button, font=('impact', 60), height=180, command=lambda: o(btn7, lst))
btn7.grid(columnspan=2, column=0, row=3)

btn8 = Button(text=8, background=colour_button, font=('impact', 60), height=180, command=lambda: o(btn8, lst))
btn8.grid(columnspan=2, column=2, row=3)

btn9 = Button(text=9, background=colour_button, font=('impact', 60), height=180, command=lambda: o(btn9, lst))
btn9.grid(columnspan=2, column=4, row=3)

window.mainloop()
