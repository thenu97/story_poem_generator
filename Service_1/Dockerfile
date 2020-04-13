FROM python:3.7-alpine

RUN apk add --update \
  && pip3 install --upgrade pip 

WORKDIR /Service_1/ 

COPY ./requirements.txt .

RUN set -e; \
        apk add --no-cache --virtual .build-deps \
                gcc \
                libc-dev 

RUN pip3 install -r requirements.txt \
  && rm -rf /var/cache/apk/* 

RUN apk add mariadb-dev \
  && pip3 install Flask-MySQLdb

COPY . .

CMD python3 app.py run -h 0.0.0.0