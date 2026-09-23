# Unit 1: Strings & Arrays

## Session 1: Advanced Problems

---

### Problem 1: Hunny Hunt

Write a function `linear_search()` to help Winnie the Pooh locate his lost items. The function accepts a list `items` and a target value `target` as parameters. The function should return the first index of `target` in `items`, and `-1` if `target` is not in `items`. 

> **Note:** Do not use any built-in functions.

#### Function Signature
```python
def linear_search(items, target):
    pass
```

#### Example Usage
```python
items = ['haycorn', 'haycorn', 'haycorn', 'hunny', 'haycorn']
target = 'hunny'
print(linear_search(items, target))
# Output: 3

items = ['bed', 'blue jacket', 'red shirt', 'hunny']
target = 'red balloon'
print(linear_search(items, target))
# Output: -1
```

---

### Problem 2: Bouncy, Flouncy, Trouncy, Pouncy

Tigger has developed a new programming language **Tiger** with only four operations and one variable `tigger`.

* `bouncy` and `flouncy` both increment the value of `tigger` by $1$.
* `trouncy` and `pouncy` both decrement the value of `tigger` by $1$.

Initially, the value of `tigger` is $1$ because he's the only tigger around! Given a list of strings `operations` containing a list of operations, return the final value of `tigger` after performing all operations.

#### Function Signature
```python
def final_value_after_operations(operations):
    pass
```

#### Example Usage
```python
operations = ["trouncy", "flouncy", "flouncy"]
print(final_value_after_operations(operations))
# Output: 2

operations = ["bouncy", "bouncy", "flouncy"]
print(final_value_after_operations(operations))
# Output: 4
```

---

### Problem 3: T-I-Double Guh-Er II

T-I-Double Guh-Er: That spells Tigger! 

Write a function `tiggerfy()` that accepts a string `word` and returns a new string that removes any substrings `"t"`, `"i"`, `"gg"`, and `"er"` from `word`. The function should be **case-insensitive**.

#### Function Signature
```python
def tiggerfy(word):
    pass
```

#### Example Usage
```python
word = "Trigger"
print(tiggerfy(word))
# Output: "r"

word = "eggplant"
print(tiggerfy(word))
# Output: "eplan"

word = "Choir"
print(tiggerfy(word))
# Output: "Chor"
```

---

### Problem 4: Non-decreasing Array

Given an array `nums` with $n$ integers, write a function `non_decreasing()` that checks if `nums` could become non-decreasing by modifying at most one element.

We define an array as non-decreasing if `nums[i] <= nums[i + 1]` holds for every $i$ ($0$-based) such that $0 \le i \le n - 2$.

#### Function Signature
```python
def non_decreasing(nums):
    pass
```

#### Example Usage
```python
nums = [4, 2, 3]
print(non_decreasing(nums))
# Output: True

nums = [4, 2, 1]
print(non_decreasing(nums))
# Output: False
```

---

### Problem 5: Missing Clues

Christopher Robin set up a scavenger hunt for Pooh, but it's a blustery day and several hidden clues have blown away. Write a function `find_missing_clues()` to help Christopher Robin figure out which clues he needs to remake. 

The function accepts two integers `lower` and `upper` and a unique integer array `clues`. All elements in `clues` are within the inclusive range $[\text{lower}, \text{upper}]$.

A clue $x$ is considered missing if $x$ is in the range $[\text{lower}, \text{upper}]$ and $x$ is not in `clues`.

Return the shortest sorted list of ranges that exactly covers all missing numbers. That is, no element of `clues` is included in any of the ranges, and each missing number is covered by one of the ranges.

#### Function Signature
```python
def find_missing_clues(clues, lower, upper):
    pass
```

#### Example Usage
```python
clues = [0, 1, 3, 50, 75]
lower = 0
upper = 99
print(find_missing_clues(clues, lower, upper))
# Output: [[2, 2], [4, 49], [51, 74], [76, 99]]

clues = [-1]
lower = -1
upper = -1
print(find_missing_clues(clues, lower, upper))
# Output: []
```



