letter = '''Dear <|NAME|>,
Greetings from Amdocs. I am happy to tell you about your selection
You are selected!
Have a great day ahead.
Thanks and regards,
Floria
Date: <|DATE|>
'''
name = input("Enter your name\n")
date = input("Enter date\n")
letter = letter.replace("<|NAME|>", name)
letter = letter.replace("<|DATE|>", date)
print(letter)