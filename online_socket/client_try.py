import socket  # Импортируем модуль для работы с сетевыми соединениями
import json  # Импортируем модуль для работы с данными в формате JSON
import time


def start_client():
    # Создаем сокет. Это как телефон, который можно использовать для звонков.
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Подключаемся к серверу. 'localhost' и 12345 - это адрес и порт сервера.
    client_socket.connect(('localhost', 12345))

    # Начальное состояние игры - поле для игры и состояние игры.
    game_state = {'field': [1, 2, 3, 4, 5, 6, 7, 8, 9]}
    count = 1
    while True:
        # Преобразуем начальное состояние игры в формат JSON и отправляем серверу.
        # Это как отправка сообщения с описанием игры.
        data = json.dumps(game_state).encode('utf-8')
        client_socket.send(data)

        # Ждем ответа от сервера и получаем обновленное состояние игры.
        # Это как получение ответного сообщения.
        updated_state = client_socket.recv(1024)
        game_state = json.loads(updated_state.decode('utf-8'))

        # Печатаем обновленное состояние игры, полученное от сервера.
        print("Обновленное состояние от сервера: ", game_state)
        time.sleep(5)
        try:
            # Обновляем состояние игры. Например, ставим 'X' в ячейку поля.
            game_state['field'][int(input()) - 1] = 'X'
            # count += 2
        except IndexError:
            print('Закончились свободные поля, игра окончена')
            break

    # Закрываем соединение с сервером. Это как завершение звонка.
    client_socket.close()


if __name__ == "__main__":
    start_client()
