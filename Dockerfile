FROM python:3.10-slim

WORKDIR /app
COPY requirements.txt .
ENV PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_NO_CACHE_DIR=off
ENV DJANGO_SUPERUSER_PASSWORD $SUPERUSER_USERNAME
ENV DJANGO_SUPERUSER_USERNAME $SUPERUSER_PASSWORD
RUN pip install -r requirements.txt
COPY . .
CMD python manage.py create superuser --noinput
CMD python manage.py runserver 0.0.0.0:8000
