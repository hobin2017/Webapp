# -*- coding: utf-8 -*-
"""
Chapter 2
Be careful that the new line character '\n' will affect your idea about the structure of the whole HTML page.
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

soup = BeautifulSoup(markup=html_doc, features='html.parser')
# print(type(soup))  # <class 'bs4.BeautifulSoup'>
# print(soup.prettify())  # beautify the HTML string
print(soup.title)  # <title>The Dormouse's story</title>; the first one in the html;
# The usage 'soup.title' is equivalent to the usage soup.find('title') (chapter 7)
print(soup.title.name)  # title
print(soup.title.string)  # The Dormouse's story
print(soup.title.parent.name)  # head
print(soup.p)  # <p class="title"><b>The Dormouse's story</b></p>; the first one in the html;
print(soup.p['class'])  # ['title']
print(soup.a)  # <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>; the first one in the html;
print(soup.find_all(name='a'))  # a list of <class 'bs4.element.Tag'> object
# The shortcut for soup.find_all(name='a') is soup(name='a'). Chapter 7
print(soup.find(id='link3'))  # <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>
print('------------------------------------------------------------')
for link in soup.find_all('a'):
    # print(type(link))  # <class 'bs4.element.Tag'>
    print(link.get('href'))
print('------------------------------------------------------------')
print(soup.get_text())  # chapter 9

