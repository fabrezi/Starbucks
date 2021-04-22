#convert fahrenheit to celsius
def fahrenheit_to_celsius():
    F = float(input("Input Fahrenheit temperature:"))
    C = (F - 32) * 5 / 9


    #C = 0

    print("temperature in celsius:" , C)


    return C


if __name__ == '__main__':
    fahrenheit_to_celsius()


    
'''''
c = 299792458  # Speed of light [m/s]

#def main():
def light_time():
    t = 0

    distance = int(input("Input the distance travelled:"))
    # Calculate the time taken using t = d/c and return it.
    t = distance / c
    print(t)

    return t

if __name__ == "__main__":
    light_time()
