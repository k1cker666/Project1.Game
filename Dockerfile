FROM python:3-slim

WORKDIR /packman/

COPY config /packman/
COPY fonts /packman/
COPY images /packman/
COPY sounds /packman/
COPY /src/*.py /packman/src/
COPY /src/engine/*.py /packman/src/engine/
COPY /src/engine/board/*.py /packman/src/engine/board/
COPY /src/engine/entity/*.py /packman/src/engine/entity/

RUN pip install pygame
