'''Graph of notes'''

import re
import os

def build_graph_from_note(note_path: str, graph = None) -> dict:
    '''
    Show notes with that other note is connected.
    >>> build_graph_from_note('notes/note.md')
    {'note': ['note4'], 'note4': ['note']}
    >>> build_graph_from_note('notes/note3.md')
    {'note3': []}
    '''
    if graph is None:
        graph = {}

    path = os.path.abspath(note_path)

    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    links = re.findall(r'\[\[([^\]]+)\]\]', content)
    graph[os.path.basename(path)[:-3]] = links
    for item in links:
        link_path = os.path.join(os.path.dirname(path), f'{item}.md')
        if item not in graph:
            build_graph_from_note(link_path, graph)

    for key in graph:
        graph[key] = sorted(graph[key])
    mykeys = list(graph.keys())
    mykeys.sort()
    sorted_dict = {i: graph[i] for i in mykeys}

    return sorted_dict

def convert_to_dot(graph: dict) -> None:
    '''
    Convert dictionary to graph and write it to the 'graph.dot' file.
    >>> convert_to_dot({'note1': ['note3', 'note2'], 'note3': ['note1'], 'note2': []})
    >>> with open('graph.dot', 'r', encoding = 'UTF-8') as dotfile:
    ...     dotfile.read()
    'digraph {\\nnote1 -> note2\\nnote1 -> note3\\nnote3 -> note1\\n}'
    '''
    for key in graph:
        graph[key] = sorted(graph[key])
    mykeys = list(graph.keys())
    mykeys.sort()
    sorted_dict = {i: graph[i] for i in mykeys}

    content = 'digraph {\n'
    for key, values in sorted_dict.items():
        for value in values:
            content += f'{key} -> {value}\n'
    content += '}'
    with open('graph.dot', 'w', encoding = 'UTF-8') as file:
        file.write(content)
