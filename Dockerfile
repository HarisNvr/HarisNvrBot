FROM python:3.12

WORKDIR /harisnvrbot

COPY requirements.txt .

RUN pip install -r requirements.txt --no-cache-dir

COPY . .

CMD python3 main.py