# Unit 4 Session 1 Version 1

#PROBLEM 1: NFT NAME EXTRACTOR
# Why this problem: This problems deals with nested data structures (a list of dictionaries), which we haven't talked much about in this class yet.
### U - Understand 
'''
1. Share 2 questions you would ask to help understand the question:
    1. To clarify, I only need to return the name of each NFT in the list?
    2. Is there a solution more efficient than O(n) time complexity?
'''
### P - Plan
'''
2. Write out in plain English what you want to do: 
    - create list for nft names
    - in a for loop that iterates through nft_collection:
        - search for key "name", and add the value there to the list for nft names
    - return nft names list
3. Translate each sub-problem into pseudocode:
  def extract_nft_names(nft_collection):
    names = newlist
    for dict in nft_collection:
        names.append(dict.get("name"))
    return names
'''
### I - Implement
'''
4. Translate the pseudocode into Python and share your final answer:
'''
def extract_nft_names(nft_collection):
    names = []
    for dict in nft_collection:
        names.append(dict.get("name"))
    return names

# Example usage:
print("Problem 1 Examples:")
nft_collection = [
    {"name": "Abstract Horizon", "creator": "ArtByAlex", "value": 5.4},
    {"name": "Pixel Dreams", "creator": "DreamyPixel", "value": 7.2},
    {"name": "Future City", "creator": "UrbanArt", "value": 3.8}
]
nft_collection_2 = [
    {"name": "Crypto Kitty", "creator": "CryptoPets", "value": 10.5},
    {"name": "Galactic Voyage", "creator": "SpaceArt", "value": 6.7}
]
nft_collection_3 = [
    {"name": "Golden Hour", "creator": "SunsetArtist", "value": 8.9}
]
print(extract_nft_names(nft_collection))
print(extract_nft_names(nft_collection_2))
print(extract_nft_names(nft_collection_3))

# -------------------------------------------------------------------------------------------------


#PROBLEM 3:IDENTIFY POPULAR CREATORS
# Why this problem: This problem requires students to go through a nested data structure and save properties of it.
### U - Understand 
'''
1. Share 2 questions you would ask to help understand the question:
    1. To clarify, its a list of ALL creators with more than one NFT?
    2. Is there a solution with a space complexity smaller than O(N)?
'''
### P - Plan
'''
2. Write out in plain English what you want to do: 
    - create new list for popular creators:
    - establish new dict, that'll act as a frequency map to count the number of times a creator appears
    - in a for loop iterating over nft_collection:
        - in freq_map, under the key that matches the current nft creator, add +1 to the value
    - in a second for loop iterating over freq_map:
        - for each value thats >=2, append key to list for popular creators
    - return popular creators
3. Translate each sub-problem into pseudocode:
  def identify_popular_creators(nft_collection):
    popular =[]
    freq_map = {}
    for nft in nft_collection:
        freq_map[nft.get("creator")] += 1
    for creator in freq_map:
        if freq_map[creator] >= 2:
            popular.append(creator)
    return popular
'''
### I - Implement
'''
4. Translate the pseudocode into Python and share your final answer:
'''
def identify_popular_creators(nft_collection):
    popular =[]
    freq_map = {}
    for nft in nft_collection:
        if nft.get("creator") not in freq_map:
            freq_map[nft.get("creator")] = 0
        freq_map[nft.get("creator")] += 1
    for creator in freq_map:
        if freq_map[creator] >= 2:
            popular.append(creator)
    return popular
# Example usage:
print("Problem 3 Examples:")
nft_collection = [
    {"name": "Abstract Horizon", "creator": "ArtByAlex", "value": 5.4},
    {"name": "Pixel Dreams", "creator": "DreamyPixel", "value": 7.2},
    {"name": "Urban Jungle", "creator": "ArtByAlex", "value": 4.5}
]
nft_collection_2 = [
    {"name": "Crypto Kitty", "creator": "CryptoPets", "value": 10.5},
    {"name": "Galactic Voyage", "creator": "SpaceArt", "value": 6.7},
    {"name": "Future Galaxy", "creator": "SpaceArt", "value": 8.3}
]
nft_collection_3 = [
    {"name": "Golden Hour", "creator": "SunsetArtist", "value": 8.9}
]
print(identify_popular_creators(nft_collection))
print(identify_popular_creators(nft_collection_2))
print(identify_popular_creators(nft_collection_3))



# -------------------------------------------------------------------------------------------------

#PROBLEM 5: NFT TAG SEARCH
# Why this problem: This is problem with nested collections to third degree (a list in a dictionary in a list), could be hard for students
### U - Understand 
'''
1. Share 2 questions you would ask to help understand the question:
    1. How is the nft_collection nested? Is it a list of lists of dicts?
    2. Can the tag variable be multiple tags (list), or only one (string)?
'''
### P - Plan
'''
2. Write out in plain English what you want to do: 
    - create list for nft_names that have the wanted tag
    - in a for loop, traverse nft_collection:
        - collect each nft that had the wanted tag
        - add their names to nft_names
    -return nft_names


3. Translate each sub-problem into pseudocode:
  nft_names = []
    for group in nft_collections:
        for nft in group:
            if tag in set(nft.get('tags')):
                nft_names.append(nft.get('name'))
    return nft_names    
'''
### I - Implement
'''
4. Translate the pseudocode into Python and share your final answer:
'''
def search_nft_by_tag(nft_collections,tag):
    nft_names = []
    for group in nft_collections:
        for nft in group:
            if tag in set(nft.get('tags')):
                nft_names.append(nft.get('name'))
    return nft_names    
# Example usage:
print("Problem 5 Examples:")
nft_collections = [
    [
        {"name": "Abstract Horizon", "tags": ["abstract", "modern"]},
        {"name": "Pixel Dreams", "tags": ["pixel", "retro"]}
    ],
    [
        {"name": "Urban Jungle", "tags": ["urban", "landscape"]},
        {"name": "City Lights", "tags": ["modern", "landscape"]}
    ]
]
nft_collections_2 = [
    [
        {"name": "Golden Hour", "tags": ["sunset", "landscape"]},
        {"name": "Sunset Serenade", "tags": ["sunset", "serene"]}
    ],
    [
        {"name": "Pixel Odyssey", "tags": ["pixel", "adventure"]}
    ]
]
nft_collections_3 = [
    [
        {"name": "The Last Piece", "tags": ["finale", "abstract"]}
    ],
    [
        {"name": "Ocean Waves", "tags": ["seascape", "calm"]},
        {"name": "Mountain Peak", "tags": ["landscape", "adventure"]}
    ]
]
print(search_nft_by_tag(nft_collections, "landscape"))
print(search_nft_by_tag(nft_collections_2, "sunset"))
print(search_nft_by_tag(nft_collections_3, "modern"))