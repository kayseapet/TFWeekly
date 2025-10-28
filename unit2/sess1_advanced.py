# Unit 2, Session 1 Advanced Set Version 1

# PROBLEM 1
### U - Understand 
'''
1. Share 2 questions you would ask to help understand the question:
  - To clarify, can we assume all the dictionary values will be an integer, or should we test for other posible variables?
  - Can the integer be a negative number, and does that change how the function should proceed?
'''
### P - Plan
'''
2. Write out in plain English what you want to do: 
  - collect all values from the given dictionary into a list
  - add all the values together
  - return the sum

3. Translate each sub-problem into pseudocode:
  def total_treasure(treasure_map):
    treasure = treasure_map.values()
    return sum(treasure)
'''
### I - Implement
'''
4. Translate the pseudocode into Python and share your final answer:
'''
def total_treasures(treasure_map):
    treasure = treasure_map.values()
    return(sum(treasure))
    

# PROBLEM 2
### U - Understand 
'''
1. Share 2 questions you would ask to help understand the question:
  - Is there a specific way i should solve this other than using a for-loop?
  - To clarify, this function does not need to be case sensitive?
'''
### P - Plan
'''
2. Write out in plain English what you want to do: 
  - make a set of the alphabet, and a set containing the message
  - find if the message has all letters of the alphabet
  - return true/false based on that result

3. Translate each sub-problem into pseudocode:
  def can_trust_message(message):
    msg = set(message)
    abc = {a,b,c,..., z}
    if letter is in abc but not msg:
      return False
    else:
      return true
'''
### I - Implement
'''
4. Translate the pseudocode into Python and share your final answer:
'''
def can_trust_message(message):
    msg = set(message)
    abc = {"a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"}
    if len(abc - msg)>=1:
        return False
    else:
        return True 


#PROBLEM 3
### U - Understand 
'''
1. Share 2 questions you would ask to help understand the question:
  - Is there a specific data variable we should use (list,dict, set)?
  - To clarify, we are return the list of elements that ARE duplicates, correct?
'''
### P - Plan
'''
2. Write out in plain English what you want to do: 
  - I want to make a frequency dictionary that counts the amount of times a number is shown in a list
  - given that dictionary, for each number that shows up more than once, their add to the duplicates list
  - return the list of duplicates

3. Translate each sub-problem into pseudocode:
  def duplicates(chests):
    freq = counter(chests)
    dups = []
    for i in range(chests):
      if freq[i] > 1:
        dups.append(i)
    return dups
'''
### I - Implement
'''
4. Translate the pseudocode into Python and share your final answer:
'''
from collections import Counter
def find_duplicate_chests(chests):
    freq_map = Counter(chests)
    duplicates = []
    for i in range(len(chests)):
        if freq_map[i] > 1:
            duplicates.append(i)
    return duplicates


# PROBLEM 4
### U - Understand 
'''
1. Share 2 questions you would ask to help understand the question:
  - To clarify, the only return value is true/false for if it can be balanced?
  - what is the result in the event the code is an empty string?
'''
### P - Plan
'''
2. Write out in plain English what you want to do: 
  - get a frequency map for the letters in the code
  - turn the values of the frequency map into a set
  - if there are not 2 values in the set, the code cannot be balanced with one removal.
  
3. Translate each sub-problem into pseudocode:
  def can_make_balanced(code):
    freq_map = Counter(code)
    counts = set(freq_map.values())
    if len(counts) != 2:
      return False
    return True
'''
### I - Implement
'''
4. Translate the pseudocode into Python and share your final answer:
'''
def can_make_balanced(code):
    freq_map = Counter(code)
    counts = set(freq_map.values())
    if len(counts) != 2:
      return False
    return True


#PROBLEM 5
### U - Understand 
'''
1. Share 2 questions you would ask to help understand the question:
  - Is there a more optimized way to do this of than a nested loop?
  - Is the list of gold amounts sorted or unsorted?
'''
### P - Plan
'''
2. Write out in plain English what you want to do: 
  - nested loop that compares every combination of two indices until it matches the gold amount

3. Translate each sub-problem into pseudocode:
  def function(gold, target):
    for i in (0, len(gold)):
      for j in (i, len(gold)):
        if gold[i] + gold[j] == target:
          return([i,j])
'''
### I - Implement
'''
4. Translate the pseudocode into Python and share your final answer:
'''
def find_treasure_indices(gold_amounts, target):
    for i in range(len(gold_amounts)):
      for j in range(i+1,len(gold_amounts)):
          if gold_amounts[i]+gold_amounts[j] == target:
              lst = []
              lst.append(i)
              lst.append(j)
              return lst
