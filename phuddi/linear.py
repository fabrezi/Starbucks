import math

def linear(intlist, target):
    found = False
    position = 0
    while position < len(intlist):
        if intlist[position] == target:
            found = True
            break
        position = position +1

    return found

list = [1,2,3,4,5,10]

user = int(input("what values you want"))
num = linear(list, user)
if (num == True):
    print("the number is here")
else:
    print("null for days")



