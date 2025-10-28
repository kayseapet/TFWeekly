#Unit 7 Session 1, Advanced Problem set Version 1

# -------------------------------------
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next
# -------------------------------------



#Problem 1: Counting the Layers of a Sandwich
### U - Understand 
'''
1. Share 2 questions you would ask to help understand the question:
    1. To clarify, a "list of lists" parameter means each layer is a list seperate from each other, or is the next layer inside the list of the previous one?
    2. Is it possible for two layers to be held in one list? For Example: ["bread", "cheese", [*other layers]]
'''
### P - Plan
'''
2. Write out in plain English what you want to do:
    -First, handle the base cases:
        - if there is no parameter (layers_list is None), return count
        - if there is no next layer (the length of the layer_list is 1), return 1
    - Next, the recursive case:
        - count the layers by the current layer (1) plus the rest of layers in the list at index=1 of the current list
        - return that count 

3. Translate each sub-problem into pseudocode:
    if not sandwich: return 0
    if len(sandwich)==1: return 1
    return 1 + count_layers(sandwich[1])
'''
### I - Implement
'''
4. Translate the pseudocode into Python and share your final answer:
'''
def count_layers(sandwich):
    if not sandwich: return 0
    if len(sandwich)==1: return 1
    return 1 + count_layers(sandwich[1])
#Problem 1 Examples:
print("Problem 1 Output:")            
sandwich1 = ["bread", ["lettuce", ["tomato", ["bread"]]]]
sandwich2 = ["bread", ["cheese", ["ham", ["mustard", ["bread"]]]]]
print(count_layers(sandwich1))
print(count_layers(sandwich2))



#Problem 2: Reversing Deli Orders
### U - Understand 
'''
1. Share 2 questions you would ask to help understand the question:
    1. Does the result need to be returned as a string or a list?
    2. Is recursion the more efficent method for this question compared to just turning the string into a list, reversing it, and then transforming it back to a string?
'''
### P - Plan
'''
2. Write out in plain English what you want to do: 
    - make the string into a list split by the Whitespace
    - Make a recursive helper:(works similar to a stack reversal)
        - base case: if list has one or zero elements: return 
        - recursion: for a list, return a string of the function(list- 1st element) + the 1st element
    - use the recursive helper and given the list made as it's parameter. return that value

3. Translate each sub-problem into pseudocode:
    orders = orders.split()
    def helper(list):
        if not list:
            return ""
        if len(list)==1:
            return list[0]
        return str(helper(list[1:])) + " " + list[0]
    return helper(orders)
'''
### I - Implement
'''
4. Translate the pseudocode into Python and share your final answer:
'''
def reverse_orders(orders):
    orders = orders.split()
    def helper(list):
        if not list:
            return ""
        if len(list)==1:
            return list[0]
        return str(helper(list[1:])) + " " + list[0]
    return helper(orders)
#Problem 2 Examples:
print("Problem 2 Output:")         
print(reverse_orders("Bagel Sandwich Coffee"))



#Problem 3: Sharing the Coffee
### U - Understand 
'''
1. Share 2 questions you would ask to help understand the question:
    1. Should the function decide early if the volumes of coffee is divisable by n, or collect ALL volumes before deciding?
    2.  Is this possible to calculate without a recursive helper?
'''
### P - Plan
'''
2. Write out in plain English what you want to do: 
    - in a recursive helper:given a list
        - base case: length of list is 1
            - return element
        -recursive:
            - return the int of the first element plus function(rest of list)
    - if count = recursive helper (list) % n == 0, return true
    - else return false

3. Translate each sub-problem into pseudocode:
     def helper(list):
        if len(list)==1:
            return list[0]
        return list[0] + helper(list[1:])
    count = helper(coffee)
    if count % n == 0: 
        return True
    else: 
        return False 
'''
### I - Implement
'''
4. Translate the pseudocode into Python and share your final answer:
'''
def can_split_coffee(coffee, n):
    def helper(list):
        if len(list)==1:
            return list[0]
        return list[0] + helper(list[1:])
    count = helper(coffee)
    if count % n == 0: return True
    else: return False 
