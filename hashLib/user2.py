import hashlib

class User:
    def __init__(self,name,email,password) -> None:
        self.name=name
        self.email=email
        self.password=password
        encrypted_pass=hashlib.md5((self.password).encode()).hexdigest()
        with open("user3.bin","a") as userFile:
            userFile.write(f"{self.name} {encrypted_pass} \n")
        userFile.close()
        print(self.name, "is created successfully")

    @staticmethod
    def login():
        singleUsers=""
        with open("user3.bin","r") as userFile:
           singleUsers =userFile.readlines() 
        userFile.close()
        print(singleUsers)



user1=User("shakil","shakil@email.com","123654")
user3=User("sabbir","shaksdadfail@email.com","123654")
user5=User("zihad","shssakil@email.com","123654")
user7=User("enamul","skil@email.com","123654")

# print(User.login)
User.login()