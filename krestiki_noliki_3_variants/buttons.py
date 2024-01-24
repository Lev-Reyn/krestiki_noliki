from tkinter import *
from tkmacosx import Button
from vin import vin, nichya
import random


class Buttons:
    """Класс родитель, самостоятельно нерабочий"""

    def grid_forget(self):
        """Убрать из окна все кнопки"""
        for btn in self.buttons['buttons']:
            btn: Button
            btn.grid_forget()

    def grid(self):
        """Разместить все кнопки на экран"""
        for i, btn in enumerate(self.buttons['buttons']):
            place = self.buttons['place'][i]
            btn: Button
            btn.grid(row=place['row'], column=place['column'], columnspan=place['columnspan'])


class ButtonsVariantGame(Buttons):
    def __init__(self, label_title: Label):
        self.label_title = label_title
        self.__buttons_variants_game()

    def variant_game(self, var_game: str):
        self.var_game = var_game
        btn_pole = ButtonsPole(label_title=self.label_title, var_game=self.var_game)  # запускаем игровое поле
        if self.var_game == 'comp' or self.var_game == 'second_player':
            btn_pole.grid()
        else:
            # по сети
            self.label_title.configure(text='В разработке')
            pass

    def __buttons_variants_game(self):
        colour_button = 'blue'
        self.btn_comp = Button(text='с компьютером', background=colour_button, font=('impact', 30), width=240,
                               height=180, fg='yellow', activebackground='yellow', activeforeground='blue',
                               command=lambda: [self.grid_forget(), self.variant_game(var_game='comp')])
        self.btn_second_player = Button(text='с другим игроком', background=colour_button, font=('impact', 30),
                                        width=240,
                                        height=180, fg='yellow', activebackground='yellow', activeforeground='blue',
                                        command=lambda: [self.grid_forget(),
                                                         self.variant_game(var_game='second_player')])
        self.btn_online = Button(text='онлайн', background=colour_button, font=('impact', 30), width=240,
                                 height=180, fg='yellow', activebackground='yellow', activeforeground='blue',
                                 command=lambda: [self.grid_forget(),
                                                  self.variant_game(var_game='online')])

        self.buttons = {'buttons': [self.btn_comp, self.btn_second_player, self.btn_online],
                        'place': [
                            {'row': 1, 'column': 0, 'columnspan': 2},  # кнопка btn_comp
                            {'row': 1, 'column': 2, 'columnspan': 2},  # кнопка btn_second_player
                            {'row': 1, 'column': 4, 'columnspan': 2},  # кнопка btn_online
                        ]
                        }


