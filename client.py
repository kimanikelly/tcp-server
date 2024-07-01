import socket
import os
import dotenv
import click
import datetime
import hashlib
import getpass


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


class User:
    def __init__(self, username, join_date, entries):
        self.username = username
        self.join_date = join_date
        self.entries = entries


@click.group()
def cli():
    pass


@cli.command(help="Register new users")
def register():

    # Temporary placeholder
    test = "test"

    # Prompts new users for their username (whitespaces are removed)
    username = input("Create your username: ").strip()

    # Checks if the username inputs are empty or already exists
    while username == "" or username == test:

        # Checks if the username is empty
        if username == "":

            username = input(
                "Username cannot be empty, please re-enter your username: ").strip()

        # Checks if the username already exists
        if username == test:

            # Prompts the user for a new username (whitespaces are removed)
            username = input(
                "Sorry, that username already exists, please re-enter your username: ").strip()

    # Prompt new users for their password
    initial_hashed_password = hashlib.sha256(getpass.getpass(
        "Create your password: ").encode("utf-8")).hexdigest().strip()

    # Prompt new users to verify their password against the initial password entered
    verified_hashed_password = hashlib.sha256(getpass.getpass(
        "Verify your password: ").encode("utf-8")).hexdigest().strip()

    # Checks if the initial password is not equal to the verified password
    while initial_hashed_password != verified_hashed_password:

        # Prompts the user to verify their password
        verified_hashed_password = hashlib.sha256(getpass.getpass(
            "Password was not verified, please re-enter your password: ").encode("utf-8")).hexdigest().strip()

    user = User(username=username,
                join_date=datetime.datetime.now(), entries=0)

    # Prints to the CLI after successfully registering a user
    click.echo(f'Welcome, {user.username}!')


if __name__ == "__main__":
    cli()
