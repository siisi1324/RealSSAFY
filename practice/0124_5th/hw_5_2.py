def count_character(sentence, word):
    cnt = 0
    for i in sentence:
        if i == word :
            cnt += 1
    return cnt


result = count_character("Hello, World!", "o")
print(result) 
