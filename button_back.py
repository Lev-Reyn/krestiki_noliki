import tkinter as tk
from typing import List, Union
from vin import vin, O, X, nichya
from test import robot, del_x_o


def o(btn: tk.Button, lst: List[Union[int, str]], lst_btn: List[tk.Button], label_title: tk.Label, znak: str = 'O'):
    """
    Ставит нолик в то место, куда указал игрок, и компьютер потом должен будет снова запустить эту функцию,
    что бы сходить
    btn: кнопка, которую нажал игрок
    lst: список, где хранятся все значения игры
    label_title: сам Label, где будет отображаться информация об игре
    znak: какой знак ставить, O или X
    """
    label_title.configure(text='Ходи')
    if not str(btn.cget('text')).isdigit():
        label_title.configure(text='Уже занято')
        print('уже занято')
        return
    lst[int(btn.cget('text')) - 1] = znak  # заменяем в списке значение на знак (нолик или крестик)
    print(lst)
    btn.configure(text=znak)
    if vin(lst=lst) == O:
        label_title.configure(text='Победил игрок')
        print('победил игрок')
        return
    if nichya(lst):
        label_title.configure(text='Ничья')
        print('ничья')
        return
        # print(lst_btn)
    if znak == X:
        return
    chose_step_robot = robot(del_x_o(lst=lst))  # шаг робота
    btn_for_robot = lst_btn[chose_step_robot - 1]  # кнопка для хода робота
    o(btn=btn_for_robot, lst=lst, lst_btn=lst_btn, label_title=label_title, znak=X)
    if vin(lst) == X:
        label_title.configure(text='Победил компьютер')
        print('Победил компьютер')
        return
    if nichya(lst):
        label_title.configure(text='Ничья')
        print('ничья')
        return
