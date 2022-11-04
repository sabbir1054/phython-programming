class Pair:
    def get_id(lst,target):
        for idx,num in enumerate(lst):
            if((lst[idx]+lst[idx+1])==target):
                print(idx+1,idx+2)
                break

Pair.get_id([10,20,10,40,50,60,70],50)


