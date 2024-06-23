#!/bin/sh
#Script para carregar dados
python manage.py makemigrations api
python manage.py migrate
