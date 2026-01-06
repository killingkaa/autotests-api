import socket

def server():
    messages_list = []

    server_socker = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 12345)
    server_socker.bind(server_address)

    server_socker.listen(10)
    print("Сервер запущен и ждёт подключений...")

    while True:
        client_socket, client_address = server_socker.accept()
        print(f"Пользователь с адресом: {client_address} подключился к серверу")

        message = client_socket.recv(1024).decode()
        print(f"Пользователь с адресом: {client_address} отправил сообщение: {message}")

        messages_list.append(message)
        client_socket.send('\n'.join(messages_list).encode())

        client_socket.close()

if __name__ == "__main__":
    server()