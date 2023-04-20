# Use a Python 3.9 base image
FROM python:3.9-slim-buster

RUN mkdir /app
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
CMD ["python","-u", "main.py"]