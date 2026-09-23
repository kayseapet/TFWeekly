# Session 2 Standard Version 1

# PROBLEM 1
### U - Understand 
''' 1. Share 2 questions you would ask to help understand the question:
    - Are we allowed to use built-in functions here?
    - What should the function do if the sentence variable is empty
'''
### P - Plan
'''
    2. Write out in plain English what you want to do:
    - I first want to split the sentence into a list with each word split by where the spaces are in the string
    - then I would use the two pointer method to swap the first and last indexes in place, and go inwards until each index is swapped
    - lastly, i'll rejoin the list into a string, and add back the spaces.

    3. Translate each sub-problem into pseudocode:
    def rev_sen(sentence):
        lst = sentence.split(" ")
        if len(lst) < 2:
            return sentence
        first = 0
        last = len(lst) - 1
        while (last > first):
            temp = lst[first]
            swap first and last
            first++
            last--
        rev = lst.join(" ")
        return rev


'''
### I - Implement
''' 4. Translate the pseudocode into Python and share your final answer:'''
def reverse_sentence(sentence):
    lst = sentence.split(" ")
    if len(lst) <2:
        print(sentence)
        return sentence
    else:
        first = 0 
        last = len(lst)-1
        while (first <last):
            temp= lst[first]
            lst[first] = lst[last]
            lst[last] = temp
            first +=1
            last -= 1
        reverse = " ".join(lst)
        print(reverse)

# PROBLEM 2
### U - Understand 
''' 1. Share 2 questions you would ask to help understand the question:
    - Can we use built in functions for this one?
    - Does it have to be the first number that isnt the max or min?
'''
### P - Plan
'''
    2. Write out in plain English what you want to do:
    - I plan to first get the max() and min() numbers
    - then I'll a for-loop that goes through all  the nums
    - the first number that isnt the max or min, the for-loop will stop and return that number

    3. Translate each sub-problem into pseudocode:
        def goldilock(nums):
            max = max(nums)
            min = min(nums)

            for num in nums:
                if not max or min:
                    return num

'''
### I - Implement
''' 4. Translate the pseudocode into Python and share your final answer:'''
def goldilocks_approved(nums):
    maxx = max(nums)
    minn = min(nums)
    for num in nums:
        if num != maxx and num != minn:
            print(num)
            return
    print(-1)
    return -1



# PROBELM 3
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


#PROBLEM 4
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

num = 423
sum_of_digits(num)

num = 4
sum_of_digits(num)

# PROBLEM 5
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