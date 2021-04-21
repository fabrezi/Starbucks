#convert fahrenheit to celsius
def fahrenheit_to_celsius():
    F = float(input("Input Fahrenheit temperature:"))
    C = (F - 32) * 5 / 9


    #C = 0

    print("temperature in celsius:" , C)


    return C


if __name__ == '__main__':
    fahrenheit_to_celsius()

