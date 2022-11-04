# problem 01
def checkPalindrome(strInput):
    if strInput.lower()==strInput[::-1].lower():
        print("Yes")
    else: 
        print("No")

strInput=input()
checkPalindrome(strInput)
