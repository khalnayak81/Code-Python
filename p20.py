from sqlite3 import converters


# weight converter
weight = int (input("Enter the weight: \n"))
unit = input("enter the unit. \n (L)bs or (k)g : \n")
if unit.upper() == "L":
    converted = weight * 0.45 
    print(f"You  have {converted} Killos")
    
else:
       converted = weight / 0.45 
       print(f"You  have {converted} pounds.")
       
       