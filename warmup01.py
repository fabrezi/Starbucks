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

#population projection
time = 3600*24*365
born = time/7
death = time /13
immigrant = time/45

current_population = 3120322486
population = born + immigrant - death

for i in range(1,6):
    current_population = current_population + population
    print(i, "yearly population:", round(current_population))
    
#payroll
name = input("enter the employee name:")
work_hour = int(input("enter the number of hours worked in a week:"))
pay_rate  = float(input("enter hourly pay rate:"))
fed_tax = 0.20
state_tax = 0.09

gross_pay = work_hour * pay_rate
deduction01 = gross_pay * fed_tax
deduction02 = gross_pay * state_tax
total_deduction = deduction01 + deduction02
net_pay = gross_pay - total_deduction
print(name, "earned:", net_pay)

#sum the digits in the integer
number = int(input("enter the integer:"))
bur=sum(map(int,str(number)))
print(bur)
