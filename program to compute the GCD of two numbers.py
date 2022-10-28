from ast import Return
from math import gcd
from re import A
def gcd(number1,number2):
    if(number2==0):
        return number1
    else:
        return gcd(number2,number1%number2)
number1 = int(input("Enter the first number:"))
number2 = int(input("Enter the second number:"))
GCD = gcd(number1,number2)
print(f"The GCD of {number1} and {number2} is : {GCD}")

