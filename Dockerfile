# ==== FRONTEND BUILD STAGE ====
FROM node:18 AS frontend

WORKDIR /app/frontend
COPY frontend/package.json frontend/package-lock.json ./
RUN npm install
COPY frontend/ ./
RUN npm run build

# ==== BACKEND BUILD STAGE ====
FROM python:3.13 AS backend

WORKDIR /app

# Install Poetry
RUN pip install poetry

COPY pyproject.toml poetry.lock README.md ./

COPY backend/ /app/backend/
RUN poetry config virtualenvs.create false && poetry install

COPY --from=frontend /app/frontend/dist ./static

EXPOSE 8000
ENV prod=1

CMD ["uvicorn", "backend.src.main:app", "--host", "0.0.0.0", "--port", "8000"]

