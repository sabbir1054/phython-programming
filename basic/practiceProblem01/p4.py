

check=""

while(check!="Quit"):
    num=int(input("Enter the number : "))
    if(num<0):
        print(f"{num} is negative")
    else: 
        print(f"{num} is positive")
    check=input("if you want to quit write Quit otherwise write no :")
