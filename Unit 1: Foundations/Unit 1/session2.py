# Session 2 Version 1 Problems

# PROBELM 3: Delete Minimum
### U - Understand 
''' 1. Share 2 questions you would ask to help understand the question:
    - Can we use built-in functions here?
    - Which type of loop should I use for this?

'''
### P - Plan
'''
    2. Write out in plain English what you want to do:
    - I want to make a while loop that continues until the given list is empty
    - first I'd find the index of the min number, then pop it from the list
    - I'd add them to a new list as they're removed, and return the new list.
    

    3. Translate each sub-problem into pseudocode:
    def min_ele(list1):
        list2 = []
        while(list1):
            min_index =  index of min(list1)
            new = list1.pop(min_index)
            list2.append(new)
        return list2

'''
### I - Implement
''' 4. Translate the pseudocode into Python and share your final answer:'''
def delete_minimum_elements(hunny_jar_sizes):
    new_list = []
    while (hunny_jar_sizes):
        mini = hunny_jar_sizes.index(min(hunny_jar_sizes))
        num = hunny_jar_sizes.pop(mini)
        new_list.append(num)
    print (new_list)
#Problem 3 Examples:
print("Problem 3 Output:")            # expecting: ( add this line to print statements)
hunny_jar_sizes = [5, 3, 2, 4, 1]
delete_minimum_elements(hunny_jar_sizes)
hunny_jar_sizes = [5, 2, 1, 8, 2]
delete_minimum_elements(hunny_jar_sizes)





#PROBLEM 4:  Sum of Digits
### U - Understand 
''' 1. Share 2 questions you would ask to help understand the question:
    - Is the parameter taken as a string?
    - Can we use built-in functions for this?

'''
### P - Plan
'''
    2. Write out in plain English what you want to do:
    - I'm going to get each digit by turn the int into a str
    - I can use the a for loop to add each number together
    - and return the sum 

    3. Translate each sub-problem into pseudocode:
    def func (num):
        string = str(num)
        for each num in string:
            sum += num
        return sum

'''
### I - Implement
''' 4. Translate the pseudocode into Python and share your final answer:'''
def sum_of_digits(num):
    word = str(num)
    sum = 0
    for n in word:
        sum += int(n)
    print(sum)
#Problem 4 Examples:
print("Problem 4 Output:")            # expecting: ( add this line to print statements)
num = 423
sum_of_digits(num)
num = 4
sum_of_digits(num)






# PROBLEM 5: Bouncy, Flouncy, Trouncy, Pouncy
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
#Problem 5 Examples:
print("Problem 5 Output:")            # expecting: ( add this line to print statements)
operations = ["trouncy", "flouncy", "flouncy"]
final_value_after_operations(operations)
operations = ["bouncy", "bouncy", "flouncy"]
final_value_after_operations(operations)
