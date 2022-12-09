myDict = {
    'Pankha': 'Fan',
    'Dabba': 'Box',
    'Vastu': 'Item'
}

print("Options are", myDict.keys())
a = input('Enter the hindi word\n')
# print('the meaning of your word is: ',myDict[a])
print('the meaning of your word is: ',myDict.get(a))
# print(myDict[a])