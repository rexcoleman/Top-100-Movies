import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
empire_online_webpage = response.text
soup = BeautifulSoup(empire_online_webpage, "html.parser")

movie_titles = soup.find_all(name="h3", class_="title")

movie_titles = [movie.getText() for movie in movie_titles]
movies = movie_titles[::-1]
print(movies)

with open("movies.txt", mode="w") as file:
    for movie in movies:
        file.write(f"{movie}\n")

