# socket module - Provides access to the BSD Socket Interface.

# BSD Socket Interface - Berkeley Software Distribution sockets an API for Internet sockets
# used for Inter Process Communication.

# What is a socket - A Network Socket is an endpoint for sending and receiving
# data across the network.
import socket

# threading module - Allows multpile threads of execution to take place in a Python program.
import threading

from database.db_connection import cursor, query, db

import datetime

ip_address = "0.0.0.0"

# Port number the TCP Server will listen on
port = 80


def main():
    # Instantiates an instance of the Socket class
    # AF_INET - Internet Address Family for IPV4
    # IPV4 - Internet Protocol Version 4 as the Address Family
    # SOCK_STREAM - Socket type provides a TCP connection
    socket_instance = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket instance to the ip address and the port number
    socket_instance.bind((ip_address, port))

    # Set the socket instance to listening mode
    socket_instance.listen(5)
    print(f'[*] Listening on {ip_address}:{port}')

    # Put the socket instance into a loop while it waits for an incoming connection
    while True:

        # client - Returns a new Socket instance representing the connection
        # address - Returns a tuple containing the clients Host Address and Port number
        client, address = socket_instance.accept()

        # Stores the client_address, client_port, and time of connection
        # val = (address[0], address[1], datetime.datetime.now())

        # cursor.execute(query, val)

        # db.commit()

        print(f'[*] Accepted connection from {address[0]:{address[1]}}')

        client_handler = threading.Thread(target=handle_client, args=(client,))
        client_handler.start()


def handle_client(client_socket: socket):

    # Returns the request as bytes
    request = client_socket.recv(1024)

    # Prints the request received from bytes to a string
    print(f'[*] Received: {request.decode("utf-8")}')

    # Sends this message back to the client as bytes
    client_socket.send(b'TCP Server')


if __name__ == "__main__":
    main()
