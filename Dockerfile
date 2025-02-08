FROM python:3.10-slim

COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir  -r /app/requirements.txt

COPY . /app
WORKDIR /app

CMD ["gunicorn"  , "-b", "0.0.0.0:8000", "main:app"]