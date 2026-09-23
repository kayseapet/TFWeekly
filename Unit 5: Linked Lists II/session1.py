# Unit 5 Advanced Problem Set Version 1
"NOTE: For this session, I'll the Understand & Part for problems 2-4, and have the Implementation for all three problems in one group. Problem 6 & 7 are as normal."

#  ----------------------------------------------------------------
    # Classes & Functions needed for testing (problems 6 & 7)
class Node:
    def __init__(self, fish_name, next=None):
        self.fish_name = fish_name
        self.next = next
def print_linked_list(head):
    current = head
    while current:
        print(current.fish_name, end=" -> " if current.next else "\n")
        current = current.next
#  ----------------------------------------------------------------        

#Problem 2: Add Furniture
### U - Understand 
'''
1. Share 2 questions you would ask to help understand the question:
    1. can I use a blank return to end the function?
    2. Can the item be added if it has a substring matching one of the values, for example can "black acoustic guitar" be added?
'''
### P - Plan
'''
2. Write out in plain English what you want to do: 
    - establish set with all accepted values,
         - Making it a set bc searching a set in python has an avg. O(1) time complexity.
    - if item_name is in the set, we add it to villager's funiture list.
3. Translate each sub-problem into pseudocode:
    set = {"acoustic guitar", "ironwood kitchenette", "rattan armchair", "kotatsu", "cacao tree"}
        if item_name in set: self.furniture.append(item_name)
        pass
'''


#Problem 3: Group by Personality
### U - Understand 
'''
1. Share 2 questions you would ask to help understand the question:
    1. Can we assume the list ONLY has Villagers?
    2. Should we assume that personality_type is a string?
'''
### P - Plan
'''
2. Write out in plain English what you want to do: 
    - create filtered list
    - in a for loop:
        - for each villager, if their personality is the personality we're searching for, add the Villager's name to the filtered list.
    - return the filtered list
3. Translate each sub-problem into pseudocode:
    filtered = []
    for townie in townies:
         if townie.personality == personality_type
            append townie.name
    return filtered
'''


#Problem 4: Telephone
### U - Understand 
'''
1. Share 2 questions you would ask to help understand the question:
    1. This reminds me of linked lists, would that make each Villager a node?
    2. To clarify, each can only have one other villager as their neighbor?
'''
### P - Plan
'''
2. Write out in plain English what you want to do: 
    - Edge case, If the villager is None OR the villager's neighbor is None:
        - return false
    - create 'current' Villager variable, and set it to the start_villager
    - In a while loop: while the current villager is not None
        - if the current villager's name is the target_villager's name:
            - return true
        - Other wise, move current to their neighbor
    - now, return false
3. Translate each sub-problem into pseudocode:
    if start_villager is None:
        return False
    curr = start_villager
    while curr is not None:
        if curr == target_villager:
            return True
        curr = curr.neighbor
    return False
'''

# ----------------------------------IMPLEMENTATION FOR PROBLEMS(2,3,4)----------------------------
class Villager:
    def __init__(self, name, species, personality=None ,catchphrase=None, neighbor=None):
        self.name = name
        self.species = species
        self.personality = personality
        self.catchphrase = catchphrase
        self.furniture = []
        self.neighbor = neighbor

    'Problem 2:'
    def add_item(self, item_name):
        set = {"acoustic guitar", "ironwood kitchenette", "rattan armchair", "kotatsu", "cacao tree"}
        if item_name in set: self.furniture.append(item_name)
        pass

'   Problem 3:'
def of_personality_type(townies, personality_type):
    filtered = [townie.name for townie in townies if townie.personality == personality_type]
    return filtered

'   Problem 4'
def message_received(start_villager, target_villager):
    if start_villager is None:
        return False
    curr = start_villager
    while curr is not None:
        if curr == target_villager:
            return True
        curr = curr.neighbor
    return False
# --------------------------------------------TESTING------------------------------------------------
    #Problem 2 Examples:
print("Problem 2 Output:")            
alice = Villager("Alice", "Koala", "guvnor")
print(alice.furniture)            # expecting:[]
alice.add_item("acoustic guitar")
print(alice.furniture)            # expecting:["acoustic guitar"]
alice.add_item("cacao tree")
print(alice.furniture)            # expecting:["acoustic guitar", "cacao tree"]
alice.add_item("nintendo switch")
print(alice.furniture)            # expecting:["acoustic guitar", "cacao tree"]

    #Problem 3 Examples:
