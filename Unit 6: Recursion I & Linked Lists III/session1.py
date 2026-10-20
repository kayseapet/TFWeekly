# Unit 6, Session 1 Version 1
# -------------------
# functions needed for testing
class SongNode:
    def __init__(self, song, artist, next=None):
        self.song = song
        self.artist = artist
        self.next = next

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

# For testing
def print_linked_list(node):
    current = node
    while current:
        print((current.song, current.artist), end=" -> " if current.next else "")
        current = current.next
    print()
# -------------------

# Problem  2: Top Artists
# Why this problem:This sproblem challenges to traverse a linked list and use it's information to form a frequency map.
### U - Understand 
'''
1. Share 2 questions you would ask to help understand the question:
    1. is the 'playlist' variable confirmed to be a valid linked list?
    2. what if the artist named is not capitalized?

'''
### P - Plan
'''
2. Write out in plain English what you want to do: 
    - make an empty dict
    - in a hwile loop: go through linked list
        - if node.artist isnt a key:
            - make it a key and set the starting value to 1
        - otherwise
            - increase the value by 1
    -return the dict

3. Translate each sub-problem into pseudocode:
    map = {}
    curr = playlist
    while curr:
        if not map.get(curr.artist): map[curr.artist] = 1
        else: map[curr.artist] += 1
    return map
 
'''
### I - Implement
'''
4. Translate the pseudocode into Python and share your final answer:
'''
def get_artist_frequency(playlist):
    map = {}
    curr = playlist
    while curr:
        if not map.get(curr.artist): map[curr.artist] = 1
        else: map[curr.artist] += 1
        curr = curr.next
    return map

#Problem 2 Examples:
print("Problem 2 Output:")            # expecting: ( add this line to print statements)
playlist = SongNode("Saturn", "SZA", 
                SongNode("Who", "Jimin", 
                        SongNode("Espresso", "Sabrina Carpenter", 
                                SongNode("Snooze", "SZA"))))

print(get_artist_frequency(playlist))
# -------------------------------------------------------------------------------------------------


# Problem 4: On Repeat
# Why this problem: This problem is testing students' understanding on the slow and fast pointer method
### U - Understand 
'''
1. Share 2 questions you would ask to help understand the question:
    1. can a node point to itself?
    2. what happens when the list is empty?
''' 
### P - Plan
'''
2. Write out in plain English what you want to do: 
    - edge case: if the list is empty OR the head.next is none (only one node)
        - return false
    
        - make the slow & fast pointers
        - while loop: until we reach the end of a list
            - move slow pointer + 1
            - move fast pointer + 2
            - if the slow pointer == fast pointer
                - return true
        - return false

3. Translate each sub-problem into pseudocode:
    if not playlist_head or not playlist_head.next: 
        return false

    slow, fast = playlist_head, playlist_head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return true
    return false 

'''
### I - Implement
'''
4. Translate the pseudocode into Python and share your final answer:
'''
def on_repeat(playlist_head):
    if not playlist_head or not playlist_head.next: 
            return False
    
    slow, fast = playlist_head, playlist_head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False 

#Problem 4 Examples:
print("Problem 4 Output:")            # expecting: ( add this line to print statements)
song1 = SongNode("GO!", "Common")
song2 = SongNode("N95", "Kendrick Lamar")
song3 = SongNode("WIN", "Jay Rock")
song4 = SongNode("ATM", "J. Cole")
song1.next = song2
song2.next = song3
song3.next = song4
song4.next = song2

print(on_repeat(song1))
# -------------------------------------------------------------------------------------------------


# Problem 6: Volume Control
# Why this problem: This problem has multiple 'conditions' for what counts as a critical point is, so students could get confused.
### U - Understand 
'''
1. Share 2 questions you would ask to help understand the question:
    1. What is minimum possible length of the list?
    2. How should ties/equal adjacent values be handled?
'''
### P - Plan
'''
2. Write out in plain English what you want to do: 
    - edgecase: if there's two or less nodes:
        - return 0
    
    - make a critical point counter
    - make the prev, curr,and next node pointers
        - start prev at head and curr at head.next, so the head node is automatically not considered as a possible critical point.
    -in a while loop: while next is not none (so it stops before the tail node.)
        - if prev and next are less than curr: (LOCAL MIN)
            - increase counter by 1
        - if prev and next are more than curr: (LOCAL MAX) 
            - increase counter by 1
        - update the pointers
    - return counter value

3. Translate each sub-problem into pseudocode:
    if not song_audio or not song_audio.next:
        return 0

    crits = 0
    prev, curr, next = song_audio, song_audio.next, song_audio.next.next
    while next:
        if prev.value < curr.value and next.value < curr.value:
            crits += 1
        if prev.value > curr.value and next.value > curr.value:
                    crits += 1
        prev = curr
        curr = next
        next = next.next
    return crits
'''
### I - Implement
'''
4. Translate the pseudocode into Python and share your final answer:
'''
def count_critical_points(song_audio):
    if not song_audio or not song_audio.next:
        return 0

    crits = 0
    prev, curr, next = song_audio, song_audio.next, song_audio.next.next
    while next:
        if prev.value < curr.value and next.value < curr.value:
            crits += 1
        if prev.value > curr.value and next.value > curr.value:
                    crits += 1
        prev = curr
        curr = next
        next = next.next
    return crits
#Problem 6 Examples:
print("Problem 6 Output:")            # expecting: ( add this line to print statements)
song_audio = Node(5, Node(3, Node(1, Node(2, Node(5, Node(1, Node(2)))))))
print(count_critical_points(song_audio))
# -------------------------------------------------------------------------------------------------

