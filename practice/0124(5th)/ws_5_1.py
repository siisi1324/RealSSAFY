def reverse_string(sentence):
    new_sentence = reversed(sentence)
    newnew = ''.join(new_sentence)
    return newnew

# reversed()의 결과는 이터레이터이므로 문자열로 사용하려면 이를 다시 조합해야 한다. 


result = reverse_string("Hello, World!")
print(result)  
