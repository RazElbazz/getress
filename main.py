import socket
import threading
from typing import Tuple

SocketAddress = Tuple[str, int]


def is_port_available(address: SocketAddress) -> bool:
    """
        Function that returns whether or not
        the given port is in use.
    """

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        result = sock.connect_ex(address)
        return result != 0


def handle_client(client_socket):
    request = client_socket.recv(1024)
    print(f"{request = }")

    client_socket.close()


class GetressApp():
    def __init__(self):
        pass

    def listen(self, ip = None, port = None):
        if ip is None:
            ip = "0.0.0.0"
        if port is None:
            port = 3000
            while not is_port_available((ip, port)):
                print(f"Port {port} is not available")
                port += 1
        if not is_port_available((ip, port)):
            raise Exception(f"Port {port} is not available.")

        print(f"Making TCP socket")

        # make TCP socket
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_sock:
            # bind socket to ip and port
            server_sock.bind((ip, port))
            server_sock.listen()

            print(f"Listening on {server_sock.getsockname()}")

            # start listening to clients
            while True:
                client, addr = server_sock.accept()

                client_handler = threading.Thread(target=handle_client, args=(client,))
                client_handler.start()
