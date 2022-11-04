import time
class School:
    def __init__(self,name,address,principal=" ") -> None:
        self.name=name
        self.name=address
        self.principal=principal
        self.grades=[]
    def add_grade(self,name,teacher):
        new_grade=Grade(name,teacher)
        self.grades.append(new_grade)
    def remove_grade(self,name):
        idx=0
        for i,grade in enumerate(self.grades):
            if grade.name==name:
                idx=i
        del self.grades[idx]

    
class Grade:
    # constructor
    def __init__(self,name,teacher) -> None:
        self.name=name
        self.students=[]
        self.teacher=teacher
    def __repr__(self) -> str:
        return f"class of {self.name} with teacher {self.teacher}"
#    distructor
    def __del__(self):
        print (f'Deleting {self.name} class with teacher{self.teacher}')

oxford=School("Oxford","mirpur","shakil")

oxford.add_grade("class_3",'Osman goni')
oxford.add_grade("class 4",'nazma mam')
oxford.add_grade("class 9",'Rajib sir')

print(oxford.grades)
oxford.remove_grade("class 4")
print(oxford.grades)

print("My code is running done")
time.sleep(5)