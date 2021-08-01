# tutorial
- [part 1, start server](https://docs.djangoproject.com/en/2.2/intro/tutorial01/)
> The `urls.py` file maps the views to urls. The `views.py` is to return html-string.
```shell script
django-admin startproject ${proj_name}
python manage.py runserver 0:8080
python manage.py startapp ${app_name}
```

- [part 2, orm and database](https://docs.djangoproject.com/en/2.2/intro/tutorial02/)
```python
from django.db import models

class Table01(models.Model):
    # The primary key is the id column that is created by default
    column01 = models.CharField(max_length=200)
    column02 = models.CharField(max_length=200)


# select
_val = Table01.objects.filter(column01='1')
print(_val)
# insert
new_row = Table01(column01='1', column02='2')
new_row.save()
# update
new_row.column01 = '11'
new_row.save()
# delete
new_row.delete()
```
```shell script
python manage.py migrate
python manage.py makemigration polls
python manage.py check
# 
python manage.py creatsuperuser
```

- [part 3, views and urls](https://docs.djangoproject.com/en/2.2/intro/tutorial03/)
`django.urls.path()` function: 
- route parameter. It accepts a string. The string may contain angle brackets as part of the url and these brackets will be sent as keyword argument to the view. The angle brackets may include a specification, like <int: var01>. 
- view parameter. This parameter can accept these thing: a function, `django.urls.include()` function, and `django.views.View.as_view()` function.
- kwargs parameter. It is the additional arguments for the view. 
- name parameter. It is url namespace. For instance, django template `{% url %}` will use it to get url. 

Each view want HttpResponse class or an exception. 
`django.shortcuts.render()` function convert the django template tag written in a html file to a pure html. 

- [part 4, using generic view](https://docs.djangoproject.com/en/2.2/intro/tutorial04/)
> The generic views represent a common case of basic Web development: getting data from the database according to a parameter passed in the URL, loading a template and returning the rendered template.

- [part 5, test](https://docs.djangoproject.com/en/2.2/intro/tutorial05/)

- [part 6, static file & Django](https://docs.djangoproject.com/en/2.2/intro/tutorial06/)
You can put static files directly under `$app_name/static` directory, but it would actually be a bad idea. It is recommended to put static files under `$app_name/static/$app_name` directory. 
`{% load static %}` will enable the usage such as `<link rel='stylesheet' type='text/css' href='{% static "app_name/css_name.css" %}' >`.

