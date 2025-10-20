### Unit 1: Strings \& Arrays



##### Session 1 Advanced Problems:



Problem 1: Hunny Hunt

Write a function linear\_search() to help Winnie the Pooh locate his lost items. The function accepts a list items and a target value as parameters. The function should return the first index of target in items, and -1 if target is not in items. Do not use any built-in functions.



Example Usage:

items = \['haycorn', 'haycorn', 'haycorn', 'hunny', 'haycorn']

target = 'hunny'

linear\_search(items, target)



items = \['bed', 'blue jacket', 'red shirt', 'hunny']

target = 'red balloon'

linear\_search(items, target)



Example Output:

3

-1



Problem 2: Bouncy, Flouncy, Trouncy, Pouncy

Tigger has developed a new programming language Tiger with only four operations and one variable tigger.

bouncy and flouncy both increment the value of the variable tigger by 1.

trouncy and pouncy both decrement the value of the variable tigger by 1.

Initially, the value of tigger is 1 because he's the only tigger around! Given a list of strings operations containing a list of operations, return the final value of tigger after performing all the operations.



Example Usage:

operations = \["trouncy", "flouncy", "flouncy"]

final\_value\_after\_operations(operations)



operations = \["bouncy", "bouncy", "flouncy"]

final\_value\_after\_operations(operations)



Example Output:

2

4



Problem 3: T-I-Double Guh-Er II

T-I-Double Guh-Er: That spells Tigger! Write a function tiggerfy() that accepts a string word and returns a new string that removes any substrings t, i, gg, and er from word. The function should be case insensitive.



def tiggerfy(word):

&nbsp;	pass

Example Usage:



word = "Trigger"

tiggerfy(word)



word = "eggplant"

tiggerfy(word)



word = "Choir"

tiggerfy(word)

Example Output:



"r"

"eplan"

"Chor"





Problem 4: Non-decreasing Array

Given an array nums with n integers, write a function non\_decreasing() that checks if nums could become non-decreasing by modifying at most one element.



We define an array is non-decreasing if nums\[i] <= nums\[i + 1] holds for every i (0-based) such that (0 <= i <= n - 2).



def non\_decreasing(nums):

&nbsp;	pass

Example Usage:



nums = \[4, 2, 3]

non\_decreasing(nums)



nums = \[4, 2, 1]

non\_decreasing(nums)

Example Output:



True

False





Problem 5: Missing Clues

Christopher Robin set up a scavenger hunt for Pooh, but it's a blustery day and several hidden clues have blown away. Write a function find\_missing\_clues() to help Christopher Robin figure out which clues he needs to remake. The function accepts two integers lower and upper and a unique integer array clues. All elements in clues are within the inclusive range \[lower, upper].

A clue x is considered missing if x is in the range \[lower, upper] and x is not in clues.

Return the shortest sorted list of ranges that exactly covers all the missing numbers. That is, no element of clues is included in any of the ranges, and each missing number is covered by one of the ranges.



def find\_missing\_clues(clues, lower, upper):

&nbsp;  pass

Example Usage:



clues = \[0, 1, 3, 50, 75]

lower = 0

upper = 99

find\_missing\_clues(clues, lower, upper)



clues = \[-1]

lower = -1

upper = -1

find\_missing\_clues(clues, lower, upper)

Example Output:



\[\[2, 2], \[4, 49], \[51, 74], \[76, 99]]

\[]



