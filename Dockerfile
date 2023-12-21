FROM alpine:3.14

RUN mkdir /var/wordspeak

COPY ./web/ ./var/wordspeak

WORKDIR /var/wordspeak

RUN apk update

RUN apk add python3 py3-pip --no-cache

RUN pip install -r requirements.txt

COPY . .

ENV port=8000

EXPOSE 8000

CMD ["python3", "test.py"]