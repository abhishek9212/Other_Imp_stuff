def greatestnum(num1, num2, num3):
    if(num1>num2):
        greater = num1
    else:
        greater = num2
    if(greater<num3):
        greater = num3
    return greater

max_val = greatestnum(78, 95, 86)
print(max_val)