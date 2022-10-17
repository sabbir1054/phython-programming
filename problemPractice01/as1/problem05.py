d = {'!': 1, '@' : 2, '#': 3, '$' : 4, '%' : 5, '^' : 6}

def create_list():
    new_list=[]
    for i in d:
        k= [i,d[i] ]
        new_list.extend(k)
    print(new_list)


create_list()