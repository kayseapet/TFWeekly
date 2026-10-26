# Unit 7, Session 2 version 1

# Problem 4: Calculating Groot's Growth
# Why this problem:This problem is another recursive one, which students can really struggle with when then they don't understand how to trace through the process of a call stack.
### U - Understand 
'''
1. Share 2 questions you would ask to help understand the question:
    1. can n be negative?
    2. what would the output be if n were a negative number?
'''
### P - Plan
'''
2. Write out in plain English what you want to do: MEMOIZATION LOOK UP
    - main funtion: for memoization
        - make a dict, for saving the fibonacci results
            where function(n) = result is dict[n]= result

    - recursive function: recursive fibonacci
        - BASE CASE(S):
            - if n <= 0, return 0   #edge case: negative n rounds to 0
            - if n == 1, return 1
        - RECURSIVE CASE:
            n1 = if dict.get(n-1), dict[n-1]  otherwise function(n-1)
            n2 = if dict.get(n-2), dict[n-2]  otherwise function(n-2)
            return n1 + n2

3. Translate each sub-problem into pseudocode:
    map = {}
    def fibonacci(n):
        if map.get(n) is not None: return map[n]    #starting check: do i already know the answer to this function?
        if n <= 0: return 0
        if n == 1: return 1

        n1 = fibonacci(n-1)
        n2 = fibonacci(n-2)
        map[n] = n1 + n2
        return n1 + n2
    return fibonacci(n)

'''
### I - Implement
'''
4. Translate the pseudocode into Python and share your final answer:
'''
def fibonacci_growth(n):
    map = {}
    def fibonacci(n):
        if map.get(n) is not None: return map[n]    #starting check: do i already know the answer to this function?
        if n <= 0: return 0
        if n == 1: return 1

        n1 = fibonacci(n-1)
        n2 = fibonacci(n-2)
        map[n] = n1 + n2
        return n1 + n2
    return fibonacci(n)
#Problem 4 Examples:
print("Problem 4 Output:")            # expecting: ( add this line to print statements)
print(fibonacci_growth(5))
print(fibonacci_growth(8))
# -------------------------------------------------------------------------------------------------


# Problem 6: Strongest Avenger
# Why this problem: This problem challenges students to find an alternative to the "easy way" that python functions give them using recursion.
### U - Understand 
'''
1. Share 2 questions you would ask to help understand the question:
    1. What should the function do if the input list is completely empty ([])?
    2. Can values be negative, zero, or floating-point numbers?
'''
### P - Plan
'''
2. Write out in plain English what you want to do: 
    - recursive relation: where the max_avenger(x,y) = max(avengers[x], avengers[y]), where x is the index of the highest value seen so far in the list, and y anf the index of the next value to be seen.
    - in the main function:
        - edge cases:
            - if list is empty: return None
            - if theres onlly one avenger, return that value
        - we start the recursion comparing the first two values in the list(x = 0, y =1): return value is the max value between the two
            - base cases:
                - if y == length of avengers:
                    - return the final max value
            - recursive
                - if avengers[x] >= avengers[y]:
                    return function(x,y+1)
                -  otherwise:
                    return function (y, y+1)

3. Translate each sub-problem into pseudocode:
    if not strengths: return none
    if len(strengths) == 1: return strengths[0]
    def max_aven(max, i):
        if i == len(strengths): return max

        if strengths[max] >= strengths[i]: return max_aven(max, i+1)
        else: return max_aven(i, i+1)
    return max_aven(strengths[0],strengths[1])
        
'''
### I - Implement
'''
4. Translate the pseudocode into Python and share your final answer:
'''

def strongest_avenger(strengths):
        # Edge cases
        if not strengths: return None
        if len(strengths) == 1: return strengths[0]
        def max_aven(max_i, i): 
        # where max = index of the highest value seen so far and i = index of the next value to be seen
            if i == len(strengths): return strengths[max_i]

            if strengths[max_i] >= strengths[i]: return max_aven(max_i, i+1)
            else: return max_aven(i, i+1)
        return max_aven(0,1)
  
#Problem 6 Examples:
print("Problem 6 Output:")            # expecting: ( add this line to print statements)
print(strongest_avenger([88, 92, 95, 99, 97, 100, 94]))
print(strongest_avenger([50, 75, 85, 60, 90]))
# -------------------------------------------------------------------------------------------------

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

# Problem 8: Merging Missions
# Why this problem: This problem is asking student to do a merge sort, recursively, which can be difficult for some.
### U - Understand 
'''
1. Share 2 questions you would ask to help understand the question:
    1. Are the priorities sorted in ascending or descending order?
    2. What if one or both lists are empty (None)?
'''
### P - Plan
'''
2. Write out in plain English what you want to do: 
    - base case:
        - if both lists are empty, return None
        - if one list is empty, return the remaining head node
    - recursive case
        - save the next nodes of each head node:
            - next1 = head1.next
            - next2 = head2.next
        - compare the two head nodes:
           - link the greater node to the lesser node
           - lesser node.next should be function(next1, next2)
        - return greater node
            
3. Translate each sub-problem into pseudocode:
    if not mission1: mission2
    if not mission2: mission1

    next1 = misssion1.next
    next2 = misssion2.next

    greater,lesser = mission1, mission2
    if misssion2.value >= misssion1.value:
        greater, lesser = mission2, mission1

    greater.next = lesser
    lesser = merge_missions(next1, next2)
    return greater
'''
### I - Implement
'''
4. Translate the pseudocode into Python and share your final answer:
'''
def merge_missions(mission1, mission2):
    if not mission1: return mission2
    if not mission2: return mission1

    if mission1.value <= mission2.value:
        mission1.next = merge_missions(mission1.next, mission2)
        return mission1
    else:
        mission2.next = merge_missions(mission1, mission2.next)
        return mission2

#Problem 8 Examples:
print("Problem 8  Output:")            # expecting: ( add this line to print statements)
mission1 = Node(1, Node(2, Node(4)))
mission2 = Node(1, Node(3, Node(4)))
print_linked_list(merge_missions(mission1, mission2))
# -------------------------------------------------------------------------------------------------

