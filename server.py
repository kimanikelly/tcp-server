# socket module - Provides access to the BSD Socket Interface.

# BSD Socket Interface - Berkeley Software Distribution sockets an API for Internet sockets
# used for Inter Process Communication.

# What is a socket - A Network Socket is an endpoint for sending and receiving
# data across the network.
import socket

# threading module - Allows multpile threads of execution to take place in a Python program.
import threading

IP_ADDRESS = "0.0.0.0"

PORT = 3001


def main():
    # Initializes an instance of the socket class
    # AF_INET - Internet Address Family for IPV4
    # IPV4 - Internet Protocol Version 4 as the Address Family
    # SOCK_STREAM - Socket type provides a TCP connection
    socket_instance = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket instance to the ip address and the port number
    socket_instance.bind((IP_ADDRESS, PORT))

    # Set the socket instance to listening mode
    socket_instance.listen(5)
    print(f'[*] Listening on {IP_ADDRESS}:{PORT}')

    # Put the socket instance into a loop while it waits for an incoming connection
    while True:

        # When a client con
        # address - Returns a tuple containing the clients eg
        client, address = socket_instance.accept()

        print(f'[*] Accepted connection from {address[0]:{address[1]}}')
        client_handler = threading.Thread(target=handle_client, args=(client,))
        client_handler.start()


def handle_client(client_socket):
    with client_socket as sock:
        request = sock.recv(1024)
        print(f'[*] Received: {request.decode("utf-8")}')
        sock.send(b'ACK')


if __name__ == "__main__":
    main()
