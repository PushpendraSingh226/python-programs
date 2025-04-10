#Conditional Statements:
x=18;
if 20<x:
 print('x is greater than 20')
else:
    print("x is less than 20")

x=20;
y=20;
if x>y:
    print('x is greater than y')
elif x<y:
    print('x is less than y')
else:
    print('x is equal to y')

#Looping/Iterator
    num1= 12;
while num1<=100:
    print(num1)
    num1 +=20

#Loop Condition checking;
    loop_condition = True

while loop_condition:
    print("Loop Condition keeps: %s" %(loop_condition))
    loop_condition = False
for i in range(1, 17):
  print(i)
  
#List: Collection | Array | Data Structure
my_arr = [2,24,19,14,36,"Apple","mosambi","pineapple"]
print(my_arr[6])
print(my_arr[7])

my_passion = []
my_passion.append("Being a Front end Developer")
my_passion.append("to create various projects and web applications")
print(my_passion[0])
print(my_passion[1])

#Dictionary: Key-Value Data Structure
my_bio = {
    "name":"Pushpendra Singh",
    "Gender":"male",
    "Education qualification":"Undergraduate",
    "Contact": "7340141042"
}
print("My name is %s" %(my_bio["name"]))
print("My  contact no. is %s" %(my_bio["Contact"]))

#Iteration: Looping Through Data Structures
dictionary = { "Pushpendra": "Programmer" }

for Pushpendra in dictionary:
    print("%s = %s" %(Pushpendra, dictionary[Pushpendra]))

#Another way
dictionary = { "Pushpendra": "Cpp" }

for Pushpendra, Cpp in dictionary.items():
    print("%s --> %s" %(Pushpendra,Cpp ))

#Looping continue
    Biodata_PP = {
  "name": "Pushpendra",
  "nickname": "PP",
  "nationality": "Indian",
  "age": 20
}

for attribute, value in Biodata_PP.items():
    print("My %s is %s" %(attribute, value))

#Classes and Objects
    class Vehicle:
     def __init__(self, number_of_wheels, type_of_tank, seating_capacity, maximum_velocity):
        self.number_of_wheels = number_of_wheels
        self.type_of_tank = type_of_tank
        self.seating_capacity = seating_capacity
        self.maximum_velocity = maximum_velocity
    @property
    def number_of_wheels(self):
        return self.__number_of_wheels
    
    @number_of_wheels.setter
    def number_of_wheels(self, number):
        self.__number_of_wheels = number

tesla_model_s = Vehicle(6, 'electric', 5, 250)
print(tesla_model_s.number_of_wheels) 
tesla_model_s.number_of_wheels = 2 
print(tesla_model_s.number_of_wheels) 














