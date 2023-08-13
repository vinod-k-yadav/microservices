# Dockerfile
FROM alpine:latest
# Install Python 3 and pip
RUN apk add --update python3 py3-pip

COPY  . /frontend_app/
WORKDIR /frontend_app
RUN pip install -r requirements.txt
EXPOSE 6000

ENTRYPOINT ["python3", "application/app.py"]
