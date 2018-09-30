FROM python:3.6

RUN apt-get update
RUN apt-get install vim git -y

RUN pip install rasa_core

WORKDIR bot/

CMD sleep infinity
