# Slim Python base
FROM python:3.11-slim

ENV PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential curl && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copy only what’s needed to resolve/install Python deps
COPY pyproject.toml README.md /app/
COPY backend /app/backend

# Install the project (reads dependencies from pyproject)
RUN pip install --upgrade pip && pip install .

# Copy the rest if you need other backend files at runtime.
# (We do NOT need to copy the frontend for the API image.)
# COPY . /app

# Cloud Run will inject $PORT
ENV PORT=8080

# Point to your app inside backend/main.py
CMD ["python", "-c", "import os, uvicorn; uvicorn.run('backend.main:app', host='0.0.0.0', port=int(os.environ.get('PORT','8080')))"]
