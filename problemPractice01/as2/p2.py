str=input("enter numbers: ")
str_list=str.split('-')
sum=0.0
for num in str_list:
    sum+=float(num)
print(f"sum is: {sum}")