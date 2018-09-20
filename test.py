#solve fibo: apply recursion
#fibo: 1,1,2,3,5,8,13...


def factorial(n):

    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

n = int(input("enter the value for n:"))
print("the factorail is:" , factorial(n))


#implement fibo recursively:

def fibo(n):

    if (n <= 1):
        return 1
    else:
        return fibo(n-1) + fibo(n-2)


n = int(input("enter the value here:"))
print(fibo(n))


#implement fibo in DP:

def fibo(n):

    f = [0] * (n +1)
    f[0] = f[1] = 1

    if (n <= 1):
        return f[0]
    else:
        for i in range(2, n+1):
            f[i] = f[i-1] + f[i-2]
        return f[n]

n = int(input("enter the value:"))
print(fibo(n))

