import datetime
print("Pushpendra Singh 18EJICS126 B section")
print("Name : ")
First_Name = str(input("Enter your First Name : "))
Last_Name = str(input("Enter your Last Name : "))
temp1 = First_Name
temp2 = Last_Name
First_Name = First_Name.replace(First_Name,temp2)
Last_Name = Last_Name.replace(Last_Name,temp1)
print(First_Name,Last_Name)
print("Date of Birth : ")
year = int(input("Enter the year:"))
month = int(input("Enter the month:"))
day = int(input("Enter the day:"))
birth_date = datetime.date(year, month, day)
end_date = datetime.date(2021,10,23)
time_difference = end_date - birth_date
age = time_difference.days
print(age)
