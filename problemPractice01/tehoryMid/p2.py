def center_align(str):
    print(str.center(60))

# str=input()
# center_align(str)

f = open("txt.txt", "r")
broken_text=(f.read()).split(" \n")

for text in broken_text:
    center_align(text)