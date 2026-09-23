# Session 1 - Advanced Version 1
# Kayla Peters

# Problem 1 - Hunny Hunt
### U - Understand 
#1. Share 2 questions you would ask to help understand the question:
'''
    2 Questions I would ask:
    1. The question says " do not use any built-in functions". What is a built-in function?
    2. What should the program do if the iteams in the list are not all strings?
'''

### P - Plan
#2. Write out in plain English what you want to do: 
'''
    I want to make a function that, after acceptig the needed parameters, runs a for-loop in the range of zero to the length of the items list.
    Inside the loop, the program will compare the target to a single item in the items list, using the loop iteration number as an index number of the list.
    If the target is found during an iteration, the program will end and return the index number the target was found at.
    If the target is not found, the program will countinue to the next iteration.
    If the loop is completed without finding the target, that means the target was not in the list so the program returns -1.  
'''

#3. Translate each sub-problem into pseudocode:
'''
    def linear_search(items, target)
    {
        for index in items:
            if items(index) == target
            {
                return index
            }
            else
            {
                continue
            }
        
        return -1
    
    }
'''



### I - Implement
#4. Translate the pseudocode into Python and share your final answer:
def linear_search(items, target):
    for ind in range(0,len(items)):
        if items[ind] is target:
            print(ind)
            return 
        else:
            continue
    print(-1)
    return 


#PROBLEM 2 - Bouncy,Flouncy,Trouncy,Pouncy
### U - Understand 
''' 1. Share 2 questions you would ask to help understand the question:
    - why isnt their a parameter for the tigger variable?
    - What should the program do if a string in operations is not one of the four accepted operations?
'''
### P - Plan
'''
    2. Write out in plain English what you want to do:
        I would first make the tigger variable, then I would make a for-loop to perform each operation in the list
        For each string in the operations list, if the string is "bouncy" or "flouncy" then +1 to tigger. If the string is "trouncy" or "pouncy", we -1 from tigger.
        After the for-loop is complete, I would return the final value of the tigger variable.

    3. Translate each sub-problem into pseudocode:
        def problem_2(operations):
            tigger = 1
            for str in operations:
                if str is "bouncy" or "flouncy":
                    tigger = tigger + 1
                if str is "trouncy" or "pouncy":
                    tigger = tigger + 1
            return tigger

'''
### I - Implement
''' 4. Translate the pseudocode into Python and share your final answer:'''
def final_value_after_operations(operations):
    tigger = 1
    for op in operations:
        if op == "bouncy" or op == "flouncy":
            tigger += 1
        elif op == "trouncy" or op == "pouncy":
            tigger -= 1
    print(tigger)
    return


# PROBLEM 3 
### U - Understand 
''' 1. Share 2 questions you would ask to help understand the question:
    - Should the function remove 'er' substrings that were only made from the removal of other characters?
    - Can we use built-in functions for this problem?

'''
### P - Plan
'''
    2. Write out in plain English what you want to do:
    - First i would make a list of all the substrings I want removed
    - I want to use the reg ex to look for the substrings in a case-insensitive way, so I would import re and use re.IGNORECASE when i'm searching
    -  to find the characters, I would use a for-loop to recall the same commands to delete the characters I want, and use the iteration number as my index for the substring list
    - the re.sub() command replaces a given pattern from a string with another given replacement subtring. I can replace the substring with an empty one to delete the characters.



    3. Translate each sub-problem into pseudocode:
        def tiggerfy(word):
            to_delete = ['t', 'i', 'gg', 'er']
            for substr in to_delete:
                word = word - substr (Case Insensitive)

            

'''
### I - Implement
''' 4. Translate the pseudocode into Python and share your final answer:'''
import re
def tiggerfy(word):
    new_word = word
    to_delete = ['t', 'i', 'gg', 'er']
    for substr in to_delete:
        new_word = re.sub(substr, "", new_word, flags=re.IGNORECASE)
    print(new_word)


# PROBLEM 4
### U - Understand 
''' 1. Share 2 questions you would ask to help understand the question:
    -  Is the only output a boolean? 
    -  What should the function return if the array is empty?
'''
### P - Plan
'''
    2. Write out in plain English what you want to do:
    - I want to have a count of the amount of time the array is decreasing using a for loop
    - At the end, if the count is less than 2, than that means the array could be non-decreasing by modifying at most one element
    - if the count is over 2, the array doesnt fit that description. 

    3. Translate each sub-problem into pseudocode:
        def non_decreasing(nums):
            count = 0
            for index in nums list:
                if nums[index] <= nums[index + 1]
                    continue
                else
                    count++
            if count < 2:
                return true
            else:
                return false


'''
### I - Implement
''' 4. Translate the pseudocode into Python and share your final answer:'''
def non_decreasing(nums):
    count = 0
    for i in range(0, len(nums)-1):
        if nums[i] <= nums[i+1]:
            continue
        else:
            count += 1
    if count < 2:
        print(True)
    else:
        print(False)


# PROBLEM 5
### U - Understand 
''' 1. Share 2 questions you would ask to help understand the question:
    - So the return value is a sorted list of ranges in which there arent any clues?
    - what happens if the given lower number is greater than the given upper number?
'''
### P - Plan
'''
    2. Write out in plain English what you want to do:
    - I want to start with a large range from lower to upper, and use a while loop to remove the clues
    - I'll treat the clues list like a stack, and remove each of them as a split the lists apart, so the loop will end when there are no more clues
    - for each clue, I'll find the range which contains it, and each that list to end right before the clue, and also add another list that start right after the clue
    - i can use the enumerate() to have both the index and the list.
    - if none of the ranges contain the clue, the loop will move on.

    3. Translate each sub-problem into pseudocode:
        def find_missin_clues(clues, lower, upper):
            all = [[lower, upper]]
            while (clues):
                -take one clue
                for index, list in enumerate(all):
                    if list[start] <= clue <= list[end]:
                        if start == clue:
                            all[index] = list[start+1,end]
                        elif end == clue:
                            all[index]= list[start, clue-1]
                        else:
                            all[index] = list[start, clue-1]
                            all.insert(index+1, list[clue+1, end])
                        stop for-loop
'''
### I - Implement
''' 4. Translate the pseudocode into Python and share your final answer:'''
def find_missing_clues(clues, lower, upper):
    all= [[lower,upper]]
    while (clues):
        clue = clues.pop(0)
        for i, lst in enumerate(all):
            start= lst[0]
            end = lst[1]
            if start == clue == end:
                del all[i]
                break

            if start <= clue <= end:
                if start == clue:
                    all[i] = [clue+1, end]
                elif end == clue:
                    all[i] = [start, clue-1]
                else:
                    all[i] = [start, clue-1]
                    all.insert(i+1, [clue+1, end])
                break
            continue
    print(all)

