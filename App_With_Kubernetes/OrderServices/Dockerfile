# Dockerfile
FROM alpine:latest
# Install Python 3 and pip
RUN apk add --update python3 py3-pip

COPY  . /backendService/orderService
WORKDIR /backendService/orderService
RUN pip install -r requirements.txt

EXPOSE 6100

ENTRYPOINT ["python3", "application/app.py"]