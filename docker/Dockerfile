# =========================
# Stage 1: Builder
# =========================
FROM python:3.11-slim AS builder

# Рабочая директория внутри контейнера
WORKDIR /app

# Копируем зависимости
COPY app/requirements.txt .

# Устанавливаем зависимости в отдельную папку /install
RUN pip install --upgrade pip \
    && pip install --prefix=/install -r requirements.txt

# =========================
# Stage 2: Final image
# =========================
FROM python:3.11-slim

WORKDIR /app

# Копируем зависимости из builder
COPY --from=builder /install /usr/local

# Копируем код приложения
COPY app/ .

# Устанавливаем переменную окружения для Python
ENV PYTHONUNBUFFERED=1

# Порт приложения
EXPOSE 8000

# Команда запуска (пример для FastAPI)
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
