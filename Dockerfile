FROM ubuntu:20.04

COPY . /code/
WORKDIR /code
EXPOSE 8000
RUN apt update

RUN apt-get install python -y
RUN apt install pip -y
RUN apt-get install redis-server -y

RUN pip install -r requirements.txt
CMD ['celery', '-A', 'myshop', 'worker', '-l', 'info']