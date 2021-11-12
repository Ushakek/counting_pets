# Установка системы и python
FROM python:3.8-buster

# Выбор рабочей директории
WORKDIR /usr/src/

# Установка переменных окружения
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Создание суперпользователя django
ENV DJANGO_SU_NAME=admin
ENV DJANGO_SU_EMAIL=admin@my.company
ENV DJANGO_SU_PASSWORD=admin

# Обновление пакетов и установка пакетов для psycopg2 и postgresql
RUN apt-get -y update \
    && apt-get install -y \
		python3-dev \
		postgresql \
		postgresql-client \
		libpq-dev \
    && apt-get -y clean

# Установка зависимостей
COPY requirements.txt .
RUN pip install -r ./requirements.txt

# Копирование связанных файлов
COPY . .
