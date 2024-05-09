from  datetime import datetime
import collections
from collections import Counter
import random
now=datetime.now()
converted=now.strftime("%d.%m.%Y")


class Movie:
    def __init__(self, title,year,genre):
        self.title = title
        self.year = year
        self.genre = genre

        self._views_count = 0


    @property
    def views(self):
        return self._views_count


    def play(self):
        self._views_count += 1


    def information_movies(self):
        return (f"{self.title} ({self.year})")
    
    
class Film(Movie):
    pass


class Series(Movie):
    def __init__(self,season,episode, *args,**kwargs):
        super().__init__(*args,**kwargs)
        self.season = season
        self.episode = episode


    def information_series(self):
        self.season=self.season.replace("Season ","")
        self.episode=self.episode.replace("Episode ","")
        return (f"{self.title} S{int(self.season):02d}E{int(self.episode):02d}")


series_1 = Series("Season 1", "Episode 4","Breaking Bad", "2008", "Drama")
film_1 = Film("The Green Mile", "1999","Fantasy")
film_2 = Film("Forrest Gump","1994", "Comedy")
series_2 = Series("Season 1", "Episode 5","The Sopranos","1999","Drama")

library: list[Movie] = [series_1, film_1, film_2, series_2]


def generate_views(library: list[Movie], n=10):
    for _ in range(n):
        movie = random.choice(library)
        n = random.randint(1, 100)
        
        for i in range(n):               
            movie.play() 
           

def get_movies(library):
    for element in library:
        if isinstance(element,Film):
            details=element.information_movies()
            print(details)


def get_series(library):
    for element in library:
        if isinstance(element,Series):
            details=element.information_series()
            print(details)


def search(title,library):
    for element in library:
        details=element.title
        if title == details and isinstance(element,Film)==True:
            details=element.information_movies()
            print(details)
        elif title == details and isinstance(element,Series)==True:
            details=element.information_series()
            print(details)


def top_titles(library):
    view_collection = []
    for element in library:
        view_collection.append((element.views,element.title))
    ranked=sorted(view_collection,reverse=True)[:3]
    
    print(f"Najpopularniejsze filmy i seriale dnia {converted}: "
         f"{ranked[0][1]} {ranked[0][0]} views {ranked[1][1]} {ranked[1][0]} views "
         f"{ranked[2][1]} {ranked[2][0]} views")
    

generate_views(library)

print("Biblioteka filmów")

get_movies(library)

get_series(library)

top_titles(library)


if __name__ == "__main__":
    title=input("Provide title: ")
    search(title,library)