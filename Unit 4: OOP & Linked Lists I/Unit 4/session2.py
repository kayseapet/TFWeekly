# Unit 4 Session 2 Version 1

#PROBLEM 1: Planning Your Daily Work Schedule
### U - Understand 
'''
1. Share 2 questions you would ask to help understand the question:
    1. to clarify, its only true if the sum of two times equals the available time?
    2. is it possible for one time to satisfy the time required?
'''
### P - Plan
'''
2. Write out in plain English what you want to do:
    - in for loop, (using zip):
        - if the sum of any two elements in the list equals the available_time, return true
    - after the loop, return false
3. Translate each sub-problem into pseudocode:
    for x,y in zip(task_times, task_times[1:]):
        if x+y == available_time:
            return True
    return False
'''
### I - Implement
'''
4. Translate the pseudocode into Python and share your final answer:
'''
def find_task_pair(task_times, available_time):
    for x,y in zip(task_times, task_times[1:]):
        if x+y == available_time:
            return True
    return False

#Problem 1 Examples:
print("Problem 1 Output:")            # expecting: ( add this line to print statements)
task_times = [30, 45, 60, 90, 120]
available_time = 105
print(find_task_pair(task_times, available_time))
task_times_2 = [15, 25, 35, 45, 55]
available_time = 100
print(find_task_pair(task_times_2, available_time))
task_times_3 = [20, 30, 50, 70]
available_time = 60
print(find_task_pair(task_times_3, available_time))
# -------------------------------------------------------------------------------------------------





#Problem 3: Expense Tracking and Categorization
### U - Understand 
'''
1. Share 2 questions you would ask to help understand the question:
    1. What is the output? 
    2. to clarify, the expenses are summed up into one data structure?
'''
### P - Plan
'''
2. Write out in plain English what you want to do: 
    - create dict to accumulate expenses
    - in a for loop through expenses:
        - add expense value to expense key in dict
    - create max var, that gets the max of all dict values
    -return both dict and max value
3. Translate each sub-problem into pseudocode:
    expenses = {}
    maxx = (float('-inf'), '')
    for tuple in expensive:
        if not expenses.get(tuple[0]):expenses[tuple[0]] = 0
        expenses[tuple[0]] += tuple[1]
        if expenses[tuple[0]] > maxx[0]: maxx = (expenses[tuple[0]],tuple[0])
    return (expenses,maxx[1])

'''
### I - Implement
'''
4. Translate the pseudocode into Python and share your final answer:
'''
def calculate_expenses(expensive):
    expenses = {}
    maxx = (float('-inf'), '')
    for tuple in expensive:
        if not expenses.get(tuple[0]):expenses[tuple[0]] = 0
        expenses[tuple[0]] += tuple[1]
        if expenses[tuple[0]] > maxx[0]: maxx = (expenses[tuple[0]],tuple[0])
    return (expenses,maxx[1])
#Problem 3 Examples:
print("Problem 3 Output:")            # expecting: ( add this line to print statements)
expenses = [("Food", 12.5), ("Transport", 15.0), ("Accommodation", 50.0),
            ("Food", 7.5), ("Transport", 10.0), ("Food", 10.0)]
print(calculate_expenses(expenses))
expenses_2 = [("Entertainment", 20.0), ("Food", 15.0), ("Transport", 10.0),
              ("Entertainment", 5.0), ("Food", 25.0), ("Accommodation", 40.0)]
print(calculate_expenses(expenses_2))
expenses_3 = [("Utilities", 100.0), ("Food", 50.0), ("Transport", 75.0),
              ("Utilities", 50.0), ("Food", 25.0)]
print(calculate_expenses(expenses_3))
# -------------------------------------------------------------------------------------------------






#Problem 5: Validating HTML Tags
### U - Understand 
'''
1. Share 2 questions you would ask to help understand the question:
    1. Is there a set list of acceptable tags, or is anything written in the form of <this></this> acceptable?
    2. what is the result given an empty 'html' parameter?
'''
### P - Plan
'''
2. Write out in plain English what you want to do: 
    - use stack to track balanced tags
    - using regex to prep the string and find matching tags
        - convert the string into a list split by tags (<xyz>)
    - in a for loop traversing list:
        - if stack is empty or doesn't match last tag added to stack,
            - add tag to stack
        -else (aka if it DOES match):
            - pop last element from stack
    - if stack is not empty return false
    -else return true
3. Translate each sub-problem into pseudocode:
    stack = []
    html = re.split
    for tag in html:
        if not tag: continue
        if not stack:
            if re.search(r"(<>)", tag): return False
            stack.append(tag)
            continue
        last = re.sub(r"(<>)","",stack[-1])
        next = re.sub(r"(<>)", "", tag)
        if next[0] == "/":
            if next[1:] == last: stack.pop()
            else: return False
        else:
            stack.append(tag)
    if not stack: return True
    return False

'''
### I - Implement
'''
4. Translate the pseudocode into Python and share your final answer:
'''
import re
def validate_html_tags(html):
    stack = []
    html = re.split(r"(<\/?\w+>)",html)
    for tag in html:
        if not tag: continue
        if not stack:
            if re.search(r"(<\/\w+>)", tag): return False
            stack.append(tag)
            continue
        last = re.sub(r"(<)|(>)","",stack[-1])
        next = re.sub(r"(<)|(>)", "", tag)
        if next[0] == "/":
            if next[1:] == last: stack.pop()
            else: return False
        else:
            stack.append(tag)
    if not stack: return True
    return False
#Problem 5 Examples:
print("Problem 5 Output:")            # expecting: ( add this line to print statements)
html = "<div><p></p></div>"
print(validate_html_tags(html))
html_2 = "<div><p></div></p>"
print(validate_html_tags(html_2))
html_3 = "<div><p><a></a></p></div>"
print(validate_html_tags(html_3))
html_4 = "<div><p></a></p></div>"
print(validate_html_tags(html_4))
# -------------------------------------------------------------------------------------------------