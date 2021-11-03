FROM ubuntu:20.04
ENV DEBIAN_FRONTEND noninteractive
RUN apt update
RUN apt upgrade -y

#MongoDB install --------
RUN apt install gnupg -y
RUN apt install wget -y
RUN wget --no-check-certificate -qO - https://www.mongodb.org/static/pgp/server-4.4.asc | apt-key add -
RUN echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu focal/mongodb-org/4.4 multiverse" | tee /etc/apt/sources.list.d/mongodb-org-4.4.list
RUN apt update
RUN apt install -y mongodb-org
#-------------------------
EXPOSE 27017
RUN mkdir -p /root/data/db
CMD mongod --dbpath /root/data/db --bind_ip 0.0.0.0