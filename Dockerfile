FROM python:3.9

WORKDIR /app

COPY requirements.txt requirements.txt

COPY app.py app.py

ENTRYPOINT ["python", "app"]