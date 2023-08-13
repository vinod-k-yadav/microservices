# Dockerfile
FROM alpine:latest
# Install Python 3 and pip
RUN apk add --update python3 py3-pip

COPY  . /backendService/userService
WORKDIR /backendService/userService

RUN pip install -r requirements.txt

EXPOSE 6300

ENTRYPOINT ["python3", "application/app.py"]