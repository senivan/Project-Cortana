class Node:
    def __init__(self, data):
        self.head = data
        self.next = None  # Point to the next node in the list

class Context:
    def __init__(self, source, dest):
        self.source = source
        self.dest = dest

def move_node(source, dest):
    if source is None:
        raise ValueError('Source list is empty')
    if source.head is None:
        return Context(source, Node(source.data) if dest is None else dest)
    else:
        moved_node = source.head
        source.head = source.head.next
        moved_node.next = dest.head
        dest.head = moved_node
    return Context(source, dest)
