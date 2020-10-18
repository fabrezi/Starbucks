#hello, 5 time, loop
#area of circle
#E01

'''
i = 1
while (i < 6):
    print("hello world")
    i += 1
'''

'''
import math

r = float(input("enter the radius of the circle:"))
area = str(math.pi * r*r)
print("the area of the circle:" + area)
'''

print(sum(n for n in range(1,10) if (n%3==0 or n%5==0)))

#create table
print("a", "a^2", "a^3")
for i in range(1,10):
    b = i*i
    c = i*i*i
    print(i, b, c)
 
#convert farenheit to celsius:
TF = int(input("enter temperature in farenheit:"))
TC = (TF - 32)/1.8
print("Celsius:" , TC)
