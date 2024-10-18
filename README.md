# keyripper-server
 A server that manages and distributes blocks of private key ranges. It works with a Rust-based client that performs the key search operations on the secp256k1 elliptic curve.

## Prerequisites

Before starting, make sure Docker is installed on your machine. If Docker is not installed, follow the instructions [here](https://docs.docker.com/get-docker/).

## Installation

1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/denzylegacy/keyripper-server.git
   cd keyripper-server
   ```

2. Build the Docker image:
   ```bash
   sudo docker build -t dc-keyripper-server .
   ```

## Running the Project

After building the image, run the project using the following command:

```bash
sudo docker run -it dc-keyripper-server
```

## Dockerfile

The `Dockerfile` used in this project is as follows:

```Dockerfile
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
```

This Dockerfile defines an environment based on the `python:3.10-slim` image, installs the dependencies listed in `requirements.txt`, and copies the project contents into the container. By running the `sudo docker run -it dc-keyripper-server` command, the container will start, and the Gunicorn server will start running the ASGI application on port 8000, allowing it to receive requests.

## Contributions

Feel free to open issues or pull requests. Feedback is always welcome!
