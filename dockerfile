FROM python:3.8

RUN mkdir /app

WORKDIR /app

COPY . /app

RUN  pip install -r /app/requirements.txt

EXPOSE 5000
EXPOSE 4444
#CMD ["curl","http://172.23.0.2:4444"]
CMD ["python","server.py"] 