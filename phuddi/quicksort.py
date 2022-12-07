#simple implementation. requires to be fixed as it doesn't have stable sort.
# partition is fixed. the end node. giving wrong output --> logic error

def quicksort(A,p,r):
   if (p < r):
       q = partition(A,p,r)
       quicksort(A,p,q-1)
       quicksort(A,q+1,r)

def partition(A,p,r):
    i = p - 1
    pivot = A[r]
    for j in range(p, r-1):
        if A[j] <= pivot:
            i = i +1
            A[i] = A[j]
            A[j] = A[i]
    A[i+1] = A[r]
    A[r] = A[i+1]
    return i+1

A = [10, 7, 8, 9, 1, 5]
quicksort(A,0, len(A)-1)
print(A)
