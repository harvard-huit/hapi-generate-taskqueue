#  ARG DOCKER_PYTHON_VERSION=3.9-buster
# FROM python:$DOCKER_PYTHON_VERSION
FROM python:alpine3.17

#ENV LANG=C.UTF-8 LC_ALL=C.UTF-8 PYTHONUNBUFFERED=1 
RUN apk update && apk add git 

# Celery requirements 
COPY deploy/celeryconfig.py /app/
COPY deploy/requirements.txt /app/
COPY deploy/startCeleryWorker /app/
RUN mkdir /app/temp
COPY . /app/temp  
WORKDIR /app

#Setup Celery User
RUN addgroup celery && adduser -DH --home /app -G celery celery \
  && chown celery:celery -R /app

USER celery
WORKDIR /app

RUN python3 -m venv /app/venv
RUN source /app/venv/bin/activate
RUN /app/venv/bin/python -m pip install --upgrade pip
RUN /app/venv/bin/pip install --no-cache-dir -r requirements.txt 
RUN /app/venv/bin/pip install temp/.
RUN rm -rf /app/temp && rm -rf /app/requirements.txt


CMD ["/app/startCeleryWorker"]
