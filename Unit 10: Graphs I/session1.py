from collections import deque 
# Standard Version 1.

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



#Problem 1: Grafting Apples
### U - Understand 
'''
1. Share 2 questions you would ask to help understand the question:
    1. So are we making a function, or just coding it directly?
    2. how does evaluating the printtree Output work? is this output an in-order traversal, or level by level from left to right?
'''
### P - Plan
'''
2. Write out in plain English what you want to do: 
    - Write the left-tree:
        - Mcintosh(Fuji,Opal)
    - Write the right-tree:
        - GrannySmith(Crab,Gala)

3. Translate each sub-problem into pseudocode:
    Trunk.left = Node(Mcintosh,Node(Fuji),Node(Opal))
    Trunk.right = Node(Granny Smith, Node(Crab), Node(Gala))
'''
### I - Implement
'''
4. Translate the pseudocode into Python and share your final answer:
'''
root = TreeNode("Trunk")
root.left = TreeNode("Mcintosh",TreeNode("Fuji"), TreeNode("Opal"))
root.right = TreeNode("Granny Smith", TreeNode("Crab"), TreeNode("Gala"))
# Example usage:
print("Problem 1 Examples:")
# Using print_tree() included at the top of this page
print_tree(root)



#Problem 2: Calculating Yield
### U - Understand 
'''
1. Share 2 questions you would ask to help understand the question:
    1. Is it guaranteed that every non-int node will have two children?
    2. Is it possible for the node value to something other than an int or operator?
'''
### P - Plan
'''
2. Write out in plain English what you want to do: 
    - Writing a recursive function:
        - basecase: if node.value isnt an operator, return value
        - recursion:
            - where x = each operator value, write each recursion:
            - if node.value is x, 
                return function(node.left) x function(node.right)
            
3. Translate each sub-problem into pseudocode:
    if node.value is not {operator values}:
        - return node.value
    if node.value is {operator}:
        return function(node.left) {operator} function(node.right)
'''
### I - Implement
'''
4. Translate the pseudocode into Python and share your final answer:
'''
def calculate_yield(root):
    #base case
    if root.val not in {"*","-","+","/"}:
        return root.val  
    #recursion
    if root.val == "+":
        return calculate_yield(root.left) + calculate_yield(root.right)
    if root.val == "-":
        return calculate_yield(root.left) - calculate_yield(root.right)
    if root.val == "*":
        return calculate_yield(root.left) * calculate_yield(root.right)
    if root.val == "/":
        return calculate_yield(root.left) / calculate_yield(root.right)
# Example usage:
print("Problem 2 Examples:")
"""
    +
  /   \
 7     5
"""
apple_tree = TreeNode("+", TreeNode(7), TreeNode(5))
print(calculate_yield(apple_tree))



#Problem 3: Ivy Cutting
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


#Problem 4: Ivy Cutting II
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



#Problem 5: Count the Tree Leaves
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
print("Problem X Examples:")
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