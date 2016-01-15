1. python manage.py startapp crud
2. open django_proj_name/settings.py and add below
```python
INSTALLED_APPS = (
  :
  'crud',
  :
)
```
3. crud/models.py
4. python manage.py makemigrations
5. python manage.py migrate --list
6. python manage.py migrate 
7. http://sqlitebrowser.org/ Download the browser for browse SQLight DB




Query
-------
1. from crud.models import Crud
2. Crud.objects.all()
3. crud = Crud.objects.all(); crud[0].name
4. Crud.objects.get(id=3)
