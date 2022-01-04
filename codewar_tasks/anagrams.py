def anagrams(word, words):
    res = []
    for wrd in words:
        reswrd = 0
        if (len(wrd) != len(word)):
            reswrd = False
        else:
            reswrd = True
            for letter in wrd:
                if (word.count(letter) != wrd.count(letter)):
                    reswrd = False
                if (word.find(letter) == -1):
                    reswrd = False
        if (reswrd == True):
            res.append(wrd)
    return res


word = 'racer'
words = ['crazer', 'carer', 'racar', 'caers', 'racer']
print(anagrams(word, words))


#best practice
#def anagrams(word, words): return [item for item in words if sorted(item)==sorted(word)]