import unittest
from cmudict import dict_reader_tuple, dict_reader_dict, dict_invert

class TestCmuDict(unittest.TestCase):
    def setUp(self):
        self.file_dict = 'cmudict.txt'
        self.sample_dict = {'AABERG': {('AA1', 'B', 'ER0', 'G')}, 'A.': {('EY1',)},
                            'A': {('EY1',), ('AH0',)}, 'A42128': {('EY1', 'F', 'AO1',
                            'R', 'T', 'UW1', 'W', 'AH1', 'N', 'T', 'UW1', 'EY1', 'T')},
                            'AAA': {('T', 'R', 'IH2', 'P', 'AH0', 'L', 'EY1')}}
        self.sample_tuple = [('AABERG', 1, ['AA1', 'B', 'ER0', 'G']), ('A.', 1, ['EY1']),
                             ('A', 1, ['EY1']), ('A', 2, ['AH0']), ('A42128', 1, ['EY1', 'F', 'AO1',
                             'R', 'T', 'UW1', 'W', 'AH1', 'N', 'T', 'UW1', 'EY1', 'T']),
                             ('AAA', 1, ['T', 'R', 'IH2', 'P', 'AH0', 'L', 'EY1'])]

    def test_dict_reader_tuple(self):
        result = dict_reader_tuple(self.file_dict)
        self.assertIsInstance(result, list)
        self.assertIsInstance(result[0], tuple)
        self.assertEqual(len(result[0]), 3)

    def test_dict_reader_dict(self):
        result = dict_reader_dict(self.file_dict)
        self.assertIsInstance(result, dict)
        self.assertIsInstance(list(result.values())[0], set)

    def test_dict_invert(self):
        result1 = dict_invert(self.sample_dict)
        self.assertIsInstance(result1, dict)
        self.assertIsInstance(list(result1.values())[0], set)
        self.assertIsInstance(list(result1.keys())[0], int)
        result2 = dict_invert(self.sample_tuple)
        self.assertIsInstance(result2, dict)
        self.assertIsInstance(list(result2.values())[0], set)
        self.assertIsInstance(list(result2.keys())[0], int)
        self.assertEqual(result1, result2)
        result3 = dict_invert(None)
        self.assertIsNone(result3)

        

if __name__ == '__main__':
    unittest.main()
