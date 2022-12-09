## Creating an empty set
b = set()
print(type(b))

## Adding values to an empty set
b.add(4)
b.add(4)
b.add(5)
b.add(5)
b.add(5)
b.add(5) # Adding a value repeatedly does not changes a set
# b.add([2, 4, 54]) # gives an error as we can't add list into a set, we can only put hashable objects in a set
b.add((2, 4, 54))
# b.add({
#     'harry': 'coder',
#     'Abhishek': 'A good coder'
# }) # we can't add a dictionary into a set

## Accessing elements 
print(b)

## Length of the set
print(len(b)) # prints the length of this set

## Removal of an Item
b.remove(5) # Removes 5 from set b
# b.remove(15) # throws an error while trying to remove 15(which is not present in the set)
print(b)

print(b.pop())
print(b)