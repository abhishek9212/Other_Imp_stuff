content = True
i = 0
with open('log.txt') as f:
    
    while content:
        content = f.readline()
        i+=1
       
        if 'python' in content.lower():
            print(content)
            print(f"Yes python is present on line number {i}")
           # print(i)
