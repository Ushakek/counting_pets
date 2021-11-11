# Установка системы и python
FROM python:3.8-buster

# Выбор рабочей директории
WORKDIR /usr/src/app

# Обновление Ubuntu & Обновление pip и setuptools
RUN apt-get -y update \
    && apt-get install -y \
		python3-dev \
		libpq-dev\
    && apt-get -y clean

# Установка зависимостей
COPY requirements.txt .
RUN pip install -r ./requirements.txt

# Копирование связанных файлов
COPY . .
