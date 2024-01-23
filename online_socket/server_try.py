import socket
import json

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 12345))
    server_socket.listen()

    print("Ожидание подключения клиента...")
    client_socket, addr = server_socket.accept()
    print(f"Клиент подключен: {addr}")

    while True:
        # Получение данных от клиента
        data = client_socket.recv(1024)
        if not data:
            break

        # Обработка данных (игровая логика)
        game_state = json.loads(data.decode('utf-8'))
        print("Получено от клиента: ", game_state)

        # Здесь должна быть логика обновления состояния игры
        # Например, обновление поля после хода игрока
        game_state['field'][0] = 'X'  # Пример обновления

        # Отправка обновленного состояния обратно клиенту
        updated_state = json.dumps(game_state).encode('utf-8')
        client_socket.send(updated_state)

    client_socket.close()
    server_socket.close()

if __name__ == "__main__":
    start_server()
