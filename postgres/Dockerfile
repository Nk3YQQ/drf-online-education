FROM postgres:latest

COPY /postgres/init.sql /docker-entrypoint-initdb.d/

ENV POSGRES_DB=education_db
ENV POSTGRES_USER=test
ENV POSTGRES_PASSWORD=testpassword