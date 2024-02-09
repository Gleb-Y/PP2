# Dictionary of movies

movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]

#ex 1
def imdb(str):
    for i in movies:
        if i['name'] == str and i['imdb'] > 5.5:
            return True
    return False
s = str(input())
print(imdb(s))

#ex 2
def top_movies(score):
    movie_list = []
    for i in movies:
        if i['imdb'] > score:
            movie_list.append(i['name'])
    return movie_list
imdb = 5.5
x = str(top_movies(imdb))[1:-1]
print(x)

#ex 3
def under_category(name):
    cat_movie_list = []
    for i in movies:
        if i['category'] == name:
            cat_movie_list.append(i['name'])
    return cat_movie_list
x = str(input())
d = str(under_category(x))[1:-1]
print(d)

#ex 4
def aver_imdb(name_of_dictionary):
    counter = 0
    sum = 0
    for i in name_of_dictionary:
        sum += i['imdb']
        counter += 1
    return float(sum/counter)
a = aver_imdb(movies)
a = format(a, '.2f')
print(a)

#ex 5
def aver_imdb_by_category(category):
    counter = 0
    sum = 0
    for i in movies:
        if i['category'] == category:
            sum += i['imdb']
            counter += 1
    return float(sum/counter)
e = str(input())
p = aver_imdb_by_category(e)
print(format(p, '.2f'))