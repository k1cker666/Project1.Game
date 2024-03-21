FROM python:3-slim

WORKDIR /packman/

COPY /config/*.json /packman/config/
COPY /config/maps/*.json /packman/config/maps/
COPY /fonts/*.ttf /packman/fonts/
COPY /images/*.png /packman/images/
COPY /images/sprites/*.png /packman/images/sprites/
COPY /images/sprites/Enemy/Blinky/*.png /packman/images/sprites/Enemy/Blinky/
COPY /images/sprites/Enemy/Clyde/*.png /packman/images/sprites/Enemy/Clyde/
COPY /images/sprites/Enemy/Inky/*.png /packman/images/sprites/Enemy/Inky/
COPY /images/sprites/Enemy/Pinky/*.png /packman/images/sprites/Enemy/Pinky/
COPY /images/sprites/player/*.png /packman/images/sprites/player/
COPY /sounds/ /packman/sounds/
COPY /src/*.py /packman/src/
COPY /src/engine/*.py /packman/src/engine/
COPY /src/engine/board/*.py /packman/src/engine/board/
COPY /src/engine/entity/*.py /packman/src/engine/entity/

RUN pip install pygame

CMD [ "python3", "/packman/src/main.py" ]