## Session 1: Standard Problems

### Problem 10: Split Haycorns

Piglet has collected a big pile of his favorite food, haycorns, and wants to split them evenly amongst his friends. Write a function `split_haycorns()` to help Piglet determine the number of ways he can split his haycorns into even groups. `split_haycorns()` accepts a positive integer `quantity` as a parameter and returns a list of all divisors of `quantity`.

```python
def split_haycorns(quantity):
    pass
```

#### Example Usage:

```python
quantity = 6
split_haycorns(quantity)

quantity = 1
split_haycorns(quantity)
```

#### Example Output:

```python
[1, 2, 3, 6]
[1]
```

---

### Problem 11: T-I-Double Guh-ER

Signs in the Hundred Acre Wood have been losing letters as Tigger bounces around stealing any letters he needs to spell out his name. Write a function `tiggerfy()` that accepts a string `s`, and returns a new string with the letters `t`, `i`, `g`, `e`, and `r` removed from it.

```python
def tiggerfy(s):
    pass
```

#### Example Usage:

```python
s = "suspicerous"
tiggerfy(s)

s = "Trigger"
tiggerfy(s)

s = "Hunny"
tiggerfy(s)
```

#### Example Output:

```python
"suspcous"
""
"Hunny"
```

---

### Problem 12: Thistle Hunt

Pooh, Piglet, and Roo are looking for thistles to gift their friend Eeyore. Write a function `locate_thistles()` that takes in a list of strings `items` and returns a list of the indices of any elements with value `"thistle"`. The indices in the resulting list should be ordered from least to greatest.

```python
def locate_thistles(items):
    pass
```

#### Example Usage:

```python
items = ["thistle", "stick", "carrot", "thistle", "eeyore's tail"]
locate_thistles(items)

items = ["book", "bouncy ball", "leaf", "red balloon"]
locate_thistles(items)
```

#### Example Output:

```python
[0, 3]
[]
```




## Session 2

### Problem 3: Delete Minimum

Pooh is eating all of his hunny jars in order of smallest to largest. Given a list of integers `hunny_jar_sizes`, write a function `delete_minimum_elements()` that continuously removes the minimum element until the list is empty. Return a new list of the elements of `hunny_jar_sizes` in the order in which they were removed.

```python
def delete_minimum_elements(hunny_jar_sizes):
    pass
```

#### Example Usage:

```python
hunny_jar_sizes = [5, 3, 2, 4, 1]
delete_minimum_elements(hunny_jar_sizes)

hunny_jar_sizes = [5, 2, 1, 8, 2]
delete_minimum_elements(hunny_jar_sizes)
```

#### Example Output:

```python
[1, 2, 3, 4, 5]
[1, 2, 2, 5, 8]
```

---

### Problem 4: Sum of Digits

Write a function `sum_of_digits()` that accepts an integer `num` and returns the sum of `num`'s digits.

```python
def sum_of_digits(num):
    pass
```

#### Example Usage:

```python
num = 423
sum_of_digits(num)

num = 4
sum_of_digits(num)
```

#### Example Output:

```python
9  # Explanation: 4 + 2 + 3 = 9
4
```

---

### Problem 5: Bouncy, Flouncy, Trouncy, Pouncy

Tigger has developed a new programming language Tiger with only four operations and one variable `tigger`.

* `bouncy` and `flouncy` both **increment** the value of the variable `tigger` by 1.
* `trouncy` and `pouncy` both **decrement** the value of the variable `tigger` by 1.

Initially, the value of `tigger` is 1 because he's the only tigger around! Given a list of strings `operations` containing a list of operations, return the final value of `tigger` after performing all the operations.

```python
def final_value_after_operations(operations):
    pass
```

#### Example Usage:

```python
operations = ["trouncy", "flouncy", "flouncy"]
final_value_after_operations(operations)

operations = ["bouncy", "bouncy", "flouncy"]
final_value_after_operations(operations)
```

#### Example Output:

```python
2
4
```