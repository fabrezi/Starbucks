# code is from online source.


#p: text, k = shift
def caesar(p, k):
    encrypt = " "

    #iterate through text and save in array
    for i in range(len(p)):
        array = p[i]

        if(array.isupper()):
            encrypt += chr((ord(array) + k-65) % 26 + 65)

        else:
            encrypt += chr((ord(array) + k - 97) % 26 + 97)


    return encrypt

def main():
    p = "ps4 is better then Xbox"
    k = 3
    print ("text:" + p)
    print("shift:" + str(k))
    print("cipher:" + caesar(p,k))

if __name__== "__main__":
    main()







