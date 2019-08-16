FROM ubuntu:18.04
FROM python:3.7
RUN  apt-get update && apt-get upgrade -y && apt-get install python3-pip -y
RUN pip install --upgrade pip
WORKDIR /app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 80
ENTRYPOINT [ "scrapy" ]
CMD []
