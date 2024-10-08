def get_reversed_word(word):
    final_word=''
    for l in word:
        final_word = l + final_word
    return final_word


print(get_reversed_word(input()))