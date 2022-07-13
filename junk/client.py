import socket

SERVER_ADDRESS = "127.0.0.1"
SERVER_PORT = 6942

c = socket.socket()

c.connect((SERVER_ADDRESS, SERVER_PORT))

print("Connected to " + str((SERVER_ADDRESS, SERVER_PORT)))

while True:

    data = input("send: ")

    if data == "":
        c.send("DSC".encode("utf-8"))
        break

    c.send(data.encode("utf-8"))

c.close()
