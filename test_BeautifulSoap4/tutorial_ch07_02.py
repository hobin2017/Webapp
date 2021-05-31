# -*- coding: utf-8 -*-
"""
Chapter 7
  bs4.element.Tag.select() and bs4.BeautifulSoup.select() will search tag by using CSS selectors.
  For more information about css format, visits: https://www.w3schools.com/cssref/css_selectors.asp
"""

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


print('----------------------1, finding tags-----------------------------------------------------')
a = soup.select('p:nth-of-type(3)')  # the third <p> tag
print(a)

print('----------------------2, finding tags beneath other tags-----------------------------------------------------')
b = soup.select('body a')
print(b)

print('----------------------3, finding tags directly beneath other tags-----------------------------------------------------')
c = soup.select('p > a')
print(c)

print('----------------------4, finding the sibling of tags-----------------------------------------------------')
d = soup.select('#link1 ~ a')
print(d)

d02 = soup.select('#link1 + a')
print(d02)

print('----------------------5, finding tags by CSS selector-----------------------------------------------------')
e = soup.select('.sister')
print(e)

e02 = soup.select('[class~=sister]')
print(e02)

print('----------------------6, finding tags by ID-----------------------------------------------------')
f = soup.select('a#link1')  # the id attribute of <a> tag is link1
print(f)

f02 = soup.select('a[id=link1]')
print(f02)

print('----------------------7, finding tags by attribute value-----------------------------------------------------')
g = soup.select('''[href*=http://example.com]''')  # the href attribute contains your string
print(g)

