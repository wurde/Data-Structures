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

class LRUCache:
  """
  Our LRUCache class keeps track of the max number of nodes it
  can hold, the current number of nodes it is holding, a doubly-
  linked list that holds the key-value entries in the correct 
  order, as well as a storage dict that provides fast access
  to every node stored in the cache.
  """
  def __init__(self, limit=10):
      self.maxCount = limit
      self.currentCount = 0
      self.entries = DoublyLinkedList()
      self.storage = {}

  """
  Retrieves the value associated with the given key. Also
  needs to move the key-value pair to the end of the order
  such that the pair is considered most-recently used.
  Returns the value associated with the key or None if the
  key-value pair doesn't exist in the cache. 
  """
  def get(self, key):
      if key in self.storage:
          self.entries.move_to_front(self.entries.tail)
          return self.storage[key]
      else:
          return None

  """
  Adds the given key-value pair to the cache. The newly-
  added pair should be considered the most-recently used
  entry in the cache. If the cache is already at max capacity
  before this entry is added, then the oldest entry in the
  cache needs to be removed to make room. Additionally, in the
  case that the key already exists in the cache, we simply 
  want to overwrite the old value associated with the key with
  the newly-specified value.
  """
  def set(self, key, value):
      if key in self.storage:
          self.storage[key] = value
          return

      if self.currentCount >= self.maxCount:
          del self.storage[self.entries.tail.value]
          self.entries.remove_from_tail()
          self.currentCount -= 1

      self.entries.add_to_head(key)
      self.storage[key] = value
      self.currentCount += 1
