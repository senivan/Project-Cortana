import unittest
from keyword_processor import find_film_keywords, find_films_with_keywords

class TestKeywordProcessor(unittest.TestCase):
    def setUp(self):
        self.film_keywords = {
            'love': ['Film1', 'Film2', 'Film3'],
            'war': ['Film1', 'Film4'],
            'peace': ['Film2', 'Film5'],
            'hate': ['Film3', 'Film4', 'Film5']
        }

    def test_find_film_keywords(self):
        self.assertEqual(find_film_keywords(self.film_keywords, 'Film1'), {'love', 'war'})
        self.assertEqual(find_film_keywords(self.film_keywords, 'Film2'), {'love', 'peace'})
        self.assertEqual(find_film_keywords(self.film_keywords, 'Film6'), set())
        self.assertEqual(find_film_keywords(self.film_keywords, 'Film3'), {'love', 'hate'})

    def test_find_films_with_keywords(self):
        self.assertEqual(find_films_with_keywords(self.film_keywords, 3), [('Film1', 2), ('Film2', 2), ('Film3', 2)])
        self.assertEqual(find_films_with_keywords(self.film_keywords, 2), [('Film1', 2), ('Film2', 2)])
        self.assertEqual(find_films_with_keywords(self.film_keywords, 0), [])

if __name__ == '__main__':
    unittest.main()