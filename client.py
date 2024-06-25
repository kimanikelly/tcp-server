import socket
import os
import dotenv
import click

dotenv.load_dotenv()

development_host = os.getenv("DEVELOPMENT_HOST")

target_host = development_host
target_port = 80

# Instantiates an instance of the Socket class
# AF_INET - Internet Address Family for IPV4
# IPV4 - Internet Protocol Version 4 as the Address Family
# SOCK_STREAM - Socket type provides a TCP connection
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect Socket class to the target_host & target_port (TCP SERVER)
client.connect((target_host, target_port))
