FROM python:3.10.2
ENV PYTHONBUFFERED 1
WORKDIR /project
COPY requirements.txt requirements.txt /project/
RUN pip install -r requirements.txt
COPY . /project/