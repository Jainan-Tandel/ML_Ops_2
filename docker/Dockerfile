# FROM ubuntu:23.10
FROM python:3.9.17
COPY . /digits/
# RUN apt-get update && apt-get install -y python3 python3-pip
RUN pip3 install --no-cache-dir -r digits/requirements.txt
WORKDIR /digits
VOLUME ["/models"]
CMD sh docker/cmd_run.sh
