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
    def __init__(self, initial_data=None) -> None:
        self.root = node(parent=None, value=None, left=None, right=None, id='')
        self.size = 0
        if isinstance(initial_data, Iterable):
            for item in initial_data:
                self.insert(item)


    def __len__(self):
        return self.size


    def get_node(self, item) -> node:
        current = self.root
        while True:
            if current is None or current.value is None:
                break # because it's not here
            else:
                if item < current.value:
                    # GO LEFT
                    current = current.left
                elif item == current.value:
                    break # found it!
                else:
                    # GO RIGHT
                    current = current.right
        return current


    def insert(self, new_item):
        if self.size == 0:
            self.root.value = new_item
        else:
            # search for the right slot
            current = self.root
            while True:
                if new_item <= current.value:
                    # GO LEFT
                    # there's an equal sign since duplicates are allowed
                    if current.left is None:
                        # the right spot!
                        current.left = node(parent=current, value=new_item, id='#L')
                        break # so that we dont stuck in a loop
                    else:
                        # go left, but even deeper!
                        current = current.left
                else:
                    # GO RIGHT
                    if current.right is None:
                        # the right spot!
                        current.right = node(parent=current, value=new_item, id='#R')
                        break # so that we dont stuck in a loop
                    else:
                        # go right, but even deeper!
                        current = current.right
        # insertion complete!
        self.size += 1 # dont forget to increase the size!!!!!!!!
        return self


    def remove(self, doomed_item):
        deleted_item = None
        if self.size != 0:
            # tree is not empty, so we can remove things
            doomed_item_node = self.get_node(doomed_item)
            if doomed_item_node is not None:
                # now what we want to remove is actually in the tree, so we can remove it
                deleted_item = doomed_item_node.value
                doomed_id = doomed_item_node.id
                L, R = doomed_item_node.left is not None, doomed_item_node.right is not None
                if L and R:
                    # BOTH CHILDREN ARE NOT NONE
                    # search for the largest node in the left subtree
                    # or the smallest node in the right subtree
                    
                    # I'm gonna search for the largest in the left subtree
                    # we go as deep and far right as possible in the left subtree
                    left_largest = doomed_item_node.left
                    while left_largest.right is not None:
                        left_largest = left_largest.right
                    
                    doomed_item_node.value = left_largest.value
                    
                    # left_largest can have a left child, or no children at all, but never a right one
                    
                    # now remove left_largest
                    have_left = left_largest.left is not None
                    if have_left:
                        if left_largest.id == '#L':
                            # this happens only when the left subtree of doomed_node is a single node, namely left_largest
                            left_largest.parent.left =        left_largest.left
                            left_largest.parent.left.parent = left_largest.parent
                        else:
                            left_largest.parent.right =        left_largest.left
                            left_largest.parent.right.parent = left_largest.parent
                            left_largest.parent.right.id =     '#R'
                    else:
                        # NO CHILDREN AT ALL
                        if left_largest.id == '#L':
                            left_largest.parent.left.value = None
                            left_largest.parent.left =       None
                        else:
                            left_largest.parent.right.value = None
                            left_largest.parent.right =       None
                    # we have removed both {doomed_item} and {left_largest}
                    del left_largest
                else:
                    # either LEFT OR RIGHT, but not BOTH
                    successor = doomed_item_node.left if L else doomed_item_node.right
                    if doomed_id == '#L':
                        doomed_item_node.parent.left = successor
                        if doomed_item_node.parent.left is not None:
                            doomed_item_node.parent.left.parent = doomed_item_node.parent
                            doomed_item_node.parent.left.id = '#L'
                    else:
                        doomed_item_node.parent.right = successor
                        if doomed_item_node.parent.right is not None:
                            doomed_item_node.parent.right.parent = doomed_item_node.parent
                            doomed_item_node.parent.right.id = '#R'
                self.size = self.size - 1 # we have effectively removed {doomed_item}
            # end if doomed_item_node is not None:
        # end if self.size != 0
        return deleted_item


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


    def generate_value_view(self) -> List:
        return [n.value for n in self.generate_list_view()]


    def __repr__(self) -> str:
        # return str(self.generate_list_view())
        return ''
# end of class bs_tree

if __name__ == '__main__':
    p = [5, 1, 9, 0, 4, 7, 3, 6, 8, 2]
    t = bs_tree()
    for item in p:
        t.insert(item)
    
    for item in p:
        print(t.generate_list_view(), '\n')
        t.remove(item)