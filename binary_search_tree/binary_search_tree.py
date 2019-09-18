#
# Dependencies
#

import os
import sys
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../queue_and_stack'))
from dll_queue import Queue
from dll_stack import Stack

#
# Define data structure
#

class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        # TODO add value.
        pass

    def contains(self, target):
        # TODO check if target exists.
        pass

    def get_max(self):
        # TODO return the max value.
        pass

    def for_each(self, cb):
        # TODO run callback on all nodes.
        pass
