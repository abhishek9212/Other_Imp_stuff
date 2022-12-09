import random
randNo = random.randint(1, 100)
# print(randNo)

userInp = None
attempts = 0

while(userInp != randNo):
    userInp = int(input("Enter your number: "))
    attempts += 1
    if(userInp == randNo):
        print(f"Your guess is correct. You took {attempts} attempts")
    elif(userInp > randNo):
        print("Lower number please")
    else:
        print("Higher number please")

with open('hiscore.txt', 'r') as f:
    newbest = int(f.read())

if(attempts < newbest):
    print(f"Congrats!You have broken the best score!!. Earlier it was {newbest} and your's is {attempts} attempts")
    with open('hiscore.txt', 'w') as f:
        f.write(str(attempts))
else:
    print(f"You didn't beat the best score which was {newbest} :( \n Good luck next time :)")

