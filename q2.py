def gcd(m,n):
   gcd = 1
   if(m==n):
       gcd = m
       return gcd
   if m % n == 0:
       return n   
   for k in range(int(n / 2), 0, -1):
       if m % k == 0 and n % k == 0:
           gcd = k
           break 
   return gcd
print("kailash prajapat\n18ejics072\n")
a = int(input("enter 1st number : "))
b = int(input("enter 2nd number : ")) 

print("GCD of " , a ,"& " , b," is : ",gcd(a,b))
