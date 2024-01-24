from tkinter import *
from tkmacosx import Button
from button_back import *

colour_button = 'blue'  # цвет фона кнопок
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]

window = Tk()
geometry = WindowGeometry(window=window, window_geometry='725x600')
window.protocol("WM_DELETE_WINDOW", lambda: geometry.next_place())

window.title('Крестики нолики')

# window.geometry('725x600')
window.resizable(width=False, height=False)  # запрещаем изменять размер окна

# заголовок в игре
label_title = Label(text='Ходи', background='cyan', font=('impact', 15), width=80)
label_title.grid(columnspan=6, column=0, row=0)

# поля (кнопки)
btn1 = Button(text=1, background=colour_button, font=('impact', 60), height=180, fg='blue', activebackground='blue',
              activeforeground='blue',
              command=lambda: o(btn1, lst, lst_btn, label_title))
btn1.grid(columnspan=2, column=0, row=1)

btn2 = Button(text=2, background=colour_button, font=('impact', 60), height=180, fg='blue', activebackground='blue',
              activeforeground='blue',
              command=lambda: o(btn2, lst, lst_btn, label_title))
btn2.grid(columnspan=2, column=2, row=1)

btn3 = Button(text=3, background=colour_button, font=('impact', 60), height=180, fg='blue', activebackground='blue',
              activeforeground='blue',
              command=lambda: o(btn3, lst, lst_btn, label_title))
btn3.grid(columnspan=2, column=4, row=1)

btn4 = Button(text=4, background=colour_button, font=('impact', 60), height=180, fg='blue', activebackground='blue',
              activeforeground='blue',
              command=lambda: o(btn4, lst, lst_btn, label_title))
btn4.grid(columnspan=2, column=0, row=2)

btn5 = Button(text=5, background=colour_button, font=('impact', 60), height=180, fg='blue', activebackground='blue',
              activeforeground='blue',
              command=lambda: o(btn5, lst, lst_btn, label_title))
btn5.grid(columnspan=2, column=2, row=2)

btn6 = Button(text=6, background=colour_button, font=('impact', 60), height=180, fg='blue', activebackground='blue',
              activeforeground='blue',
              command=lambda: o(btn6, lst, lst_btn, label_title))
btn6.grid(columnspan=2, column=4, row=2)

btn7 = Button(text=7, background=colour_button, font=('impact', 60), height=180, fg='blue', activebackground='blue',
              activeforeground='blue',
              command=lambda: o(btn7, lst, lst_btn, label_title))
btn7.grid(columnspan=2, column=0, row=3)

btn8 = Button(text=8, background=colour_button, font=('impact', 60), height=180, fg='blue', activebackground='blue',
              activeforeground='blue',
              command=lambda: o(btn8, lst, lst_btn, label_title))
btn8.grid(columnspan=2, column=2, row=3)

btn9 = Button(text=9, background=colour_button, font=('impact', 60), height=180, fg='blue', activebackground='blue',
              activeforeground='blue',
              command=lambda: o(btn9, lst, lst_btn, label_title))
btn9.grid(columnspan=2, column=4, row=3)

# кнопка для выхода из игры
btn_exit = Button(text='Закончить игру', font=('impact', 15), background='red', width=240,
                  command=lambda: WM_DELETE_WINDOW_YES_NO(window=window))
btn_exit.grid(columnspan=2, column=4, row=4)
lst_btn = [btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9]






window.mainloop()