#Problem 3 Examples:
print("Problem 3 Output:")            # expecting: ( add this line to print statements)
print(can_split_coffee([4, 4, 8], 2))
print(can_split_coffee([5, 10, 15], 4))



#Problem 4: Super Sandwich
### U - Understand 
'''
1. Share 2 questions you would ask to help understand the question:
    1. Can it be assumed that the two parameter are linked lists or None?
    2. What does the function do if one of the lists are empty?
'''
### P - Plan
'''
2. Write out in plain English what you want to do: 
    - edge case: If list1 or list2 doesn't exist
        - return the head of the list that does exist, or None if neither exist
    - in a recursive helper:given two nodes A & B
        - base case: if A OR B is None
            - return
        - recursive: 
            - save a.next temp1
            - set a.next as B
            - recall recursive helper where node A = B and node B = temp 1
    - call the recursive helper
    - return head of list1

3. Translate each sub-problem into pseudocode:
 
'''
### I - Implement
'''
4. Translate the pseudocode into Python and share your final answer:
'''
def merge_orders(sandwich_a, sandwich_b):
    if not sandwich_a or not sandwich_b:
        if sandwich_a: return sandwich_a
        if sandwich_b: return sandwich_b
    
    def merge(a,b):
        if not a or not b:
            return
        temp = a.next
        a.next = b
        merge (b,temp)
    
    merge(sandwich_a, sandwich_b)
    return sandwich_a
        
#Problem 4 Examples :
print("Problem 4 Output: (NOTE: Because linked lists are modified, one example must be #commented for the other to work)")          
sandwich_a = Node('Bacon', Node('Lettuce', Node('Tomato')))
sandwich_b = Node('Turkey', Node('Cheese', Node('Mayo')))
sandwich_c = Node('Bread')
#print_linked_list(merge_orders(sandwich_a, sandwich_b))
print_linked_list(merge_orders(sandwich_a, sandwich_c))



#Problem 6: Ternary Expression
### U - Understand 
'''
1. Share 2 questions you would ask to help understand the question:
    1. How do ternary expressions work?
    2. How will a recursive function keep track of the condition, & true/false choices?
'''
### P - Plan
'''
2. Write out in plain English what you want to do: 
    - save the expression as a reversed list
    - in a recursive helper: I = index in expression list
        - base case: i not index in exp, of exp[i] not T/F: return exp[i]
        -recursion:
            - collect the condition (true/false) at exp i
            - save true exp at helper(i+2)
            - save false exp at helper(i+3)
            - now evaulate expression:
                - if condition is T: return true exp
                - else return false xp
    -return helper(i=0)

3. Translate each sub-problem into pseudocode:
    exp =list(expression)
    def helper(i):
        if i >= len(exp) or (exp[i] != "T" and exp[i] != "F"):
            return exp[i]
        condition = exp[i]
        if exp[i+1] != ':':
            true = helper(i+2)
            false = helper(i+4)
            if condition == 'T': return true
            else: return false
        else: return condition
    return helper(0)
'''
### I - Implement
'''
4. Translate the pseudocode into Python and share your final answer:
'''
def evaluate_ternary_expression_recursive(expression):
    exp =list(expression)
    def helper(i):
        if i >= len(exp) or (exp[i] != "T" and exp[i] != "F"):
            return exp[i]
        condition = exp[i]
        if exp[i+1] != ':':
            true = helper(i+2)
            false = helper(i+4)
            if condition == 'T': return true
            else: return false
        else: return condition
    return helper(0)
#Problem 6 Examples:
print("Problem 6 Output:")            # expecting: ( add this line to print statements)
print(evaluate_ternary_expression_recursive("T?2:3"))
print(evaluate_ternary_expression_recursive("F?1:T?4:5"))
print(evaluate_ternary_expression_recursive("T?T?F:5:3"))
