#Unit 10, Session 2 Version 1

#Problem 1: Can Rebook Flight
# Why this problem:
### U - Understand 
'''
1. Share 2 questions you would ask to help understand the question:
    1. how do we move throught the matrix to find a path?
    2. Whats the return value?
'''
### P - Plan
'''
2. Write out in plain English what you want to do: 
    DFS helper recursive function
        - base case(s):
          if flights is empty, return False
          if the destination has a direct path from source, return true
        - recursion
          for one row in the matirx, loop through each element
            if the elemeent is one & hasnt been visited yet, check is the search at that index's row has the destination:
                if helper(index) is true, return true
          after the loop, return false.
3. Translate each sub-problem into pseudocode:
    if not flights or flights[stop] == [0]* len(flights):
            return False
        if flights[stop][dest] == 1:
            return True
        for i in range(len(flights)):
            if flights[stop][i] == 1 and i not in visited:
                visited.add(i)
                if search(i, visited) == True: return True
        return False
'''
### I - Implement
'''
4. Translate the pseudocode into Python and share your final answer:
'''
def can_rebook(flights, source, dest):
    def search(stop, visited = set()):
        if not flights or flights[stop] == [0]* len(flights):
            return False
        if flights[stop][dest] == 1:
            return True

        for i in range(len(flights)):
            if flights[stop][i] == 1 and i not in visited:
                visited.add(i)
                if search(i, visited) == True: return True
        return False
    return search(source)


#Problem 1 Examples:
print("Problem 1 Output:")            # expecting: ( add this line to print statements)
flights1 = [
    [0, 1, 0], # Flight 0
    [0, 0, 1], # Flight 1
    [0, 0, 0]  # Flight 2
]
flights2 = [
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
]
print(can_rebook(flights1, 0, 2))
print(can_rebook(flights2, 0, 2)) 
# -------------------------------------------------------------------------------------------------------------------------

#Problem 2: Can Rebook Flight II
# Why this problem:
### U - Understand 
'''
1. Share 2 questions you would ask to help understand the question:
    1. How do I know when I'm using DFS vs BFS?
    2. What's the difference in spcae/time complexities?
'''
### P - Plan
'''
2. Write out in plain English what you want to do: 
    Iterative version of the last question:
    - using seen as a set and next as a list (with first element)
    - while next isnt empty,
        - pop the next element from next, & if has a direct path to destination, return true
        - otherwise, loop through the rest of theflight connections for the current row.
    - after next is empty, return False
3. Translate each sub-problem into pseudocode:
     while next:
        stop = next.pop()
        seen.add(stop)
        if flights[stop][dest] == 1: return True
        for i in range(len(flights)):
            if i not in seen and flights[stop][i]:
                next.append(i)
    return False
'''
### I - Implement
'''
4. Translate the pseudocode into Python and share your final answer:
'''
def can_rebook2(flights, source, dest):
    seen = set()
    next = [source]

    while next:
        stop = next.pop()
        seen.add(stop)
        if flights[stop][dest] == 1: return True
        for i in range(len(flights)):
            if i not in seen and flights[stop][i]:
                next.append(i)
    return False

#Problem 2 Examples:
print("Problem 2 Output:")            # expecting: ( add this line to print statements)
flights1 = [
    [0, 1, 0], # Flight 0
    [0, 0, 1], # Flight 1
    [0, 0, 0]  # Flight 2
]
flights2 = [
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
]
print(can_rebook2(flights1, 0, 2))
print(can_rebook2(flights2, 0, 2)) 
# -----------------------------------------------------------------------------------------------------------------------

#Problem 3: Number of Flights
# Why this problem:
### U - Understand 
'''
1. Share 2 questions you would ask to help understand the question:
    1. do we include the starting point in the number of flights?
    2. How do we know if theres a path of not?

'''
### P - Plan
'''
2. Write out in plain English what you want to do: 
    Iterative search using a stack & set
    - where next = list of indices to be handled next & seen = set of all recorded & completed nodes
    - while next
        -get the last element
        - add to the count
        - loop through the elements at the current row, where ints not yet seen & that correspond to a space on the matrix is added to next.
        -return - 1 after next is empty
3. Translate each sub-problem into pseudocode:
     next = [i]
    count = 0
    while next:
        stop = next.pop()
        count += 1
        seen.add(stop)
        if flights[stop][j] == 1: return count
        for x in range(len(flights)):
            if x not in seen and flights[stop][x]:
                next.append(x)
    return -1
'''
### I - Implement
'''
4. Translate the pseudocode into Python and share your final answer:
'''
def counting_flights(flights, i, j):
    seen = set()
    next = [i]
    count = 0
    while next:
        stop = next.pop()
        count += 1
        seen.add(stop)
        if flights[stop][j] == 1: return count
        for x in range(len(flights)):
            if x not in seen and flights[stop][x]:
                next.append(x)
    return -1

#Problem 3 Examples:
print("Problem 3 Output:")            # expecting: ( add this line to print statements)
flights = [
    [0, 1, 1, 0, 0], # Airport 0
    [0, 0, 1, 0, 0], # Airport 1
    [0, 0, 0, 1, 0], # Airport 2
    [0, 0, 0, 0, 1], # Airport 3
    [0, 0, 0, 0, 0]  # Airport 4
]
print(counting_flights(flights, 0, 2))  
print(counting_flights(flights, 0, 4))
print(counting_flights(flights, 4, 0))
# ------------------------------------------------------------------------------------------------------------------------
