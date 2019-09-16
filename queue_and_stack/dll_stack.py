#
# Dependencies
#

import sys
# sys.path.append('../doubly_linked_list')
# from doubly_linked_list import DoublyLinkedList

#
# Define data structure
#

class Stack:
  def __init__(self):
    self.size = 0
    # TODO Why is our DLL a good choice to store our elements?
    self.storage = []

  def push(self, value):
    self.storage.append(value)
  
  def pop(self):
    if self.len() == 0:
      return None
    return self.storage.pop()

  def len(self):
    return len(self.storage)
