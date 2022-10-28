base = int(input("Enter the base :"))
exponent = int(input("Enter the exponent :"))
result = base 
if exponent != 0:
  for i in range(exponent - 1):
       result = result * base  
else:
  result == 1
print("Exponential value is : ", result)
