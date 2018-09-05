#Donald Knuth is a prophet from computing dimension

#implement knuth arrow beta


def fib(n):
    if (n < 0):
        print("Error beta")
    elif n <= 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)



def main():
    n = int(input("Enter the Birthday person's name: "))
    print(fib(n))
main()