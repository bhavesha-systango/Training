#factorial using recursion
def recur_factorial(n):  
   if n == 1:  
       return n  
   else:  
       return n*recur_factorial(n-1)  
# take input from the user  
num = int(input("Enter a number: ")) 
print("factorial of",num,"is",recur_factorial(num)) 