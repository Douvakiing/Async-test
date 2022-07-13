from task import Task
import socket, select


class TCP_Server(Task):
    def __init__(self, port=6942):
        super().__init__()
        super().set_tasks(self.print_hostname_port)
        super().set_looping_tasks(self.server_handler)

        self.port = port

        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        self.server.setblocking(False)

        self.server.bind(("", port))
        self.server.settimeout(0.5)
        self.server.listen(5)

        self.connected_list = []
        self.addresses = []

        self.connected_list.append(self.server)
        self.msg = ""

        # self.rList, _, _ = select.select(self.connected_list, [], [])

    def precancel(self):
        for sock in self.rList:
            sock.shutdown(socket.SHUT_RDWR)
            sock.close()

    def print_hostname_port(self):
        print(str((socket.gethostbyname(socket.gethostname()), self.port)))

    def server_handler(self):
        self.rList = select.select(self.connected_list, [], [], 0.01)[0]

        for sock in self.rList:
            if sock == self.server:
                client, addr = self.server.accept()
                self.connected_list.append(client)
                self.addresses.append(addr[0])

                print(f"Client {addr} connected")

            else:
                msg = sock.recv(1024).decode("utf-8")
                sock_addr = self.addresses[self.connected_list.index(sock) - 1]

                self.msg = msg

                if msg == "DSC" or not msg:
                    self.connected_list.remove(sock)
                    self.addresses.remove(sock_addr)
                    sock.close()

                    print(f"{sock_addr} disconnected")
                    break

                print(f"{sock_addr} sent {msg}")

    def get_msg(self):
        return self.msg


if __name__ == "__main__":
    try:
        SERV = TCP_Server()
        SERV.print_hostname_port()
        while True:
            SERV.server_handler()
    except KeyboardInterrupt:
        exit(0)
