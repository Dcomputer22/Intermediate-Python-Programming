import requests
from bs4 import BeautifulSoup

URL = "https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
response = requests.get(URL)
movie_website = response.text

soup = BeautifulSoup(movie_website, "html.parser")
movies = soup.find_all(name="h3", class_="listicleItem_listicle-item__title__hW_Kn")
movie_names = [movie.getText() for movie in movies]
movie_names_reversed = movie_names[::-1]

with open("movie.txt", "w") as file:
    for movie_title in movie_names_reversed:
        content = file.write(f"{movie_title}\n")
