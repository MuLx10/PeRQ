FROM python:3.5.2

WORKDIR /usr/src/app

# Install postgres
RUN apt-get update && apt-get install -y --no-install-recommends \
    libpq-dev && \
    rm -rf /var/lib/apt/lists/*
RUN apt-get -y install unzip && apt-get install redis-server

# install requirements
# this way when you build you won't need to install again
# and since COPY is cached we don't need to wait
COPY app/conf/requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt

# Copy the Configuration and the Scripts
COPY app/conf /conf
COPY app/scripts /usr/src/scripts
RUN chmod a+x /usr/src/scripts/runserver.sh

# Copy the source
COPY app/src /usr/src/app

WORKDIR /usr/src/app/bot

ENV CHATBOT_SECRET_KEY="dgfhfsdcdh=27)f6_fdsffsdf434332^%%$3=v^$bh9p0ihd-%v"
ENV CHATBOT_REDIS_URL="redis"
ENV POSTGRES_USERNAME="admin"
ENV POSTGRES_PASSWORD="xxxxxxx" # get this password by executin
ENV POSTGRES_HOSTNAME="localhost"
ENV POSTGRES_PORT="6432"

# App port number is configured through the gunicorn config file
ENTRYPOINT ["/usr/src/scripts/runserver.sh"]
