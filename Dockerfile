FROM python:3.6.6-alpine3.8 as base_builder
RUN apk add build-base python-dev py-pip
ENV LIBRARY_PATH=/lib:/usr/lib
ENV ENV_PATH=/root
ENV ENVIRONMENT=prod
ENV PYTHONPATH=/root/adservice
ENV FLASK_ENV=production
WORKDIR /root/adservice/
COPY requirements.txt /root/adservice
RUN pip install -r requirements.txt

# service docker image
FROM base_builder as service_image
ENV ENV_PATH=/root
ENV ENVIRONMENT=prod
ENV PYTHONPATH=/root/adservice
ENV FLASK_ENV=production
COPY . /root/adservice
EXPOSE 7000
WORKDIR /root/adservice/adservice/conf
ENTRYPOINT [ "./entrypoint.sh" ]