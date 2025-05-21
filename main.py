import socket
import threading

def is_port_available(port: int) -> bool:
    """

    """

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex(('127.0.0.1', port))

    return result == 0


def handle_client(client_socket):
    request = client_socket.recv(1024)
    print(f"{request = }")

    client_socket.close()


class GetressApp():
    def __init__(self):
        pass

    def listen(ip = None, port = None):
        if port is None:
            port = 3000
            while not is_port_available(port):
                port += 1
        if not is_port_available(port):
            raise Exception(f"Port {port} is not available.")

        if ip is None:
            ip = "0.0.0.0"

        # make TCP socket
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_sock:
            # bind socket to ip and port
            server_sock.bind(address=(ip, port))

            # start listening to clients
            while True:
                client, addr = server_sock.accept()

                client_handler = threading.Thread(target=handle_client, args=(client,))
                client_handler.start()
