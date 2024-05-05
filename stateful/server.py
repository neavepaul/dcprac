import socket

def handle_client(client_socket, client_states):
    while True:
        request = client_socket.recv(1024).decode()
        if not request:
            break
        
        if request == 'get_state':
            response = client_states.get(client_socket, "No state set")
        else:
            client_states[client_socket] = request
            response = "State updated"
        
        client_socket.send(response.encode())

    client_socket.close()

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('127.0.0.1', 8888))
    server_socket.listen(5)
    print("Server listening on port 8888...")
    
    client_states = {}

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Accepted connection from {client_address}")
        handle_client(client_socket, client_states)

if __name__ == "__main__":
    main()
