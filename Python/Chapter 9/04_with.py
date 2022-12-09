with open('another.txt', 'r') as f:
    a = f.read()
with open('another.txt', 'w') as f:
    a = f.write('Abhishek')
print(a) # this now prints how many character have been written to the file