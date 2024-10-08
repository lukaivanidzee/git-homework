def count_letters(word):
    letters_list={}
    for l in word:
        if l in letters_list:
            letters_list[l] = letters_list[l] + 1
        else:
            letters_list[l] = 1
    return letters_list

print(count_letters(input()))