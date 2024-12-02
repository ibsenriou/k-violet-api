web: gunicorn --bind 0.0.0.0:$PORT --workers 1 --threads 8 --timeout 0 settings.wsgi:application
migrate: python manage.py migrate && python manage.py collectstatic --noinput --clear
makemigrations: python manage.py makemigrations
createuser: python manage.py createsuperuser --email admin@homespace.digital --first_name admin --last_name homespace --noinput