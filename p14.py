# Ask the user for a string and print out whether this string is a palindrome or not (A palindrome is a string that reads the same forwards and backwards)
a=input("Please enter a word: ") 
c = a.casefold() 
b = reversed(c)
if list(c) == list(b): 
    print("It is palindrome") 
    
    
else: print("It is not palindrome")