l=["This","is","very","fantastic"]

def create_string():
    my_string=""
    length=int(len(l))
    for i in l:
        my_string+=i+" "
    
    print(my_string)

create_string()