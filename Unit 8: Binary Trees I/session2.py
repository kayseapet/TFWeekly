from collections import deque 
# Standard Problems Version 1

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


#Problem 1: Monstera Madness
### U - Understand 
'''
1. Share 2 questions you would ask to help understand the question:
    1. does each node represent a leaf, or only nodes without children?
    2. To clarify, is the return the number of splits or number of nodes?
'''
### P - Plan
'''
2. Write out in plain English what you want to do: 
    - base cases: 
        - if root's none, return 0
        - if leaf, return 1 if node value is odd
    - Recursion:
        - return function(node.left) + function(node.right)

3. Translate each sub-problem into pseudocode:
    if root is None: return 0
    if root.left is None and root.right is None:
        if root.value%2 == 1: return 1
        else: return 0
    return function(root.left) + function(root.right)
'''
### I - Implement
'''
4. Translate the pseudocode into Python and share your final answer:
'''
def count_odd_splits(root):
    if root is None: return 0
    if root.left is None and root.right is None:
        if root.val % 2 == 1: return 1
        else: return 0
    if root.val % 2 == 1:
        return 1 + count_odd_splits(root.left) + count_odd_splits(root.right)
    else:
        return count_odd_splits(root.left) + count_odd_splits(root.right)
# Example usage:
print("Problem 1 Examples:")
"""
      2
     / \
    /   \
   3     5
  / \     \
 6   7     12
"""

# Using build_tree() function included at top of page
values = [2, 3, 5, 6, 7, None, 12]
monstera = build_tree(values)
print(count_odd_splits(monstera))
print(count_odd_splits(None))



#Problem 2: Flower Finding
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



#Problem 4: Adding a New Plant to the Collection
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




#Problem 5: Sorting Plants by Rarity
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
        basecase: if node is none, return
        recursion:
            function(node.left)
            list.append(root)
            function(node.right)
      return list

3. Translate each sub-problem into pseudocode:

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


# Advanced Problem Version 1:
#Problem 4: Remove Plant
### U - Understand 
'''
1. Share 2 questions you would ask to help understand the question:
    1. If node is the one we want deleted and it has two children, what happens to node.left's children when node.right must go under it?
    2. What is a cohesive way to solve this iteratively?
'''
### P - Plan
'''
2. Write out in plain English what you want to do:
    -basecase: if node is none, return None
    - traverse the tree based on where the wanted name should be (left or right)
    - when we find the node we want to delete:
     - if node.right exists: set node to node.right & new node.left to previous node.left
     - if node.left exists: set node to node.left
      - else (neither exist): set node to none

3. Translate each sub-problem into pseudocode:
     if collection is None: return None
    if collection.val == name:
        if collection.left:
            collection.left.right = collection.right
            return collection.left
        if collection.right: 
            return collection.right
        else:
            return None
    else:
        if collection.val < name:
            collection.right = remove_plant(collection.right, name)
            return collection
        else: 
            collection.left = remove_plant(collection.left, name)
            return collection
'''
### I - Implement
'''
4. Translate the pseudocode into Python and share your final answer:
'''
def remove_plant(collection, name):
    if collection is None: return None
    if collection.val == name:
        if collection.left:
            collection.left.right = collection.right
            return collection.left
        if collection.right: 
            return collection.right
        else:
            return None
    else:
        if collection.val < name:
            collection.right = remove_plant(collection.right, name)
            return collection
        else: 
            collection.left = remove_plant(collection.left, name)
            return collection

# Example usage:
print("Problem 4 Examples: (Advance)")
"""
              Money Tree
             /         \
           Hoya        Pilea
              \        /   \
             Ivy    Orchid  ZZ Plant
"""
# Using build_tree() function at the top of page
values = ["Money Tree", "Hoya", "Pilea", None, "Ivy", "Orchid", "ZZ Plant"]
collection = build_tree(values)
# Using print_tree() function at the top of page
print_tree(remove_plant(collection, "Pilea"))