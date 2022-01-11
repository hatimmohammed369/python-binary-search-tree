from typing import Iterable
from tree_node import node


# class bs_tree (binary search tree)
#   duplicates are allowed
#
# attributes:
#   root, size, get_node, insert, remove
# 
# root:
#   default: node(parent=None, value=None, left=None, right=None, id='')
#   represents tree root
#
# size:
#   default: 0
#   how many "real-life tree leafs" are there, simply put, how many elements in out tree
#
# get_node:
#   method
#   given an item, like 4, returns the first node(n) with attribute 


class bs_tree:
    def __init__(self, init=None) -> None:
        self.root = node(parent=None, value=None, left=None, right=None, id='')
        self.size = 0
        if isinstance(init, Iterable):
            for item in init:
                self.insert(item)
    
    
    def get_node(self, item) -> node:
        current = self.root
        while True:
            if current is None or current.value is None:
                break # because it's not here
            else:
                if item <= current.value:
                    # GO LEFT
                    current = current.left
                else:
                    # GO RIGHT
                    current = current.right
        return current

    
    def insert(self, item):
        if self.size == 0:
            self.root.value = item
        else:
            # search for the right slot
            current = self.root
            while True:
                if item <= current.value:
                    # GO LEFT
                    # there's an equal sign since duplicates are allowed
                    if current.left is None:
                        # the right spot!
                        current.left = node(parent=current, value=item, id='#L')
                        break # so that we dont stuck in a loop
                    else:
                        # go left, but even deeper!
                        current = current.left
                else:
                    # GO RIGHT
                    if current.right is None:
                        # the right spot!
                        current.right = node(parent=current, value=item, id='#R')
                        break # so that we dont stuck in a loop
                    else:
                        # go right, but even deeper!
                        current = current.right
        # insertion complete!
        self.size += 1 # dont forget to increase the size!!!!!!!!
        return self
    
    
    def remove(self, item):
        item_node = self.get_node(item)
        deleted_value = item_node.value
        if self.size == 1 and self.root.value == item:
            self.root.value = None
        elif item_node is not None: # then we can delete
            L, R = item_node.left is not None, self.right is not None
            if L or (L and R):
                pass
            else:
                # item_node has a right child only
                
                if item_node.id == '':
                    # item_node is root
                    self.root = item_node.right
                    self.root.id = ''
                elif item_node.id == '#L':
                    # item_node is left node
                    item_node.parent.left = item_node.right
                    item_node.parent.left.id = '#L'
                else:
                    # item_node is a right node
                    item_node.parent.right = item_node.right
                    item_node.parent.right = '#R'
        # deletion complete
        self.size = self.size - 1
        return deleted_value