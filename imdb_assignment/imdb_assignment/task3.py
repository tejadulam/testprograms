# 3. Print out the top ten movies, according to imdb score.

import json
with open('imdb_assignment\imdb_assignment\imdb_movies.json') as f:
    data = json.load(f)
    # print(data)
    print(sorted(data,key=lambda x:x['imdb_score'], reverse=True)[:10])


# 1. Print the top director with maximum number of movies.
import json

def read_json_file(file_name):
    with open(file_name,'r') as jsonfile:
        imdb_movie_data = json.load(jsonfile)
    return imdb_movie_data

def top_dir_with_max_movies(file_name):
    imdb_movie_data = read_json_file(file_name)
    dir = {}
    for i in imdb_movie_data:
        director = i['director']
        if director in dir:
            dir[director] += 1
        else:
            dir[director] = 1
    return dir

top_dir = top_dir_with_max_movies('imdb_assignment\imdb_assignment\imdb_movies.json')
top_director = max(top_dir.items(),key=lambda x: x[1])
print(top_director)
print(f"The top director is {top_director[0]} and his movies are {top_director[1]}")