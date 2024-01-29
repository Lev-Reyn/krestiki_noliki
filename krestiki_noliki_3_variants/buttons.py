import time
from tkinter import *
from tkmacosx import Button
from vin import vin, nichya
from typing import Union, Dict, List
import random
import socket  # Импортируем модуль для работы с сетевыми соединениями
import json  # Импортируем модуль для работы с данными в формате JSON


class Buttons:
    """Класс родитель, самостоятельно нерабочий"""

    def __init__(self, label_title: Label, window: Tk):
        self.window = window
        self.label_title = label_title

    def grid_forget(self, btns: Union[bool, Dict] = False):
        """Убрать из окна все кнопки (но если передали в btns другие кнопки, то удалить их) """
        if btns != False:
            for btn in btns['buttons']:
                btn: Button
                btn.grid_forget()
            return
        for btn in self.buttons['buttons']:
            btn: Button
            btn.grid_forget()

    def grid(self, btns: Union[bool, Dict] = False):
        """Разместить все кнопки на экран (но если передали в btns другие кнопки, то разместить их)"""
        if btns != False:
            for i, btn in enumerate(btns['buttons']):
                place = btns['place'][i]
                btn: Button
                btn.grid(row=place['row'], column=place['column'], columnspan=place['columnspan'])
            return
        for i, btn in enumerate(self.buttons['buttons']):
            place = self.buttons['place'][i]
            btn: Button
            btn.grid(row=place['row'], column=place['column'], columnspan=place['columnspan'])

    def on_close(self):
        """Закрытие игры"""
        self.window.destroy()


class ButtonsVariantGame(Buttons):
    def __init__(self, label_title: Label, window: Tk):
        super().__init__(label_title=label_title, window=window)
        self.__buttons_variants_game()
        self.window = window

    def variant_game(self, var_game: str):
        self.var_game = var_game
        if self.var_game == 'comp' or self.var_game == 'second_player':
            self.btn_pole = ButtonsPole(label_title=self.label_title, var_game=self.var_game,
                                        window=self.window)  # запускаем игровое поле
            self.btn_pole.grid()
        else:
            # по сети
            self.label_title.configure(text='В разработке')
            self.btn_server_client = ButtonsServerClient(label_title=self.label_title, window=self.window)
            self.btn_server_client.grid_server_client()

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

    def __init__(self, label_title, var_game: str, window: Tk):
        super().__init__(label_title=label_title, window=window)
        self.variant_game = var_game
        self.start_new_pole()
        # if self.variant_game == 'online':
        #     self.btn_server_client = ButtonsServerClient(label_title=self.label_title)
        #     self.btn_server_client.grid()
        #     self.server_client = server_client

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
        if self.variant_game != 'online':
            self.count_step += 1
            # если ход чётный по счёту, то ходит X
            if self.count_step % 2 == 0:
                znak = self.X
        self.lst[int(btn.cget('text')) - 1] = znak  # заменяем в списке значение на знак (нолик или крестик)
        # разные цвета для ходов человека и ходов компьютера
        btn.configure(text=znak)
        if znak == 'O':
            btn.configure(fg='white')
        else:
            btn.configure(fg='red')
        if vin(lst=self.lst) == self.O:
            self.label_title.configure(text='Победил O')
            print('победил O')
            self.end_game = True
            self.disable_buttons()  # отключаем кнопки, когда выиграл O
            return {'condition': 'O'}
        if vin(lst=self.lst) == self.X:
            self.label_title.configure(text='Победил X')
            print('победил X')
            self.end_game = True
            self.disable_buttons()  # отключаем кнопки, когда выиграл X
            return {'condition': 'X'}
        if nichya(lst=self.lst):
            self.label_title.configure(text='Ничья')
            print('ничья')
            self.end_game = True
            self.disable_buttons()  # отключаем кнопки, когда ничья
            return {'condition': 'ничья'}
        if self.variant_game == 'comp' and znak == 'O':  # ход компьютера, если выбран режим игры с компьютером
            num_btn = self.__robot(self.__del_x_o())
            self.o(btn=self.buttons['buttons'][num_btn - 1], znak='X')

        if self.variant_game == 'online':
            print('online')
        return {'condition': None}  # никто не выиграл, не проиграл, ничьи нет

    def disable_buttons(self):
        """Отключение всех кнопок игры"""
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

    # работа с сервером


