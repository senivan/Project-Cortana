import unittest
from keyword_ai import find_film_keywords, find_films_with_keywords
import coverage

cov = coverage.coverage()
cov.start()

class TestFindFilmKeywords(unittest.TestCase):
    def test_find_film_keywords(self):
        film_keywords = {'keyword1': ['film1', 'film2'], 'keyword2': ['film1']}
        self.assertEqual(find_film_keywords(film_keywords, 'film1'), set(['keyword1', 'keyword2']))
        self.assertEqual(find_film_keywords(film_keywords, 'film2'), set(['keyword1']))

    def test_empty_film_keywords(self):
        film_keywords = {}
        self.assertEqual(find_film_keywords(film_keywords, 'film1'), set())

    def test_film_not_found(self):
        film_keywords = {'keyword1': ['film1', 'film2'], 'keyword2': ['film1']}
        self.assertEqual(find_film_keywords(film_keywords, 'film3'), set())

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            find_film_keywords('not a dict', 'film1')

    def test_invalid_input_structure(self):
        film_keywords = {'keyword1': 'not a list'}
        result = find_film_keywords(film_keywords, 'film1')
        self.assertEqual(result, set())

    def test_film_name_is_none(self):
        film_keywords = {'keyword1': ['film1', 'film2'], 'keyword2': ['film1']}
        with self.assertRaises(TypeError):
            find_film_keywords(film_keywords, None)

    def test_film_keywords_is_none(self):
        with self.assertRaises(TypeError):
            find_film_keywords(None, 'film1')

    def test_empty_film_name(self):
        film_keywords = {'keyword1': ['film1', 'film2'], 'keyword2': ['film1']}
        with self.assertRaises(ValueError):
            find_film_keywords(film_keywords, '')

    def test_empty_film_keywords_and_film_name(self):
        with self.assertRaises(ValueError):
            find_film_keywords({}, '')
    def test_find_films_with_keywords(self):
        film_keywords = {'keyword1': ['film2'], 'keyword2': ['film1', 'film2']}
        self.assertEqual(find_films_with_keywords(film_keywords, 1), [('film2', 2)])

    def test_find_films_with_keywords_num_of_films_is_zero(self):
        film_keywords = {'keyword1': ['film2'], 'keyword2': ['film1', 'film2']}
        self.assertEqual(find_films_with_keywords(film_keywords, 0), [])

    def test_find_films_with_keywords_num_of_films_is_two(self):
        film_keywords = {'keyword1': ['film2'], 'keyword2': ['film1', 'film2'], 'keyword3': ['film1']}
        self.assertEqual(find_films_with_keywords(film_keywords, 2), [('film2', 2), ('film1', 2)])

    def test_find_films_with_keywords_num_of_films_is_three(self):
        film_keywords = {'keyword1': ['film2'], 'keyword2': ['film1', 'film2'], 'keyword3': ['film1'], 'keyword4': ['film3']}
        self.assertEqual(find_films_with_keywords(film_keywords, 3), [('film2', 2), ('film1', 2), ('film3', 1)])

    def test_find_films_with_keywords_num_of_films_is_four(self):
        film_keywords = {'keyword1': ['film2'], 'keyword2': ['film1', 'film2'], 'keyword3': ['film1'], 'keyword4': ['film3'], 'keyword5': ['film4']}
        self.assertEqual(find_films_with_keywords(film_keywords, 4), [('film2', 2), ('film1', 2), ('film3', 1), ('film4', 1)])

    def test_find_films_with_keywords_num_of_films_is_five(self):
        film_keywords = {'keyword1': ['film2'], 'keyword2': ['film1', 'film2'], 'keyword3': ['film1'], 'keyword4': ['film3'], 'keyword5': ['film4'], 'keyword6': ['film5']}
        self.assertEqual(find_films_with_keywords(film_keywords, 5), [('film2', 2), ('film1', 2), ('film3', 1), ('film4', 1), ('film5', 1)])

    def test_find_films_with_keywords_num_of_films_is_six(self):
        film_keywords = {'keyword1': ['film2'], 'keyword2': ['film1', 'film2'], 'keyword3': ['film1'], 'keyword4': ['film3'], 'keyword5': ['film4'], 'keyword6': ['film5'], 'keyword7': ['film6']}
        self.assertEqual(find_films_with_keywords(film_keywords, 6), [('film2', 2), ('film1', 2), ('film3', 1), ('film4', 1), ('film5', 1), ('film6', 1)])

    def test_find_films_with_keywords_num_of_films_is_seven(self):
        film_keywords = {'keyword1': ['film2'], 'keyword2': ['film1', 'film2'], 'keyword3': ['film1'], 'keyword4': ['film3'], 'keyword5': ['film4'], 'keyword6': ['film5'], 'keyword7': ['film6'], 'keyword8': ['film7']}
        self.assertEqual(find_films_with_keywords(film_keywords, 7), [('film2', 2), ('film1', 2), ('film3', 1), ('film4', 1), ('film5', 1), ('film6', 1), ('film7', 1)])

    def test_find_films_with_keywords_num_of_films_is_eight(self):
        film_keywords = {'keyword1': ['film2'], 'keyword2': ['film1', 'film2'], 'keyword3': ['film1'], 'keyword4': ['film3'], 'keyword5': ['film4'], 'keyword6': ['film5'], 'keyword7': ['film6'], 'keyword8': ['film7'], 'keyword9': ['film8']}
        self.assertEqual(find_films_with_keywords(film_keywords, 8), [('film2', 2), ('film1', 2), ('film3', 1), ('film4', 1), ('film5', 1), ('film6', 1), ('film7', 1), ('film8', 1)])

    def test_find_films_with_keywords_num_of_films_is_nine(self):
        film_keywords = {'keyword1': ['film2'], 'keyword2': ['film1', 'film2'], 'keyword3': ['film1'], 'keyword4': ['film3'], 'keyword5': ['film4'], 'keyword6': ['film5'], 'keyword7': ['film6'], 'keyword8': ['film7'], 'keyword9': ['film8'], 'keyword10': ['film9']}
        self.assertEqual(find_films_with_keywords(film_keywords, 9), [('film2', 2), ('film1', 2), ('film3', 1), ('film4', 1), ('film5', 1), ('film6', 1), ('film7', 1), ('film8', 1), ('film9', 1)])

    def test_find_films_with_keywords_num_of_films_is_ten(self):
        film_keywords = {'keyword1': ['film2'], 'keyword2': ['film1', 'film2'], 'keyword3': ['film1'], 'keyword4': ['film3'], 'keyword5': ['film4'], 'keyword6': ['film5'], 'keyword7': ['film6'], 'keyword8': ['film7'], 'keyword9': ['film8'], 'keyword10': ['film9'], 'keyword11': ['film10']}
        self.assertEqual(find_films_with_keywords(film_keywords, 10), [('film2', 2), ('film1', 2), ('film3', 1), ('film4', 1), ('film5', 1), ('film6', 1), ('film7', 1), ('film8', 1), ('film9', 1), ('film10', 1)])

unittest.main(exit=False)
cov.stop()
cov.report()