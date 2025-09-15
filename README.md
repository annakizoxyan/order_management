# Order Management Microservice

## Getting started

### First we need to create a `.env` file
```bash
cp .env_example .env
```

### Then build and start the container
```bash
docker compose up -d --build
```
## How to run tests

### You can run tests by pytest
```bash
docker compose run --rm test
```
### Or using pytest (if dev environment is already set up)
```bash
pytest
```