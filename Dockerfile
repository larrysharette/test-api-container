FROM alpine:latest

RUN apk add --update \
    python3 \
    py-pip \
    build-base \
  && pip install --upgrade pip \
  && pip3 install virtualenv \
  && rm -rf /var/cache/apk/*
RUN apk add --update \
    nodejs

COPY . /python_run/

EXPOSE 5000

RUN pip3 install Flask\
    gunicorn

WORKDIR /python_run/

ENV FLASK_APP=app.py
ENV FLASK_DEBUG=1

CMD [ "flask", "run", "--host=0.0.0.0" ]