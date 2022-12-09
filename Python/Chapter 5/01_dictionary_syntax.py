myDict = {
    "Fast": "In a quick manner",
    "Harry": "A Coder",
    "Marks": [1, 23, 6],
    "anotherdict": {
        'harry': 'Player' 
    }
}
print(myDict)
# print(myDict['Fast'])
# print(myDict['Harry'])
myDict['Marks'] = [23, 65]
print(myDict)
print(myDict['Marks'])
print(myDict['anotherdict']['harry'])