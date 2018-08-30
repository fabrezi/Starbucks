#simple implementation. requires to be fixed as it doesn't have stable sort.
# partition is fixed. the end node. giving wrong output --> logic error

def partition(A, p , r):
    i = p - 1
    x = A[r]
    for j in range(p,r-1,1):
        if (A[j] <= x):
            i = i+1
            A[i] = A[j]
            A[j] = A[i]
    A[p] = A[r]
    A[r] = A[p]

    return (i+1)

def quicksort(A,p,r):
    if (p < r):
        ip = partition(A,p,r)
        quicksort(A, p, ip-1)
        quicksort(A, ip+1, r)



A = [2,8,7,1]
quicksort(A,1,len(A)-1)
print(A)
