from bs4 import BeautifulSoup
# If html.parser is not working for some websites, we can use lxml
import lxml

with open("website.html", encoding="utf-8") as html_file:
    contents = html_file.read()

soup = BeautifulSoup(contents, 'html.parser')
print(soup.title)
print(soup.title.name)
print(soup.title.string)
# print(soup.prettify())
# Gives the first anchor tag found in our html file. similar to the first <li>, <p> and th like.
print(soup.a)
# Gives a list of all attributes of our anchor tag
all_anchor_tags = soup.find_all(name="a")
print(all_anchor_tags)
# If you want only the text in the anchor tag or any tag
for tag in all_anchor_tags:
    print(tag.getText())
    # for the links
    print(tag.get("href"))
heading = soup.find_all(name="h1", id="name")
print(heading)
print(heading)
section_heading = soup.find(name="h3", class_="heading")
print(section_heading)
print(section_heading.name)
print(section_heading.getText())
# to get the class value of an attribute
print(section_heading.get('class'))
# To get hold of the company url
company_url = soup.select_one(selector="p a")
# This will give you an anchor tag that sits inside a paragraph tag using the  css selector
print(company_url)
# Same with when you want to get the first id with a value of name
name = soup.select_one(selector="#name")
print(name)
# The css selector can be used to select an element by class
class_heading = soup.select(".heading")
print(class_heading)
print(class_heading[0].get("class"))


