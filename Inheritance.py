#Parent class
class College:
    def __init__(self,clg):
        self.clg = clg
    def showcollege(self):
        print(f"College Name: {self.clg}")


class Department(College):
    def __init__(self,department):
        self.department = department

    def showdept(self):
        print(f"Department: {self.department}")


#Child Class
class Student(Department):

    def __init__(self,name,rollno,department,clg):
        self.name = name
        self.rollno = rollno
        Department.__init__(self,department) #Passing the arg to parent as constructor
        College.__init__(self,clg)

    def showdetails(self):
        print(f"Name: {self.name} Rollno: {self.rollno} ")

student_1 = Student("Barath","191cs138","CSE","BIT")
student_1.showdetails()

student_1.showdept()

student_1.showcollege()



