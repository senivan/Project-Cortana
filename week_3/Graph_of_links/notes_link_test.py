import os
import shutil
import tempfile
import unittest
from unittest import TestCase
from notes_link import build_graph_from_note, convert_to_dot

class TestGraphBuilding(TestCase):
    def setUp(self):
        self.notes_dir = tempfile.mkdtemp()
        self.note_files = {
            'note.md': 'My favourite note is [[note4]].',
            'note1.md': 'See [[note]] and [[note3]].',
            'note2.md': 'See [[note]], [[note1]], and [[note3]].',
            'note3.md': '',
            'note4.md': 'See [[note]].',
        }
        for name, content in self.note_files.items():
            with open(os.path.join(self.notes_dir, name), 'w') as f:
                f.write(content)

    def tearDown(self):
        shutil.rmtree(self.notes_dir)

    def test_build_graph_from_note(self):
        graph = build_graph_from_note(os.path.join(self.notes_dir, 'note.md'))
        self.assertEqual(graph, {'note': ['note4'], 'note4': ['note']})

        graph = build_graph_from_note(os.path.join(self.notes_dir, 'note3.md'))
        self.assertEqual(graph, {'note3': []})

        graph = build_graph_from_note(os.path.join(self.notes_dir, 'note2.md'))
        self.assertEqual(graph, {
            'note': ['note4'],
            'note1': ['note', 'note3'],
            'note2': ['note', 'note1', 'note3'],
            'note3': [],
            'note4': ['note']
        })

    def test_convert_to_dot(self):
        graph = {'note': ['note4'], 'note4': ['note']}
        convert_to_dot(graph)
        with open('graph.dot') as f:
            content = f.read()
        self.assertMultiLineEqual(content, '''\
digraph {
note -> note4
note4 -> note
}''')

if __name__ == '__main__':
    unittest.main()
