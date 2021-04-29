# pull official base image
FROM python:3.9

# set work directory
WORKDIR /code

# install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# copy project
ADD . .
EXPOSE 5055