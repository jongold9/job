# Используйте официальный образ Python как базовый
FROM python:3.8-slim

# Установите рабочий каталог в контейнере
WORKDIR /usr/src/app

# Установите необходимые библиотеки
RUN pip3 install pandas==1.3.0

# Команда, исполняемая при запуске контейнера
CMD ["bash"]

#docker build -t panda . && docker run panda

