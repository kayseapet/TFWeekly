#Unit 2 Session 1 Version 1


#Problem 9: Stage Arrangement Difference Between Two Performances
### U - Understand 
'''
1. Share 2 questions you would ask to help understand the question:
    1. does the starting order of elements also go in the count?
    2. can the s and t lists be empty, and if so what occurs then?
'''
### P - Plan
'''
2. Write out in plain English what you want to do:
    - frequency map
        - in a for loop:
            - get the values at Sthe index for list s
        - make variable
        - in a for loop:
            - get the absolute difference of the current string and the value at map[string]
            - add it to the variable
        -return variable

3. Translate each sub-problem into pseudocode:
    map = {}
    for i in range(len(s)):
        map[s[i]] = i
    diff = 0
    for j in range(len(t)):
        word = t[j]
        diff += abs(map[word] - j)
    return diff
'''
### I - Implement
'''
4. Translate the pseudocode into Python and share your final answer:
'''
def find_stage_arrangement_difference(s, t):
    map = {}
    for i in range(len(s)):
        map[s[i]] = i
    diff = 0
    for j in range(len(t)):
        word = t[j]
        diff += abs(map[word] - j)
    return diff
#Problem 9 Examples:
print("Problem 9 Output:")            # expecting: ( add this line to print statements)
s1 = ["Alice", "Bob", "Charlie"]
t1 = ["Bob", "Alice", "Charlie"]
s2 = ["Alice", "Bob", "Charlie", "David", "Eve"]
t2 = ["Eve", "David", "Bob", "Alice", "Charlie"]
print(find_stage_arrangement_difference(s1, t1))
print(find_stage_arrangement_difference(s2, t2))






#Problem 11: Performer Schedule Pattern
### U - Understand 
'''
1. Share 2 questions you would ask to help understand the question:
    1. what happens if the length of the string doesn't match the length of the list?
    2. Can pattern or schedule be empty strings? How should we handle null or empty inputs?

'''
### P - Plan
'''
2. Write out in plain English what you want to do: 
    - look at the given code and determine what is SUPPOSED to be happening.
    - determine what is actually happening, and then adjust to fix the bug.

3. Translate each sub-problem into pseudocode:

    ...

     if len(genres) == len(pattern):   <-- Reverse this statement
        return True
    ...
         if char in char_to_genre:
            if char_to_genre[char] == genre:  <--- combine to the if statement above and flip second condition (!=)
                return True         <--- return false
        else:
            char_to_genre[char] = genre         <--- sent to end of for loop

        (Repeat with other if condition)

    ...
     return False           < --- return True

 
'''
### I - Implement
'''
4. Translate the pseudocode into Python and share your final answer:
'''
def schedule_pattern(pattern, schedule):
    
    genres = schedule.split()

    if len(genres) != len(pattern):
        return False

    char_to_genre = {}
    genre_to_char = {}

    for char, genre in zip(pattern, genres):
        if char in char_to_genre and char_to_genre[char] != genre:
                return False

        if genre in genre_to_char and genre_to_char[genre] != char:
                return False

        char_to_genre[char] = genre
        genre_to_char[genre] = char

    return True
#Problem 11 Examples:
print("Problem 11 Output:")            # expecting: ( add this line to print statements)
pattern1 = "abba"
schedule1 = "rock jazz jazz rock"
pattern2 = "abba"
schedule2 = "rock jazz jazz blues"
pattern3 = "aaaa"
schedule3 = "rock jazz jazz rock"
print(schedule_pattern(pattern1, schedule1))
print(schedule_pattern(pattern2, schedule2))
print(schedule_pattern(pattern3, schedule3))






#Problem 12: Sort the Performers
### U - Understand 
'''
1. Share 2 questions you would ask to help understand the question:
    1. Can 'n' be 0 or 1?
    2. Are duplicate performer names possible?
'''
### P - Plan
'''
2. Write out in plain English what you want to do: 
    - zip together the performance names and times 
    - sort the times, and add them to a dictionary list
    - then extraxt just the names from the dict and copy to empty list
    - return the list
3. Translate each sub-problem into pseudocode:
    both = defualtdict(list)
    for n, t in zip(performer_names, performer_times):
        both[t].append(n)
    sortt = sorted(both.keys())
    sortt = sort[::-1]
    result = []
    for time in sortt:
        for name in both[time]:
            result.append(name)
    return result
'''
### I - Implement
'''
4. Translate the pseudocode into Python and share your final answer:
'''
def sort_performers(performer_names, performance_times):
    both = {}
    for n, t in zip(performer_names, performance_times):
        both[t] = n
    sortt = sorted(both.keys())
    sortt = sortt[::-1]
    result = []
    for time in sortt:
        result.append(both[time])
    return result
#Problem 12 Examples:
print("Problem 12 Output:")            # expecting: ( add this line to print statements)
performer_names1 = ["Mary", "John", "Emma"]
performance_times1 = [180, 165, 170]

performer_names2 = ["Alice", "Bob", "Bob"]
performance_times2 = [155, 185, 150]

print(sort_performers(performer_names1, performance_times1)) 
print(sort_performers(performer_names2, performance_times2))


