# -*- coding: utf-8 -*-
"""
Chapter 6, 'Going down' section.
Be careful that the new line character '\n' will affect your idea about the structure of the whole HTML page.
"""

from bs4 import BeautifulSoup

soup = BeautifulSoup("""
           <html>
           <p>name1</p>
           <p><b><a>name2</a></b></p>
           <p></p>
           <p>name3</p>
           </html>""", 'html.parser')
# print(type(soup))  # <class 'bs4.BeautifulSoup'>

# 1, bs4.element.Tag.contents
# The usage of 'soup.html.contents' returns all characters which are included by the <html> tag.
print('------------------------bs4.element.Tag.contents-----------------------------------')
print(soup.html.contents)  # ['\n', <p>name1</p>, '\n', <p><b><a>name2</a></b></p>, '\n', <p></p>, '\n', <p>name3</p>, '\n']
print(type(soup.html.contents[0]))  # <class 'bs4.element.NavigableString'>
print(type(soup.html.contents[1]))  # <class 'bs4.element.Tag'>
print(soup.html.contents[1].contents)  # ['name1'] and the element is not 'str' type
print(type(soup.html.contents[1].contents[0]))  # <class 'bs4.element.NavigableString'>

# 2, bs4.element.Tag.children
# The result is a list,
print('------------------------bs4.element.Tag.children-----------------------------------')
for index, child in enumerate(soup.html.children):
    print('The child with index %s is shown below:' %index)
    print(child)

# 3, bs4.element.Tag.descendants
# It contains sub-tags and 'bs4.element.NavigableString' object inside tags.
# Example 1: the second <p> tag has a <b> tag as its sub-tag and the <b> tag contains a 'bs4.element.NavigableString' object.
# Example 2: there is no 'bs4.element.NavigableString' object
print('------------------------bs4.element.Tag.descendants-----------------------------------')
for index, descendant in enumerate(soup.html.descendants):
    print('The descendant with index %s is shown below:' %index)
    print(descendant)

# 4, bs4.element.Tag.string
# This works if a tag has only one child and the child is a 'NavigableString' object.
# This works if a tag has only one sub-tag and the sub-tag has only one child which is also a 'NavigableString' object.
# If a tag contains more than one thing, bs4.element.Tag.string will return None.
print('------------------------bs4.element.Tag.string-----------------------------------')
print(soup.html.string)  # None
print(soup.html.p.string)  # name1, and it is bs4.element.NavigableString object

# 5, bs4.element.Tag.strings & bs4.element.Tag.stripped_strings
# If there’s more than one thing inside a tag, you can still look at just the strings.
# In other words, all tags disappear.
print('------------------------bs4.element.Tag.strings-----------------------------------')
for string in soup.html.strings:
    print(string)

print('------------------------bs4.element.Tag.stripped_strings-----------------------------------')
for string in soup.html.stripped_strings:
    print(string)
