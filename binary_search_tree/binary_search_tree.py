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
        if self.value is None:
            self.value = BinarySearchTree(value)
            return

        focusNode = self
        while True:
            if value == focusNode.value:
                return

            if value < focusNode.value:
                if focusNode.left is None:
                    focusNode.left = BinarySearchTree(value)
                    return
                else:
                    focusNode = focusNode.left

            if value > focusNode.value:
                if focusNode.right is None:
                    focusNode.right = BinarySearchTree(value)
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
        focusNode = self

        while True:
            maxValue = focusNode.value

            if focusNode.right is None:
                return maxValue
            else:
                focusNode = focusNode.right

    def for_each(self, cb):
        cb(self.value)

        if self.left:
            self.left.for_each(cb)
        if self.right:
            self.right.for_each(cb)

# DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print In-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
