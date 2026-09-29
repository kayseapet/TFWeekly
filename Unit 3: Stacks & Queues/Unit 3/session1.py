# Unit 3 Session 1 Version 1

#Problem 3: Check Symmetry in Post Titles
# Why This Problem:  This is a classic 'palindrome' question, which is a great example of how left and right pointers can be used.
### U - Understand 
'''
1. Share 2 questions you would ask to help understand the question:
    1. Can the post title be empty?
    2. Are there any characters that are an exception to the rule? For example, punctuation (?  .   ,)?
'''
### P - Plan
'''
2. Write out in plain English what you want to do: 
    - edgecase: if its empty, return true (bc nothing is still nothing backwards lol)
    - establish a 'left' and 'right' pointer
        - left start at index 0
        - right start at last index of the string
    - in a while loop: before the left and right cross paths
        - if the values at each pointer are NOT the same, return false
    - when the loop is over, return true
3. Translate each sub-problem into pseudocode:
    if not title: return True
    left,right = 0, len(title)
    while left<= right:
        if title[left] != title[right]: return False
    return True
'''
### I - Implement
'''
4. Translate the pseudocode into Python and share your final answer:
'''
def is_symmetrical_title(title):
    if not title: return True
    chars = title.replace(" ","")
    left,right = 0, len(chars) -1
    while left<= right:
        if chars[left].lower() != chars[right].lower(): return False
        left += 1
        right -= 1
    return True
#Problem 3 Examples:
print("Problem 3 Output:")            # expecting: ( add this line to print statements)
print(is_symmetrical_title("A Santa at NASA"))
print(is_symmetrical_title("Social Media")) 
# -------------------------------------------------------------------------------------------------



# Problem 5: Content Cleaner
# Why this problem:Student could get stumped on this, because they'll have to find a way to be able to compare every letter with it's uppercase counterpart.
### U - Understand 
'''
1. Share 2 questions you would ask to help understand the question:
    1. Can the string be empty, or have a length of 1? What should be returned in those cases?
    2. Does the order of removal matter, or will any order of removing adjacent matching pairs yield the exact same final result?
'''
### P - Plan
'''
2. Write out in plain English what you want to do: 
    - make a stack
    - in a for loop: go trhough each character
        - if the stack is empty: just add the char to the stack
        - otherwise:
            - compare the top element in stack to current character
                - if they're the saem letter, pop the top stack element
                - otherwise: add character to the stack
    - return stack
3. Translate each sub-problem into pseudocode:
    text = list(post)
    stack = []
    for char in text:
        if not stack: stack.append(char)
        else:
            prev = stack[-1]
            if prev.lower() == char.lower(): stack.pop()
            else: stack.append(char)
    stack = stack.join()
    return stack
'''
### I - Implement
'''
4. Translate the pseudocode into Python and share your final answer:
'''
def clean_post(post):
    text = list(post)
    stack = []
    for char in text:
        if not stack: stack.append(char)
        else:
            prev = stack[-1]
            if prev.lower() == char.lower(): stack.pop()
            else: stack.append(char)
    stack = "".join(stack)
    return stack
#Problem 5 Examples:
print("Problem 5 Output:")            # expecting: ( add this line to print statements)
print(clean_post("poOost")) 
print(clean_post("abBAcC")) 
print(clean_post("s")) 
# -------------------------------------------------------------------------------------------------




# Problem 6: Post Editor
# Why this problem: This problem seems challenging because typically its stacks that are used to reverse strings easily, so it takes a little more thinking.
### U - Understand 
'''
1. Share 2 questions you would ask to help understand the question:
    1. Are there non-alphabetic characters?
    2. if so, should they be reversed alongside the letters in each word?
'''
### P - Plan
'''
2. Write out in plain English what you want to do: 
    - make a result list
    - establish the queue as a quee version of the list
    - make a temp stack
    - in a while loop: go trhough the queue
        - remove the next element from the queue
        - if the character is a space: 
            - while stack is not empty:
                - pop stack element directly in to result list
            - add queue element into result
        - otherwise:
            - append element to the stack
    - while stack is not empty:
                    - pop stack element directly in to result list
    - return the result
3. Translate each sub-problem into pseudocode:
    result = []
    q = deque(post)
    stack = []
    while q:
        char = q.popleft()
        if char == " ":
            while stack: result.append(stack.pop())
            result.append(char)
        else:
            stack.append(char)
    while stack: result.append(stack.pop())
    return result
'''
### I - Implement
'''
4. Translate the pseudocode into Python and share your final answer:
'''
from collections import deque
def edit_post(post):
    result = []
    q = deque(post)
    stack = []
    while q:
        char = q.popleft()
        if char == " ":
            while stack: result.append(stack.pop())
            result.append(char)
        else:
            stack.append(char)
    while stack: result.append(stack.pop())
    return "".join(result)

#Problem 6 Examples:
print("Problem 6 Output:")            # expecting: ( add this line to print statements)
print(edit_post("Boost your engagement with these tips")) 
print(edit_post("Check out my latest vlog")) 
# -------------------------------------------------------------------------------------------------

