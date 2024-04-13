class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Context:
    def __init__(self, source, dest):
        self.source = source
        self.dest = dest

def move_node(context: Context) -> Context:
    """Moves the node from the front of the source list to the front of the destination list.
    Args:
    context: A Context object containing the source and destination linked lists.
    Returns:
    A new Context object with the updated source and destination lists.
    Raises:
    ValueError: If the source list is empty.
    """
    if context.source is None:
        raise ValueError("Source list cannot be empty")

    # Move the node
    moved_node = context.source
    context.source = context.source.next
    moved_node.next = context.dest
    context.dest = moved_node

    return context