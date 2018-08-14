"""
- class schedule
- pending payments: healthcare
- research: symmetry vs asymmetry, functions, 
- Q1. what are the advantages/ disadvantages of HMT??
"""

#difference b/w bubble vs insert: 1. the number of for - loops
def insert(A):
    for i in range(1, len(A)):
        temp = A[i]
        j = i -1
        while (j > -1) & (temp < A[j]):
            A[j+1] = A[j]
            j = j -1

            A[j+1] = temp
        return A

A = [5,2,4,6,1,3]
insert(A)
print (A)