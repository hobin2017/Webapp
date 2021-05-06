# procedure for new application
- `django-admin startproject proj01`
- `python manage.py startapp app01`
- views,py (./app01/views.py)
- urls.py (./app01/urls.py)
- urls.py (./proj01/urls.py)
- settings.py (INSTALLED_APPS, TEMPLATES, STATICFILES_DIRS)
> If creating user-defined names here, the names are required capitalized.
- write django template to generate dynamic html as `./app01/templates/app_name/xxx.html` file
```html
{% load static %}
<link rel='stylesheet' type='text/css' href='{% static ”app_name/css_name.css” %}' >
<script type='text/javascript' src='{% static … %}' ></script>
```


# The Django template language
### [variable](https://docs.djangoproject.com/en/2.2/ref/templates/language/#variables)
`{{ var_name }}`
1, When the template engine encounters a variable, it replaces the variable with the value of the variable.
2, The 'var_name' cannot not start with an underscore. You cannot have spaces or punctuation characters in 'var_name'.
3, You can use a dot (.) to get access to attributes of the variable.
4, If you use a variable that doesn't exist, the template system will insert the value of the string_if_invalid option, which is set to '' (the empty string) by default.

`{{ var_name | filter_name }}`
1, You can use a pipe (|) to modify the display of a variable.
2, filter can be chained, such as {{ var_name | filter01 | filter02 }}
3, {{ var_name | default: 'hobin' }}
4, {{ var_name | length }} The result is like calling the len() function. 
5, {{ var_name | filesizeformat }} If value is 123456789, the output would be 117.7 MB.

### Tags
1, Some tags require beginning and ending tags. {% for item in list01 %} … {% endfor %} is one example. Some tags do not require the ending tag, such as {% extend … %}.
2, for loop statement
`{% for item in list01 %} … {% endfor %}`
`{% for key,value in dict01.items %} … {% endfor %}`
3, if statement: You can use filters and other operation with the if tag. Be aware that most template filters return strings.
```
{% if … %}
…
{% elif … %}
…
{% else %}
…
{% endif %}
```
4, comment
`{% comment %} {% endcomment %}` for multiple line
`{# … #}` for single-line comments. 


### Template inheritance
1, `{% block block_name %} {% endblock %}` You can define an empty block and let the child template to fill the empty block with contents. Thus, All the block tag does is to tell the template engine that a child template may override those portions of the template.
2, `{% extend 'file_name.html' %}` The extend tag has the location of the parent template and tells the template engine that this template "extends" another template. 
3, If you use `{% extends %}` in a template, it must be the first template tag in that template. Otherwise template inheritance won't work.
4, If you need to get the content of the block from the parent template, the `{{ block.super }}` variable will do the trick. This is useful if you want to add to the contents of a parent block instead of completely overriding it.
5, For extra readability, `{% endblock block_name %}` is better than `{% endblock %}`.
6, You cannot define multiple block tags with the same name in the same template.


# Cross-site scripting attack (XSS)
1, variable might be untrusted. `Hello, {{ name }}` -> `Hello, <script>alert('hobin')</script>`.
2, using escape filter on the variable tag `{{ var_name | escape }}`. This will convert these character (<, >, single quote ', double quote ” and &) to other characters. For instance, < will be converted to '&lt'.
3, The variable tag is escaped by default. One reason why you want to turn this behavior off is that you want to insert html code into the template by the variable tag. To disable auto-escaping for an individual variable, use the safe filter `{{ var_name | safe }}`. To disable auto-escaping for several variables, use `{% autoescape off %} … {% endautoescape %}`.


# Function call
1, `{{ var01.func01}}` is the function call and this might be no difference between calling a function and accessing an attribute. 
2, it is not possible to pass arguments to method calls accessed from within templates.

