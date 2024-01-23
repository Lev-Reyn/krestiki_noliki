import socket
import json


def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 12345))

    # Начальное состояние игры
    game_state = {'field': [0, 0, 0, 0, 0, 0, 0, 0, 0]}

    # Отправка начального состояния серверу
    data = json.dumps(game_state).encode('utf-8')
    client_socket.send(data)

    # Получение обновленного состояния от сервера
    updated_state = client_socket.recv(1024)
    game_state = json.loads(updated_state.decode('utf-8'))
    print("Обновленное состояние от сервера: ", game_state)

    client_socket.close()


if __name__ == "__main__":
    start_client()
