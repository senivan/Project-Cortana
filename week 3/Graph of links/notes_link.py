# /home/ivan/Documents/UCU/Folder for programming task
# convert_to_dot(build_graph_from_note('/home/ivan/Documents/UCU/Folder for programming task/note3.md'))
'''
This module contains function build_graph_from_note,
that returns a dictionary with all notes connections,
and a function convert_to_dot, that converts graph dictionary 
to .dot file
'''
import re
import os

def build_graph_from_note(note_path:str, graph:dict = None)->dict:
    '''
    This function takes path to notes and optionaly an already created graph to edit
    and returns a dictionary where keys are note names 
    and values are lists of names tis note is connected to
    '''
    if graph is None:
        graph = {}
    with open(note_path, 'r', encoding='utf-8') as note:
        connections = re.findall(r"\[\[(.*?)\]\]", note.read())
    path_lst = os.path.split(note_path)
    main_note_name = path_lst[-1]
    main_name_lst = main_note_name.split('.')
    main_note_name = main_name_lst[0]
    if main_note_name not in graph:
        graph[main_note_name] = connections
    else:
        graph[main_note_name].append(connections)
    for link in connections:
        new_path = os.path.join(path_lst[0], f'{link}.md')
        if link not in graph or main_note_name not in graph[link]:
            build_graph_from_note(new_path, graph)
    graph = dict(sorted(graph.items()))
    for note in graph:
        graph.update({note:sorted(graph[note])})
    return graph

def convert_to_dot(graph:dict):
    '''
    This function takes a dictionary with note connections
    and converts it to .dot file
    '''
    graph = dict(sorted(graph.items()))
    for note in graph:
        graph.update({note:sorted(graph[note])})
    result = 'digraph {\n'
    for key, item in graph.items():
        for e in item:
            result += f'{key} -> {e}'
            result += '\n'
    result += '}'
    with open('graph.dot', mode='w+', encoding='utf-8') as graph_file:
        graph_file.write(result)

if __name__ == '__main__':
    convert_to_dot(build_graph_from_note('/home/ivan/Documents/UCU/Folder for programming task/note3.md'))
    import doctest
    print(doctest.testmod())
