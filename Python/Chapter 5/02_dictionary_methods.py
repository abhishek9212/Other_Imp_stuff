from typing import MutableMapping


myDict = {
    "fast": "In a quick manner",
    "harry": "A Coder",
    "marks": [1, 23, 6],
    "anotherdict": {
        'harry': 'Player' 
    },
    1: 2
}

# Dictionary methods
# print(myDict)
# print(myDict.keys()) # prints the keys of the dictionary
# print(type(myDict.keys())) # this class is dict_keys 
# # we can typecast it into a list like below
# print(list(myDict.keys())) # prints the keys of the dictionary in a form of a list

# print(myDict.values()) # prints the values of the dictionary
# print(list(myDict.values()))

# print(myDict.items()) # prints the (key, value) for all contents of the dictionary
# print(list(myDict.items()))

# print(myDict)
# updateDict = {
#     'Sayali': 'friend',
#     'Rashmi': 'lead',
#     'Shikha': 'manager',
#     'harry': 'A Dancer'      # because harry was an existing key so it's value gets replaced in this update
# }

# myDict.update(updateDict) # updates the dictionary by adding key-value pairs from updateDict
# print(myDict)

# print(myDict.get('harry'))
# print(myDict['harry'])

# there is a difference between these two because of the below logic

print(myDict.get('harry2')) # Returns none as harry2 is not present in the dictionary
print(myDict['harry2']) # throws an error as harry2 is not present in the dictionary




