
# importing json module
import json

def read_json_file(file_name):
    with open(file_name) as json_file:
        imdb_movie_data = json.load(json_file)
        # print data in pretty format
        # pretty_print_data = json.dumps(imdb_movie_data, indent=4, sort_keys=True)
        # print(f"Data: {pretty_print_data}")
    return imdb_movie_data


def top_dir_with_max_movies(file_name):
    imdb_movie_data = read_json_file(file_name)
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


def popular_genere_watched_by_most(file_name):
    imdb_movie_data = read_json_file(file_name)
    d = {}
    for i in imdb_movie_data:
        genere = i["genre"]
        if tuple(genere) in d:
            d[tuple(genere)] += 1
        else:
            d[tuple(genere)] = 1
    return d            
top_genere_watched = popular_genere_watched_by_most('imdb_assignment\imdb_assignment\imdb_movies.json')
top_genere_watched = max(top_genere_watched.items(),key=lambda x: x[1])
print(f"The popular genere watched by audiance is {top_genere_watched}")
    


def get_top_ten_movies_by_imdb_score(file_name):
    imdb_movie_data = read_json_file(file_name)
    result = sorted(imdb_movie_data,key=lambda x:x['imdb_score'], reverse=True)[:10]
    return [(x['name'],x['imdb_score']) for x in  result]

    # write your logic here to solve the query


def least_watched_movie_by_imdb_score(file_name):
    imdb_movie_data = read_json_file(file_name)
    res = sorted(imdb_movie_data, key = lambda x:x['imdb_score'])
    least_watchedmovie = res[0]
    return least_watchedmovie['name']
    


def get_best_director_in_first_hundred_movies(file_name):
    imdb_movie_data = read_json_file(file_name)
    movies = imdb_movie_data[:100]
    print(movies)
    directors = {}
    for movie in movies:
        direc = movie['director']
        directors[direc] = directors.get(direc,0) +1
        best_dir = max(directors, key=directors.get)
        return best_dir
    
    # write your logic here to solve the query
     
  
# check the data being returned by read_json_file
print(read_json_file('imdb_assignment\imdb_assignment\imdb_movies.json'))

print(f"The top director is {top_director[0]} and his movies are {top_director[1]}")
print(popular_genere_watched_by_most('imdb_assignment\imdb_assignment\imdb_movies.json'))
print(get_top_ten_movies_by_imdb_score('imdb_assignment\imdb_assignment\imdb_movies.json'))
print(least_watched_movie_by_imdb_score('imdb_assignment\imdb_assignment\imdb_movies.json'))
print(get_best_director_in_first_hundred_movies('imdb_assignment\imdb_assignment\imdb_movies.json'))
