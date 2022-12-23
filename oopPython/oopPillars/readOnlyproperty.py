class Student:
    def __init__(self,name,id,marks) -> None:
        self.name=name
        self.__id=id
        self.marks=marks
    @property
    def studentId(self):
        return self.__id


chowdury=Student("Choto",15,55)
print(chowdury.studentId)