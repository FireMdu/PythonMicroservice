# syntax=docker/dockerfile:1

FROM python:3.8.0

WORKDIR /python_microservice

COPY requirements.txt requirements.txt

# this is required by the pyodbc python package
RUN apt-get update && apt-get install -y gcc unixodbc-dev

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

CMD [ "python", "./main.py", "--host=0.0.0.0:8000"]
