""" a=int(input())
b=int(input())

def add(a,b):
    print(a+b)

add(a,b) """

""" 
# we can pass argument by this specific way

from cgitb import reset


def add(num1,num2,num3):
    total=num1+num2+num3
    return total

#normally we can call by this way 
result=add(10,20,30)#it means 1st one is num1

#this is the sepciality of python
newResult=add(num2=20,num3=30,num1=40) 

"""
""" #we can set default value of optional perameter

def multiply(num3,num5,num1=4):
    re2sult=num1*num3*num5
    return re2sult
 """
""" 
def printFun(*numbers):
#    print(numbers) #it make tuple which is similar type array
    multResult=1
    for num in numbers:
        multResult=multResult*num
    return multResult

printresult=printFun(10,20,30,40)
print(printresult)
 """

""" 
#kargs in python it call dictionary

def longName(**kargs):
    print(kargs)


longName(first="dR",last="Khan",middle="Sabbir")

 """
""" 
 #one interesting use of kargs that is we put dictionary a specific value
from unicodedata import name


def name_mixed(first,last,**nameParts):
    print(first,last,nameParts)

name_mixed(first="khan",last="sabbir",middle="hossain")

 """


# we make a function where 

def all_types(first,*args,**kargs):
    print(first)
    print(args)
    for word in args:
        print(word)
    print(kargs)
    for key,value in kargs.items():
        print(key,value)

all_types('abd','add','kjk','lll','pp',name='Abdul',father='babul')
