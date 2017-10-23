# Backend Assignment: Simple Todos and Reminder API

installation process is for ubuntu 16.04

virtualenv -p python myproject
source myproject/bin/activate
cd myproject

pip install -r requirements.txt
git clone https://github.com/igor35hh/scalors-assignment-backend

install rabbitmq: https://www.rabbitmq.com/install-debian.html

echo 'deb http://www.rabbitmq.com/debian/ testing main' |
     sudo tee /etc/apt/sources.list.d/rabbitmq.list

wget -O- https://www.rabbitmq.com/rabbitmq-release-signing-key.asc |
     sudo apt-key add -

wget -O- https://dl.bintray.com/rabbitmq/Keys/rabbitmq-release-signing-key.asc |
     sudo apt-key add -

sudo apt-get update
sudo apt-get install rabbitmq-server

check sudo systemctl status rabbitmq-server
if doesn't run
sudo systemctl start rabbitmq-server

cd todoSAB

for sending email is necessary establish setting in the file settings.py located in root package todoSAB
also uncomment a pice of code in the file tasks.py located in reminder package

python manage.py makemigrations todo
python manage.py makemigrations reminder
python manage.py migrate
python manage.py runserver

in separate window run
celery -A mysite worker --loglevel=info
for clear queue run
celery -A mysite purge

or together: python manage.py runserver & celery -A mysite worker --loglevel=info

open browser and go to localhost:8000
