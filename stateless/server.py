import socket

def handle_client(client_socket):
    request = client_socket.recv(1024).decode()
    print(f"Received from client: {request}")
    response = f"Server received: {request}"
    client_socket.send(response.encode())
    client_socket.close()

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('127.0.0.1', 8888))
    server_socket.listen(5)
    print("Server listening on port 8888...")
    
    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Accepted connection from {client_address}")
        handle_client(client_socket)

if __name__ == "__main__":
    main()
