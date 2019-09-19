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

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

#
# Define data structure
#

class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if self.value is None:
            self.value = Node(value)
            return

        focusNode = self
        while True:
            if value == focusNode.value:
                return

            if value < focusNode.value:
                if focusNode.left is None:
                    focusNode.left = Node(value)
                    return
                else:
                    focusNode = focusNode.left

            if value > focusNode.value:
                if focusNode.right is None:
                    focusNode.right = Node(value)
                    return
                else:
                    focusNode = focusNode.right

    def contains(self, target):
        focusNode = self

        while focusNode is not None:
            if target == focusNode.value:
                return True
            elif target < focusNode.value:
                focusNode = focusNode.left
            else:
                focusNode = focusNode.right
        
        return False

    def get_max(self):
        # TODO return the max value.
        pass

    def for_each(self, cb):
        # TODO run callback on all nodes.
        pass
