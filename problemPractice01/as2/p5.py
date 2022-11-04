name,marks=input("Enter your name and marks: ").split()
with open("StudentInfo.txt","a")as file:
    file.write(f"ID:{int(marks)*7} Name: {name} Marks: {marks} \n")
