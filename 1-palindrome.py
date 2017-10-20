def is_palidrome_v1(word):
    return word == reverse_word(word)


def is_palidrome_v2(word):




# def is_palidrome_v3(word):





def reverse_word(sentence):
    result = ''
    for ch in sentence:
        result = ch + result
    return result

print(is_palidrome_v1(""))
