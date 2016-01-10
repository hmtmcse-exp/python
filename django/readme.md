1. Download python from https://www.python.org/downloads/
2. git clone git://github.com/django/django.git
3. Run CMD by administrator mode and then py -mpip install win-unicode-console
3. pip install django



create project
1. django-admin.py startproject mysite
2. python manage.py migrate
3. python manage.py createsuperuser
4. python manage.py runserver
5. http://127.0.0.1:8000/admin/.



httpd.conf
AddHandler cgi-script .cgi .pl .asp .py