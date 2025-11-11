# Unit 9, Session 2: Standard Set Version 1
#-----------------------------------
# For testing
from collections import deque 

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

#Problem 1: Balanced Baked Goods Display
### U - Understand 
'''
1. Share 2 questions you would ask to help understand the question:
    1. What is a balanced tree?
    2. is it for all subtrees?
'''
### P - Plan
'''
2. Write out in plain English what you want to do:
    Doing a recursive DFS to check height
    -  base case: if root is none: return True
    - recursion:
        - left = function(left subtree)
        - right = function(right sub)
        return absolute( left - right) <= 1

3. Translate each sub-problem into pseudocode:
     if display is None: return True
    left =  height(display.left)
    right = height(display.right)
    if abs(left- right )> 1: return False
    return is_balanced(display.left) and is_balanced(display.right)
'''
### I - Implement
'''
4. Translate the pseudocode into Python and share your final answer:
'''
def height(root):
    if not root: return 0
    return 1 + max(height(root.left),height(root.right))
def is_balanced(display):
    if display is None: return True
    left =  height(display.left)
    right = height(display.right)
    if abs(left- right )> 1: return False
    return is_balanced(display.left) and is_balanced(display.right)
#Problem 1 Examples:
print("Problem 1 Output:")            # expecting: ( add this line to print statements)
"""
      🎂
     /  \
   🥮   🍩
       /  \  
     🥖    🧁

"""
# Using build_tree() function included at top of page
baked_goods = ["🎂", "🥮", "🍩", None, None, "🥖", "🧁"] 
display1 = build_tree(baked_goods)

"""
          🥖
         /  \
       🧁    🧁
       /       \  
      🍪       🍪
     /           \
    🥐           🥐  

"""
baked_goods = ["🥖", "🧁", "🧁", "🍪", None, None, "🍪", "🥐", None, None, "🥐"]
display2 = build_tree(baked_goods)
print(is_balanced(display1)) 
print(is_balanced(display2))  





#Problem 2: Sum of Cookies Sold Each Day
### U - Understand 
'''
1. Share 2 questions you would ask to help understand the question:
    1. how do we know which number of cookies was ordered on which day?
    2. are we returning or printing a value?
'''
### P - Plan
'''
2. Write out in plain English what you want to do: 
    BFS summation:
        - create seen list, add root
        - create sums list
        While seen isnt NOne:
            new sum = 0
            - for the length of seen:
                pop an element, add children to seen
                add value to new sum
            - append new sum to sums list
        -return sums list
3. Translate each sub-problem into pseudocode:
    seen = []
    seen.append(orders)
    sums = []
    while seen:
        sum = 0
        for x in range(len(seen)):
            node = seen.pop(0)
            sum += node.val
            if node.left: seen.append(node.left)
            if node.right: seen.append(node.right)
        sums.append(sum)
    return sums
'''
### I - Implement
'''
4. Translate the pseudocode into Python and share your final answer:
'''
def sum_each_days_orders(orders):
    seen = []
    seen.append(orders)
    sums = []
    while seen:
        sum = 0
        for x in range(len(seen)):
            node = seen.pop(0)
            sum += node.val
            if node.left: seen.append(node.left)
            if node.right: seen.append(node.right)
        sums.append(sum)
    return sums
#Problem 2 Examples:
print("Problem 2 Output:")            # expecting: ( add this line to print statements)
"""
      4
     / \
    2   6
   / \  
  1   3
"""
# Using build_tree() function included at top of page
order_sizes = [4, 2, 6, 1, 3]
orders = build_tree(order_sizes)
print(sum_each_days_orders(orders))




#Problem 3: Sweetness Difference
### U - Understand 
'''
1. Share 2 questions you would ask to help understand the question:
    1. how can we calculate the absolute differences?
    2. is the row the level on the binary tree?
'''
### P - Plan
'''
2. Write out in plain English what you want to do: 
    BFS, max & min comparsion:
    - create seen list, add root
    - create diffs list
    while seen:
        - max val: negative infinity
        - min val: infintiy
        for length of seen:
            - pop element from seen, add its children
            - if node.val is >max or <min, update max/min
        append max - min to diffs list
    return diffs list

3. Translate each sub-problem into pseudocode:
 
'''
### I - Implement
'''
4. Translate the pseudocode into Python and share your final answer:
'''
def sweet_difference(chocolates):
    seen = []
    seen.append(chocolates)
    diffs = []
    while seen:
        max, min = float('-inf'),float('inf')
        for x in range(len(seen)):
            node = seen.pop(0)
            if node.left: seen.append(node.left)
            if node.right: seen.append(node.right)
            if node.val > max: max = node.val
            if node.val < min: min = node.val
        diffs.append(max-min)
    return diffs
            
