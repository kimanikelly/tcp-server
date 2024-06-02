# syntax=docker/dockerfile:1

FROM python:latest

EXPOSE 80

ENTRYPOINT [ "python3", "./server.py" ]

COPY . .