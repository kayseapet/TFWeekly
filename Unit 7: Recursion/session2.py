
#Problem 1: Finding the Perfect Cruise
### U - Understand 
'''
1. Share 2 questions you would ask to help understand the question:
    1. Given the hint to use binary search, can we assume the list is sorted?
    2. is a recursive helper needed?
'''
### P - Plan
'''
2. Write out in plain English what you want to do: 
    - base case(s): 
        - given the list is none, return false
    - recursive
        - find the middle element
        - if middle element is the target, return true
        - if greater than return function(list [left half])
        - if less than return function(list[right half])

3. Translate each sub-problem into pseudocode:
    if not cruise_lengths:False
    mid = len(cruise_lengths)//2 
    if cruise_lengths[mid] == vacation_length:
         True
    if cruise_lengths[mid] > vacation_length: 
         find_cruise_length(cruise_lengths[left], vacation_length)
    if cruise_lengths[mid] < vacation_length: 
         find_cruise_length(cruise_lengths[right], vacation_length)

'''
### I - Implement
'''
4. Translate the pseudocode into Python and share your final answer:
'''
def find_cruise_length(cruise_lengths, vacation_length):
    if not cruise_lengths:
        return False
    mid = len(cruise_lengths)//2 
    if cruise_lengths[mid] == vacation_length:
        return True
    elif cruise_lengths[mid] > vacation_length: 
        return find_cruise_length(cruise_lengths[:mid], vacation_length)
    else:  
        return find_cruise_length(cruise_lengths[mid+1:], vacation_length)

#Problem 1 Examples:
print("Problem 1 Output:")
print(find_cruise_length([9, 10, 11, 12, 13, 14, 15], 13)) # True
print(find_cruise_length([8, 9, 12, 13, 13, 14, 15], 11)) # False




#Problem 2: Booking the Perfect Cruise Cabin
### U - Understand 
'''
1. Share 2 questions you would ask to help understand the question:
    1. Is this function operating similar to a binary search?
    2. can we assmume the cabin list is sorted?
'''
### P - Plan
'''
2. Write out in plain English what you want to do: 
    - recursive helper: low, high paramters
        - base case: if the low > high
            -return low
        -recursion:
            - get middle index
            - if middle element is prefered deck: return middle index
            - If it's greater than: return function(higher half of list)
            - If it's less than: return function(low half of list)
    - call recursive helper

3. Translate each sub-problem into pseudocode:
     if low > high:
            return low
        mid = (low+high)//2
        if cabins[mid] == preferred_deck:
            return mid
        elif cabins[mid] > preferred_deck:
            return search(low, mid-1)
        else:
            return search(mid+1, high)
'''
### I - Implement
'''
4. Translate the pseudocode into Python and share your final answer:
'''
def find_cabin_index(cabins, preferred_deck):
    
    def search(low, high):
        if low > high:
            return low
        mid = (low+high)//2
        if cabins[mid] == preferred_deck:
            return mid
        elif cabins[mid] > preferred_deck:
            return search(low, mid-1)
        else:
            return search(mid+1, high)
        
    index = search(0,len(cabins)-1)
    return index
    
#Problem 2 Examples:
print("Problem 2 Output:")           
print(find_cabin_index([1, 3, 5, 6], 5))
print(find_cabin_index([1, 3, 5, 6], 2))
print(find_cabin_index([1, 3, 5, 6], 7))




#Problem 3: Count Checked In Passengers
### U - Understand 
'''
1. Share 2 questions you would ask to help understand the question:
    1. Would a recursion that sequentially searches elements be O(n) or O(log n) time complexity?
    2. If we use Binary search, how can we trust that middle element is the FIRST occurence of 1?
'''
### P - Plan
'''
2. Write out in plain English what you want to do: 
    - base case(s) if list is empty, return 0
    - recursion:
        - 
            - if 1, return len(list)
            - if 0
                - get middle index, return middle index + function(left half of list)
3. Translate each sub-problem into pseudocode:
    if not rooms: return 0
    mid = len(rooms)//2
    if rooms[mid] == 1:
        return len(rooms[mid:])
    else:
        return count_checked_in_passengers(rooms[mid+1:])
'''
### I - Implement
'''
4. Translate the pseudocode into Python and share your final answer:
'''
def count_checked_in_passengers(rooms):
    if not rooms: return 0
    mid = len(rooms)//2
    if rooms[mid] == 1:
        return len(rooms[mid:])
    else:
        return count_checked_in_passengers(rooms[mid+1:])
#Problem 3 Examples:
print("Problem 3 Output:")            # expecting: ( add this line to print statements)
rooms1 = [0, 0, 0, 1, 1, 1, 1]
rooms2 = [0, 0, 0, 0, 0, 1]
rooms3 = [0, 0, 0, 0, 0, 0]
print(count_checked_in_passengers(rooms1)) 
print(count_checked_in_passengers(rooms2))
print(count_checked_in_passengers(rooms3))



#Problem 4: Determining Profitability of Excursions
### U - Understand 
'''
1. Share 2 questions you would ask to help understand the question:
    1. How can we determine the excursion is profitable?
    2. What is the return value if it is profitable?
'''
### P - Plan
'''
2. Write out in plain English what you want to do: 
    -In a recursion helper: given a list and x = profit number
        - base case: if lift is empty, return -1
        - recursion: 
            - get middle index
                - if middle element is at least x, return x
                - if not, return function(right half of list, x)
    - call recursive helper
3. Translate each sub-problem into pseudocode:
    if not list:
            return -1
        mid = (len(list))//2
        if list[mid] >= x:
            return x
        else:
            return helper(list[mid+1:],x)
'''
### I - Implement
'''
4. Translate the pseudocode into Python and share your final answer:
'''
def is_profitable(excursion_counts):
    def helper(list, x):
        if not list:
            return -1
        mid = (len(list))//2
        if list[mid] >= x:
            return x
        else:
            return helper(list[mid+1:],x)
    return helper(excursion_counts,len(excursion_counts))
#Problem 4 Examples:
print("Problem 4 Output:")         
print(is_profitable([3, 5]))
print(is_profitable([0, 0]))



#Problem 5: Finding the Shallowest Point
### U - Understand 
'''
1. Share 2 questions you would ask to help understand the question:
    1. To clarify, the return is the minimum number in the list?
    2. Can the function be written without a recursive helper?
'''
### P - Plan
'''
2. Write out in plain English what you want to do: 
    - a recurison helper: given a list
        - base case: if list is empty, return
        - recursion:
            - left = function(left half of list)
            - right = function(right half of list)
            - if left is greater than right, return right
            - else: return left

3. Translate each sub-problem into pseudocode:
 
'''
### I - Implement
'''
4. Translate the pseudocode into Python and share your final answer:
'''
def find_shallowest_point(depths):
    def helper(list):
        if not list:
            return float('inf')
        if len(list) == 1:
            return list[0]
        mid = len(list)//2
        left = helper(list[:mid])
        right = helper(list[mid:])
        if left > right:
            return right
        else:
            return left
    return helper(depths)
#Problem 5 Examples:
print("Problem 5 Output:")       
print(find_shallowest_point([5, 7, 2, 8, 3]))
print(find_shallowest_point([12, 15, 10, 21]))
