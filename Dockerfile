FROM python:3.7

RUN apt update
RUN apt-get install cron -y

WORKDIR /exchange_rate

RUN pip3 freeze > requirements.txt

COPY . .

RUN pip3 install -r requirements.txt --no-cache-dir