print("Problem 3 Output:")
isabelle = Villager("Isabelle", "Dog", "Normal", "what's up?")
bob = Villager("Bob", "Cat", "Lazy", "pthhhpth")
stitches = Villager("Stitches", "Cub", "Lazy", "stuffin'")
print(of_personality_type([isabelle, bob, stitches], "Lazy"))   # expecting:['Bob', 'Stitches']
print(of_personality_type([isabelle, bob, stitches], "Cranky")) # expecting:[]

 #Problem 4 Examples:
print("Problem 4 Output:")   
sabelle = Villager("Isabelle", "Dog", "Normal", "what's up?")
tom_nook = Villager("Tom Nook", "Raccoon", "Cranky", "yes, yes")
kk_slider = Villager("K.K. Slider", "Dog", "Lazy", "dig it")
isabelle.neighbor = tom_nook
tom_nook.neighbor = kk_slider
print(message_received(isabelle, kk_slider))    # expecting: True
print(message_received(kk_slider, isabelle))    # expecting: False
# --------------------------------------------------------------------------------------------------

#Problem 6: Got One!
### U - Understand 
'''
1. Share 2 questions you would ask to help understand the question:
    1. Is it for the last 'fish' to point to the first, and if so would the function work the same?
    2. Is there a guarantee that the Node.next is pointing to another Node, meaning there are no other data types there? 
'''
### P - Plan
'''
2. Write out in plain English what you want to do: 
    - Edge case: If 'head' is None:
        - print "Aw! Better luck next time!"
        - return None
    - print "I caught a {head's fishname}!"
    -  return head.next
3. Translate each sub-problem into pseudocode:
    if head is None:
        print("Aw! Better luck next time!")
        return None
    print("I caught a ",head.fish_name,"!")
    return head.next
'''
### I - Implement
'''
4. Translate the pseudocode into Python and share your final answer:
'''
def catch_fish(head):
    if head is None:
        print("Aw! Better luck next time!")
        return None
    print("I caught a ",head.fish_name,"!")
    return head.next
#Problem 6 Examples:
print("Problem 6 Output:")            # expecting: ( add this line to print statements)
fish_list = Node("Carp", Node("Dace", Node("Cherry Salmon")))
empty_list = None
print_linked_list(fish_list)# Carp -> Dace -> Cherry Salmon
print_linked_list(catch_fish(fish_list))# I caught a Carp!  #new fishlist=  Dace -> Cherry Salmon
print(catch_fish(empty_list))# Aw! Better luck next time!   # new fishlist = None


#Problem 7: Fishing Probability
### U - Understand 
'''
1. Share 2 questions you would ask to help understand the question:
    1. does the function act differently if the head or fish_name is None?
    2. Is the linked list circular? meaning, is the last fish's next set to the head fish?
'''
### P - Plan
'''
2. Write out in plain English what you want to do: 
    - make two variables set to 0: 'wanted' and 'total'
    - make a 'curr' variable, that acts as a pointer
    - in a while loop: while curr is not None
        - add 1 to 'total'
        - if curr's name is the fish_name we're looking for, add 1 to wanted
    - The probabilty of an event is wanted outcome divided by total possible outcomes
    - return probability round to 2 decimal points
3. Translate each sub-problem into pseudocode:
    wanted , total = 0, 0
    curr = head
    while curr is not None:
        total += 1
        if curr.fish_name == fish_name: wanted += 1
        curr = curr.next
    return round(wanted/total, 2)
'''
### I - Implement
'''
4. Translate the pseudocode into Python and share your final answer:
'''
def fish_chances(head, fish_name):
    wanted , total = 0, 0
    curr = head
    while curr is not None:
        total += 1
        if curr.fish_name == fish_name: wanted += 1
        curr = curr.next
    return round(wanted/total, 2)
#Problem 7 Examples:
print("Problem 7 Output:")            
fish_list = Node("Carp", Node("Dace", Node("Cherry Salmon")))
print(fish_chances(fish_list, "Dace"))            # expecting: 0.33
print(fish_chances(fish_list, "Rainbow Trout"))            # expecting: 0.00