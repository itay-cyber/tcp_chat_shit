import socket

SERVER_ADDRESS = "127.0.0.1"
SERVER_PORT = 6969
SERVER_ENDPOINT = (SERVER_ADDRESS, SERVER_PORT)
clients = {}


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(SERVER_ENDPOINT)
server.listen()

print("Waiting for connection from client...")
(client, address) = server.accept()

print(f"Connected: {address[0]}:{address[1]}: ")

while True:
    try:
        message = client.recv(1024).decode()
        print(f" == CLIENT == {message}")
        response_bdy = input("Enter response: ")
        response_full = f"{response_bdy}".encode()
        client.send(response_full)
    except KeyboardInterrupt:
        break

server.close()