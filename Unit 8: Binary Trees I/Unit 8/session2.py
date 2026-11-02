from collections import deque 
# Unit 8, Session 2 Version 1

#-----------testing ---------
# Tree Node class
class TreeNode:
    def __init__(self, key, value=None, left=None, right=None):
        if key and value:
            self.key = value      # Plant rarity
            self.val = key     # Plant name
        else:
            self.val = key
            self.key = None
        self.left = left
        self.right = right

# class TreeNode:
#     def __init__(self, value, left=None, right=None):
#         self.val = value
#         self.left = left
#         self.right = right

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

def build_tree(values):
  if not values:
      return None

  def get_key_value(item):
      if isinstance(item, tuple):
          return item[0], item[1]
      else:
          return None, item

  key, value = get_key_value(values[0])
  root = TreeNode(value, key)
  queue = deque([root])
  index = 1

  while queue:
      node = queue.popleft()
      if index < len(values) and values[index] is not None:
          left_key, left_value = get_key_value(values[index])
          node.left = TreeNode(left_value, left_key)
          queue.append(node.left)
      index += 1
      if index < len(values) and values[index] is not None:
          right_key, right_value = get_key_value(values[index])
          node.right = TreeNode(right_value, right_key)
          queue.append(node.right)
      index += 1
  return root
#----------------------------

#Problem 2: Flower Finding
# Why this problem: This problem introduced the format of a Binary search tree, which could be new to some students.
### U - Understand 
'''
1. Share 2 questions you would ask to help understand the question:
    1. so the function is looking to find a value is in the tree?
    2. what if the inventory or name parameter are None?
'''
### P - Plan
'''
2. Write out in plain English what you want to do: 
    - basecase(s): 
        if root is none, return false
        if root is the target flower, return true
    - recursion
        -if target flower is after root (in the alphabet), use function(root.right)
        - else, function(root.left)
3. Translate each sub-problem into pseudocode:
    if inventory is None:
        return False
    if inventory.val == name:
        return True
    #recursion
    if name > inventory.val: 
        return find_flower(inventory.right,name)
    else:
        return find_flower(inventory.left,name)
'''
### I - Implement
'''
4. Translate the pseudocode into Python and share your final answer:
'''
def find_flower(inventory, name):
    if inventory is None:
        return False
    if inventory.val == name:
        return True
    #recursion
    if name > inventory.val: 
        return find_flower(inventory.right,name)
    else:
        return find_flower(inventory.left,name)
# Example usage:
print("Problem 2 Examples:")
"""
         Rose
        /    \
      Lily   Tulip
     /  \       \
  Daisy  Lilac  Violet
"""
# using build_tree() function at top of page
values = ["Rose", "Lily", "Tulip", "Daisy", "Lilac", None, "Violet"]
garden = build_tree(values)
print(find_flower(garden, "Lilac"))  
print(find_flower(garden, "Sunflower")) 
# -------------------------------------------------------------------------------------------------



#Problem 4: Adding a New Plant to the Collection
# Why this problem: This problem is about knowing where to add a new node to a list, and how to traverse to that spot for the node to be added.
### U - Understand 
'''
1. Share 2 questions you would ask to help understand the question:
    1. Given it's a BST, how do I compare letters as "greater than" or "less than"?
    2. Is the comparsion only for the first letter, or for every letter?
'''
### P - Plan
'''
2. Write out in plain English what you want to do:
    - a recursive function that returns the head node of an altered tree:
        base case: if node is none, return new plant node
        recursion: 
            - if node.val <= name: 
                node.right = function(node.right, name)
            - else: 
                node.left = function(node.left, name
            return node
3. Translate each sub-problem into pseudocode:
    if collection is None: return TreeNode(name)
    if collection.val <= name: 
        collection.right = add_plant(collection.right, name)
    else: 
        collection.left = add_plant(collection.left,name)
    return collection
'''
### I - Implement
'''
4. Translate the pseudocode into Python and share your final answer:
'''
def add_plant(collection, name):
    if collection is None: return TreeNode(name)
    if collection.val <= name: 
        collection.right = add_plant(collection.right, name)
    else: 
        collection.left = add_plant(collection.left,name)
    return collection
# Example usage:
print("Problem 4 Examples:")
"""
            Money Tree
        /              \
Fiddle Leaf Fig    Snake Plant
"""
# Using build_tree() function at the top of page
values = ["Money Tree", "Fiddle Leaf Fig", "Snake Plant"]
collection = build_tree(values)
# Using print_tree() function at the top of page
print_tree(add_plant(collection, "Aloe"))
# -------------------------------------------------------------------------------------------------




#Problem 5: Sorting Plants by Rarity
# Why this problem: This could be hard for students to know how to traversal a tree of all nodes, AND return sort them in a list based on the node's key.
### U - Understand 
'''
1. Share 2 questions you would ask to help understand the question:
    1. so the return value is a list of tuples?
    2. the end result should have the int value in each tuple be in order?
'''
### P - Plan
'''
2. Write out in plain English what you want to do: 
    - inorder traversal: left tree, root, right tree
      create an empty list
      - in a recursive helper:
        - basecase: if node is none, return
        - recursion:
            - recursive function with root.left
            - add root to list
            - recursive function with root.right
      - return list
3. Translate each sub-problem into pseudocode:
    list = []
        def helper(node):
            if node is None:return
            helper(node.left)
            list.append(node)
            helper(node.right)
        helper(collection)
        return list
'''
### I - Implement
'''
4. Translate the pseudocode into Python and share your final answer:
'''
def sort_plants(collection):
    lst = []
    def helper(node):
        if node is None:return
        helper(node.left)
        lst.append((node.key,node.val))
        helper(node.right)
    helper(collection)
    return lst
# Example usage:
print("Problem 5 Examples:")
"""
         (3, "Monstera")
        /               \
   (1, "Pothos")     (5, "Witchcraft Orchid")
        \                 /
  (2, "Spider Plant")   (4, "Hoya Motoskei")
"""
# Using build_tree() function at the top of page
values = [(3, "Monstera"), (1, "Pothos"), (5, "Witchcraft Orchid"), None, (2, "Spider Plant"), (4, "Hoya Motoskei")]
collection = build_tree(values)
print(sort_plants(collection))
# -------------------------------------------------------------------------------------------------
