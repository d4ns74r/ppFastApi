FROM python:3.9



# Dockerfile
WORKDIR /client-service/app

# Скопируйте requirements.txt
COPY requirements.txt .

# Установите зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Скопируйте исходный код
COPY ./app ./app

# Укажите рабочую директорию
WORKDIR /client-service/app

ENV PYTHONPATH=/app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]


