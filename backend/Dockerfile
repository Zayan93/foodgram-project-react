FROM python:3.8.5

WORKDIR /code
COPY . .
RUN pip install --upgrade pip && pip install -r /code/requirements.txt

CMD gunicorn api.wsgi:application --bind 0.0.0.0:8000