# Python 3.x code to demonstrate star pattern
# Function to demonstrate printing pattern
def pypart(n):
    
    for i in range(0, n):
        for j in range(0,i+1):
            print("*",end="")
        print("\r")
n=10
pypart(n)

#Another Way to create a star pattern
num=int(input("Enter the number of Rows:"))
#For rows outer loop::
for i in range(1,num+1):
#For columns inner loop
   for j in range(1,i+1):
      print("*",end="")
   print("\r")

      
