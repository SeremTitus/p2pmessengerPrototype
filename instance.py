import socket
import threading

def receive_messages(server_socket):
    while True:
        client_socket, client_address = server_socket.accept()
        message = client_socket.recv(1024).decode("utf-8")
        print(f"Received message from {client_address[0]}: {message}")
        client_socket.close()

def send_message(server_ip, server_port, message):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_ip, server_port))
    client_socket.send(message.encode("utf-8"))
    client_socket.close()

def main():
    # Set up the server socket
    server_ip = "0.0.0.0"  # Listen on all available interfaces
    server_port = 12345
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((server_ip, server_port))
    server_socket.listen(5)

    # Start the thread to receive messages
    receive_thread = threading.Thread(target=receive_messages, args=(server_socket,))
    receive_thread.start()

    while True:
        # Get the IP address of the recipient
        recipient_ip = input("Enter the IP address of the recipient: ")
        
        if len(recipient_ip) > 0:
            # Get the message to send
            message = input("Enter your message: ")

            # Send the message
            if len(message) > 0:
                message = "[empty message]"
            try:
                send_message(recipient_ip, server_port, message)
            except:
                print("failed to send message, check ip")

if __name__ == "__main__":
    main()
