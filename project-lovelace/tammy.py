#convert fahrenheit to celsius
#Q1
def fahrenheit_to_celsius():
    F = float(input("Input Fahrenheit temperature:"))
    C = (F - 32) * 5 / 9


    #C = 0

    print("temperature in celsius:" , C)


    return C


if __name__ == '__main__':
    fahrenheit_to_celsius()


#Q2    

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


#Q3
def moose_body_mass(latitude):
    mass = 0
    latitude = float(input("enter the latitude value:"))
    # Your code goes here!
    mass = 2.75 * latitude + 16.793
    print("output body mass:" , mass)

    return mass

if __name__=="__main__":
    moose_body_mass(1)

#Q4


#Q5



#Q6


#Q7


#Q8


#Q9


#Q10
