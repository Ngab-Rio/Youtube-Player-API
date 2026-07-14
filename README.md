# Karaoke Player API

Backend API for searching and streaming YouTube karaoke content using FastAPI.

## Features

* FastAPI-based REST API
* Docker support
* Lightweight Python image (`python:3.14-slim`)
* Easy deployment
* Uvicorn ASGI server

---

## Requirements

* Python 3.14 (optional)
* Docker 28+
* Git

---

## Clone Repository

```bash
git clone https://github.com/Ngab-Rio/Youtube-Player-API.git
cd Youtube-Player-API
```

---

## Running with Docker

### Build Image

```bash
docker build -t karaoke-player .
```

### Run Container

```bash
docker run -d \
  --name karaoke-player \
  -p 8000:8000 \
  --restart unless-stopped \
  karaoke-player
```

The API will be available at:

```
http://localhost:8000
```

---

## Using start.sh

Make the script executable:

```bash
chmod +x start.sh
```

Run:

```bash
./start.sh
```

---

## Running Without Docker

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it:

### Linux / macOS

```bash
source .venv/bin/activate
```

### Windows

```powershell
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the API:

```bash
uvicorn app.main:app --reload
```

---

## API Documentation

Swagger UI

```
http://localhost:8000/docs
```

ReDoc

```
http://localhost:8000/redoc
```

---

## Project Structure

```text
.
├── app/
│   ├── main.py
│   ├── providers/
│   ├── routes/
│   └── ...
├── requirements.txt
├── Dockerfile
├── start.sh
└── README.md
```

---

## Dockerfile

The project uses a minimal Python image:

```dockerfile
FROM python:3.14-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

---

## License

This project is released under the MIT License.

