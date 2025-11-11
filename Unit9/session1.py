# Unit 9, Session 1: Standard Set Version 1

#-----------------------------------
# For testing
from collections import deque 


class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

class Puff():
     def __init__(self, flavor, left=None, right=None):
        self.val = flavor
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
#-----------------------------------

#Problem 1: Merging Cookie Orders
### U - Understand 
'''
1. Share 2 questions you would ask to help understand the question:
    1. How are orders merging?
    2. What about if one of the node orders dont exist?
'''
### P - Plan
'''
2. Write out in plain English what you want to do: 
    - recursion: merge 
        - base case: if order1 or order 2 is None, return the existing node
        - recursion:
            create node with order1 + order2
            set its left subtree and right subtree
            return new node
3. Translate each sub-problem into pseudocode:
    if not order1 or not order2:
        if order1: return order1
        else: return order2
    new = TreeNode(order1.val+order2.val)
    new.right = merge_orders(order1.right, order2.right)
    new.left = merge_orders(order1.left,order2.left)
    return new
'''
### I - Implement
'''
4. Translate the pseudocode into Python and share your final answer:
'''
def merge_orders(order1,order2):
    if not order1 or not order2:
        if order1: return order1
        else: return order2
    new = TreeNode(order1.val+order2.val)
    new.right = merge_orders(order1.right, order2.right)
    new.left = merge_orders(order1.left,order2.left)
    return new
#Problem 1 Examples:
print("Problem 1 Output:")           
"""
     1             2         
    /  \         /   \       
   3    2       1     3   
 /               \      \   
5                 4      7   
"""
# Using build_tree() function included at top of page
cookies1 = [1, 3, 2, 5]
cookies2 = [2, 1, 3, None, 4, None, 7]
order1 = build_tree(cookies1)
order2 = build_tree(cookies2)
# Using print_tree() function included at top of page
print_tree(merge_orders(order1, order2))





#Problem 2: Croquembouche
### U - Understand 
'''
1. Share 2 questions you would ask to help understand the question:
    1. does the order have to be from left to right?
    2. does the order have to be from top level to bottom level?
'''
### P - Plan
'''
2. Write out in plain English what you want to do: 
    a Breadth First Search:
    - create new list, seen
    - create new list, final
    add root to seen
    while seen is not empty:
        - take the first element & add its children to seen
        - add name to final list
    - PRINT final
3. Translate each sub-problem into pseudocode:
    seen = []
    final = []
    seen.append(design)
    while seen:
        node = seen.pop(0)
        if node.left:seen.append(node.left)
        if node.right:seen.append(node.right)
        final.append(node.val)
    print(final)
'''
### I - Implement
'''
4. Translate the pseudocode into Python and share your final answer:
'''
def print_design(design):
    seen = []
    final = []
    seen.append(design)
    while seen:
        node = seen.pop(0)
        if node.left:seen.append(node.left)
        if node.right:seen.append(node.right)
        final.append(node.val)
    print(final)
#Problem 2 Examples:
print("Problem 2 Output:")            # expecting: ( add this line to print statements)

"""
            Vanilla
           /       \
      Chocolate   Strawberry
      /     \
  Vanilla   Matcha  
"""
croquembouche = Puff("Vanilla", 
                    Puff("Chocolate", Puff("Vanilla"), Puff("Matcha")), 
                    Puff("Strawberry"))
print_design(croquembouche)




#Problem 3: Maximum Tiers in Cake 
### U - Understand 
'''
1. Share 2 questions you would ask to help understand the question:
    1. what is defined as a "section" of the cake?
    2. so in other words, return the height of the tree?
'''
### P - Plan
'''
2. Write out in plain English what you want to do: 
    In a recursive function:
    - base: if root is none return 0
    - recursion:
        find max height in left subtree
        find max height in right subtree
        - if left > right: return 1 + left
            else, return 1 + right

3. Translate each sub-problem into pseudocode:
    if not cake: return 0
    left = max_tiers(cake.left)
    right = max_tiers(cake.right)
    if left > right: return 1 + left
    else: return 1 + right
'''
### I - Implement
'''
4. Translate the pseudocode into Python and share your final answer:
'''
def max_tiers(cake):
    if not cake: return 0
    left = max_tiers(cake.left)
    right = max_tiers(cake.right)
    if left > right: return 1 + left
    else: return 1 + right
