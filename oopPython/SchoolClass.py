class Student:
    def __init__(self,name,age,id):
        self.name=name
        self.age=age
        self.id=id
    

class Course:
    def __init__(self,name,teacher):
        self.name=name
        self.teacher=teacher

class Teacher:
    def __init__(self,name,course):
        self.name=name
        self.courses=course
        

class School:
    def __init__(self,name,teachers,courses,students):
        self.name=name
        self.teachers=teachers
        self.courses=courses
        self.students=students

    def get_students(self):
        for student in self.students:
            print(student.name)



  

school_name='Phitron'
ds_course=Course('Data Structure','Einstein')
teacher_1=Teacher('Einstein',ds_course)

algo_course=Course('Algorithm','Edison')
teacher_2=Teacher('Edison',algo_course)

student_1=Student('Rohomot',19,99)
student_2=Student('Shakil',22,65)
student_3=Student('Jihad',23,74)


teachers=[teacher_1,teacher_2]
courses=[ds_course,algo_course]
students=[student_1,student_2,student_3]


my_school=School(school_name,teachers,courses,students)

my_school.get_students()