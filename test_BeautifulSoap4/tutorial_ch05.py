# -*- coding: utf-8 -*-
"""
Chapter 5
You can access a tag's attributes by treating the tag like a dictionary;
If you change a tag's attribute, the change will be reflected in any HTML markup;
The value of tag['class'] is a list since the class attribute can have multi-value(like <p class='class1 class2'></p> ).
You can use 'get_attribute_list' function to get a value that is always a list.
"""

import bs4

soup = bs4.BeautifulSoup('''
           <b class="class1">Extremely bold</b>
           <b class="class2">bold</b>
           ''',features='html.parser')
# print(type(soup))  # <class 'bs4.BeautifulSoup'>
print('--------------------------------------------------------------------')
# using the attributes of<class 'bs4.element.Tag'>
tag = soup.b  # <class 'bs4.element.Tag'> and it only represents the first <b> tag in the html.
print(tag.name)  # b
print(tag.attrs)  # {'class': ['class1']}
print(tag['class'])  # ['class1'] The value is a list since the 'class' attribute can have multi-value.
# print(tag['id'])  # It will raise KeyError since the dict does not has the key 'id'.
print(tag.string)  # Extremely bold; However it is a class.
print(type(tag.string))  # <class 'bs4.element.NavigableString'>

print('--------------------------------------------------------------------')
tag['id'] = 'new_id'  # adding new element by using <class 'bs4.element.Tag'>
print(tag.get_attribute_list('id'))  # ['new_id']
print(tag['id'])  # new_id
tag.string.replace_with('new text')  # replacing the whole text of the tag with a new one
print(tag)  # <b class="class1" id="new_id">new text</b>

