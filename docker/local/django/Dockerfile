FROM python:3.10.0-slim-buster

ENV APP_HOME=/app
RUN mkdir $APP_HOME
RUN mkdir $APP_HOME/staticfiles
WORKDIR $APP_HOME

LABEL maintainer='pnakitaren2@gmail.com'
LABEL description='Development image for Real Estate Project'

ENV PYTHONDONTWRITEBYTECODE 1

ENV PYTHONUNBUFFERED 1

RUN apt-get update \
    && apt-get install -y build-essential \
    && apt-get install -y libpq-dev \
    && apt-get install gettext \
    && apt-get -y install netcat gcc postgresql \
    && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendSIMPORTANT=false \
    && rm -rf /var/lib/apt/lists/*

RUN pip3 install --upgrade pip3
COPY ./requirements.txt /app/requirements.txt

RUN pip3 install -t requirements.txt

COPY ./docker/local/django/entrypoint /entrypoint
# process the line-endings of the showscripts, converting any windows line endings to unix/linux line endings
RUN sed -i 's/\$//g' /entrypoint 
RUN chmod +x /entrypoint

COPY ./docker/local/django/start /start
RUN sed -i 's/\r$//g' start
RUN chmod +x /start

ENTRYPOINT [ "/entrypoint" ]
# COPY ./docker/local/django/celery/worker/start /start-celeryworker
# RUN sed -i 's/\$//g' /start-celeryworker
# RUN chmod +x /start-celeryworker




