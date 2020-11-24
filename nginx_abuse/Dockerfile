FROM python:3.8
RUN mkdir /src
WORKDIR /src
COPY ./nginx_abuse/abuse/requirements.txt /scripts/
RUN pip3 install -r /scripts/requirements.txt