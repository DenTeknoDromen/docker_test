FROM python:3.12-slim

WORKDIR /sandbox

COPY "requirements.txt" ./

RUN pip install -r requirements.txt

COPY . .

ENV port=8000

EXPOSE 8000

CMD ["python", "./test.py"]