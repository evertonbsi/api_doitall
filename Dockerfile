FROM python:slim

WORKDIR /app

RUN apt-get update

COPY requirements.txt /app
RUN pip3 install --upgrade pip -r requirements.txt

COPY . /app

ENV LANG pt_BR.UTF-8
ENV FLASK_DEBUG=1

CMD ["python", "app.py"]
