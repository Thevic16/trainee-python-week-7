FROM python:3.10-alpine

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DEBUG 0

RUN pip install --upgrade pip
COPY Pipfile .
COPY Pipfile.lock .
RUN pip install pipenv
RUN pipenv lock --requirements > requirements.txt
RUN apk add zlib-dev jpeg-dev gcc musl-dev
RUN pip install -r requirements.txt
COPY . .
RUN pip install -e .

# CMD ["chmod", "+x", "exec docker-entrypoint.sh > docker.log 2>&1"]
CMD "python manage.py collectstatic --noinput"
CMD "python manage.py makemigrations > docker.log 2>&1"
CMD "python manage.py migrate > docker.log 2>&1"
CMD gunicorn film_rental_system.wsgi:application --bind 0.0.0.0:$PORT