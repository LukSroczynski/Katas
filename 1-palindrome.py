def is_palidrome_v1(word):
    return word == reverse_string(word)


def is_palidrome_v2(word):

    length = len(word)
    left_half = word[:length // 2]
    right_half = reverse_string(word[length - (length // 2):])
    return left_half == right_half

def is_palidrome_v3(word):

    length = len(word)
    index = 0

    for i in word:
        if i == word[index]:
            return False

    return True

def reverse_string(sentence):
    result = ''
    for ch in sentence:
        result = ch + result
    return result

print(is_palidrome_v1(""))
print(is_palidrome_v2("adYeda"))
print(is_palidrome_v3("ada"))
print(len("12345") // 2)
