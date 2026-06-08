import socket

SERVER_ADDRESS = "127.0.0.1"
SERVER_PORT = 6969
SERVER_ENDPOINT = (SERVER_ADDRESS, SERVER_PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(SERVER_ENDPOINT)
print(f"Connected to server at {SERVER_ADDRESS}:{SERVER_PORT}")
while True:
    try:
        message_bdy = input("Send a message to server: ").encode()
        client.send(message_bdy)
        response = client.recv(1024).decode()
        print(f" == SERVER == {response}")
    except KeyboardInterrupt:
        break

client.close()