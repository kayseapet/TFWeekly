#Unit 2 Session 2 Version 1

# PROBLEM 3: Navigating the Research Station
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
#Problem 3 Examples:
print("Problem 3 Output:")            # expecting: ( add this line to print statements)
station_layout1 = "pqrstuvwxyzabcdefghijklmno"
observations1 = "wildlife"
station_layout2 = "abcdefghijklmnopqrstuvwxyz"
observations2 = "cba"
print(navigate_research_station(station_layout1, observations1))  
print(navigate_research_station(station_layout2, observations2))








# PROBLEM 4: Prioritizing Endangered Species Observations
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
from collections import Counter
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
#Problem 4 Examples:
print("Problem 4 Output:")            # expecting: ( add this line to print statements)
observed_species1 = ["🐯", "🦁", "🦌", "🦁", "🐯", "🐘", "🐍", "🦑", "🐻", "🐯", "🐼"]
priority_species1 = ["🐯", "🦌", "🐘", "🦁"]  
observed_species2 = ["bluejay", "sparrow", "cardinal", "robin", "crow"]
priority_species2 = ["cardinal", "sparrow", "bluejay"]
print(prioritize_observations(observed_species1, priority_species1))
print(prioritize_observations(observed_species2, priority_species2)) 






# PROBLEM 5: Calculating Conservation Statistics
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
#Problem 5 Examples:
print("Problem 5 Output:")            # expecting: ( add this line to print statements)  
species_populations1 = [4,1,4,0,3,5]
species_populations2 = [1,100]
print(distinct_averages(species_populations1))
print(distinct_averages(species_populations2)) 