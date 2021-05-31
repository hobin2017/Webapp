# -*- coding: utf-8 -*-
"""
Chapter 7
  Be careful that the new line character '\n' will affect your idea about the structure of the whole HTML page.

  Any argument that is not stated in the find_all() function, will be consider as a filter on tag's attributes. For
instance, you pass a value for the 'id' argument and BeautifulSoup will filter against each tag's id attribute.
  If you call bs4.element.Tag.find_all(), Beautiful Soup will examine all the descendants of the tag: its children, its
children’s children, and so on.
  find() & find_all(limit=1): find_all(limit=1) function returns a list containing the single result, and find()
function just returns the result.

  find_parents() function is the opposite function of find_all() function. This search method actually use .parents to
iterate over all the parents and might check each one against the provided filter.
  find_parent() & find_parents(limit=1): find_parents(limit=1) function returns a list containing the single result,
and find_parent() function just returns the result.

  Other type of functions are: find_next_siblings & find_next_sibling, find_previous_siblings & find_previous_sibling,
find_all_next & find_next, find_all_previous & find_previous
"""
import re

from bs4 import BeautifulSoup

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
</body></html>
"""
soup = BeautifulSoup(html_doc, 'html.parser')
# print(type(soup))  # <class 'bs4.BeautifulSoup'>

print('------------------------1, tag related-------------------------------------------')
# 1, when you pass in a value for 'name' argument, BeautifulSoup will consider tags with certain names.
# The shortcut for soup.find_all(name='title') is soup(name='title')
a01 = soup.find_all(name='title')  # finds the title tag
print(a01)

print('------------a02 related----------------')
def filter_function_a02(target_element):
    """
    The target_element represents bs4.element.Tag, bs4.element.NavigableString or the attribute value.
    If you pass this function into the 'name' argument of find_all() function, target_element will be bs4.element.Tag.
    If you pass this function into the 'string' argument of find_all() function, target_element will be  bs4.element.NavigableString.
    Otherwise, target_element should be a value such as attribute value.
    :param target_element:
    :return: return True if the argument matches and False otherwise.
    """
    # print(type(target_element))  # bs4.element.Tag
    return target_element.has_attr('id')
# pass a function name into bs4.BeautifulSoup.find_all() function
a02 = soup.find_all(name=filter_function_a02)  # finds a tag which defines class attribute and does not defines id attribute
print('The total length of result is %s' %len(a02))
print(a02)

print('------------a03 related----------------')
a03 = soup.html.body.find_all(recursive=False)  # The search range is restricted to direct children
print('The total length of result is %s' %len(a03))
print(a03)

print('------------------------2, tag attribute related-------------------------------------------')
# 2, Any argument that is not stated in the find_all() function, will be consider as a filter on tag's attributes.

#   If html page has a tag with 'data-foo' attribute, you cannot filter by passing  a value to 'data-foo' argument since
# the argument of function cannot contain this '-' symbol.
filter_dict = {'class':'sister'}  # return all tags whose class attribute is 'sister'.
b00 = soup.find_all(attrs=filter_dict)
print(b00)

b01 = soup.find_all(id='link2')  # return all tags whose id attribute contains 'link2'.
print(b01)

print('------------b02 related----------------')
b02 = soup.find_all(href=re.compile('elsie'))  # return all tags whose href attribute contains 'elsie'.
print(b02)

b02_1 = soup.find_all(href='http://example.com/tillie')
print(b02_1)

b02_2 = soup.find_all(href=True)  # return all tags whose href attribute has a value, regardless of what the value is.
print(b02_2)

print('------------b03 related----------------')
def filter_function_b03(target_element):
    """
    The target_element represents bs4.element.Tag, bs4.element.NavigableString or the attribute value.
    If you pass this function into the 'name' argument of find_all() function, target_element will be bs4.element.Tag.
    If you pass this function into the 'string' argument of find_all() function, target_element will be  bs4.element.NavigableString.
    Otherwise, target_element should be a value such as attribute value.
    :param target_element:
    :return: return True if the argument matches and False otherwise.
    """
    # print(type(target_element))  # NoneType, str, etc
    # Be careful that object of type 'NoneType' has no len() function.
    return target_element is not None and len(target_element) == 6
# class_ attribute represents the class attribute. The reason wht it is changed is 'class' is reserved in Python.
b03 = soup.find_all(class_=filter_function_b03)
print(b03)

print('------------------------3, string argument of find_all() -------------------------------------------')
def filter_function_c01(target_element):
    """
    The target_element represents bs4.element.Tag, bs4.element.NavigableString or the attribute value.
    If you pass this function into the 'name' argument of find_all() function, target_element will be bs4.element.Tag.
    If you pass this function into the 'string' argument of find_all() function, target_element will be  bs4.element.NavigableString.
    Otherwise, target_element should be a value such as attribute value.
    :param target_element:
    :return: return True if the argument matches and False otherwise.
    """
    # print(type(target_element))  # bs4.element.NavigableString
    return True
# The html can be regraded as a object consisting of only bs4.element.NavigableString object.
# In other words, the bs4.element.Tag object is represented by its content (bs4.element.NavigableString).
# The number of total result is restricted if limit=5.
# The string argument is new in BeautifulSoup4.4.0. In earlier version is was called text.
c01 = soup.find_all(string=filter_function_c01, limit=5)  # finds all string which satisifies your requirement
print(c01)  # a list of bs4.element.NavigableString object
# for item in c01:
#     print(type(item))

c02 = soup.find_all(name='a', string=re.compile('E'))
print(c02)  # a list of bs4.element.Tag object
# for item in c02:
#     print(type(item))

print('------------------------4, find_all() & find()-------------------------------------------')
d01 = soup.find_all(name='p', limit=1)
print(d01)
print('------------d02 related----------------')
d02 = soup.find(name='p')
print(d02)

