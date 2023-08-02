# As Scrapy runs on Python, I choose the official Python 3 Docker image.
FROM python:3.11.3-slim


WORKDIR /crawler


COPY requirements.txt .

RUN pip3 install -r requirements.txt


COPY ./url /crawler/src/


RUN chmod a+xwr /crawler/src/*.sh

 
# Répertoire où les logs seront positionnés
RUN mkdir -p /crawler/log
RUN chmod a+xwr /crawler/log
VOLUME /crawler/log


WORKDIR /crawler/src


ENTRYPOINT ["tail", "-f", "/dev/null"]
