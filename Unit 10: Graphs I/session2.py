#Unit 10 Session 2, Standard Version 1


#Problem 1: Can Rebook Flight
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






#Problem 2: Can Rebook Flight II
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






#Problem 3: Number of Flights
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






#Problem 4: Number of Airline Regions
### U - Understand 
'''
1. Share 2 questions you would ask to help understand the question:
    1. how do we get to every airport?
    2. what if the matrix[a][b] is equal to something other than 1 and 0?
'''
### P - Plan
'''
2. Write out in plain English what you want to do: 
    DFS helper and looping through each row
    - helper function that accepts a number as its 'source'
        -base case: if soure isnt an index of the matrix's rows, return out of the helper
        - recursion:
            add source to a set for visited nodes
            in a for loop: for every value in the list fucntion[source]
                - if the value there is one, and the index hasnt been visited,  recursivly call helper again
    - to make sure each row is checked, outside of the helper, loop through every row that hasn't been visited & call the helper
3. Translate each sub-problem into pseudocode:
    def search(source):
        if is_connected[source] is None:
            return 
        visited.add(source)
        for dest in range(source, len(is_connected)):
            if source == dest:
                continue
            if is_connected[source][dest] == 1 and dest not in visited:
                search(dest)
'''
### I - Implement
'''
4. Translate the pseudocode into Python and share your final answer:
'''
def num_airline_regions(is_connected):
    visited = set()
    count = 0
    def search(source):
        if is_connected[source] is None:
            return 
        visited.add(source)
        for dest in range(source, len(is_connected)):
            if source == dest:
                continue
            if is_connected[source][dest] == 1 and dest not in visited:
                search(dest)
    
    for i in range(len(is_connected)):
        if i not in visited:
            count += 1
            search(i)

    return count

#Problem 4 Examples:
print("Problem 4 Output:")            # expecting: ( add this line to print statements)
is_connected1 = [
    [1, 1, 0],
    [1, 1, 0],
    [0, 0, 1]
]
is_connected2 = [
    [1, 0, 0, 1],
    [0, 1, 1, 0],
    [0, 1, 1, 0],
    [1, 0, 0, 1]
]
print(num_airline_regions(is_connected1))
print(num_airline_regions(is_connected2)) 







#Problem 5: Get Flight Cost
### U - Understand 
'''
1. Share 2 questions you would ask to help understand the question:
    1. What type of travesal gives the minimum total wieght?
    2. Can this problem be solved using recursion?

'''
### P - Plan
'''
2. Write out in plain English what you want to do: 
    iterative traversal using a stack:
    - given seen is a set & next is a list with tuples (airport name, weight):
        - while next, remove the last element
        - if the element is the destination, return count
        - add its wieght to the count, and add its name to seen
        - now loop through its values as a dictionary key, where any airport names not in seen are added to next.
    - return -1
3. Translate each sub-problem into pseudocode:
    while next:
        stop = next.pop()
        count += stop[1]
        seen.add(stop[0])
        if stop[0] == dest: return count
        branches = flights.get(stop[0])
        for port in branches:
            if port[0] not in seen:
                next.append(port)
'''
### I - Implement
'''
4. Translate the pseudocode into Python and share your final answer:
'''
def calculate_cost(flights, start, dest):
    count = 0
    seen = set()
    next = [(start,0)]
    while next:
        stop = next.pop()
        count += stop[1]
        seen.add(stop[0])
        if stop[0] == dest: return count
        branches = flights.get(stop[0])
        for port in branches:
            if port[0] not in seen:
                next.append(port)
    return -1
        
#Problem 5 Examples:
print("Problem 5 Output:")            # expecting: ( add this line to print statements)
flights = {'LAX': [('SFO', 50)],'SFO': [('LAX', 50), ('ORD', 100), ('ERW', 210)],'ERW': [('SFO', 210), ('ORD', 300)],'ORD': [('ERW', 300), ('SFO', 100), ('MIA', 400)],'MIA': [('ORD', 400)]}

print(calculate_cost(flights, 'LAX', 'MIA'))

