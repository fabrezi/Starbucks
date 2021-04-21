#######################################################################
#If we list all the natural numbers below 10 that are multiples of 3
# or 5, we get 3, 5, 6 and 9.
#The sum of these multiples is 23.

#Find the sum of all the multiples of 3 or 5 below 1000.
##################################################################



def fahrenheit_to_celsius():
    F = float(input("Input Fahrenheit temperature:"))
    C = (F - 32) * 5 / 9


    #C = 0

    print("temperature in celsius:" , C)


    return C


if __name__ == '__main__':
    fahrenheit_to_celsius()

