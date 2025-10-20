"NOTE: when I press the session 1 for unit 4, it doesnt have any problems, so I'm using the pratice problems under the session 2 tab."

# Standard Problems Version 1


#PROBLEM 1: NFT NAME EXTRACTOR
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


#PROBLEM 2: NFT COLLECTION REVIEW
### U - Understand 
'''
1. Share 2 questions you would ask to help understand the question:
    1. What was the plan of the existing code? aka what is it supposed to do?
    2. What what does the code do instead?
'''
### P - Plan
'''
2. Write out in plain English what you want to do: 
  - Run the existing code to identify the current output
  - Because this problem is identical to the previous one, its most likely a syntax issue
  - fix the bugs in the code and rerun
  - once the output matches expected output, the code is fixed.

3. Translate each sub-problem into pseudocode:
    originial code: 
        def extract_nft_names(nft_collection):
            nft_names = []
            for nft in nft_collection:
                nft_names += nft["name"]
            return nft_names
    bug: name is added to nft_names letter by letter
    revised code: 
        def extract_nft_names(nft_collection):
            nft_names = []
            for nft in nft_collection:
                nft_names.append(nft["name"])       #line revised
            return nft_names
'''
### I - Implement
'''
4. Translate the pseudocode into Python and share your final answer:
'''
def extract_nft_names(nft_collection):
    nft_names = []
    for nft in nft_collection:
        nft_names.append(nft["name"])
    return nft_names

# Example usage:
print("Problem 2 Examples:")
nft_collection = [
    {"name": "Abstract Horizon", "creator": "ArtByAlex", "value": 5.4},
    {"name": "Pixel Dreams", "creator": "DreamyPixel", "value": 7.2}
]
nft_collection_2 = [
    {"name": "Golden Hour", "creator": "SunsetArtist", "value": 8.9}
]
nft_collection_3 = []
print(extract_nft_names(nft_collection))
print(extract_nft_names(nft_collection_2))
print(extract_nft_names(nft_collection_3))

#PROBLEM 3:IDENTIFY POPULAR CREATORS
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


#PROBLEM 4: NFT COLLECTION STATISTICS
### U - Understand 
'''
1. Share 2 questions you would ask to help understand the question:
    1. Should the average be include up to a certain decimal place, or be an interger?
    2. Are there invalid values that shouldnt be included in the average, like negative values or values over 10?
'''
### P - Plan
'''
2. Write out in plain English what you want to do: 
    - create a list for nft_values
    - using a for loop, collect all nft values from the nft_collection
    - calculate the average as the sum of the nft_values / number of nfts.
    -return the average value
3. Translate each sub-problem in-to pseudocode:
  def average_nft_value(nft_collection):
    nft_values = [nft.get("value") for nft in nft_collection]
    average = sum(nft_values) / len(nft_values)
    return average
'''
### I - Implement
'''
4. Translate the pseudocode into Python and share your final answer:
'''
def average_nft_value(nft_collection):
    if not nft_collection: return 0
    nft_values = [nft.get("value") for nft in nft_collection]
    average = sum(nft_values) / len(nft_values)
    return average
# Example usage:
print("Problem 4 Examples:")
nft_collection = [
    {"name": "Abstract Horizon", "creator": "ArtByAlex", "value": 5.4},
    {"name": "Pixel Dreams", "creator": "DreamyPixel", "value": 7.2},
    {"name": "Urban Jungle", "creator": "ArtByAlex", "value": 4.5}
]
print(average_nft_value(nft_collection))
nft_collection_2 = [
    {"name": "Golden Hour", "creator": "SunsetArtist", "value": 8.9},
    {"name": "Sunset Serenade", "creator": "SunsetArtist", "value": 9.4}
]
print(average_nft_value(nft_collection_2))
nft_collection_3 = []
print(average_nft_value(nft_collection_3))


#PROBLEM 5: NFT TAG SEARCH
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