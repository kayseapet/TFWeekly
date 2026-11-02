#Unit 10 Session 1, Standard Version 1

#Problem 2: There and Back
# Why this problem:
### U - Understand 
'''
1. Share 2 questions you would ask to help understand the question:
    1. how do we know if the edge is directed or not?
    2. does the node value represented in it's place in the flights list?
'''
### P - Plan
'''
2. Write out in plain English what you want to do: 
    BFS:
    - make a 'next' list and a 'seen' set
    - while there are still nodes to be visitied next,
        - take the next one (as a queue)
        - add any unseen indexes to the seen & next lists
        - use seen as a set to reduced time complexity
    - if the number of flights (vertices) matches the amount of numbers in seen, return true
    - otherwise return false
3. Translate each sub-problem into pseudocode:
    while next:
        vert = next.pop(0)
        for node in flights[vert]:
            if node not in seen:
                seen.add(node)
                next.append(node)
    if len(flights) == len(seen):
        return True
    else:
        return False
'''
### I - Implement
'''
4. Translate the pseudocode into Python and share your final answer:
'''
def bidirectional_flights(flights):
    if not flights:
        return True
    
    seen = set()
    next = [0]
    seen.add(0)

    while next:
        vert = next.pop(0)
        for node in flights[vert]:
            if node not in seen:
                seen.add(node)
                next.append(node)
    if len(flights) == len(seen):
        return True
    else:
        return False
            
#Problem 2 Examples:
print("Problem 2 Output:")            # expecting: ( add this line to print statements)
flights1 = [[1, 2], [0], [0, 3], [2]]
flights2 = [[1, 2], [], [0], [2]]
print(bidirectional_flights(flights1))
print(bidirectional_flights(flights2))
# -------------------------------------------------------------------------------------------------

#Problem 3: Finding Direct Flights
# Why this problem:
### U - Understand 
'''
1. Share 2 questions you would ask to help understand the question:
    1. how does the traversal change when the graph has direction?
    2. how do we know what vertices each index in the flight lists belongs to?

'''
### P - Plan
'''
2. Write out in plain English what you want to do: 
    - locate the source list
    - create list
    - for each stop in the source:
        - its = 1, add the stop's index to the list
    -return the list of stops
3. Translate each sub-problem into pseudocode:
    port = flights[source]
    stops = []
    for i in range(len(port)):
        if port[i] == 1:
            stops.append(i)
'''
### I - Implement
'''
4. Translate the pseudocode into Python and share your final answer:
'''
def get_direct_flights(flights, source):
    port = flights[source]
    stops = []
    for i in range(len(port)):
        if port[i] == 1:
            stops.append(i)
    return stops

#Problem 3 Examples:
print("Problem 3 Output:")            # expecting: ( add this line to print statements)
flights = [
            [0, 1, 1, 0],
            [1, 0, 0, 0],
            [1, 1, 0, 1],
            [0, 0, 0, 0]]
print(get_direct_flights(flights, 2))
print(get_direct_flights(flights, 3))
# -------------------------------------------------------------------------------------------------

#Problem 4: Converting Flight Representations
# Why this problem:
### U - Understand 
'''
1. Share 2 questions you would ask to help understand the question:
    1. How do we know what flights have been counted?
    2. does each flight go both ways?
'''
### P - Plan
'''
2. Write out in plain English what you want to do: 
    - create a dict where:
        - key = destination name
        - value = a list of other available destinations
    - return dict
3. Translate each sub-problem into pseudocode:
    dict = {}
    for flight in flights:
        dict[flight[0]].append(flight[1])
        dict[flight[1]].append(flight[0])
    return dict
'''
### I - Implement
'''
4. Translate the pseudocode into Python and share your final answer:
'''
def get_adj_dict(flights):
    dict = {}
    for flight in flights:
        if dict.get(flight[0]) is None:
            dict[flight[0]]= []
        if dict.get(flight[1]) is None:
             dict[flight[1]]= []
        dict[flight[0]].append(flight[1])
        dict[flight[1]].append(flight[0])
    return dict

#Problem 4 Examples:
print("Problem 4 Output:")            # expecting: ( add this line to print statements)
flights = [['Cape Town', 'Addis Ababa'], ['Cairo', 'Lagos'], ['Lagos', 'Addis Ababa'], 
            ['Nairobi', 'Cairo'], ['Cairo', 'Cape Town']]
print(get_adj_dict(flights))
# -------------------------------------------------------------------------------------------------
