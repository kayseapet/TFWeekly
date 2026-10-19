# Unit 6, Session 2 Version 1
# -------------------
# functions needed for testing
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next
# ----------------------

#Problem 1: Wild Goose Chase
# Why this problem: This question is asking students to be able to identify a circular list. Students will have to choose a method to find the end node connecting to the front as effieciently as possible.
### U - Understand 
'''
1. Share 2 questions you would ask to help understand the question:
    1.To clarify, it has to be the last node that's connected to the head?
    2. Is it possible for two clues to be identical?
'''
### P - Plan
'''
2. Write out in plain English what you want to do: 
    - traverse the list until current node is None
        - if the current node's next is the head node, return true
    - once the loop is over, return false
3. Translate each sub-problem into pseudocode:
    curr = head
    while curr:
        if curr.next is head:
            return True
        move to next
    return False
'''
### I - Implement
'''
4. Translate the pseudocode into Python and share your final answer:
'''
def is_circular(clues):
    curr = clues
    while curr:
        if curr.next == clues:
            return True
        curr = curr.next
    return False
# Example usage:
print("Problem 1 Examples:")
clue1 = Node("The stolen goods are at an abandoned warehouse")
clue2 = Node("The mayor is accepting bribes")
clue3 = Node("They dumped their disguise in the lake")
clue1.next = clue2
clue2.next = clue3
clue3.next = clue1
print(is_circular(clue1)) # expect: True
# -----------------------------------------------------------------------------------------------

#Problem 3: Prioritizing Suspects
# Why this problem:
### U - Understand 
'''
1. Share 2 questions you would ask to help understand the question:
    1. Is the linked list circular?
    2. Does the list have to be fully sorted?
'''
### P - Plan
'''
2. Write out in plain English what you want to do: 
    - have curr and prev pointer
    - while traversing the loop:
        - if the current node is greater than threshold, 
        -  set curr to head of linked list, and connect the previous and next nodes
    return head of list
3. Translate each sub-problem into pseudocode:
    prev,head,curr = None, suspect_ratings, suspect_ratings
    while curr:
        if curr.value > threshold:
            if prev:
                prev.next = curr.next
                curr.next = head
                head = curr
                curr = prev.next
                continue
        prev = curr
        curr = curr.next
    return head
'''
### I - Implement
'''
4. Translate the pseudocode into Python and share your final answer:
'''
def partition(suspect_ratings, threshold):
    prev,head,curr = None, suspect_ratings, suspect_ratings
    while curr:
        if curr.value > threshold:
            if prev:
                prev.next = curr.next
                curr.next = head
                head = curr
                curr = prev.next
                continue
        prev = curr
        curr = curr.next
    return head
# Example usage:
print("Problem 3 Examples:")
suspect_ratings = Node(1, Node(4, Node(3, Node(2, Node(5, Node(2))))))
print_linked_list(partition(suspect_ratings, 3))
# -------------------------------------------------------------------------------------------------

#Problem 5: A New Perspective
# Why this problem:
### U - Understand 
'''
1. Share 2 questions you would ask to help understand the question:
    1. to clarify, rotate means to shift the list over to the right k spaces?
    2. Is the given linked list circular?
'''
### P - Plan
'''
2. Write out in plain English what you want to do: 
    - create head, tail, prev pointer
    - traverse the entire list and find the length head node, tail node
    - once we reach the tail, connect it to the head node.
    - traverse list len - (k%length) -1 times to find the new tail
        - set head to tail.next
        -set tail.next to None
    return head
3. Translate each sub-problem into pseudocode:
    if k == 0:
        return evidence
    length = 1
    head, tail, curr = evidence, None , evidence
    while curr.next:
        length += 1
        curr = curr.next
    curr.next = evidence
    for i in range(length - (k%length)):
        curr = curr.next
    tail = curr
    head = curr.next
    tail.next = None
    return head
'''
### I - Implement
'''
4. Translate the pseudocode into Python and share your final answer:
'''
def rotate_right(evidence, k):
    if k == 0:
        return evidence
    length = 1
    head, tail, curr = evidence, None , evidence
    while curr.next:
        length += 1
        curr = curr.next
    curr.next = evidence
    for i in range(length - (k%length)):
        curr = curr.next
    tail = curr
    head = curr.next
    tail.next = None
    return head
# Example usage:
print("Problem 5 Examples:")
evidence_list1 = Node(1, Node(2, Node(3, Node(4, Node(5)))))
evidence_list2 = Node(0, Node(1, Node(2)))
print_linked_list(rotate_right(evidence_list1, 2))
print_linked_list(rotate_right(evidence_list2, 4))
# -------------------------------------------------------------------------------------------------
