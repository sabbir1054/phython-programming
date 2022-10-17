def clean_string(text):
    res=''.join(letter for letter in text if letter.isalnum())
    return res

s = "P::::::,,,,,h;;;;i,,,t--r;,:o..N"
output = clean_string(s)
print(output)
