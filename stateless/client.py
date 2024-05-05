import socket

def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('127.0.0.1', 8888))
    
    while True:
        message = input("Enter message to send to server (type 'exit' to quit): ")
        if message.lower() == 'exit':
            break
        
        client_socket.send(message.encode())
        response = client_socket.recv(1024).decode()
        print(f"Response from server: {response}")

    client_socket.close()

if __name__ == "__main__":
    main()
