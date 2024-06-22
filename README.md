# TCP-Server

[![Python application](https://github.com/kimanikelly/tcp-server/actions/workflows/python-app.yml/badge.svg)](https://github.com/kimanikelly/tcp-server/actions/workflows/python-app.yml)

## Summary

Used the server code from Chapter 2: Basic Networking Tools, pages 12-13 in [Black Hat Python: Python Programming for Hackers and Pentesters](https://www.amazon.com/Black-Hat-Python-2nd-Programming/dp/1718501129).

Implemented custom containerization that was not included with the server code by building a Dockerfile and deployed the Dockerized server to an AWS EC2 instance with the help of [Hosting a Docker Container on AWS EC2 Free Tier in under 12 minutes](https://www.youtube.com/watch?v=qNIniDftAcU).

## AWS EC2 Instance

- http://54.221.151.58:80

## Prerequisites

- [Install Python](https://www.python.org/downloads/)
- [Install Docker](https://docs.docker.com/engine/install/)
- [Install MySQL](https://dev.mysql.com/downloads/workbench/)

## Getting Started

### Clone Repository

```
git clone https://github.com/kimanikelly/tcp-server.git
```

### Start Server Locally

```
python3 server.py
```

## Resources

- TCP Server Example - [Black Hat Python: Python Programming for Hackers and Pentesters](https://www.amazon.com/Black-Hat-Python-2nd-Programming/dp/1718501129)

- Deploying Docker Container to EC2 - [Hosting a Docker Container on AWS EC2 Free Tier in under 12 minutes](https://www.youtube.com/watch?v=qNIniDftAcU)

- Creating MySQL Database - [W3 Schools Python MySQL (Create Database)](https://www.w3schools.com/python/python_mysql_create_db.asp)

- Creating MySQL Table - [W3 Schools Python MySQL (Create Table)](https://www.w3schools.com/python/python_mysql_create_table.asp)

- Insert Into MySQL Table - [W3 Schools Python MySQL (Insert Into Table)](https://www.w3schools.com/python/python_mysql_insert.asp)
