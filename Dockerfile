# Use ubuntu as base image
FROM ubuntu:latest

# Metadata
LABEL version="1.0"
LABEL maintainers="Jason Gayle, Peter Harrison"


# Update packages
RUN apt-get update && apt-get upgrade -y

# Install 
RUN apt-get update \
  && apt-get install -y python3-pip python3-dev \
  && cd /usr/local/bin \
  && ln -s /usr/bin/python3 python \
  && pip3 install --upgrade pip

# Set Debian frontend
ARG DEBIAN_FRONTEND=noninteractive


# Set working directorya
WORKDIR "/pattoo-web"

# Install systemd
RUN apt-get install -y systemd


# Copy Pattoo contents

# Copy Pattoo web contents
COPY . /pattoo-web

# Expose ports
EXPOSE 20201
EXPOSE 20200
EXPOSE 20202

# Install configuration
RUN setup/install.py install configuration


# Start systemd
CMD ["/usr/bin/systemd"]
