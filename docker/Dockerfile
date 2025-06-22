# test-weather-mvp Dockerfile
FROM python:3.11-slim

WORKDIR /app

# Установим зависимости (requirements.txt ещё добавим позже)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем весь код проекта
COPY . .

# Точка входа — скрипт предсказания
ENTRYPOINT ["python", "scripts/predict.py"]
