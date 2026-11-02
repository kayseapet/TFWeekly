from collections import deque 
# Unit 8, Session 1 Version 1

# ------------------------------------
# Tree Node class
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def print_tree(root):
    if not root:
        return "Empty"
    result = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    while result and result[-1] is None:
        result.pop()
    print(result)
# -------------------------------------

#Problem 3: Ivy Cutting
# Why this problem: Students may have a challange figuring out how to keep track of the right nodes in a list when doing the function recursively.
### U - Understand 
'''
1. Share 2 questions you would ask to help understand the question:
    1. What does the function do in the event the root is none?
    2. what is the return value? 
'''
### P - Plan
'''
2. Write out in plain English what you want to do: 
    - create an empty list
    - in a recrusive helper:
        -base case: if root is none: return
        -recursion:
            - append root.value to list
            - function(root.right)
    - return list
3. Translate each sub-problem into pseudocode:
    list = []
    def helper(root):
        if root is None:
            return
        list.append(root.value)
        helper(root.right)
'''
### I - Implement
'''
4. Translate the pseudocode into Python and share your final answer:
'''
def right_vine(root):
    lis = []
    def helper(node):
        if node is None:
            return
        lis.append(node.val)
        helper(node.right)
    helper(root)
    return lis
# Example usage:
print("Problem 3 Examples:")
"""
        Root
      /      \
    Node1    Node2
  /         /    \
Leaf1    Leaf2  Leaf3
"""
ivy1 = TreeNode("Root", 
                TreeNode("Node1", TreeNode("Leaf1")),
                TreeNode("Node2", TreeNode("Leaf2"), TreeNode("Leaf3")))
"""
      Root
      /  
    Node1
    /
  Leaf1  
"""
ivy2 = TreeNode("Root", TreeNode("Node1", TreeNode("Leaf1")))
print(right_vine(ivy1))
print(right_vine(ivy2))
# -------------------------------------------------------------------------------------------------

#Problem 4: Ivy Cutting II
# Why this problem: This could be easier for the students who aren't great with recursion, but students who have gotten used to recursion may have an issue.
### U - Understand 
'''
1. Share 2 questions you would ask to help understand the question:
    1. What would be the time complexity or the iterative function?
    2. Can you traverse a binary tree using a for loop,  or should it always be a while loop?

'''
### P - Plan
'''
2. Write out in plain English what you want to do: 
    - create an empty list
    - create pointer 'node' that starts at root
    - in a while loop: node isnt None
        - append node value
        - node = node.right
    - return list

3. Translate each sub-problem into pseudocode:
    list = []
    node = root
    while node:
        list.append(node.val)
        node = node.right
    return list
'''
### I - Implement
'''
4. Translate the pseudocode into Python and share your final answer:
'''
def right_vine_iterative(root):
    lst = []
    node = root
    while node:
        lst.append(node.val)
        node = node.right
    return lst
# Example usage:
print("Problem 4 Examples:")
print(right_vine_iterative(ivy1))
print(right_vine_iterative(ivy2))
# -------------------------------------------------------------------------------------------------



#Problem 5: Count the Tree Leaves
# Why this problem: This is a full list traversal, and may be challenging for students new to tree traversal.
### U - Understand 
'''
1. Share 2 questions you would ask to help understand the question:
    1. are we looking in a specific subtree, or the entire tree?
    2. what's a way I could do it iteratively, and is it more efficient?
'''
### P - Plan
'''
2. Write out in plain English what you want to do: 
    - base case: if node has no children, return 1
    - recursion:
        - return function(node.left) + function(node.right)

3. Translate each sub-problem into pseudocode:
    if root is None: return 0
    if root.left is None and root.right is None:return 1
    return function(root.left) + function(root.right)
'''
### I - Implement
'''
4. Translate the pseudocode into Python and share your final answer:
'''
def count_leaves(root):
    #base case(s)
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return 1
    #recursion
    return count_leaves(root.left) + count_leaves(root.right)
# Example usage:
print("Problem 5 Examples:")
"""
        Root
      /      \
    Node1    Node2
  /         /    \
Leaf1    Leaf2  Leaf3
"""

oak1 = TreeNode("Root", 
                TreeNode("Node1", TreeNode("Leaf1")),
                TreeNode("Node2", TreeNode("Leaf2"), TreeNode("Leaf3")))

"""
      Root
      /  
    Node1
    /
  Leaf1  
"""
oak2 = TreeNode("Root", TreeNode("Node1", TreeNode("Leaf1")))
print(count_leaves(oak1))
print(count_leaves(oak2))
# -------------------------------------------------------------------------------------------------
