
python manage.py makemigrations

echo "Making migrations."
python manage.py migrate

echo "Loading demo data from fixtures.json"
python manage.py loaddata -i ingredients.json

echo "Collecting static files."
python manage.py collectstatic --noinput

# echo "Compressing static files."
# python manage.py compress

# Запускаем gunicorn на нашем $PORT
# echo "Starting gunicorn"
# gunicorn api.wsgi:application --bind 0.0.0.0:8000 \

exec "$@"