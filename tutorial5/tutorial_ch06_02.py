# -*- coding: utf-8 -*-
"""
Chapter 6, 'Going up', 'Going sideways' and 'Going back and forth' sections.
Be careful that the new line character '\n' will affect your idea about the structure of the whole HTML page.
The 'bs4.BeautifulSoup', 'bs4.element.Tag' and 'bs4.element.NavigableString' have parent attribute;

P.S. all objects of bs4.element.Tag.next_elements should be the sibling or child of the current object.
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

# 1, bs4.element.Tag.parent
print('------------------------bs4.element.Tag.parent-----------------------------------')
print(soup.a.parent)  # soup.a is the first <a> tag and the result is 'bs4.element.Tag' class;
print(soup.html.parent)  # soup.html is the first <html> tag and the result is 'bs4.BeautifulSoup' class;
print(soup.parent)  # None

# 2, bs4.element.Tag.parents
print('------------------------bs4.element.Tag.parents-----------------------------------')
# the parent of the first <a> tag: <b> --> <p> --> <html> --> the whole html page (bs4.BeautifulSoup)
for index, parent in enumerate(soup.a.parents):
    print('The parent with index %s is shown below:' % index)
    print(parent)

# 3, bs4.element.Tag.next_sibling & bs4.element.Tag.previous_sibling
# Both attributes return the object that are on the same level of the parse tree.
print('------------------------bs4.element.Tag.next_sibling & bs4.element.Tag.previous_sibling-----------------------------------')
# be careful that the new line character (the NavigableString type) is the next sibling of the first <p> tag.
print(soup.p)  # the first <p> tag
print(soup.p.next_sibling.next_sibling)  # the second <p> tag
print(soup.p.previous_sibling)  # '\n' and it is <class 'bs4.element.NavigableString'>
print(soup.p.previous_sibling.previous_sibling)  # None

# 4, bs4.element.Tag.next_siblings & bs4.element.Tag.previous_siblings
print('------------------------bs4.element.Tag.next_siblings & bs4.element.Tag.previous_siblings-----------------------------------')
for index, next_sibling in enumerate(soup.p.next_sibling.next_sibling.next_siblings):
    # those next siblings of the second <p> tag
    print('The next sibling with index %s is shown below:' % index)
    print(next_sibling)

#5, bs4.element.Tag.next_element & bs4.element.Tag.previous_element
# Compared with bs4.element.Tag.next_sibling, bs4.element.Tag.next_element returns next object which are immediately
# after the current object.
print('------------------------bs4.element.Tag.next_element & bs4.element.Tag.previous_element-----------------------------------')
second_tag = soup.p.next_sibling.next_sibling
print(second_tag.next_element)  # The result is the <b> tag: <b><a>name2</a></b>; It is not the sibling object.
# print(second_tag.next_sibling)  # '\n' and it is  <class 'bs4.element.NavigableString'>

#6, bs4.element.Tag.next_elements & bs4.element.Tag.previous_elements
# P.S. all objects of bs4.element.Tag.next_elements should be the sibling or child of the current object.
print('------------------------bs4.element.Tag.next_elements & bs4.element.Tag.previous_elements-----------------------------------')
for index, element in enumerate(soup.p.next_elements):
    print('The next element with index %s is shown below:' % index)
    print(element)


