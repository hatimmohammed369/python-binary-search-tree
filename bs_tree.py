from typing import Iterable, List
from tree_node import node


# class bs_tree (binary search tree)
#   duplicates are allowed
#
# attributes:
#   root, size, get_node, insert, remove, generate_list_view
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
#
# generate_list_view:
#   method
#   returns list containing all nodes in tree


class bs_tree:
    def __init__(self, init=None) -> None:
        self.root = node(parent=None, value=None, left=None, right=None, id='')
        self.size = 0
        if isinstance(init, Iterable):
            for item in init:
                self.insert(item)


    def __len__(self):
        return self.size


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
            L, R = item_node.left is not None, item_node.right is not None
            if L and R:
                # search for the largest node in the left subtree
                # or the smallest node in the right subtree
                
                # I will search for the largest node in the left subtree
                left_largest = item_node.left
                while left_largest.right is not None:
                    left_largest = left_largest.right
                
                item_node.value = left_largest.value
                
                # remove left_largest
                leftL, leftR = left_largest.left is not None, left_largest.right is not None
                # since left_largest is the largest node if the left subtree
                # it must be as deep as possible and as far right as possible
                # so left_largest.id='#R'
                if leftL and not leftR:
                    # left_largest has a left node but no right node
                    left_largest.parent.right = left_largest.left
                    left_largest.parent.right.id = '#R'
                elif not leftR and leftR:
                    # left_largest has no left node but a right node
                    left_largest.parent.right = left_largest.left
                    left_largest.parent.right.id = '#R'
                else:
                    # no children, just delete
                    left_largest.parent.right.value = None
                    left_largest.parent.right = None
                pass
            elif L:
                pass
            else:
                # just R
                pass
            pass
        # deletion complete
        self.size = self.size - 1
        return deleted_value
    
    
    def generate_list_view(self) -> List[node]:
        ls: List[node] = []
        begin, end = 0, 1
        while len(ls) < self.size:
            if len(ls) == 0:
                ls.append(self.root)
            else:
                old_length = len(ls)
                for n in ls[begin:end]:
                    child_left = n.left
                    if child_left is not None:
                        ls.append(child_left)
                    
                    child_right = n.right
                    if child_right is not None:
                        ls.append(child_right)
                begin, end = old_length, len(ls)
        return ls
    
    
    def __repr__(self) -> str:
        return str(self.generate_list_view())
# end of class bs_tree

if __name__ == '__main__':
    p = [6, 0, 7, 5, 1, 4, 8, 9, 3, 2]
    t = bs_tree()
    for item in p:
        t.insert(item)
    print(t.generate_list_view())