import math

class Calculator:

   def inp(slef,i):
     x=input("enter first number")
     y=input("enter second number")
     switcher = {
         1: print(x + y),
         2: print(x - y),
         3: print(x * y),
         4: print(x / y)
    }


print("******** Weclome to teezee Advanced Calultor  ************ ")

print("1: Addition")
print("2: Substraction")
print("3: Multiplication")
print("4: Division")

i=input("Enter Your Choice")
p=Calculator(i)
