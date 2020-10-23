#financial application: compound value
#Java_bk_chp02_q13

saving = int(input("enter the monthly saving amount:"))
#saving = 100
#interest_rate = 0.05
monthly_rate = 0.00417
account = 0

for i in range(0,6):
    account = (saving+account)*(1+monthly_rate)
print("after sixth month the account value is:", "$",account)
