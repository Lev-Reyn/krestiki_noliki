import tkinter as tk
from typing import List, Union
from vin import vin, O, X, nichya
from test import robot, del_x_o

end = False


def o(btn: tk.Button, lst: List[Union[int, str]], lst_btn: List[tk.Button], label_title: tk.Label, znak: str = 'O'):
    """
    Ставит нолик в то место, куда указал игрок, и компьютер потом должен будет снова запустить эту функцию,
    что бы сходить
    btn: кнопка, которую нажал игрок
    lst: список, где хранятся все значения игры
    label_title: сам Label, где будет отображаться информация об игре
    znak: какой знак ставить, O или X
    """
    global end
    if end:  # если кто-то победил, или уже ничья, то больше не позволяем ходить
        return
    label_title.configure(text='Ходи')
    if not str(btn.cget('text')).isdigit():
        label_title.configure(text='Уже занято')
        print('уже занято')
        return
    lst[int(btn.cget('text')) - 1] = znak  # заменяем в списке значение на знак (нолик или крестик)
    print(lst)
    # разные цвета для ходов человека и ходов компьютера
    if znak == O:
        btn.configure(text=znak, fg='white')
    else:
        btn.configure(text=znak, fg='red')
    if vin(lst=lst) == O:
        label_title.configure(text='Победил игрок')
        print('победил игрок')
        end = True
        return
    if nichya(lst):
        label_title.configure(text='Ничья')
        print('ничья')
        end = True
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
        end = True
        return
    if nichya(lst):
        label_title.configure(text='Ничья')
        print('ничья')
        end = True
        return


def exit_game(window: tk.Tk):
    window.destroy()


def WM_DELETE_WINDOW_YES_NO(window: tk.Tk):
    """Закрытие окна"""
    popup = tk.Toplevel(window)
    popup.resizable(width=False, height=False)  # запрещаем изменять размер окна
    popup.geometry('200x100')
    popup.title("Предупреждение")

    label = tk.Label(popup, text="Вы уверены, что хотите\n закрыть приложение?")
    label.pack(padx=10, pady=10)

    yes_button = tk.Button(popup, text="Да", command=window.destroy)
    yes_button.pack(side="left", padx=5)

    no_button = tk.Button(popup, text="Нет", command=popup.destroy)
    no_button.pack(side="right", padx=5)


# def WM_DELETE_WINDOW_NO(window: tk.Tk):
#     """не закрывает окно, а переносит в другое место его просто"""
#
#     window.geometry(f'725x600+{}+{}')
class WindowGeometry:
    __diferent_places = [
        ['100', '100'],
        ['400', '100'],
        ['100', '400'],
        ['400', '400'],
    ]

    def __init__(self, window: tk.Tk, window_geometry: str, place_x: str = '20', place_y: str = '20'):
        """
        window_geometry: только разрешение
        place_x: где находится будет по x
        place_y: где находится будет по y
        """
        self.window_geometry = window_geometry
        self.place_x = place_x
        self.place_y = place_y
        self.__n_position = [self.place_x, self.place_y]
        self.window = window
        window.geometry(str(self))
        self.__n = 0

    def __str__(self):
        return f'{self.window_geometry}+{self.place_x}+{self.place_y}'

    def change_place(self, place_x: str, place_y: str):
        self.place_x = place_x
        self.place_y = place_y
        self.window.geometry(str(self))

    def next_place(self):
        self.change_place(place_x=self.__diferent_places[self.__n % len(self.__diferent_places)][0],
                          place_y=self.__diferent_places[self.__n % len(self.__diferent_places)][1])
        # print(self.__diferent_places[self.__n % len(self.__diferent_places)])
        self.__n += 1

# t = RandomWindow('100x200', '100', '120')
