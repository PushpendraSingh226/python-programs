def factorial(n):
  fact = 1
  return 1 if(n==1 or n==0) else n * factorial(n - 1);
n = int(input("Input a number to compute the factiorial :"))

print("Factorial of",n,"is",factorial(n))

#Another way to calculate he factorial of any number
def Factorial(n):
    if n < 0:
        return 0
    elif n == 0 or n == 1:
        return 1
    else:
        fact = 1
        while(n > 1):
            fact *= n
            n -= 1
        return fact
 
# Driver Code
num = int(input('Enter any number:'))
print("Factorial of",num,"is",
factorial(num))
 
