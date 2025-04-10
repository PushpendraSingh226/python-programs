#Compute Greatest common Divisor
def Computehcf(a,b):
    if b==0:
       return a
    else:
       return Computehcf(b,a%b)
print("Pushpendra Singh\n18JICS126\n")
num1= int(input("Enter the first number:"))
num2= int(input("Enter the Second number:"))

print("GCD of " , a ,"& " , b," is : ",Computehcf(num1,num2))


