FROM python:3.12-alpine

WORKDIR /app

COPY requirements.txt .

# Install system dependencies
RUN apk add --no-cache \
        gcc \
        musl-dev \
        libffi-dev \
        postgresql-libs \
        postgresql-dev \
    && pip install --no-cache-dir -r requirements.txt \
    && apk del gcc musl-dev postgresql-dev

# Copy application
COPY src ./src

# Ensure Python sees the src directory
ENV PYTHONPATH=/app/src

# Run the app
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
