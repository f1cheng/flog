echo "Blog server migrate and run"
python manage.py migrate
python manage.py runserver 0.0.0.0:9000
