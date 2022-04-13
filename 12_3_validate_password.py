import math

print(math.pi)

def ValidatePassword(Pass):
    numLower = 0
    numUpper = 0
    numNum = 0
    for i in range(len(Pass)):
        if ord(Pass[i]) >= 65 and ord(Pass[i]) <= 90:
            numUpper += 1
        elif ord(Pass[i]) >= 97 and ord(Pass[i]) <= 122:
            numLower += 1
        elif ord(Pass[i]) >= 48 and ord(Pass[i])<= 57:
            numNum += 1
        else:
            return False
    if numLower >= 2 and numUpper >=2 and numNum >= 3:
        return True
    else:
        return False



print(ValidatePassword("HEllo123")) # print True