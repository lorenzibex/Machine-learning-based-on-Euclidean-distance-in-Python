ratings={
'Alan': {'Jurassic Parc': 1, 'Terminator': 5,'Gone with the wind': 2.5, 
'Superman Returns': 5, 'Groundhog day': 2.5,'The notebook': 2.5},
'Thomas': {'Jurassic Parc': 4, 'Terminator': 5,'Gone with the wind': 1.5,
 'Superman Returns': 5.0, 'The notebook': 2.5,'Groundhog day': 5},
'Michael': {'Jurassic Parc': 3, 'Terminator': 2.5,'Superman Returns': 5,
 'The notebook': 4.0},
'Hillary': {'Terminator': 5, 'Gone with the wind': 2.5,'The notebook': 4.5, 
'Superman Returns': 4.0,'Groundhog day': 2.5},
'Alex': {'Jurassic Parc': 2.5, 'Terminator': 4.0,'Gone with the wind': 2.0, 
'Superman Returns': 2.5, 'The notebook': 2.5,'Groundhog day': 2.0},
'Julian': {'Jurassic Parc': 1.5, 'Terminator': 3.0,'Gone with the wind': 2.0,
 'Superman Returns': 2.5, 'The notebook': 2.5,'Groundhog day': 2.0},
'Anna': {'Jurassic Parc': 2.5, 'Terminator': 4.0,'The notebook': 2.5,
 'Superman Returns': 5.0, 'Groundhog day': 5},
'Toby': {'Terminator':4.5,'Groundhog day':1.5,'Superman Returns':4.0,
'Gone with the wind': 2.5}}
print ratings['Toby'] 
print 
print ratings['Toby']['Terminator']

from math import sqrt
sqrt(pow(3-1,2)+pow(6-1,2))


#Return a distance-based similarity score for person1 and person2 
def distance(dictionary, personA, personB):
    si={}
    for item in dictionary[personA]:
        if item in dictionary[personB]:
            si[item]=1
    if len(si) ==0: return 0
    sum_of_squares = sum([pow(dictionary[personA][item]-dictionary[personB][item],2)
                          for item in dictionary[personA] if item in dictionary[personB]])
    return 1/(1+sum_of_squares)

distance(ratings, 'Toby', 'Julian')
