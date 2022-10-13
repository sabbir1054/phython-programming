numbers = [12,34,5,66,55,98,67,7]

# normal return function
def double_it(x):
    return x*2


double_it2=lambda x:x*2

double_numbers=map(lambda x:x*2,numbers)
squared_numbers=map(lambda x:x*x,numbers)
filtered_numbers=filter(lambda x:x>50,numbers)
# print(numbers)
# print(list(double_numbers))
# print(list(squared_numbers))
# print(list(filtered_numbers))

users=[
    {'name':'sabbir','age':30},
    {'name':'khan','age':34},
    {'name':'jihad khan','age':343},
    {'name':'tareq','age':43},
    {'name':'jinaas','age':93},
]

senior_artist=filter(lambda actor:actor['age']>40,users)
print(users)
print(list(senior_artist))