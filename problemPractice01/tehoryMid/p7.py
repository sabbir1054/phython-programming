text_str=""
with open("books.txt","r") as textFile:
    text_str=textFile.read()
textFile.close()

broken_text_str=text_str.split("--")



print(broken_text_str[0])
page_input = input("[enter - read more or page number, press q to quit]: ")
 
if page_input == 'q':
        print("Exited !")
elif page_input == '':
      print(broken_text_str[1])
   


