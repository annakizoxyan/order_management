FROM python:3.11-slim AS base
WORKDIR /app

COPY pyproject.toml poetry.lock ./
RUN pip install --upgrade pip \
    && pip install poetry \
    && poetry config virtualenvs.create false


RUN poetry install --no-root --only main

COPY ./app ./app

EXPOSE 8000

CMD ["uvicorn", "app.asgi:app", "--host", "0.0.0.0", "--port", "8000"]


FROM base AS dev

RUN poetry install --no-root --with dev

CMD ["pytest"]
