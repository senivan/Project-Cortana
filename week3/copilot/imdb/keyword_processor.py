"""IMDB task module"""
def find_film_keywords(film_keywords: dict, film_name: str):
    """
    Find and return the list of keywords for the film
    >>> find_film_keywords({'keyword1': ['film1', 'film2'],\
 'keyword2': ['film1']}, 'film1') == set(['keyword1', 'keyword2'])
    True
    >>> find_film_keywords({'keyword1': ['film1', 'film2'], \
'keyword2': ['film1']}, 'film2') == set(['keyword1'])
    True
    """
    result = set()
    for key in film_keywords:
        if film_name in film_keywords[key]:
            result.add(key)
    return result


def find_films_with_keywords(film_keywords: dict, num_of_films: int):
    """
    Find and return the list of films and ammonut of keywords for the film
    >>> find_films_with_keywords({'keyword1': ['film2'], 'keyword2': ['film1', 'film2']}, 1)
    [('film2', 2)]
    """
    if num_of_films == 0:
        return []
    films = list({lst1 for lst in film_keywords.values() for lst1 in lst})
    films = sorted(films, key=lambda x: len(find_film_keywords(film_keywords, x)), reverse=True)
    result = []
    mid_res = {}
    for film in films:
        if len(find_film_keywords(film_keywords, film)) not in mid_res:
            mid_res[len(find_film_keywords(film_keywords, film))] = [film]
        else:
            mid_res[len(find_film_keywords(film_keywords, film))].append(film)
    for key in mid_res:
        mid_res[key] = sorted(mid_res[key], reverse=False)
    result = [(film, len(find_film_keywords(film_keywords, film))
               ) for _, films in mid_res.items() for film in films]
    return result[:num_of_films]


if __name__== "__main__":
    import doctest
    print(doctest.testmod())
