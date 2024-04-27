'''Graph unit tests'''

# By creating tests from the condition, he covered the task only by 50%.
# Then he added corner cases by considering graphs of different structures
# and None cases. The coverage in the end was 100%. AI also added a case
# that was not taken into account in the implementation of the problem,
# but he hit a dead end and did not find all the cases for tests to
# completely solve the problem correctly. 

import unittest
from graph import build_graph_from_note, convert_to_dot
import os

class TestNoteLink(unittest.TestCase):
    def setUp(self):
        self.note_path = "notes/note.md"
        self.note3_path = "notes/note3.md"
        self.graph_path = "graph.dot"

    def test_build_graph_from_note(self):
        # Test when graph is None
        graph = build_graph_from_note(self.note_path)
        self.assertEqual(graph, {"note": ["note4"], "note4": ["note"]})

        # Test when graph is not None
        existing_graph = {"note": ["note4"]}
        graph = build_graph_from_note(self.note3_path, existing_graph)
        self.assertEqual(graph, {"note": ["note4"], "note3": []})

    def test_convert_to_dot(self):
        graph = {"note": ["note4"], "note4": ["note"]}
        convert_to_dot(graph)
        self.assertTrue(os.path.exists(self.graph_path))

        with open(self.graph_path, 'r') as f:
            content = f.read()
            self.assertIn('note -> note4', content)
            self.assertIn('note4 -> note', content)

    def tearDown(self):
        if os.path.exists(self.graph_path):
            os.remove(self.graph_path)

if __name__ == '__main__':
    unittest.main()

# python -m coverage run graph_unitests.py
# python -m coverage report -m
