"""
Given the root to a binary tree, implement serialize(root), 
which serializes the tree into a string, and deserialize(s), 
which deserializes the string back into the tree.

For example, given the following Node class

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
The following test should pass:

node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'
"""

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

node = Node('root', Node('left', Node('left.left')), Node('right'))

def serialize(node: Node, treeString="") -> str:
    treeString = node.val
    if (node.left != None):
        treeString = treeString + "," + serialize(node.left)
    if (node.right != None):
        treeString = treeString + "," + serialize(node.right)
    return treeString


def buildNode(childs: [str]) -> Node:
    rights = [string for string in childs if string.startswith("right")]
    lefts = [string for string in childs if string.startswith("left")]
    if(len(childs) > 0):
        return Node(childs[0], buildNode(childs[1:]))
    else:
        return None


def deserialize(nodeString: str) -> Node:
    nodeList = nodeString.split(",")
    rights = [string for string in nodeList[1:] if string.startswith("right")]
    lefts = [string for string in nodeList[1:] if string.startswith("left")]
    #nodes = [node.split(".") for node in nodeList]
    root = Node(nodeList[0], buildNode(lefts), buildNode(rights))
    return root
    
def depugNode(node: Node):
    print(node.val)
    if (node.left != None):
        depugNode(node.left)
    if (node.right != None):
        depugNode(node.right)


node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'