#1Write a function Shift (Arr, n) in Python ,which accepts a list
#Arr of numbers and n is a numeric value by which all elements of
#the list are shifted to left.
print("Pushpendra Singh\n18EJICS126\nSec B3")
def LShift(Arr,n):
    X = Arr[n:]+Arr[:n]
    return X
Arr = [10,20,30,40,12,11]
n = 2
print("Array before LShift",Arr)
result = LShift(Arr, n)
print("Array after LShift",result)

#2.Write a program in python to input any customer name and
#display customer phone number if the customer name is exist in the list.
name_list = {"Pushpendra":'7340142023',"Praveen": '9868676523'}
print(name_list)
name = input("enter the customer name:")

if name not in name_list.keys():
    print("Does not exist in Database")
else:
        print(name_list[name])
               
#3.question
roll = int(input("enter the last two digits of roll no."))

if roll%2 == 0:
   for i in range(2,roll+1,2):
       print(roll/i)
else:
    for i in range(1,10,2):
        print(3*roll+i)
