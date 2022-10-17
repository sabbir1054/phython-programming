def replace_comma_with_space(text):
    broken_text=text.split(',')
    newText=""
    for word in broken_text:
        newText+=word+" "
    return newText

s = "I,have,been,practising,python,since,the,course,started"
output = replace_comma_with_space(s)
print(output)