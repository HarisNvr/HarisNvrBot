FROM python:3.12-slim

WORKDIR /bot_backend

COPY requirements.txt .

RUN pip install -r requirements.txt --no-cache-dir

COPY . .

CMD python3 main.py