class ButtonsPole(Buttons):
    O = 'O'
    X = 'X'

    def __init__(self, label_title, var_game: str):
        self.variant_game = var_game
        self.label_title = label_title
        self.start_new_pole()
        pass

    def __buttons_pole(self):
        colour_button = 'blue'
        self.btn1 = Button(text=1, background=colour_button, font=('impact', 60), height=180, fg='blue',
                           activebackground='blue', activeforeground='blue',
                           command=lambda: self.o(btn=self.btn1, znak='O'))
        self.btn2 = Button(text=2, background=colour_button, font=('impact', 60), height=180, fg='blue',
                           activebackground='blue', activeforeground='blue',
                           command=lambda: self.o(btn=self.btn2, znak='O'))
        self.btn3 = Button(text=3, background=colour_button, font=('impact', 60), height=180, fg='blue',
                           activebackground='blue', activeforeground='blue',
                           command=lambda: self.o(btn=self.btn3, znak='O'))
        self.btn4 = Button(text=4, background=colour_button, font=('impact', 60), height=180, fg='blue',
                           activebackground='blue', activeforeground='blue',
                           command=lambda: self.o(btn=self.btn4, znak='O'))
        self.btn5 = Button(text=5, background=colour_button, font=('impact', 60), height=180, fg='blue',
                           activebackground='blue', activeforeground='blue',
                           command=lambda: self.o(btn=self.btn5, znak='O'))
        self.btn6 = Button(text=6, background=colour_button, font=('impact', 60), height=180, fg='blue',
                           activebackground='blue', activeforeground='blue',
                           command=lambda: self.o(btn=self.btn6, znak='O'))
        self.btn7 = Button(text=7, background=colour_button, font=('impact', 60), height=180, fg='blue',
                           activebackground='blue', activeforeground='blue',
                           command=lambda: self.o(btn=self.btn7, znak='O'))
        self.btn8 = Button(text=8, background=colour_button, font=('impact', 60), height=180, fg='blue',
                           activebackground='blue', activeforeground='blue',
                           command=lambda: self.o(btn=self.btn8, znak='O'))
        self.btn9 = Button(text=9, background=colour_button, font=('impact', 60), height=180, fg='blue',
                           activebackground='blue', activeforeground='blue',
                           command=lambda: self.o(btn=self.btn9
                                                  , znak='O'))

        self.buttons = {'buttons': [self.btn1, self.btn2, self.btn3, self.btn4, self.btn5,
                                    self.btn6, self.btn7, self.btn8, self.btn9],
                        'place': [
                            {'row': 1, 'column': 0, 'columnspan': 2},  # кнопка 1
                            {'row': 1, 'column': 2, 'columnspan': 2},  # кнопка 2
                            {'row': 1, 'column': 4, 'columnspan': 2},  # кнопка 3
                            {'row': 2, 'column': 0, 'columnspan': 2},  # кнопка 4
                            {'row': 2, 'column': 2, 'columnspan': 2},  # кнопка 5
                            {'row': 2, 'column': 4, 'columnspan': 2},  # кнопка 6
                            {'row': 3, 'column': 0, 'columnspan': 2},  # кнопка 7
                            {'row': 3, 'column': 2, 'columnspan': 2},  # кнопка 8
                            {'row': 3, 'column': 4, 'columnspan': 2},  # кнопка 9
                        ]
                        }

    def start_new_pole(self):
        """Обнуляет поле"""
        self.lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.__buttons_pole()
        self.count_step = 0
        self.end_game = False

    def o(self, btn: Button, znak: str = 'O'):
        label_title: Label
        self.label_title.configure(text='Ходи')
        if not str(btn.cget('text')).isdigit():
            self.label_title.configure(text='Занято')
            return False
        self.count_step += 1
        # если ход чётный по счёту, то ходит X
        if self.count_step % 2 == 0:
            znak = self.X
        self.lst[int(btn.cget('text')) - 1] = znak  # заменяем в списке значение на знак (нолик или крестик)
        # разные цвета для ходов человека и ходов компьютера
        btn.configure(text=znak)
        if znak == ButtonsPole.O:
            btn.configure(fg='white')
        else:
            btn.configure(fg='red')
        if vin(lst=self.lst) == self.O:
            self.label_title.configure(text='Победил O')
            print('победил O')
            self.end_game = True
            self.disable_buttons()  # отключаем кнопки, когда выиграл O
            return True
        if vin(lst=self.lst) == self.X:
            self.label_title.configure(text='Победил X')
            print('победил X')
            self.end_game = True
            self.disable_buttons()  # отключаем кнопки, когда выиграл X
            return True
        if nichya(lst=self.lst):
            self.label_title.configure(text='Ничья')
            print('ничья')
            self.end_game = True
            self.disable_buttons()  # отключаем кнопки, когда ничья
            return
        if self.variant_game == 'comp' and znak == 'O':  # ход компьютера, если выбран режим игры с компьютером
            num_btn = self.__robot(self.__del_x_o())
            self.o(btn=self.buttons['buttons'][num_btn - 1], znak='X')

    def disable_buttons(self):
        for btn in self.buttons['buttons']:
            btn['state'] = 'disabled'

    def __del_x_o(self) -> list:
        """Возвращает список без X и O"""
        lst_del = []
        for i in range(len(self.lst)):
            if type(self.lst[i]) != str:
                lst_del.append(self.lst[i])

        return lst_del

    def __robot(self, lst_del: list) -> int:
        """Выбирает куда ставить X"""
        return random.choice(lst_del)
