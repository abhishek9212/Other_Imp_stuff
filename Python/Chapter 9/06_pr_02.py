def game():
    return 44677

score = game()

with open('hiscore.txt') as f:
    hiscoreStr = f.read()

if hiscoreStr == '':
    with open('hiscore.txt', 'w') as f:
        f.write(str(score))

elif score>int(hiscoreStr):                   # we can't put these two conditions together because when 
    with open('hiscore.txt', 'w') as f:       # the file will be blank then it's contents can't be converted 
        f.write(str(score))                   # to int
