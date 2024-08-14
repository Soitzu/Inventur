FROM python:3.11-slim

ENV PYTHONUNBUFFERED 1

WORKDIR /main
COPY requirements.txt .
RUN pip install  -r requirements.txt

COPY . .

USER root

RUN apt-get update && apt-get upgrade -y

RUN python3 manage.py makemigrations
RUN python3 manage.py migrate
COPY create_superuser.py .
RUN python3 create_superuser.py

RUN rm create_superuser.py

CMD ["gunicorn", "inventur.wsgi:application", "--bind", "0.0.0.0:8080", "--workers", "3"]
