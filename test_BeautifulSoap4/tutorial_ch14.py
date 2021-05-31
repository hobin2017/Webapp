# -*- coding: utf-8 -*-
"""
  Beautiful Soup actually parse the entire document and then go over it again looking for the things you want.
  To save time, there is the SoupStrainer class to parse the only interesting part.
"""

from bs4 import SoupStrainer, BeautifulSoup

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

attrs = {'class':'sister'}
soupstrainer01 = SoupStrainer(name='a', attrs=attrs)

soup = BeautifulSoup(markup=html_doc, features='html.parser', parse_only=soupstrainer01)
print(soup)

