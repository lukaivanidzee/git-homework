def get_unique_word(word):
    wordlist=[]
    for l in word:
        if l in wordlist:
            return False
        wordlist.append(l)
    return True

print(get_unique_word(input()))
    