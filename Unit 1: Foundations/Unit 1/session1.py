# Session 1 Version 1

#Problem 10: Split Haycorns
## WHY THIS PROBLEM? These problems should be familarly simple, so I wanted to practice the problems later in the set because they are a bit more difficult.
### U - Understand 
'''
1. Share 2 questions you would ask to help understand the question:
    1. how do we know what numbers we need to return?
    2. what about if the number is 0?
'''
### P - Plan
'''
2. Write out in plain English what you want to do: 
    - in a for loop: iterate 1 to n-1 times
        - if the quantity is divisible by the iteration number, it should be included in the output list
    - afterwards, return the output list.
3. Translate each sub-problem into pseudocode:
    output = []
    for i in range(quantity):
        if quantity % (i+1) == 0:
            output.append(i+1)
    return output
'''
### I - Implement
'''
4. Translate the pseudocode into Python and share your final answer:
'''
def split_haycorns(quantity):
    output = []
    for i in range(quantity):
        if quantity % (i+1) == 0:
            output.append(i+1)
    print(output)
#Problem 10 Examples:
print("Problem 10 Output:")            # expecting: ( add this line to print statements)
quantity = 6
split_haycorns(quantity)
quantity = 1
split_haycorns(quantity)


#Problem 11: T-I-Double Guh-ER
## WHY THIS PROBLEM? this one relies on students being a little more familiar with python string methods, and may need help from the cheatsheet.
### U - Understand 
'''
1. Share 2 questions you would ask to help understand the question:
    1. how can we remove specific letters from a list?
'''
### P - Plan
'''
2. Write out in plain English what you want to do:
    - make a set of the letters to be removed.
    - make an empty list
    - in a for loop: go through the string
        - if the character is NOT in the set, add it to the output list
    - retun a joined vers. of the output list.

3. Translate each sub-problem into pseudocode:
    remove = {'t', 'i', 'g', 'e', 'r'}
    output = []
    for char in s:
        if lowercase(char) not in remove:
            output.append(char)
    return "".join(output)

'''
### I - Implement
'''
4. Translate the pseudocode into Python and share your final answer:
'''
def tiggerfy(s):
    remove = {'t', 'i', 'g', 'e', 'r'}
    output = []
    for char in s:
        if char.lower() not in remove:
            output.append(char)
    print ("".join(output))
#Problem 11 Examples:
print("Problem 11 Output:")            # expecting: ( add this line to print statements)
s = "suspicerous"
tiggerfy(s)
s = "Trigger"
tiggerfy(s)
s = "Hunny"
tiggerfy(s)



#Problem 12: Thistle Hunt
## WHY THIS PROBLEM? This is the last problem, so it should be a bit more difficult!
### U - Understand 
'''
1. Share 2 questions you would ask to help understand the question:
    - what if 'thistle' isn't in the list?
    - should we account from capitalization?
'''
### P - Plan
'''
2. Write out in plain English what you want to do: 
    - make an empty output list
    - in a for loop: go through each item
        - if the item is equal to 'thistle', we add the index to the output list
    - print output list

3. Translate each sub-problem into pseudocode:
    output = []
    for i in range(items):
        if items[i].lower() == 'thistle':
            output.append(i)
    print output
'''
### I - Implement
'''
4. Translate the pseudocode into Python and share your final answer:
'''
def locate_thistles(items):
    output = []
    for i in range(len(items)):
        if items[i].lower() == 'thistle':
            output.append(i)
    print (output)
#Problem 12 Examples:
print("Problem 12 Output:")            # expecting: ( add this line to print statements)
items = ["thistle", "stick", "carrot", "thistle", "eeyore's tail"]
locate_thistles(items)
items = ["book", "bouncy ball", "leaf", "red balloon"]
locate_thistles(items)