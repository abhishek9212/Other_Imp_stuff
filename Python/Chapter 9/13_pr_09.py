file1 = 'log.txt'
file2 = 'this.txt'

with open(file1, 'r') as f:
    content1 = f.read()

with open(file2, 'r') as f:
    content2 = f.read()

if content1 == content2:
    print("These files are identical.")
else:
    print("These files are different.")
    