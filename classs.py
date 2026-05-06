class Student:
    name = "waqas Hanif"
    rollnumber = "23011598-154"

    # def __init__(self):
    #     print("Your name is", self.name, "and rollnumber is", self.rollnumber)

    def Student_Marks_Average(self, marks):
        avg = 0
        sum = 0

        for i in marks:
            sum = sum + i

        self.avg = sum / i

    def welcome(self):
        print("Welcome", self.name, "Your Average of Marks is", self.avg)





s1 = Student()
s1.Student_Marks_Average([1, 2, 3, 4])
s1.welcome()
