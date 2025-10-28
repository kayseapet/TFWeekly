# Unit 5 Session 2, Standard Problems Version 1


#  ----------------------------------------------------------------
    # Classes & Functions needed for testing (problems 2-5)
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next
#  ----------------------------------------------------------------

#Problem 1: Mutual Friends
### U - Understand 
'''
1. Share 2 questions you would ask to help understand the question:
    1. Is it guaranteed that the new_contact is a villager instance?
    2. To clarify, Villager.friends is a list that ONLY consists of pre-existing Villagers?
'''
### P - Plan
'''
2. Write out in plain English what you want to do: 
    - make two sets: my_friends and their_friends
        - get lists of each villager's friend's names
        - where its a set of the list of friends for self(my_friends names) and new_contact(their_friends names)
    - return the intersection of the two sets as a list
3. Translate each sub-problem into pseudocode:
    def get_mutuals(self,new_contact):
        myFriends = [friend.name for friend in self.friends]
        theirFriends = [friend.name for friend in new_contact.friends]
        myFriends, theirFriends = set(myFriends), set(theirFriends)
        return list(myFriends & theirFriends)
'''
### I - Implement
'''
4. Translate the pseudocode into Python and share your final answer:
'''
class Villager:         
    def __init__(self, name, species, catchphrase):
        self.name = name
        self.species = species
        self.catchphrase = catchphrase
        self.friends = []

    # function implemented
    def get_mutuals(self,new_contact):
        myFriends = [friend.name for friend in self.friends]
        theirFriends = [friend.name for friend in new_contact.friends]
        myFriends, theirFriends = set(myFriends), set(theirFriends)
        return list(myFriends.intersection(theirFriends))

#Problem 1 Examples:
print("Problem 1 Output:")  
bob = Villager("Bob", "Cat", "pthhhpth")
marshal = Villager("Marshal", "Squirrel", "sulky")
ankha = Villager("Ankha", "Cat", "me meow")
fauna = Villager("Fauna", "Deer", "dearie")
raymond = Villager("Raymond", "Cat", "crisp")
stitches = Villager("Stitches", "Cub", "stuffin")
bob.friends = [stitches, raymond, fauna]
marshal.friends = [raymond, ankha, fauna]
print(bob.get_mutuals(marshal))           # expecting: ['Raymond', 'Fauna']
ankha.friends = [marshal]
print(bob.get_mutuals(ankha))           # expecting: []


# --needed for testing problem 2 ---
kk_slider = Node("K.K. Slider")
harriet = Node("Harriet")
saharah = Node("Saharah")
isabelle = Node("Isabelle")
# ----------------------------------

#Problem 2: Linked Up
### U - Understand 
'''
1. Share 2 questions you would ask to help understand the question:
    1. Would it be prefered if I create a function for future use, or should I code for the given example specifically?
    2. Can Node.next point to anything other than another Node, & if it can, is that good or should we specify the data structure in the constructor?
'''
### P - Plan
'''
2. Write out in plain English what you want to do: 
    - Match the example by changing the nodes' .next:
        - kk_slider's next is Harriet
        - Harriet's next is Saharah
        - Saharah's next is Isabelle
3. Translate each sub-problem into pseudocode:
    kk_slider.next = harriet
    harriet.next = saharah
    saharah.next = isabelle

'''
### I - Implement
'''
4. Translate the pseudocode into Python and share your final answer:
'''
kk_slider.next = harriet
harriet.next = saharah
saharah.next = isabelle
#Problem 2 Examples:
print("Problem 2 Output:")            
print_linked_list(kk_slider)            # expecting: K.K. Slider -> Harriet -> Saharah -> Isabelle

#Problem 3: Daily Tasks
### U - Understand 
'''
1. Share 2 questions you would ask to help understand the question:
    1. does the function change if the value for the task given is None or not a string?
    2. Is this linked list circular meaning, do I need to set the last node's next to the head node?
'''
### P - Plan
'''
2. Write out in plain English what you want to do: 
    - create the new node: set the value to 'task' and its next node to 'head'
    - return new node
3. Translate each sub-problem into pseudocode:
    def add_dirst(head,task):
    newNode = Node(task,head)
    return newNode
'''
### I - Implement
'''
4. Translate the pseudocode into Python and share your final answer:
'''
def add_first(head,task):
    newNode = Node(task,head)
    return newNode
#Problem 3 Examples:
print("Problem 3 Output:")
task_1 = Node("shake tree")
task_2 = Node("dig fossils")
task_3 = Node("catch bugs")
task_1.next = task_2
task_2.next = task_3
    # Linked List: shake tree -> dig fossils -> catch bugs
print_linked_list(add_first(task_1, "check turnip prices"))               # expecting:check turnip prices -> shake tree -> dig fossils -> catch bugs


#Problem 4: Halve List
### U - Understand 
'''
1. Share 2 questions you would ask to help understand the question:
    1. To clarify, every value in the linked list is divided by 2?
    2. Is the linked list circular?
'''
### P - Plan
'''
2. Write out in plain English what you want to do: 
    - make a 'curr' variable: set it to 'head'
    - in a while loop: while 'curr' is not none
        - curr's value is now divided by 2
        - curr is now the next node
    - return head
3. Translate each sub-problem into pseudocode:
    curr = head
    while curr is not None:
        curr.value = curr.value/2
        curr = curr.next
    return head
'''
### I - Implement
'''
4. Translate the pseudocode into Python and share your final answer:
'''
def halve_list(head):
    curr = head
    while curr is not None:
        curr.value = curr.value/2
        curr = curr.next
    return head
#Problem 4 Examples:
print("Problem 4 Output:")
### U - Understand 
node_one = Node(5)
node_two = Node(6)
node_three = Node(7)
node_one.next = node_two
node_two.next = node_three
    # Input List: 5 -> 6 -> 7
print_linked_list(halve_list(node_one))              # expecting:2.5  -> 3 -> 3.5


#Problem 5: Remove Last
'''
1. Share 2 questions you would ask to help understand the question:
    1. What does the function return if there is no nodes at 'head'?
    2. Is this linked list circular?
'''
### P - Plan
'''
2. Write out in plain English what you want to do: 
    - edge case: If 'head' is none OR head.next is none:
        - return None
    - make 'prev' variable: set it to None
    - make 'curr' variable: set it to 'head'
    -in while loop: while curr.next is not none
        - set prev to curr's value
        - set curr to curr.next's value
    - set prev.next's value to None
    -return head
3. Translate each sub-problem into pseudocode:
    if head is None or head.next is None:
        return None
    prev, curr = None, head
    while curr.next is not None:
        prev = curr
        curr = curr.next
    prev.next = None
    return head
'''
### I - Implement
'''
4. Translate the pseudocode into Python and share your final answer:
'''
def delete_tail(head):
    if head is None or head.next is None:
        return None
    prev, curr = None, head
    while curr.next is not None:
        prev = curr
        curr = curr.next
    prev.next = None
    return head
#Problem 5 Examples:
print("Problem 5 Output:")
butterfly = Node("Common Butterfly")
ladybug = Node("Ladybug")
beetle = Node("Scarab Beetle")
butterfly.next = ladybug
ladybug.next = beetle
    # Input List: butterfly -> ladybug -> beetle
print_linked_list(delete_tail(butterfly))              # expecting:Common Butterfly -> Ladybug