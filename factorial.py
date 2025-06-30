def factorial(n):
    if n<2:
        return 1 
    else:
        for i in range(n,2,-1):
            n = n*(i-1)
           
        return n
        
n=int(input("Enter a number:"))
print(f"Factorial of  {n} is {factorial(n)}")
    