#Problem 3 Examples:
print("Problem 3 Output:")            # expecting: ( add this line to print statements)
"""
  3
 / \
9  20
   / \
  15  7
"""
# Using build_tree() function included at top of page
sweetness_levels1 = [3, 9, 20, None, None, 15, 7]
chocolate_box1 = build_tree(sweetness_levels1)
"""
    1
   / \
  2   3
 / \   \
4   5   6

"""
sweetness_levels2 = [1, 2, 3, 4, 5, None, 6]
chocolate_box2 = build_tree(sweetness_levels2)
print(sweet_difference(chocolate_box1))  
print(sweet_difference(chocolate_box2))  




#Problem 4: Transformable Bakery Orders
### U - Understand 
'''
1. Share 2 questions you would ask to help understand the question:
    1. What are the conditions in which we return false? (edge cases?)
    2. is the number of swaps unlimited?
'''
### P - Plan
'''
2. Write out in plain English what you want to do: 
    - base case(s): 
        - both node1 & node2 are NOne: return true
        - if node1 or node2 is none(only one): return false
        - node1 != node2: return false
    -recursion:
        - nonswap = function( comparing lefts) and function( comparing rights)
        - swap = fucntion(node1.right, node2.left ) and (vice versa)
        - return swap or nonswap. if one is true, itll return true

3. Translate each sub-problem into pseudocode:
 
'''
### I - Implement
'''
4. Translate the pseudocode into Python and share your final answer:
'''
def can_rearrange_orders(order1, order2):
    if not order1 and not order2: return True
    if not order1 or not order2: return False
    if order1.val != order2.val: return False
    nonswap = can_rearrange_orders(order1.left, order2.left) and can_rearrange_orders(order1.right, order2.right)
    swap = can_rearrange_orders(order1.left, order2.right) and can_rearrange_orders(order1.right, order2.left)
    return swap or nonswap
#Problem X Examples:
print("Problem X Output:")            # expecting: ( add this line to print statements)
"""
              Red Velvet                             Red Velvet
             /          \                           /           \
        Vanilla         Lemon                   Lemon            Vanilla
        /      \        /   \                  /     \           /      \
      Ube    Almond  Chai   Carrot       Carrot      Chai    Almond    Ube 
                     /   \        \       /          /   \      
                 Chai   Maple   Smore   Smore    Maple   Chai
"""

# Using build_tree() function included at top of page
flavors1 = ["Red Velvet", "Vanilla", "Lemon", "Ube", "Almond", "Chai", "Carrot", 
            None, None, None, None, "Chai", "Maple", None, "Smore"]
flavors2 = ["Red Velvet", "Lemon", "Vanilla", "Carrot", "Chai", "Almond", "Ube", "Smore", None, "Maple", "Chai"]
order1 = build_tree(flavors1)
order2 = build_tree(flavors2)
print(can_rearrange_orders(order1, order2))




#Problem 5: Larger Order Tree
### U - Understand 
'''
1. Share 2 questions you would ask to help understand the question:
    1. so, for each node, we have to find the sum of all node greater & have that be the node value?
    2. how do we know what nodes exist that are greater than the current node?
'''
### P - Plan
'''
2. Write out in plain English what you want to do: 
    - recursive tree alteration:
        in a helper function, that accepts a "sum" as a parameter:
            - base cases: if node is none, return sum
               
            -recursion: 
                sum = current node value + fucntion(right tree)
                set node value to new sum
                return function of left tree

3. Translate each sub-problem into pseudocode:
 
'''
### I - Implement
'''
4. Translate the pseudocode into Python and share your final answer:
'''
def larger_order_tree(orders):
    def helper(node,sum):
        if not node: return sum
        sum = node.val + helper(node.right, sum)
        node.val = sum
        return helper(node.left,sum)
    helper(orders, 0)
    return orders
#Problem 5 Examples:
print("Problem 5 Output:")            # expecting: ( add this line to print statements)
"""
         4
       /   \
      /     \
     1       6
    / \     / \
   0   2   5   7
        \       \
         3       8   
"""
# using build_tree() function included at top of page
order_sizes = [4,1,6,0,2,5,7,None,None,None,3,None,None,None,8]
orders = build_tree(order_sizes)

# using print_tree() function included at top of page
print_tree(larger_order_tree(orders))


