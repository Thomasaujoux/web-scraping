# As Scrapy runs on Python, I choose the official Python 3 Docker image.
FROM python:3.9.13
 
RUN apt update && \
    apt upgrade -y && \
    apt install -y python3-pip && \
    apt install -y build-essential libssl-dev libffi-dev python3-dev && \
    pip install Scrapy && \
    pip install python-dotenv


RUN mkdir -p /crawler
COPY ./url /crawler/src/
RUN chmod a+xwr /crawler/src/*.sh
 

# Répertoire où les logs seront positionnés
RUN mkdir -p /crawler/log
RUN chmod a+xwr /crawler/log
VOLUME /crawler/log

WORKDIR /crawler/src


ENTRYPOINT ["tail", "-f", "/dev/null"]
