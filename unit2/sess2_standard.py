# Unit 2, Session 2 Standard Set Vers.1

# PROBLEM 1
### U - Understand 
'''
1. Share 2 questions you would ask to help understand the question:
  - WHat should the functionr eturn int he event the list in empty?
  - Are all the dictionaries assumed to have the name and population keys, or should there be an error for that?
'''
### P - Plan
'''
2. Write out in plain English what you want to do: 
  - sequential search for lowest population using a for-loop
  - unless the population is less than the lowest, the name variable wont change

3. Translate each sub-problem into pseudocode:
  def most_endangered(species_list):
    min_name = None
    min_pop = float('inf')
    for data in species_list:
        if data["population"] < min_pop:
            min_pop = data["population"]
            min_name = data["name"]
    return min_name

'''
### I - Implement
'''
4. Translate the pseudocode into Python and share your final answer:
'''
def most_endangered(species_list):
    min_name = None
    min_pop = float('inf')
    for data in species_list:
        if data["population"] < min_pop:
            min_pop = data["population"]
            min_name = data["name"]
    return min_name


# PROBLEM 2
### U - Understand 
'''
1. Share 2 questions you would ask to help understand the question:
  - to clarify, we return the number of times an observed species is also endangered?
  - can we use built in functions?
'''
### P - Plan
'''
2. Write out in plain English what you want to do:
    - frequency map of the observed species
    - in a for loop, for each endangered species, add their frequency to the counter
    - return the counter
  
3. Translate each sub-problem into pseudocode:
  def count_endangered_species(endangered_species, observed_species):
    count = 0
    freq = Counter(observed_species)
    for x in endangered_species:
        if freq.get(x) is not None:
            count += freq[x]
    return count
'''
### I - Implement
'''
4. Translate the pseudocode into Python and share your final answer:
'''
from collections import Counter
def count_endangered_species(endangered_species, observed_species):
    count = 0
    freq = Counter(observed_species)
    for x in endangered_species:
        if freq.get(x) is not None:
            count += freq[x]
    return count


# PROBLEM 3
### U - Understand 
'''
1. Share 2 questions you would ask to help understand the question:
  - to clarify, we always at index 0 of the station layout?
  - how do we calculate the difference in indices when going backwards?
'''
### P - Plan
'''
2. Write out in plain English what you want to do: 
  - establish current index, and total distance traveled
  - for each letter in the observation, find the index, calculate its distance from current index, and add the distance to the total
  - return the total
3. Translate each sub-problem into pseudocode:
  def navigate_research_station(station_layout, observations):
    curr = 0
    total = 0
    for stop in observations:
        next = station_layout.index(stop)
        diff = abs(curr - next)
        total += diff
        curr = next
    return total
'''
### I - Implement
'''
4. Translate the pseudocode into Python and share your final answer:
'''
def navigate_research_station(station_layout, observations):
    curr = 0
    total = 0
    for stop in observations:
        next = station_layout.index(stop)
        total += abs(curr - next)
        curr = next
    return total


# PROBLEM 4
### U - Understand 
'''
1. Share 2 questions you would ask to help understand the question:
  - Are there repeats in the list?
  - Is there a way to do this without a for-loop
'''
### P - Plan
'''
2. Write out in plain English what you want to do: 
    - get frequency of each species
    - in a for loop, store priority speices' in the sorted list,
    - extend the list to the rest of the species not in the list.

3. Translate each sub-problem into pseudocode:
  def prioritize_observations(observed_species, priority_species):
    freq = Counter(observed_species)
    sort = []
    for x in priority_species:
        for i in range(freq[x]):
            sort.append(x)
        del freq[x]
    for x in sorted(freq):
        for i in range(freq[x]):
            sort.append(x)
        del freq[x]
    return sort
'''
### I - Implement
'''
4. Translate the pseudocode into Python and share your final answer:
'''
def prioritize_observations(observed_species, priority_species):
    freq = Counter(observed_species)
    sort = []

    for x in priority_species:
        for i in range(freq[x]):
            sort.append(x)
        del freq[x]

    for x in sorted(freq):
        for i in range(freq[x]):
            sort.append(x)
        del freq[x]
    return sort


# PROBLEM 5
### U - Understand 
'''
1. Share 2 questions you would ask to help understand the question:
 - to clarify, we're returning the number of distinct averages calculated?
 - what do we do in the event that the list starts empty?
'''
### P - Plan
'''
2. Write out in plain English what you want to do: 
  - Identify min and max
  - calculatr average, and add it to a set
  - repeat until population list is empty, then return set length
3. Translate each sub-problem into pseudocode:
    def distinct_averages(species_populations):
        dis_avg = set()
        while species_populations:
            minn = min(species_populations)
            maxx = max(species_populations)
            species_populations.remove(minn)
            species_populations.remove(maxx)
            avg = (minn + maxx)/2
            dis_avg.add(avg)
        return len(dis_avg)    
'''
### I - Implement
'''
4. Translate the pseudocode into Python and share your final answer:
'''
def distinct_averages(species_populations):
    dis_avg = set()
    while species_populations:
        minn = min(species_populations)
        maxx = max(species_populations)
        species_populations.remove(minn)
        species_populations.remove(maxx)
        avg = (minn + maxx)/2
        dis_avg.add(avg)
    return len(dis_avg)    
