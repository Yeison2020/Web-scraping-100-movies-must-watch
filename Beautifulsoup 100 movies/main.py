import requests
import bs4

res = requests.get(url="https://www.empireonline.com/movies/features/best-movies-2/")
movies = res.text


soup = bs4.BeautifulSoup(movies, "html.parser")


Data_movies = soup.find_all(name="h3", class_="title")




list_movies = [movies.getText() for movies in Data_movies]

movies = list_movies[::-1]

with open("movies.txt", mode="w", encoding="utf-8") as file:
    for movie in movies:
        file.write(f"{movie}\n")