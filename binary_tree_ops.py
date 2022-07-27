"""
This file will contain all things I find related to 
Binary Trees. First, the classification of TreeNode
is described and then the various functions will be
designed
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

"""
Binary Tree Right Side View - Recursive Solution

Given the root of a binary tree, return a list of values
for the furthest-right node in a level
"""

def rightSideView(root: TreeNode) -> list[int]:
    result = []        
    _rightSideView(root, 0, result)
    return result

def _rightSideView(root: TreeNode, current_level, result: list[int]) -> None:
    # Base case
    if root is None:
        return
    
    # if this is the last TreeNode of its level
    if current_level == len(result):
        result.append(root.val)
    
    # recurse for right subtree first, then left subtree
    _rightSideView(root.right, current_level+1, result)
    _rightSideView(root.left, current_level+1, result)

"""
Binary Tree Left Side View - using Queue

Given the root of a binary tree, return a list of values
for the furthest-right node in a level
"""
def leftSideView(root: TreeNode) -> list[int]:
    result = []
    _leftSideView(root, result)
    return result

def _leftSideView(root: TreeNode, result: list[int]) -> None:
    if not root:
        return

    q = []
    q.append(root)

    while len(q):
        nodes_at_level = len(q)

        # traverse all nodes of current level
        for i in range(1, nodes_at_level+1):
            temp = q[0]
            q.pop(0)

            # add leftmost element at current level
            if i == 1:
                result.append(temp.val)

            # add left node to queue
            if (temp.left):
                q.append(temp.left)

            # add right node to queue
            if (temp.right):
                q.append(temp.right)

root = TreeNode(4)
root.left = TreeNode(5)
root.right = TreeNode(2)
root.right.right = TreeNode(1)
root.right.left = TreeNode(3)
root.right.left.right = TreeNode(7)
root.right.left.left = TreeNode(6)

print(rightSideView(root))
print(leftSideView(root))