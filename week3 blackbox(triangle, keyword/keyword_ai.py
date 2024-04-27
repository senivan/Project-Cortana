def find_film_keywords(film_keywords: dict, film_name: str):
    """
    Find and return the list of keywords for the film
    """
    result = set()
    if isinstance(film_keywords, tuple):
        film_keywords = film_keywords[1]
    for key in film_keywords:
        if film_name in film_keywords[key]:
            result.add(key)
    return result

def find_films_with_keywords(film_keywords: dict, num_of_films: int):
    """
    Find and return the list of films and ammonut of keywords for the film
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
        mid_res[key] = sorted(mid_res[key], reverse=True)
    result = [(film, len(find_film_keywords(film_keywords, film))) \
for key in mid_res for film in mid_res[key]]
    return result[:num_of_films]
