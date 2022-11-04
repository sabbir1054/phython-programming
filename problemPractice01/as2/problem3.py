s="Programming Hero is the best"
broken_words=s.split(" ")
str=""
for word in broken_words:
    str+=word[::-1]+" "
print(str)