class ButtonsServerClient(ButtonsPole):
    def __init__(self, label_title: Label, window: Tk):
        super().__init__(label_title=label_title, var_game='online', window=window)
        self.window = window
        self.__buttons_server_client()
        # Начальное состояние игры - поле для игры и состояние игры.
        self.game_state = {'field': [1, 2, 3, 4, 5, 6, 7, 8, 9],
                           'condition': None}
        self.client = False
        self.server = False
        pass

    def __buttons_server_client(self):
        colour_button = 'blue'

        self.btn_server = Button(text='server', background=colour_button, font=('impact', 60), width=362,
                                 height=180, fg='yellow', activebackground='yellow', activeforeground='blue',
                                 command=lambda: self.start_server())
        self.btn_client = Button(text='client', background=colour_button, font=('impact', 60), width=362,
                                 height=180, fg='yellow', activebackground='yellow', activeforeground='blue',
                                 command=lambda: self.client_entry_ip())

        self.buttons_client_server = {'buttons': [self.btn_server, self.btn_client],
                                      'place': [
                                          {'row': 1, 'column': 0, 'columnspan': 3},  # кнопка запуска сервера
                                          {'row': 1, 'column': 3, 'columnspan': 3},
                                          # кнопка запуска клиента (поиск сервера)
                                      ]
                                      }

    def start_server(self):
        """Создаём сервер и начинаем прослушивать входящие соединения"""
        self.server = True  # обозначаем, что данный человек включил сервер
        # Создаем сокет. Это как телефон, который может звонить и принимать звонки.
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print(socket.gethostname())
        # Настраиваем сокет на определенный адрес и порт. 'localhost' - это ваш компьютер.
        self.label_title.configure(text=f'Ждём подключения клиента\n'
                                        f'со стороны клиента введите '
                                        f'{socket.gethostbyname_ex(socket.gethostname())[-1][-1]}')
        self.window.update()
        self.server_socket.bind((socket.gethostbyname_ex(socket.gethostname())[-1][-1], 12345))
        print(socket.gethostbyname_ex(socket.gethostname()))

        # Говорим сокету начать прослушивание входящих соединений (как будто мы ожидаем звонка).
        self.server_socket.listen()

        print("Ожидание подключения клиента...")  # Печатаем сообщение о начале ожидания подключения

        # Принимаем подключение от клиента (другого компьютера). Это как ответ на звонок.
        self.client_socket, self.addr = self.server_socket.accept()

        # Печатаем информацию о подключившемся клиенте.
        print(f"Клиент подключен: {self.addr}")
        self.label_title.configure(text=f'Клиент {self.addr} подключён и начинает ходить первым, ожидаем его хода')
        self.grid_forget_server_client()  # убираем кнопки сервера и клиента

        # ----------  # здесь будет код получения и отправки информации
        # ----------

        self.server_receiving_msg()  # получаем сообщение (ждём, когда клиент пришлёт сообщение)
        # ----------

    def server_close(self):
        """Закрывает соединение сервера"""
        # Закрываем соединение с клиентом и сокет сервера.
        self.client_socket.close()
        self.server_socket.close()
        print('Соединение закрыто')

    def server_receiving_msg(self):
        """Получаем сообщение от клиента"""
        # Получаем данные от клиента. Это как получение сообщения.
        data = self.client_socket.recv(1024)
        # Преобразуем полученные данные из формата JSON в словарь Python.
        self.game_state = json.loads(data.decode('utf-8'))
        self.lst = self.game_state['field']  # изменяем lst
        self.grid_pole()  # размещаем в окне кнопки игры
        self.change_buttons()  # изменяем игровое поле, как сходил клиент
        if self.game_state['condition'] == 'O':
            self.label_title.configure(text='победил O')  # обновляем информацию, что победил O
            self.disable_buttons()
        if self.game_state['condition'] == 'ничья':
            self.label_title.configure(text='Ничья')  # обновляем информацию, что ничья
            self.disable_buttons()
        print("Получено от клиента: ", self.game_state)  # Печатаем полученные данные.

    def server_send(self, key: str, value: Union[list, str], **kwargs):
        self.game_state[key] = value
        self.game_state |= kwargs  # добавляем всё, что добавлено в kwargs
        # for key, value in kwargs.items():
        #     self.game_state[key] = value
        # Переводим обновленное состояние игры обратно в формат JSON и отправляем клиенту.
        self.updated_state = json.dumps(self.game_state).encode('utf-8')
        self.client_socket.send(self.updated_state)
        self.server_receiving_msg()
        pass

    def client_entry_ip(self):
        """
        После того, как клиент нажимает, что он клиент, появляется меню, для ввода самого ip адреса,
        по которому подключиться
        """
        self.entry_ip = Entry(width=15, font=('impact', 40))
        self.btn_send_ip = Button(text='Подключиться', width=380, font=('impact', 40),
                                  command=lambda: self.start_client_after_entry_ip())
        self.grid_forget_server_client()
        self.button_entry_ip = {'buttons': [self.entry_ip, self.btn_send_ip],
                                'place': [
                                    {'row': 1, 'column': 0, 'columnspan': 1},  # entry для ip адреса
                                    {'row': 1, 'column': 2, 'columnspan': 5},  # btn для подключения
                                ]
                                }
        self.grid(btns=self.button_entry_ip)

    def start_client_after_entry_ip(self):
        """
        Клиент хранит ip адрес, по которому осуществляется подключение к сервер
        """
        self.ip_server_for_client = self.entry_ip.get()  # переменная, которая хранит ip адрес сервера, для подключения
        # нужно запустить асинхронный таймер, который сбросит код для подключения
        self.grid_forget(btns=self.button_entry_ip)
        self.window.update()
        self.start_client()

    def start_client(self):
        self.client = True  # обозначаем, что данный человек включил клиента
        # Создаем сокет. Это как телефон, который можно использовать для звонков.
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.client_socket.settimeout(10)  # Установка времени ожидания в 10 секунд
        try:
            # Подключаемся к серверу. 'localhost' и 12345 - это адрес и порт сервера.
            self.client_socket.connect((self.ip_server_for_client, 12345))
        except socket.timeout:
            print("Не удалось подключиться за отведенное время")
            self.label_title.configure(text=f'Не удалось подключиться за отведенное время / сервер не подключён\n'
                                            f'попробуйте снова ввести ip адрес')
            self.client_entry_ip()  # запускаем повторно возможность ввести ip адрес
            return
        except socket.error as err:
            print(f"Произошла ошибка сокета: {err}")
            self.label_title.configure(text=f'Произошла ошибка сокета: {err} / сервер не подключён\n'
                                            f'попробуйте снова ввести ip адрес')
            self.client_entry_ip()  # запускаем повторно возможность ввести ip адрес
            return

        # Печатаем информацию о том, что успешно подключились
        print(f"Успешно подключились")
        self.label_title.configure(text=f'Успешно подключились, твой ход первый')
        # ----------  # здесь будет код получения и отправки информации
        # ----------

        self.grid_forget_server_client()  # убираем кнопки сервера и клиента
        self.grid_pole()  # размещаем в окне кнопки игры

    def client_receiving_msg(self):
        """Получаем сообщение от сервера"""
        # Ждем ответа от сервера и получаем обновленное состояние игры.
        # Это как получение ответного сообщения.
        self.updated_state = self.client_socket.recv(1024)
        self.game_state = json.loads(self.updated_state.decode('utf-8'))
        self.lst = self.game_state['field']  # изменяем lst
        self.grid_pole()  # размещаем в окне кнопки игры
        self.change_buttons()  # изменяем игровое поле, как сходил клиент
        if self.game_state['condition'] == 'X':
            self.label_title.configure(text='победил X')  # обновляем информацию, что победил O
            self.disable_buttons()
        if self.game_state['condition'] == 'ничья':
            self.label_title.configure(text='Ничья')  # обновляем информацию, что ничья
            self.disable_buttons()
        print("Получено от клиента: ", self.game_state, f'list {print(self.lst)}')  # Печатаем полученные данные.
        # Печатаем обновленное состояние игры, полученное от сервера.
        print("Обновленное состояние от сервера: ", self.game_state)

    def client_close(self):
        # Закрываем соединение с сервером. Это как завершение звонка.
        self.client_socket.close()
        print('соединение закрыто')

    def client_send(self, key: str, value: Union[list, str], **kwargs):
        self.game_state[key] = value
        self.game_state |= kwargs  # добавляем всё, что добавлено в kwargs
        # Преобразуем начальное состояние игры в формат JSON и отправляем серверу.
        # Это как отправка сообщения с описанием игры.
        data = json.dumps(self.game_state).encode('utf-8')
        self.client_socket.send(data)
        self.client_receiving_msg()

    def grid_pole(self):
        super().grid()

    def grid_server_client(self):
        self.label_title.configure(text='Выберите вы клиент или сервер')
        self.grid(btns=self.buttons_client_server)

    def grid_forget_pole(self):
        self.grid()

    def grid_forget_server_client(self):
        self.grid_forget(btns=self.buttons_client_server)

    def __buttons_pole(self):  # кнопки для онлайн игры будут немного иными
        colour_button = 'blue'
        self.btn1 = Button(text=1, background=colour_button, font=('impact', 60), height=180, fg='blue',
                           activebackground='blue', activeforeground='blue',
                           command=lambda: self.o(btn=self.btn1, znak='O'))

    def o(self, btn: Button, znak: str = 'O'):
        # self.disable_buttons()
        if self.server:
            condition = super().o(btn=btn, znak='X')['condition']  # состояние игры
            self.window.update()
            self.server_send(key='field', value=self.lst, condition=condition)
            # self.server_close()

        if self.client:
            condition = super().o(btn=btn, znak='O')['condition']  # состояние игры
            print(f'client work {btn} \n{btn.cget("text")}')
            self.window.update()
            self.client_send(key='field', value=self.lst, condition=condition)

            # self.client_close()  # закрываем соединение клиента

    def change_buttons(self):
        # изменяем все кнопки под обновлённый список
        for i, btn in enumerate(self.buttons['buttons']):
            if self.lst[i] == 'X':
                btn.configure(text=str(self.lst[i]), fg='red')
            elif self.lst[i] == "O":
                btn.configure(text=str(self.lst[i]), fg='white')
            # print(f'{i} изменили на кнопке {btn}, {self.lst[i]}')

    def on_close(self):
        """
        Помимо основного закрытия игры отключаем сервер и клиента
        """
        if self.client:
            self.client_close()

        if self.server:
            self.server_close()
        super(ButtonsServerClient, self).on_close()
        self.window.destroy()
