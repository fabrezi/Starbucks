#difference b/w bubble vs insert: 1. the number of for - loops
 #we start loop at second element (index 1) since the first item is already sorted
def insert(A):
    for j in range(1,len(A)):
        key = A[j]#current vlaue
        i = j -1#previous value 
        while(i>-1) & (A[i] > key):
            A[i+1] = A[i]
            A[i+1] = key
         i = i-1
    return A

A = [5,2,4,6,1,3]
insert(A)
print(A)
