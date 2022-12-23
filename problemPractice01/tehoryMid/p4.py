
def anagrams(anagramsList):
    grouped_anagrams = {}
    for string in anagramsList:
        sorted_string = str(sorted(string))
        if sorted_string in grouped_anagrams:
         grouped_anagrams[sorted_string].append(string)
        else:
         grouped_anagrams[sorted_string] = [string]
    print(list(grouped_anagrams.values()))

anagrams(['eat', 'ate', 'done', 'tea', 'soup', 'node'])