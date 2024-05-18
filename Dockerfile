# syntax=docker/dockerfile:1

FROM python:3.10

EXPOSE 8080

ENTRYPOINT [ "python3", "./server.py" ]

COPY . .