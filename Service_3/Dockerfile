FROM python:3.7-alpine

RUN apk add --update \
  && pip3 install --upgrade pip

WORKDIR /SFIA2/Service_3/

COPY ./requirements.txt .

RUN pip3 install -r requirements.txt \
  && rm -rf /var/cache/apk/*

COPY . .

CMD python3 app.py run -h 0.0.0.0

