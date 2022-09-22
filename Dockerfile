# syntax=docker/dockerfile:1
FROM python:3.9
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /
COPY requirements.txt /requirements.txt
# RUN apk update \
    # && apk --no-cache --update add build-base
RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip3 install -r requirements.txt
EXPOSE 3000
# ENTRYPOINT ["python", "PocketAssist/manage.py"]
# RUN apk update && apk add  build-essential && apk add  unixodbc-dev && pip install --upgrade pip && pip install -r requirements.txt
COPY . /
CMD python3 manage.py makemigrations && python3 manage.py migrate && python3 manage.py runserver 0.0.0.0:3000
