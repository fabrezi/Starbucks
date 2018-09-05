#works but get runtime errors at larger values. I should try the memoization technique


def fib(n):
    if (n < 0):
        print("Error beta")
    elif n <= 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)



def main():
    n = int(input("Enter value beta: "))
    print(fib(n))
main()
