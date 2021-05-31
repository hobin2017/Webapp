# -*- coding: utf-8 -*-
"""
Chapter 9 & Chapter 11
  bs4 might fix your html text if it is broken. For instance, some tags in your html text is not closed because of your mistake.
"""

from bs4 import BeautifulSoup, UnicodeDammit

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
# html_doc2 is equivalent to html_doc
html_doc2 = """\n<html><head><title>The Dormouse's story</title></head>\n<body>\n<p class="title"><b>The Dormouse's story</b></p>\n<p class="story">Once upon a time there were three little sisters; and their names were\n<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,\n<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and\n<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;\nand they lived at the bottom of a well.</p>\n<p class="story">...</p>\n</body></html>\n"""
soup = BeautifulSoup(html_doc, 'html.parser')
print(len(html_doc))  # 505
print(len(html_doc2)) # 505
# If the length of str(soup)is longer than the origin one, perhaps bs4 detects some tags are not closed and then fixes it.
print(len(str(soup)))  # 505

print('-------------------------Chapter 9---------------------------------------------')
# html text might contain successive characters which represents the html entity;
html_doc_with_entities = """&pound; &yen; &ldquo; &rdquo; &lt; &gt; &"""
soup2 = BeautifulSoup(html_doc_with_entities, 'html.parser')
print('&pound; &yen; &ldquo; &rdquo;')  # html entities
print('\u00a3 \u00a5 \u201c \u201d')  # unicode character unique id
print('----------------------------------------')
# By default, Beautiful Soup does not convert bare ampersands and angle brackets to avoid invalid HTML or XML;
# Hence, & in html will become '&amp;' while '&lt' '&gt;' and '&amp;' stay the same.
print('the result of print(soup) is given below:\n%s' %soup2)
print('the result of print(str(soup)) is given below:\n%s' %str(soup2))
# default value of 'formatter' parameter
print("the result of soup2.prettify(formatter='minimal') is given below:\n%s" %soup2.prettify(formatter='minimal'))
print("the result of soup2.prettify(formatter='html') is given below:\n%s" %soup2.prettify(formatter='html'))
print("the result of soup2.prettify(formatter=None) is given below:\n%s" %soup2.prettify(formatter=None))  # well displayed
# Besides, you can pass a function to the formatter argument of the prettify() function

print('----------------------------------------------------------------------')
html_doc3 = '<a href="http://example.com/">&pound; &yen; &ldquo; &rdquo; &lt; &gt; & <i>example.com</i>\n</a>'
soup3 = BeautifulSoup(html_doc3, 'html.parser')
print(soup3.get_text())  # all html entities are converted.
print(soup3.get_text(strip=True)) # all '\n' is deleted
print([text for text in soup.stripped_strings])  #

print('-------------------------Chapter 11---------------------------------------------')
# the unicode of é is \u00e9 and its utf-8 code is \xc3\xa9
html_doc4 = "<h1> \xc3\xa9 \u00e9</h1>"
print(html_doc4)  # The '\xc3\xa9' string in Python script, Python will take these two thing as identical thing.
soup4 = BeautifulSoup(html_doc4, 'html.parser')
print(soup4.original_encoding)  #  None
print(soup4.get_text())
print('----------------------------------------')
html_doc5 = b"<h1> \xc3\xa9 \u00e9</h1>"
print(html_doc5)  # The '\u00e9' bytes in Python script, Python will not take it as a unicode character.
soup5 = BeautifulSoup(html_doc5, 'html.parser')
print(soup5.original_encoding)  # utf-8
print(soup5.get_text())
print('----------------------------------------')
# Beautiful Soup actually uses a sub-library called Unicode Dammit to detect the document encoding and convert it to Unicode.
html_doc6 = b"<h1> \xc3\xa9 </h1>"
dammit = UnicodeDammit(html_doc6, ['utf-8','latin-1'])
print(dammit.original_encoding)
print(dammit.unicode_markup)


