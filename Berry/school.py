class School:
    pass

class Student(School):
    def __init__(
        self,
        student_id,
        student_name,
        student_f_name,
        student_phone_num,
        student_address,
        student_fees
    ):
        
        self.student_id= student_id
        self.student_name=student_name
        self.student_f_name= student_f_name
        self.student_phone_num= student_phone_num
        self.student_address= student_address
        self.student_fees= student_fees

    def getStudent(self):
        return f"name={self.student_name},
        father name = {self.student_f_name}"
    
class Teacher(School):
    pass

class Classrooms(School):
    pass

class Admin(School):
    pass




student1 = Student(
    "1",
    "Ali",
    "Usman",
    "923001020300"
    "Azam Town Karachi",
    "1000"
)

v= student1.getStudent()

print(v)