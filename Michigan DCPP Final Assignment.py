#This project will take you through the process of mashing up data from two different APIs to make movie recommendations.
#The TasteDive API lets you provide a movie (or bands, TV shows, etc.) as a query input, and returns a set of related items.
#The OMDB API lets you provide a movie title as a query input and get back data about the movie, including scores from
#various review sites (Rotten Tomatoes, IMDB, etc.).

#You will put those two together. You will use TasteDive to get related movies for a whole list of titles.
#You’ll combine the resulting lists of related movies, and sort them according to their Rotten Tomatoes scores
#(which will require making API calls to the OMDB API.)

#To avoid problems with rate limits and site accessibility, we have provided a cache file with results for all the queries
#you need to make to both OMDB and TasteDive. Just use requests_with_caching.get() rather than requests.get().
#If you’re having trouble, you may not be formatting your queries properly, or you may not be asking for data that exists
#in our cache. We will try to provide as much information as we can to help guide you to form queries for which data
#exists in the cache.

#Your first task will be to fetch data from TasteDive. The documentation for the API is at https://tastedive.com/read/api.
#Define a function, called get_movies_from_tastedive. It should take one input parameter, a string that is the name of a
#movie or music artist. The function should return the 5 TasteDive results that are associated with that string; be sure
#to only get movies, not other kinds of media. It will be a python dictionary with just one key, ‘Similar’.

#Try invoking your function with the input “Black Panther”.
#
#HINT: Be sure to include only q, type, and limit as parameters in order to extract data from the cache.
#If any other parameters are included, then the function will not be able to recognize the data that you’re attempting
#to pull from the cache. Remember, you will not need an api key in order to complete the project, because all data will
#be found in the cache. The cache includes data for the following queries:

#This project will take you through the process of mashing up data from two different APIs to make movie recommendations.
#The TasteDive API lets you provide a movie (or bands, TV shows, etc.) as a query input, and returns a set of related items.
#The OMDB API lets you provide a movie title as a query input and get back data about the movie, including scores from
#various review sites (Rotten Tomatoes, IMDB, etc.).

#You will put those two together. You will use TasteDive to get related movies for a whole list of titles.
#You’ll combine the resulting lists of related movies, and sort them according to their Rotten Tomatoes scores
#(which will require making API calls to the OMDB API.)

#To avoid problems with rate limits and site accessibility, we have provided a cache file with results for all the queries
#you need to make to both OMDB and TasteDive. Just use requests_with_caching.get() rather than requests.get().
#If you’re having trouble, you may not be formatting your queries properly, or you may not be asking for data that exists
#in our cache. We will try to provide as much information as we can to help guide you to form queries for which data
#exists in the cache.

#Your first task will be to fetch data from TasteDive. The documentation for the API is at https://tastedive.com/read/api.
#Define a function, called get_movies_from_tastedive. It should take one input parameter, a string that is the name of a
#movie or music artist. The function should return the 5 TasteDive results that are associated with that string; be sure
#to only get movies, not other kinds of media. It will be a python dictionary with just one key, ‘Similar’.

#Try invoking your function with the input “Black Panther”.
#
#HINT: Be sure to include only q, type, and limit as parameters in order to extract data from the cache.
#If any other parameters are included, then the function will not be able to recognize the data that you’re attempting
#to pull from the cache. Remember, you will not need an api key in order to complete the project, because all data will
#be found in the cache. The cache includes data for the following queries:

import requests
import json

def get_movies_from_tastedive(name, key="327878-course3p-I4ZNBN4A"):
    baseurl = "https://tastedive.com/api/similar"
    params_d = {}
    params_d["q"] = name
    params_d["type"] = "movies"
    params_d["limit"] = "5"
    params_d["k"] = key
    resp = requests.get(baseurl, params=params_d)
    resp_dict = resp.json()
    resp_dict = json.dumps(resp_dict, indent=2)
    resp_dict = json.loads(resp_dict)
    return resp_dict

#Please copy the completed function from above into this active code window. Next, you will need to write a function
#that extracts just the list of movie titles from a dictionary returned by get_movies_from_tastedive.
#Call it extract_movie_titles.

def extract_movie_titles(get_movies_resp_dict):
    mov_lst = get_movies_resp_dict['Similar']['Results']
    resp = [similar_mov['Name'] for similar_mov in mov_lst if True]
    return resp

#Please copy the completed functions from the two code windows above into this active code window. Next, you’ll write
#a function, called get_related_titles. It takes a list of movie titles as input. It gets five related movies for
#each from TasteDive, extracts the titles for all of them, and combines them all into a single list.
#Don’t include the same movie twice.

def get_related_titles(mov_list):
    li = []
    for movie in mov_list:
        li.extend(extract_movie_titles(get_movies_from_tastedive(movie)))
    return list(set(li))

#Your next task will be to fetch data from OMDB. The documentation for the API is at https://www.omdbapi.com/
#Define a function called get_movie_data. It takes in one parameter which is a string that should represent the title
#of a movie you want to search. The function should return a dictionary with information about that movie.
#Again, use requests_with_caching.get(). For the queries on movies that are already in the cache, you won’t need an
#api key. You will need to provide the following keys: t and r. As with the TasteDive cache, be sure to only include
#those two parameters in order to extract existing data from the cache.

def get_movie_data(name, key="546c6742"):
    baseurl = "http://www.omdbapi.com/"
    params_d = {}
    params_d["t"] = name
    params_d["r"] = "json"
    params_d["apikey"] = key
    resp = requests.get(baseurl, params=params_d)
    resp_dict = resp.json()
    resp_dict = json.dumps(resp_dict, indent=2)
    resp_dict = json.loads(resp_dict)
    return resp_dict

#Please copy the completed function from above into this active code window. Now write a function called get_movie_rating.
#It takes an OMDB dictionary result for one movie and extracts the Rotten Tomatoes rating as an integer.
#For example, if given the OMDB dictionary for “Black Panther”, it would return 97. If there is no Rotten Tomatoes
#rating, return 0.

def get_movie_rating(get_movdata_resp_dict):
    OMDB_rating = ""
    get_movdata_resp_dict = get_movie_data(get_movdata_resp_dict)
    for rating in get_movdata_resp_dict["Ratings"]:
        if rating["Source"] == "Rotten Tomatoes":
            OMDB_rating = rating["Value"].split("%")
    if OMDB_rating != "":
        movie_rating = int(OMDB_rating[0])
    else:
        movie_rating = 0
    return movie_rating

#Now, you’ll put it all together. Don’t forget to copy all of the functions that you have previously defined into this
#code window. Define a function get_sorted_recommendations. It takes a list of movie titles as an input.
#It returns a sorted list of related movie titles as output, up to five related movies for each input movie title.
#The movies should be sorted in descending order by their Rotten Tomatoes rating, as returned by the get_movie_rating
#function. Break ties in reverse alphabetic order, so that ‘Yahşi Batı’ comes before ‘Eyyvah Eyvah’.

def get_sorted_recommendations(movie_list):
    movie_list = get_related_titles(movie_list)
    final_list = sorted(movie_list, key=lambda name: (get_movie_rating(name), name), reverse=True)
    return final_list

print(get_sorted_recommendations(["Jurassic Park"]))







