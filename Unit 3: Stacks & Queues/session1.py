#Session 1, Advanced Problem Set Ver.1

# PROBLEM 1: Arrange Guest Arrival Order
#### U - Understand 
'''
1. Share 2 questions you would ask to help understand the question:
  1. Can I assume the string 'arrival_pattern' will only contain 'I' or 'D', or should there be a validity check?
  2. To confirm, we return the string closest to being in order?
'''
### P - Plan
'''
2. Write out in plain English what you want to do: 
    - create empty stack
    - initialize list for ordered guests
    - create for loop: add the next number to stack , until letter = 'I', then move all in stack to list 
    - we process backwards until "I" then add from stack to list to make it fowards.
    - return list
  
3. Translate each sub-problem into pseudocode:
  def arrange_guest_arrival_order(arrival_pattern):
    stack = []
    order = []
    for i in range(len(arrival_pattern)+1):
      stack.append(str(i+1))
      if i == len(arrival_pattern) or arrival_pattern[i]== "I" :
         while len(stack)>=1 :
            order.append(stack.pop())

    return "".join(order)
'''
### I - Implement
'''
4. Translate the pseudocode into Python and share your final answer:
'''
def arrange_guest_arrival_order(arrival_pattern):
    stack = []
    order = []
    for i in range(len(arrival_pattern)+1):
      stack.append(str(i+1))
      if i == len(arrival_pattern) or arrival_pattern[i]== "I" :
         while len(stack)>=1 :
            order.append(stack.pop())

    return "".join(order)


# PROBLEM 2: 
#### U - Understand 
'''
1. Share 2 questions you would ask to help understand the question:
  1. Shoudld we use a helper function, or should we avoid using one?
  2. Is the list of attendees giving in order, or not always?
'''
### P - Plan
'''
2. Write out in plain English what you want to do: 
  - initialize queue with range (0,length)
  - initalize final list with n spots
  - make sorted list
  - for each index, put sorted[0] in queue[0] 
  - then send next queue[0] to the back of queue.
  - after, return final list

3. Translate each sub-problem into pseudocode:
  def reveal_attendee_list_in_order(attendees):
    n = len(attendees)
    q = deque(range(0,n))
    sort = sorted(attendees)
    final = [0] * len(attendees)
    for i in range(len(sort)):
       final[q.popleft()] = sort[i]
       if q: q.append(q.popleft())
    return final
'''
### I - Implement
'''
4. Translate the pseudocode into Python and share your final answer:
'''
from collections import deque 
def reveal_attendee_list_in_order(attendees):
    n = len(attendees)
    q = deque(range(0,n))
    sort = sorted(attendees)
    final = [0] * len(attendees)
    for i in range(len(sort)):
       final[q.popleft()] = sort[i]
       if q: q.append(q.popleft())
    return final

    
# PROBLEM 3:
#### U - Understand 
'''
1. Share 2 questions you would ask to help understand the question:
  - to clarify, the whole list doesnt need to be sorted, just put in an order of numbers less than, equal, & greater than a specific number?
  - What do we return in the event that the specified number is not in the list?
'''
### P - Plan
'''
2. Write out in plain English what you want to do: 
  - initalize a,b index pointers for end of less than & beginning on more than
  - p = iteration pointer
  - in while loop: p<= b,
    - check if attendees[p] < priority: if false, push attendees[p] to end and b-=1.
    - if true, when end of less than != priotity, append attendees[p] to end of less than section (a)
    - when attendees[a] == priority, insert attendees[p] to just before attendees[a]
    return attendees list.
3. Translate each sub-problem into pseudocode:
  def arrange_attendees_by_priority(attendees, priority):
    a,b = 0,len(attendees)-1
    p = 0
    while (p <= b):
       check = attendees[p] <= priority
       if check:
          if attendees[a]!= priority:
             a = p
             p+=1
          else:
             attendees.insert(a,attendees.pop(p))
             a += 1
             p+=1
       else:
          attendees.append(attendees.pop(p))
          b-=1    
    return attendees
'''
### I - Implement
'''
4. Translate the pseudocode into Python and share your final answer:
'''
def arrange_attendees_by_priority(attendees, priority):
    a,b = 0,len(attendees)-1
    p = 0
    while (p <= b):
       check = attendees[p] <= priority
       if check:
          if attendees[a]!= priority:
             a = p
             p+=1
          else:
             attendees.insert(a,attendees.pop(p))
             a += 1
             p+=1
       else:
          attendees.append(attendees.pop(p))
          b-=1    
    return attendees
print(arrange_attendees_by_priority([9,12,5,10,14,3,10], 10)) 
print(arrange_attendees_by_priority([-3,4,3,2], 2)) 


# PROBLEM 4:
#### U - Understand 
'''
1. Share 2 questions you would ask to help understand the question:
  - does this have to be an inplace sort?
  - what do i do in the event there are no positive numbers?
'''
### P - Plan
'''
2. Write out in plain English what you want to do: 
  - intialize two lists: pos & neg
  - empty final list
  - for loop: for each num in guests list, add positive nums to 'pos' list, and negative nums to 'neg'list.
  - while pos & neg are not None, alternate between adding first elment in each list.
  -return final list
3. Translate each sub-problem into pseudocode:
  def rearrange_guests(guests):
    pos = []
    neg = []
    final = []
    for x in guests:
        if x >=0:
          pos.append(x)
        else:
           neg.append(x)      
    while pos and neg:
        if pos:
           final.append(pos.pop(0))
        if neg:
            final.append(neg.pop(0))
    return final
'''
### I - Implement
'''
4. Translate the pseudocode into Python and share your final answer:
'''
def rearrange_guests(guests):
    pos = []
    neg = []
    final = []
    for x in guests:
        if x >=0:
          pos.append(x)
        else:
           neg.append(x)      
    while pos and neg:
        if pos:
           final.append(pos.pop(0))
        if neg:
            final.append(neg.pop(0))
    return final


# PROBLEM 5:
#### U - Understand 
'''
1. Share 2 questions you would ask to help understand the question:
  - to clarify, are we only looking for stray '('? or ')' as well?
  - should we code an error in the event there is characters other than parentheses in the string?
'''
### P - Plan
'''
2. Write out in plain English what you want to do: 
  - initialize a stack
  - for loop: for every in char in the schedule
    - if there is one, view last element from stack.
    - if char == '(' and last element is not ')', add the char to the stack
    - do the same for ')' and '('
  - return stack length
3. Translate each sub-problem into pseudocode:
  def min_changes_to_make_balanced(schedule):
   stack = []
   for char in schedule:
        if len(stack) < 1:
            stack.append(char)
        else:
            top = stack[-1]
            if char == '(' and top == ')':
               stack.pop()
            elif char == ')' and top == '(':
               stack.pop()
            else:
               stack.append(char)
   return len(stack)
'''
### I - Implement
'''
4. Translate the pseudocode into Python and share your final answer:
'''
def min_changes_to_make_balanced(schedule):
   stack = []
   for char in schedule:
        if len(stack) < 1:
            stack.append(char)
        else:
            top = stack[-1]
            if char == '(' and top == ')':
               stack.pop()
            elif char == ')' and top == '(':
               stack.pop()
            else:
               stack.append(char)
   return len(stack)
