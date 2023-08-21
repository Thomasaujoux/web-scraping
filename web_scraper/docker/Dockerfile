FROM mongo:latest

RUN apt update && \
    apt upgrade -y && \
    apt install -y python3-pip && \
    apt install -y build-essential libssl-dev libffi-dev python3-dev && \
    pip install Scrapy pymongo pandas js2py

RUN mkdir -p /global 
COPY ./global/global /global/global
COPY ./global/* /global/
RUN chmod +x /global/global/start.sh

WORKDIR /global/global

#ENTRYPOINT ["tail", "-f", "/dev/null"]
ENTRYPOINT ["mongod"]
