FROM ubuntu:20.04
ENV DEBIAN_FRONTEND noninteractive
RUN apt update
RUN apt upgrade -y

EXPOSE 80
RUN apt install screen -y
RUN apt install python3 python3-pip vim curl -y
RUN pip3 install pymongo fastapi uvicorn pyyaml
RUN mkdir /root/project
COPY ./main.py /root/project
COPY ./api_manual.yaml /root/project
WORKDIR /root/project
CMD uvicorn main:app --reload --port 80 --host 0.0.0.0