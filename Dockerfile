FROM python:3.7-slim

LABEL maintainer="contact@madalinpopa.com"

# Update 
RUN apt-get -y update && apt-get -y upgrade

# Make a local directory
RUN mkdir /opt/app

# Set "app" as the working directory from which CMD, RUN, ADD references
WORKDIR /opt/app

# Copy requirements.txt to /app
ADD ./requirements.txt .

# Pip install the local requirements.txt
RUN pip3 install -r requirements.txt

# Now copy all the files in this directory to /code
ADD . .

# Define our command to be run when launching the container
CMD ["python3", "./main.py"]
