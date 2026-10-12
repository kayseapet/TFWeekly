# Unit 5 Session 1 Version 1
# NOTE: For this session, I'll the Understand & Plan part for problems, and have the Implementation for all three problems in one group.

#Problem 5: Add Furniture
# Why this problem: this problem is editing a villager's furniture feature, but ONLy is the item to be added is 'valid'.
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


#Problem 7: Group by Personality
# Why this problem: This problem requires students to be able to look for and verify a specific trait of each villager in a list of them.
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


#Problem 8: Telephone
# Why this problem: This problem could be more challenging for students, because they'll have to traverse villagers to see if there's a path from villager A to villager B.
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

# ----------------------------------IMPLEMENTATION FOR PROBLEMS(5,7,8)----------------------------
class Villager:
    def __init__(self, name, species, personality=None ,catchphrase=None, neighbor=None):
        self.name = name
        self.species = species
        self.personality = personality
        self.catchphrase = catchphrase
        self.furniture = []
        self.neighbor = neighbor

    'Problem 5:'
    def add_item(self, item_name):
        set = {"acoustic guitar", "ironwood kitchenette", "rattan armchair", "kotatsu", "cacao tree"}
        if item_name in set: self.furniture.append(item_name)
        pass

'   Problem 7:'
def of_personality_type(townies, personality_type):
    filtered = [townie.name for townie in townies if townie.personality == personality_type]
    return filtered

'   Problem 8'
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
    #Problem 5 Examples:
print("Problem 5 Output:")            
alice = Villager("Alice", "Koala", "guvnor")
print(alice.furniture)            # expecting:[]
alice.add_item("acoustic guitar")
print(alice.furniture)            # expecting:["acoustic guitar"]
alice.add_item("cacao tree")
print(alice.furniture)            # expecting:["acoustic guitar", "cacao tree"]
alice.add_item("nintendo switch")
print(alice.furniture)            # expecting:["acoustic guitar", "cacao tree"]

    #Problem 7 Examples:
print("Problem 7 Output:")
isabelle = Villager("Isabelle", "Dog", "Normal", "what's up?")
bob = Villager("Bob", "Cat", "Lazy", "pthhhpth")
stitches = Villager("Stitches", "Cub", "Lazy", "stuffin'")
print(of_personality_type([isabelle, bob, stitches], "Lazy"))   # expecting:['Bob', 'Stitches']
print(of_personality_type([isabelle, bob, stitches], "Cranky")) # expecting:[]

 #Problem 8 Examples:
print("Problem 8 Output:")   
sabelle = Villager("Isabelle", "Dog", "Normal", "what's up?")
tom_nook = Villager("Tom Nook", "Raccoon", "Cranky", "yes, yes")
kk_slider = Villager("K.K. Slider", "Dog", "Lazy", "dig it")
isabelle.neighbor = tom_nook
tom_nook.neighbor = kk_slider
print(message_received(isabelle, kk_slider))    # expecting: True
print(message_received(kk_slider, isabelle))    # expecting: False
# --------------------------------------------------------------------------------------------------
