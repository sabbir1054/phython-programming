numbers=[10,22,66,55,45,22]

# normally we do
odd_numbers=[]
for num in numbers:
    if num%2==1:
        odd_numbers.append(num)
#print(odd_numbers)

odd_numbers_2=[num for num in numbers if num %2 == 0]
print(odd_numbers_2)