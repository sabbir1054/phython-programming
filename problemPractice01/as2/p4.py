str=input()   #input: x3b4U5i2
letter_list=[]
number_list=[]
unsorted_str=""
for idx,letter in enumerate(str,1):
    if(idx%2==0):
        number_list.append(int(letter))
    else:
        letter_list.append(letter.lower())
j=0
for letter in letter_list:
    i=0
    while(i<number_list[j]):
        unsorted_str+=letter
        i+=1
    j+=1
sorted_str=sorted(unsorted_str)
sorted_word = ''.join(sorted_str)
result=""
for letter in sorted_word:
    if(letter=='u'):
        u=letter.capitalize()
        result+=u
    else:
        result+=letter


print(result)
