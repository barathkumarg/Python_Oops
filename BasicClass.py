class College:
    CLG = "BIT"
    def __init__(self,name,rollno):
        self.name = name
        self.rollno = rollno

    def showdetails(self):
        print(f"Name: {self.name} Roll No: {self.rollno} College: {self.CLG}")

    def updatename(self,name):
        self.name = name

    def setmarks(self,marks):
        self.marks = marks

    def showmarks(self):
        print("Marks:")
        for key,values in self.marks.items():
            print(f"{key} : {values} ",end="")



student_1 = College("Barath","191CS138")

student_1.showdetails()

student_1.updatename("Barathkumar")

student_1.showdetails()

student_1.setmarks({"English":90,"Tamil":100,"Mathematics":80})

student_1.showmarks()




