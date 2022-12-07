#Input: words length n.
#Algo: if n < 10: word
#       if n > 10: new-word
#Output: new-word

user_input = input("Please enter an english word: ")

#print(user_input)
i = len(user_input)
j = user_input[0]
z = user_input[-1]

if (i < 10):
 print(user_input)
else:
    print(j,i,z)




