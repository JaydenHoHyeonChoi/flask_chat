import requests
import random
from bs4 import BeautifulSoup

url = "https://movie.naver.com/movie/running/current.nhn"
req = requests.get(url).text
doc = BeautifulSoup(req, 'html.parser')

title_tag = doc.select('dt.tit > a')
star_tag = doc.select('div.star_t1 > a > span.num')
reserve_tag = doc.select('div.star_t1.b_star > span.num')
image_tag = doc.select('div.thumb > a > img')

# 순위 정보에 따라 dict로 만들기
movie_dic = {}
for i in range(0, 10):
    movie_dic[i] = {
        "title":title_tag[i].text,
        "star":star_tag[i].text,
        "reserve":reserve_tag[i].text,
        "image":image_tag[i].get('src')
    }
    
pick_movie = movie_dic[random.randrange(0,10)]
print(pick_movie)

# return_doc = doc.select('dt.tit > a')
# list_movies = []
# for i in return_doc:
#     list_movies.append(i.text)
# print(list_movies)


# return_doc = doc.select('a > span.num')
# list_stars = []
# for i in return_doc:
#     list_stars.append(i.text)
# print(list_stars)


# return_doc = doc.select('div.star_t1.b_star > span.num')
# list_reservation = []
# for i in return_doc:
#     list_reservation.append(i.text)
# print(list_reservation)