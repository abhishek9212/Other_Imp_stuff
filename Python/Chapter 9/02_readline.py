f = open('sample.txt') 
# read first line
data = f.readline() 
print(data)

# read second line
data = f.readline() 
print(data)  # One extra space is coming in the output because after the first line there is a newline character.

# read third line
data = f.readline() 
print(data) 

# read fourth line ... and so on ...
data = f.readline() 
print(data) 
f.close()