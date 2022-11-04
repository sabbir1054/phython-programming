from unicodedata import name


class School:
    def __init__(self,name) -> None:
        self.name=name
        print('School init called')


class Grade:
    def __init__(self,grade_name) -> None:
        self.grade_name=grade_name
        print('Grade  class init called')



class SportsTeam:
    def __init__(self,sport_name) -> None:

        self.name=name
    
    def add_player(self,player_name):
        self.team.append(player_name)

class Student(School,Grade,SportsTeam):
    def __init__(self, name,grade_name,school) -> None:
        self.name=name
        Grade.__init__(self,grade_name)
        School.__init__(self,school)


ananta=Student("AJ","MBA","Uk School")

print(ananta.name)