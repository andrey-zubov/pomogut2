FROM postgres:latest

ARG psql_pass
ARG psql_db
ARG psql_user
ARG psql_port

ENV POSTGRES_USER=$psql_user
ENV POSTGRES_PASSWORD=$psql_pass
ENV POSTGRES_DB=$psql_db
ENV POSTGRES_PORT=$psql_port

COPY init.sql /docker-entrypoint-initdb.d/
