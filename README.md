# TCP-Server

## Summary

Used the server code from Chapter 2: Basic Networking Tools, pages 12-13 in [Black Hat Python: Python Programming for Hackers and Pentesters](https://www.amazon.com/Black-Hat-Python-2nd-Programming/dp/1718501129).

Implemented custom containerization that was not included with the server code by building a Dockerfile and deployed the Dockerized server to an AWS EC2 instance with the help of [Hosting a Docker Container on AWS EC2 Free Tier in under 12 minutes](https://www.youtube.com/watch?v=qNIniDftAcU).

## AWS EC2 Instance

- http://54.221.151.58:80

## Prerequisites

- [Install Python](https://www.python.org/downloads/)
- [Install Docker](https://docs.docker.com/engine/install/)

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

- [Black Hat Python: Python Programming for Hackers and Pentesters](https://www.amazon.com/Black-Hat-Python-2nd-Programming/dp/1718501129)

- [Hosting a Docker Container on AWS EC2 Free Tier in under 12 minutes](https://www.youtube.com/watch?v=qNIniDftAcU)
