a = ['oh', 'Emelia', 'to']
s = "Oh, I got two tickets for Dhaka. I and Emelia love to visit different places very much. This time we are going to Bangladesh."

def make_lower(x):
    return x.lower()

def create_new_string():
    # make new list and string and convert it to lowercase for comparing 
    b=list(map(make_lower,a))
    lowerCase=s.lower()
    removeDot=lowerCase.replace('.','')
    removeComma=removeDot.replace(',','')
    remove_first_to=removeComma.replace("love to","love")
    broken_words=remove_first_to.split(" ")
    # make string after matching
    newText=""
    for word in broken_words:
        if  word in b:
            nextelement=broken_words[broken_words.index(word)-len(broken_words)+1]
            newText+=nextelement.capitalize()+" "
    # capitalization correction
    new_string=newText.replace('Love','love')
    # save in the file
    textFile= open('out.txt','a')
    textFile.write(new_string)
    textFile.close()


create_new_string()

