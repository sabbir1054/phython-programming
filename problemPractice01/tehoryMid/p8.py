text_str=""
with open("books.txt","r") as textFile:
    text_str=textFile.read()
textFile.close()

broken_text_str=text_str.split("--")

length = len(broken_text_str)
print(broken_text_str[0])
 
 
page_input = input("[enter - read more or page number, press q to quit]: ")
 

while True:
    if page_input=="q":
        print("Exited \n")
    else:
        if int(page_input)<0:
            print("Try again negative page number not allow \n")
        else:
            if int(page_input)<=length:
                if int(page_input)==0:
                    print(broken_text_str[0])
                else:
                    print(broken_text_str[(int(page_input)-1)])
            else:
                print("\n*Page not found , go to page 1\n")
                print(broken_text_str[0])
    page_input = input("[enter - read more or page number, press q to quit]: ")