#Problem 3 Examples:
print("Problem 3 Output:")            # expecting: ( add this line to print statements)
"""
        Chocolate
        /        \
    Vanilla    Strawberry
                /     \
         Chocolate    Coffee
"""
# Using build_tree() function included at top of page
cake_sections = ["Chocolate", "Vanilla", "Strawberry", None, None, "Chocolate", "Coffee"]
cake = build_tree(cake_sections)
print(max_tiers(cake))




#Problem 4: Maximum Tiers in Cake II
### U - Understand 
'''
1. Share 2 questions you would ask to help understand the question:
    1. how can I use BFS for this problem?
    2. Whats the difference between BFS & DFS?
'''
### P - Plan
'''
2. Write out in plain English what you want to do: 
    - new list, seen
    - counter, height
    - add root to seen
    while seen:
        - for length of seen:
             - pop first from seen 
             - add its children to seen
        add 1 to height
3. Translate each sub-problem into pseudocode:
    seen = []
    height = 0
    seen.append(cake)
    while seen:
        for x in range(len(seen)):
            node = seen.pop(0)
            if node.left: seen.append(node.left)
            if node.right: seen.append(node.right)
        height += 1
    return height
'''
### I - Implement
'''
4. Translate the pseudocode into Python and share your final answer:
'''
def max_tiersBFS(cake):
    seen = []
    height = 0
    seen.append(cake)
    while seen:
        for x in range(len(seen)):
            node = seen.pop(0)
            if node.left: seen.append(node.left)
            if node.right: seen.append(node.right)
        height += 1
    return height
#Problem 4 Examples:
print("Problem 4 Output:")            # expecting: ( add this line to print statements)
"""
        Chocolate
        /        \
    Vanilla    Strawberry
                /     \
         Chocolate    Coffee
"""
# Using build_tree() function included at top of page
cake_sections = ["Chocolate", "Vanilla", "Strawberry", None, None, "Chocolate", "Coffee"]
cake = build_tree(cake_sections)
print(max_tiersBFS(cake))




#Problem 5: Can Fulfill Order
### U - Understand 
'''
1. Share 2 questions you would ask to help understand the question:
    1. can it be the sum of any path of nodes?
    2. Is the tree a BST?
'''
### P - Plan
'''
2. Write out in plain English what you want to do: 
    - in a recursive helper that accepts the current count,
        base case: if root is None: return False
                    if root is a leaf: 
                        - if root.val + count = target, return true
                        - else, return false
        recursive:
            - add root.val to count
            return helper(root.left) OR helper(root.right)
    - then call the helper
3. Translate each sub-problem into pseudocode:
    def helper(root,count):
        if not root: return False
        if not root.right and not root.left:
            if root.val + count == order_size:
                return True
            else: return False
        count += root.val
        return helper(root.left,count) or helper(root.right,count)
    return helper(inventory,0)
'''
### I - Implement
'''
4. Translate the pseudocode into Python and share your final answer:
'''
def can_fulfill_order(inventory, order_size):
    def helper(root,count):
        if not root: return False
        if not root.right and not root.left:
            if root.val + count == order_size:
                return True
            else: return False
        count += root.val
        return helper(root.left,count) or helper(root.right,count)
    return helper(inventory,0)
#Problem 5 Examples:
print("Problem 5 Output:")            # expecting: ( add this line to print statements)
"""
             5
           /   \
          4     8
        /      /  \
       11     13   4
      /  \          \
     7   2           1   
"""
# Using build_tree() function included at top of the page
quantities = [5,4,8,11,None,13,4,7,2,None,None,None,1]
baked_goods = build_tree(quantities)
print(can_fulfill_order(baked_goods, 22))
print(can_fulfill_order(baked_goods, 2))
