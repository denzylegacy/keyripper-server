FROM python:3.10-slim

RUN apt-get update && \
    apt-get install -y \
        libgmp-dev \
        gcc \
        build-essential \
        && apt-get clean && \
        rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD ["gunicorn", "-w", "3", "-k", "uvicorn.workers.UvicornWorker", "app:app"]
