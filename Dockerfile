#FROM python:3
#
#WORKDIR /usr/local/app
#
#COPY requirements.txt ./
#
#COPY Pages ./Pages
#
#RUN pip install --no-cache-dir -r requirements.txt
#
#CMD ["python", "test_Login_Page.py"]

# Укажите базовый образ Python
FROM python:3.10

# Установите необходимое ПО
RUN apt-get update && apt-get install -y --no-install-recommends \
    firefox-esr \
    && rm -rf /var/lib/apt/lists/*

# Установите GeckoDriver для Selenium
RUN pip install selenium

# Укажите рабочую директорию
WORKDIR /app

# Копируйте файл с зависимостями
COPY requirements.txt .

# Установите зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируйте остальные файлы проекта
COPY . .

# Укажите команду для запуска приложения
CMD ["python", "test_Login_Page.py"]



