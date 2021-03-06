# A class represeting nodes in out tree
# Each node has 5 attributes:
# parent:
# type: node
# 
# value:
# type: Any
#
# left node:
# type is clear right from name
# 
# right node:
# so does this one
# 
# id:
# a string basically indicating if this node is left node (id='#L')
# or a right node (id='#R')
# default: '', in case this node is the root
# 
# * EXCEPT FOR (id), ALL ATTRIBUTES HAVE (NONE) AS THEIR DEFAULT
#


class node:
    """
    the actual code, documentation above
    """
    
    def __init__(self, parent=None, value=None, left=None, right=None, id='') -> None:
        self.parent: node = parent
        self.value = value
        self.left: node = left
        self.right: node = right
        self.id: str = id
    
    def __repr__(self) -> str:
        p = None if self.parent is None else repr(self.parent.value)
        v = repr(self.value)
        l = None if self.left is None else repr(self.left.value)
        r = None if self.right is None else repr(self.right.value)
        return f'({p})=>({l}, {v}{self.id}, {r})'