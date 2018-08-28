#difference b/w bubble vs insert: 1. the number of for - loops
 #we start loop at second element (index 1) since the first item is already sorted
 # file("name", "mode")
 # mode: r, w, a

file = open("lo", "r")
A = []
for val in file.read().split():
    A.append(int(val))
    file.close()
    y = len(A)

def insert(A):
    for j in range(1,len(A)):
        key = A[j]
        i = j-1
        while (i>-1) and (A[i] > key):
            A[i+1] = A[i]
            A[i] = key
            i = i-1
    return A
insert(A)
print(A)
print(y)
