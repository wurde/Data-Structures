#
# Dependencies
#

import os
import sys
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../doubly_linked_list'))
from doubly_linked_list import DoublyLinkedList

#
# Define data structure
#

class Queue:
  def __init__(self):
    self.size = 0
    self.storage = DoublyLinkedList()

  def enqueue(self, value):
    self.storage.add_to_head(value)
  
  def dequeue(self):
    if self.len() == 0:
      return None
    return self.storage.remove_from_tail()

  def len(self):
    return len(self.storage)
