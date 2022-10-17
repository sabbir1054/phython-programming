replace_with = ["chief", "thief", "superintendent", "sweeper",
"married", "left", "tried", "died"]
s = "I am the chief of Baghdad. Before that I used to be a superintendent of Bank Asia. Things have changed a lot since Jorina married me. A lot of girls tried to marry me."

def replace_word():
    broken_words=s.split(" ")
    newText=""
    for word in broken_words:
        newText+=word+" "
        if word in replace_with:
            nextelement=replace_with[replace_with.index(word)-len(replace_with)+1]
            newText=newText.replace(word,nextelement)
    print(newText)
   

replace_word()

