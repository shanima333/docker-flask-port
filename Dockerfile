FROM alpine:3.8

RUN mkdir /app

WORKDIR /app

COPY . . 

RUN apk update && apk add python3

RUN pip3 install -r requirements.txt

EXPOSE 5000

CMD ["/usr/bin/python3", "app.py"]

