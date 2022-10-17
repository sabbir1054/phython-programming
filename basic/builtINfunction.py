numbers=[10,20,304,00,225,88,899]

max_number=max(numbers)
min_number=min(numbers)
reverse_list=reversed(numbers)
sort_list=sorted(numbers)
reverse_sort_list=sorted(numbers,reverse=True)
# print(max_number)
# print(min_number)
# print(list(reverse_list))
# print(list(sort_list))
# print(list(reverse_sort_list))

users=[
    {'name':'shakil','age':34},
    {'name':'rajib','age':38},
    {'name':'Nokib','age':38},
    {'name':'salman','age':39},
    {'name':'kasu','age':39},
    {'name':'jubaye','age':39},
    {'name':'hayder','age':39},
    {'name':'sabbir','age':49},
    {'name':'ashik','age':59},
]


sorted_users=sorted(users,key=lambda user:user['name'],reverse=True)
print(sorted_users)