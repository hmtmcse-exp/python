class Student:
    count = 0

    def __init__(self, count):
        self.count = count


    def displayCount(self):
        print("Total Student %d" % self.count)



student = Student(10)
student.displayCount()