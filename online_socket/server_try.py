import socket  # Импортируем модуль для работы с сетевыми соединениями
import json  # Импортируем модуль для работы с данными в формате JSON
import time  # Импортируем модуль для работы со временем (например, задержка)


def start_server():
    # Создаем сокет. Это как телефон, который может звонить и принимать звонки.
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Настраиваем сокет на определенный адрес и порт. 'localhost' - это ваш компьютер.
    server_socket.bind(('localhost', 12345))

    # Говорим сокету начать прослушивание входящих соединений (как будто мы ожидаем звонка).
    server_socket.listen()

    print("Ожидание подключения клиента...")  # Печатаем сообщение о начале ожидания подключения

    # Принимаем подключение от клиента (другого компьютера). Это как ответ на звонок.
    client_socket, addr = server_socket.accept()

    # Печатаем информацию о подключившемся клиенте.
    print(f"Клиент подключен: {addr}")

    # Запускаем бесконечный цикл, чтобы постоянно общаться с клиентом.
    count = 0
    while True:
        # Получаем данные от клиента. Это как получение сообщения.
        data = client_socket.recv(1024)
        if not data:
            break  # Если данных нет, выходим из цикла.

        # Преобразуем полученные данные из формата JSON в словарь Python.
        game_state = json.loads(data.decode('utf-8'))
        print("Получено от клиента: ", game_state)  # Печатаем полученные данные.

        time.sleep(5)  # Ждем 5 секунд перед ответом.

        # Обновляем состояние игры. Например, ставим 'O' в ячейку поля.
        game_state['field'][count] = 'O'
        count += 2

        # Переводим обновленное состояние игры обратно в формат JSON и отправляем клиенту.
        updated_state = json.dumps(game_state).encode('utf-8')
        client_socket.send(updated_state)

    # Закрываем соединение с клиентом и сокет сервера.
    client_socket.close()
    server_socket.close()


if __name__ == "__main__":
    start_server()
