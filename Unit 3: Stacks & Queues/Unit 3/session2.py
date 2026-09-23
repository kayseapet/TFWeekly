# Unit 3 Session 2 Version 1

#PROBLEM 1: Manage Performance Stage Changes
### U - Understand 
'''
1. Share 2 questions you would ask to help understand the question:
    1. Is there a specifc way we should splice the string to process it?
    2. Should there be error handling for strings other than the three approved strings?
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
#Problem 1 Examples:
print("Problem 1 Output:")            # expecting: ( add this line to print statements)
print(manage_stage_changes(["Schedule A", "Schedule B", "Cancel", "Schedule C", "Reschedule", "Schedule D"]))  
print(manage_stage_changes(["Schedule A", "Cancel", "Schedule B", "Cancel", "Reschedule", "Cancel"])) 
print(manage_stage_changes(["Schedule X", "Schedule Y", "Cancel", "Cancel", "Schedule Z"])) 
# -------------------------------------------------------------------------------------------------





#PROBLEM 3: Collecting Points at Festival Booths
### U - Understand 
'''
1. Share 2 questions you would ask to help understand the question:
    1. What is the purpose of using a stack rather than the sum() method?
    2. Should the stack add the point as it gets them, or add the all at the end?
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
#Problem 3 Examples:
print("Problem 3 Output:")            # expecting: ( add this line to print statements)
print(collect_festival_points([5, 8, 3, 10])) 
print(collect_festival_points([2, 7, 4, 6])) 
print(collect_festival_points([1, 5, 9, 2, 8])) 
# -------------------------------------------------------------------------------------------------




#PROBLEM 5: Merge Performance Schedules
### U - Understand 
'''
1. Share 2 questions you would ask to help understand the question:
    1. What should it end the loop after one string is over?
    2. To confirm, we are just alternating bewteening adding from one list and the other?
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
#Problem 5 Examples:
print("Problem 5 Output:")            # expecting: ( add this line to print statements)
print(merge_schedules("abc", "pqr")) 
print(merge_schedules("ab", "pqrs")) 
print(merge_schedules("abcd", "pq")) 
# -------------------------------------------------------------------------------------------------

