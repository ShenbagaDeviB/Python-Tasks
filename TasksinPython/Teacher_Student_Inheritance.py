class Teacher:
    def school(self):
        print("Go to school")
    def lunch(self):
        print("Bring your lunch")
    
class Student(Teacher):
    def study(self):
        print("Study regularly")
    def exam(self):
        print("Score good marks")
s=Student()
s.school()
s.study()
s.lunch()
s.exam()