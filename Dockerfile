# syntax=docker/dockerfile:1

FROM python:3.10

EXPOSE 80

ENTRYPOINT [ "python3", "./server.py" ]

COPY . .