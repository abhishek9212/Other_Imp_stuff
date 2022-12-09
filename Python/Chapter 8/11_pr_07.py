# this = "    Harry is a good     "
# print(this)
# print(this.strip())   # strip function removes extra spaces from the beginning and end of a string

def remove_and_strip(string, word):
    newStr = string.replace(word, "")
    return newStr.strip()

this = "    Harry is a good     "
print(remove_and_strip(this, "is "))
