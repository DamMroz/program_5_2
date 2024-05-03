from  datetime import datetime
import collections
from collections import Counter
import random
now=datetime.now()
converted=now.strftime("%d.%m.%Y")


television_list=[("The Green Mile", "1999","Fantasy"),("Pulp Fiction", "1994", "Thriller"), 
                 ("Forrest Gump","1994", "Comedy"), 
                 ("Breaking Bad", "2008", "Drama", "Season 1", "Episode 4"),
                 ("Breaking Bad", "2008","Drama", "Season 1","Episode 2"),
                 ("Breaking Bad", "2009","Drama", "Season 2","Episode 10")]


class television:
   def __init__(self, title, year, genre,*views, **kwargs): 
           
       self.title = title
       self.year = year
       self.genre = genre
       self.views = views
    

   def play (self):  
       with open("out.txt", "r") as in_file:
           views = sum(line.count(self.title) for line in in_file)
       print(f"{views} views")


   def information_film (self):
       with open('out.txt', 'a') as f:
               print(self.title, file=f)
       return  f"{self.title} ({self.year})"
       

class series(television):
   def __init__(self,season,episode, *args,**kwargs):
       super().__init__(*args,**kwargs)
       self.season = season
       self.episode = episode


   def information_series (self):
       with open('out.txt', 'a') as f:
               print(self.title, file=f)
       self.season=self.season.replace("Season ","")
       self.episode=self.episode.replace("Episode ","")
       return f"{self.title} S{int(self.season):02d}E{int(self.episode):02d} "
   

def generate_views():
    n=random.randint(0,len(television_list)-1)
    n_2=random.randint(1,100)
    with open('out.txt', 'a') as f:
               title_element=television_list[n][0]
               for x in range (0,n_2):
                   print(title_element, file=f)


def activate_generate_views():
    print("Biblioteka filmów")
    for x in range (0,10):
        generate_views()


activate_generate_views()


def sort_movies():
     movies_list=[]
     for x in range (0,len(television_list)):
        if len(television_list[x])==3:
            movies_initial=television_list[x]
            movies_list.append(movies_initial)
     return sorted(movies_list)


def sort_series():
     series_list=[]
     for x in range (0,len(television_list)):
        if len(television_list[x])>3:
            series_initial=television_list[x]
            series_list.append(series_initial)
     return sorted(series_list)

list_only_movies=sort_movies()
list_only_series=sort_series()


def get_movies():
    for x in range (0,len(list_only_movies)):
        if len(list_only_movies[x])==3:
            
            movies_information=television(*list_only_movies[x]).information_film()
            movies_list=television(*list_only_movies[x])
            print(movies_information)
            movies_list.play()
           
get_movies()


def get_series():
    for x in range (0,len(list_only_series)):
        if len(list_only_series[x])>3:
            series_information=series( title=list_only_series[x][0],year=list_only_series[x][1],
                                             genre=list_only_series[x][2],
                                             season=list_only_series[x][3],
                                             episode=list_only_series[x][4]).information_series()
            series_list=series(title=list_only_series[x][0],year=list_only_series[x][1],
                                             genre=list_only_series[x][2],
                                             season=list_only_series[x][3],
                                             episode=list_only_series[x][4])
            print(series_information)
    series_list.play()


get_series()
title=input("Please provide title: ")
def search(title):
    for x in range (0,len(television_list)):
        if title in television_list[x]:
            if len(television_list[x])==3:
               film_information=television(*television_list[x]).information_film()
               print(film_information)
            elif len(television_list[x])>3:
                series_information=series(title=television_list[x][0],year=television_list[x][1],
                                             genre=television_list[x][2],
                                             season=television_list[x][3],
                                             episode=television_list[x][4]).information_series()
                print(series_information)


search(title)


def top_titles():
    with open('out.txt') as infile:
        counts = collections.Counter(element.strip() for element in infile)
    print(f"Najpopularniejsze filmy i seriale dnia {converted}")
    for line, count in counts.most_common(3):
        print(f"{line}, {count} views")


top_titles()