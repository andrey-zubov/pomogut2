FROM ubuntu:latest

RUN apt-get update && apt-get install -y locales \
    && localedef -i en_US -c -f UTF-8 -A /usr/share/locale/locale.alias en_US.UTF-8
ENV LANG en_US.utf8

RUN apt-get install -y \
    python3-pip \
    python3-psycopg2 \
    && rm -rf /var/lib/apt/lists/*

RUN mkdir /src3 && mkdir /static
WORKDIR /src3

COPY ./ButonBotDjango/requirements.txt /src3/
#RUN pip3 install --upgrade pip
RUN pip3 install --no-cache-dir -r /src3/requirements.txt
