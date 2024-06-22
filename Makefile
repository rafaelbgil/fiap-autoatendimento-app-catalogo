DJANGO_KEY ?= dsadsadada
export DJANGO_KEY
test:
	coverage run --source=./  ./manage.py test 
	coverage html

test-xml:
	coverage run --source=./  ./manage.py test
	coverage xml

run:
	python manage.py runserver 0.0.0.0:8090

run-prod:
	uwsgi --ini uwsgi.ini

update-db:
	python manage.py makemigrations
	python manage.py migrate
	python manage.py makemigrations api
	python manage.py migrate



