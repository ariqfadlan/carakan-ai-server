FROM python:3.7-slim-buster

RUN apt-get update && apt-get -y install libglib2.0; apt-get clean
COPY requirements.txt /
RUN pip install -r /requirements.txt

RUN mkdir /code
WORKDIR /code
ADD . /code/

EXPOSE 8080
CMD ["python", "/code/app.py"]
