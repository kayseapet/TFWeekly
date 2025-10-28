#Session 2, Standard Vers 1.

#PROBLEM 1
### U - Understand 
'''
1. Share 2 questions you would ask to help understand the question:
  - Is there a specifc way we should splice the string to process it?
  - Should there be error handling for strings other than the three approved strings?
'''
### P - Plan
'''
2. Write out in plain English what you want to do: 
  - intializes two stacks, confirmed & cancelled
  - for each string in list:
    - split str into list or words by space
    - if list[0] == "schedule", append list[1] to confirmed stack
    - if list[0] == "cancel", pop from confirmed stack and append to cancelled
    -if list[0] == "reschedule", pop from cancelled and append to confirmed.
    - return confirmed list

3. Translate each sub-problem into pseudocode:
  def manage_stage_changes(changes):
    confirmed = []
    cancelled = []
    for str in changes:
        act = str.split()
        if act[0] == "Schedule":
            confirmed.append(act[1])
        elif act[0] == "Cancel":
            cancelled.append(confirmed.pop())
        elif act[0] == "Reschedule":
            confirmed.append(cancelled.pop())
    return confirmed
'''
### I - Implement
'''
4. Translate the pseudocode into Python and share your final answer:
'''
def manage_stage_changes(changes):
    confirmed = []
    cancelled = []
    for str in changes:
        act = str.split()
        if act[0] == "Schedule":
            confirmed.append(act[1])
        elif act[0] == "Cancel":
            cancelled.append(confirmed.pop())
        elif act[0] == "Reschedule":
            confirmed.append(cancelled.pop())
    return confirmed


#PROBLEM 2
### U - Understand 
'''
1. Share 2 questions you would ask to help understand the question:
  - What is the data variable in the list? 
  - Do I need to import collections to solve this problem
'''
### P - Plan
'''
2. Write out in plain English what you want to do: 
    - use Priority Queue (from imports)
    - use for loop to insert each request into Priority Queue
    - use for loop to remove request with highest priority
    - add request names to seperate list
    -return final list
3. Translate each sub-problem into pseudocode:
  def process_performance_requests(requests):
    final = []
    queue = []
    for num, r in requests:
        heapq.heappush(queue,(-num,r))
    
    while queue:
        num, name = heapq.heappop(queue)
        final.append(name)
    return final
'''
### I - Implement
'''
4. Translate the pseudocode into Python and share your final answer:
'''
import heapq
def process_performance_requests(requests):
    final = []
    queue = []
    for num, r in requests:
        heapq.heappush(queue,(-num,r))
    
    while queue:
        num, name = heapq.heappop(queue)
        final.append(name)
    return final


#PROBLEM 3
### U - Understand 
'''
1. Share 2 questions you would ask to help understand the question:
  - What is the purpose of using a stack rather than the sum() method?
  - should the stack add the point as it gets them, or add the all at the end?
'''
### P - Plan
'''
2. Write out in plain English what you want to do: 
    - initalize stack as reverse list of points list and total variable
    - for each booth:
        pop points off stack
        add the number of points to the current total.
    - return total

3. Translate each sub-problem into pseudocode:
  def collect_festival_points(points):
    stack = points[::-1]
    total = 0
    for x in points:
        total += stack.pop()
    return total
'''
### I - Implement
'''
4. Translate the pseudocode into Python and share your final answer:
'''
def collect_festival_points(points):
    stack = points[::-1]
    total = 0
    for x in points:
        total += stack.pop()
    return total


#PROBLEM 4
### U - Understand 
'''
1. Share 2 questions you would ask to help understand the question:
  - Are the numbers input as strings or ints?
  - what would happen if the first instruction is 'back'?
'''
### P - Plan
'''
2. Write out in plain English what you want to do: 
  - make empty stack
  - for each clues:
    - if clue == 'back', stack.pop()
    - if not, add clue to stack
    -return stack
3. Translate each sub-problem into pseudocode:
  def booth_navigation(clues):
    stack = []
    for clue in clues:
        if clue == "back":
            if stack:stack.pop()
        else:
            stack.append(clue)
    return stack
'''
### I - Implement
'''
4. Translate the pseudocode into Python and share your final answer:
'''
def booth_navigation(clues):
    stack = []
    for clue in clues:
        if clue == "back":
            if stack:stack.pop()
        else:
            stack.append(clue)
    return stack


#PROBLEM 5
### U - Understand 
'''
1. Share 2 questions you would ask to help understand the question:
  - What should it end the loop after one string is over?
  - To confirm, we are just alternating bewteening adding from one list and the other?
'''
### P - Plan
'''
2. Write out in plain English what you want to do: 
  - make empty string
  - while both schedules arent empty:
    - add schedule1[0] and schedule2[0]to the string and remove them from their lists
  - if one of them still not None, add the rest to the string
  - return string
3. Translate each sub-problem into pseudocode:
  def merge_schedules(schedule1, schedule2):
    schedule1 = list(schedule1)
    schedule2 = list(schedule2)
    final = []
    while schedule1 and schedule2:
        final.append(schedule1.pop(0))
        final.append(schedule2.pop(0))
    if schedule1:
        final.extend(schedule1)
    elif schedule2:
        final.extend(schedule2)
    return "".join(final)
'''
### I - Implement
'''
4. Translate the pseudocode into Python and share your final answer:
'''
def merge_schedules(schedule1, schedule2):
    schedule1 = list(schedule1)
    schedule2 = list(schedule2)
    final = []
    while schedule1 and schedule2:
        final.append(schedule1.pop(0))
        final.append(schedule2.pop(0))
    if schedule1:
        final.extend(schedule1)
    elif schedule2:
        final.extend(schedule2)
    return "".join(final)
