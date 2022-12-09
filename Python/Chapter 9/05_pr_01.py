f = open('poems.txt', 'r')
t = f.read()
if 'twinkle' in t:
    print("Twinkle is present in the file")
else:
    print("Twinkle is not present in the file")
f.close()