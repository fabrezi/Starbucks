#implement bubble sort

def bubble(list):#input parameter in the bracket
    for passnum in range(0,len(list)):#range(start,stop,step)
        for i in range(passnum):
            if list[i]>list[i+1]:
                temp = list[i]
                list[i] = list[i+1]
                list[i+1] = temp

list = [54,16,99,75,3,90]
bubble(list)
print(list)

