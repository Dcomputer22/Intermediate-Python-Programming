from bs4 import BeautifulSoup
import requests
import lxml

response = requests.get("https://news.ycombinator.com/")
yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, "lxml")
# print(soup.title)
articles = soup.find_all(name="span", class_="titleline")
article_texts = []
article_links = []
for article_tag in articles:
    text = article_tag.getText()
    article_texts.append(text)
    for tag in article_tag:
        link = tag.get("href")
        article_links.append(link)
        article_links = [link for link in article_links if link is not None]
article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

# print(article_texts)
# print(article_links)
# print(article_upvotes)
highest_upvote = max(article_upvotes)
highest_index = article_upvotes.index(highest_upvote)

print(article_texts[highest_index])
print(article_links[highest_index])
print(highest_upvote)
