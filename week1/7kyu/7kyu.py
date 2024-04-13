"""
Prompt: Write a MoveNode() function which takes the node from the front 
of the source list and moves it to the front of the destintation list. 
You should throw an error when the source list is empty. 
For simplicity, we use a Context object to store and return the state of the two linked lists. 
A Context object containing the two mutated lists should be returned by moveNode.
---
Copilot gave perfect solution for this problem from the first try.
Code:
"""
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Context:
    def __init__(self, source, dest):
        self.source = source
        self.dest = dest

def MoveNode(source, dest):
    if source is None:
        raise ValueError("Source list is empty")
    
    moved_node = source
    source = source.next
    moved_node.next = dest
    dest = moved_node
    
    return Context(source, dest)