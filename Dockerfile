# Установка системы и python
FROM python:3.8-buster
# Обновление Ubuntu & Обновление pip и setuptools
RUN apt-get -y update \
    && apt-get -y clean

# Установка зависимостей
COPY requirements.txt .
RUN pip install -r ./requirements.txt

# Копирование связанных файлов
COPY . .
