class Student:
    def __init__(self):
        self.roll=0
        self.name=""
        self.marks=[]
        self.total=0
        self.per=0
        self.grade=""
        self.result=""

    def setStudent(self):
        self.roll=input("Enter Roll: ")
        self.name=input("Enter Name: ")
        for i in range(2):
            self.marks.append(int(input("enter marks of mid term "+str(i+1)+" (out of 250) : ")))
        self.marks.append(int(input("enter marks of sports activity (out of 200) :")))
        for j in range(3):
            self.marks.append(int(input("enter marks of other activity "+str(j+1)+" (out of 100) : ")))
			
    def calculateTotal(self):
        for x in self.marks:
            self.total+=x
			
    def calculatePercentage(self):
        self.per=self.total/10
		
    def calculateGrade(self):
        if self.per>=85:
            self.grade="A++"
        elif self.per>=75:
            self.grade="A"
        elif self.per>=65:
            self.grade="B"
        elif self.per>=55:
            self.grade="C"
        elif self.per>=45:
            self.grade="D"
        else:
            self.grade="F"
            
    def showStudent(self):
        self.calculateTotal()
        self.calculatePercentage()
        self.calculateGrade()
        print("-------*****--------")
        print("Roll no : ",self.roll,"\nName :",self.name,"\nTotal Marks : ",self.total,"\nPercentage : ",self.per,"\nGrade : ",self.grade)


def main():
    #Student object
    s=Student()
    s.setStudent()
    s.showStudent()

if __name__=="__main__":
    main()
