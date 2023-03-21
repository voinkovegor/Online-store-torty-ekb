FROM python:3

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements2.txt ./

RUN pip install --upgrade pip && pip install -r requirements2.txt

COPY . .
