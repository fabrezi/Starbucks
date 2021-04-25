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
def NAND(A, B):
    A = int(input("Input A:"))
    B = int(input("Input B:"))
    nand = 0
    # Your code goes here!
    if(A == 0 & B == 0):
        print(1)
    elif (A== 1 & B == 1 ):
        print(1)
    elif (A == 1 & B == 0):
        print(1)
    elif (A == 0 & B == 1):
        print(1)
    elif (A == 1 & B == 1):
        print(0)

    return nand

if __name__ == "__main__":
    NAND(1,2)

#Q5
def compound_interest(amount, rate, years):
    #new_amount = 0
    amount=(int(input("amount:")))
    rate = float(input("rate:"))
    years = int(input("years:"))

    new_amount = ((amount * (1 + rate)) ** (years))

    # Your code goes here!
    print(new_amount)

    return new_amount

if __name__ == "__main__":
    compound_interest(1,1,2)


#Q6
def wind_chill(T_a, v):
    T_wc = 0

    T = int(input("Input temperature:"))
    V = int(input("Input wind speed:"))

    T_wc = 13.12 + 0.62 * T + 11.37 * (V)**2

    print("the wind chill is:" , T_wc)

    # Your code goes here!

    return T_wc

if __name__ == "__main__":
    wind_chill(1,2)

#Q7
from math import radians, sqrt, asin, sin, cos

R  = 6372.1  # Radius of the Earth [km]

def haversine_distance(lat1, lon1, lat2, lon2):
    d = 0
    # Your code goes here!

    lat1 = int(input("lat1:"))
    lon1 = int(input("long1:"))

    lat2 = int(input("lat1:"))
    lon2 = int(input("long2:"))

    r1 = radians(lat1)
    r2 = radians(lon1)
    r3 = radians(lat2)
    r4 = radians(lon2)



    d = 2 * R * asin(sqrt(sin(r1 - r3) + cos(r1) * sin(r2 - r4)))

    print(d)


if __name__  == "__main__":
    haversine_distance(1,2,2,3)

#Q8


#Q9


#Q10
