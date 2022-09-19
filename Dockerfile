# syntax=docker/dockerfile:1
FROM python:3.9 
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
RUN apk add --update --no-cache python3 && ln -sf python3 /usr/bin/python
RUN apk add libffi-dev
RUN python3 -m ensurepip
RUN pip3 install --no-cache --upgrade pip setuptools
RUN pip3 install --upgrade pip
# RUN apk add g++ gcc unixodbc-dev
RUN apk add curl
RUN apk add python3-dev
# RUN curl -O https://download.microsoft.com/download/b/9/f/b9f3cce4-3925-46d4-9f46-da08869c6486/msodbcsql18_18.0.1.1-1_amd64.apk
# RUN curl -O https://download.microsoft.com/download/b/9/f/b9f3cce4-3925-46d4-9f46-da08869c6486/mssql-tools18_18.0.1.1-1_amd64.apk
# RUN apk add --allow-untrusted msodbcsql18_18.0.1.1-1_amd64.apk
# RUN apk add --allow-untrusted mssql-tools18_18.0.1.1-1_amd64.apk
WORKDIR /
COPY requirements.txt /requirements.txt
RUN apk update \
    && apk --no-cache --update add build-base
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
# RUN apk update && apk add  build-essential && apk add  unixodbc-dev && pip install --upgrade pip && pip install -r requirements.txt
COPY . /
CMD python3 manage.py makemigrations && python3 manage.py migrate && python3 manage.py runserver 0.0.0.0:80



# #(Optional) Verify signature, if 'gpg' is missing install it using 'apk add gnupg':
# curl -O https://download.microsoft.com/download/b/9/f/b9f3cce4-3925-46d4-9f46-da08869c6486/msodbcsql18_18.0.1.1-1_amd64.sig
# curl -O https://download.microsoft.com/download/b/9/f/b9f3cce4-3925-46d4-9f46-da08869c6486/mssql-tools18_18.0.1.1-1_amd64.sig

# curl https://packages.microsoft.com/keys/microsoft.asc  | gpg --import -
# gpg --verify msodbcsql18_18.0.1.1-1_amd64.sig msodbcsql18_18.0.1.1-1_amd64.apk
# gpg --verify mssql-tools18_18.0.1.1-1_amd64.sig mssql-tools18_18.0.1.1-1_amd64.apk


# #Install the package(s)
# sudo apk add --allow-untrusted msodbcsql18_18.0.1.1-1_amd64.apk
# sudo apk add --allow-untrusted mssql-tools18_18.0.1.1-1_amd64.apk
