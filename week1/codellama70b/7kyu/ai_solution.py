# Problem : https://www.codewars.com/kata/55da347204760ba494000038/train/python

#Prompt:
# Solve the following task in python
# Linked Lists - Move Node

# Write a MoveNode() function which takes the node from the front of the source list and moves it to the front of the destintation list. You should throw an error when the source list is empty. For simplicity, we use a Context object to store and return the state of the two linked lists. A Context object containing the two mutated lists should be returned by moveNode.

# Here is your starting file:
# class Node(object):
#     def __init__(self, data):
#         self.data = data
#         self.next = None
    
# class Context(object):
#     def __init__(self, source, dest):
#         self.source = source
#         self.dest = dest
    
# def move_node(source, dest):
#     # Your code goes here.
#     # Remember to return the context.
#     return Context(source, dest)

# Here is some examples of result:
# source = 1 -> 2 -> 3 -> None
# dest = 4 -> 5 -> 6 -> None
# move_node(source, dest).source == 2 -> 3 -> None
# move_node(source, dest).dest == 1 -> 4 -> 5 -> 6 -> None

#Solution:

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
class Context:
    def __init__(self, source, dest):
        self.source = source
        self.dest = dest
        
def move_node(source, dest):
    if not isinstance(Context().source, Node) or \
       not isinstance(Context().dest, Node):
           raise TypeError('Source and Destination must be an instance of Node') 
    
    if source == None:
        return Context(source, dest) #raise IndexError('Source list does not exist.')
        
    first = source #keep original address of source head
    toMove = source #pointer for traversing the source list
    
    while toMove != None and toMove.next != None: 
        toMove = toMove.next #move pointer ahead
    else:# now we are at tail of source, about to move it.
        lastOfSource = toMove
        
    if dest == None: #if destination is empty, then assign first node from source and return the remaining list
       newDestination = first
          
       first = first.next
       lastOfSource.next = None  #first.next #re-assign head of source to next in line.
        
    else: #if destination has nodes, then insert the node at the front and point its next to original dest.
        newDestination = first
          
        first = first.next
        lastOfSource.next = None  #first.next #re-assign head of source to next in line.
        
    return Context(source = first, dest = newDestination)


# The code does not pass the test cases. It is failing beacuse of bad indents
# and wrong if on the start, and also bad logic.


# Prompt:
# Solve the following task in python
# Linked Lists - Move Node

# Write a MoveNode() function which takes the node from the front of the source list and moves it to the front of the destintation list. You should throw an error when the source list is empty. For simplicity, we use a Context object to store and return the state of the two linked lists. A Context object containing the two mutated lists should be returned by moveNode.

# Your task is just to move head of source and make it head of dest. Only dest can be None, source must be not None

# Here is your starting file:
# class Node(object):
#     def __init__(self, data):
#         self.data = data
#         self.next = None
    
# class Context(object):
#     def __init__(self, source, dest):
#         self.source = source
#         self.dest = dest
    
# def move_node(source, dest):
#     # Your code goes here.
#     # Remember to return the context.
#     return Context(source, dest)

# Here is some examples of result:
# source = 1 -> 2 -> 3 -> None
# dest = 4 -> 5 -> 6 -> None
# move_node(source, dest).source == 2 -> 3 -> None
# move_node(source, dest).dest == 1 -> 4 -> 5 -> 6 -> None

#Solution:
class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
    
class Context(object):
    def __init__(self, source, dest):
        self.source = source
        self.dest = dest
    
def move_node(source, dest):
    # Your code goes here.
    # Remember to return the context.
    if not source: 
      raise Exception('Error')
      
    head_to_be_removed = source.data
    source.next, Context.dest = Context.dest, Node(head_to_be_removed) 
    
    while True:
      if source.next == None:
        break
        
      source = source.next  
      
    return Context(source.next, dest)

# The code is not working as expected. It is failing the test cases because of bad indents and wrong logic.

# Changed solution:
class Node(object):
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
    
class Context(object):
    def __init__(self, source, dest):
        self.source = source
        self.dest = dest
    
def move_node(source, dest):
    # Your code goes here.
    # Remember to return the context.
    if not source: 
        raise Exception('Error')
    temp = source.data
    return Context(source.next, Node(data=temp, next=dest))

# The code is working as expected. It is passing all the test cases.

#Comment about ai's solution:
# The code has some problems with the logic and indents. It's passing 80% of the test cases.