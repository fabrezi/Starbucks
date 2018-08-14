#difference b/w bubble vs insert: 1. the number of for - loops
 #we start loop at second element (index 1) since the first item is already sorted
def insert(A):
    for i in range(1, len(A)):
        temp = A[i]
        j = i -1#the last item
        while (j > -1) & (temp < A[j]):
            A[j+1] = A[j]
            j = j -1

            A[j+1] = temp
        return A

A = [5,2,4,6,1,3]
insert(A)
print (A)
