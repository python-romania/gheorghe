FROM ubuntu

MAINTAINER Madalin Popa, contact@madalinpopa.com

# Update 
RUN apt-get -y update && apt-get -y upgrade

# Install python and pip
RUN apt-get -y install python3 python3-pip

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

# Set languages preferences
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

# Expose port 80
EXPOSE 80

# Define our command to be run when launching the container
CMD ["python3", "main.py","--host", "0.0.0.0"]
