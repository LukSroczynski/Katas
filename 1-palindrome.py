def is_palindrome_v1(word):
    return word == reverse_string(word)


def is_palindrome_v2(word):

    length = len(word)
    left_half = word[:length // 2]
    right_half = reverse_string(word[length - (length // 2):])
    return left_half == right_half

def is_palindrome_v3(word):

    i = 0             # start-index of the string
    j = len(word) - 1 # last-index of the string

    while i < j and ( word[i] == word[j] ):
        i += 1
        j -= 1

    return j <= i

def reverse_string(sentence):
    result = ''
    for ch in sentence:
        result = ch + result
    return result

# print(is_palidrome_v1(""))
# print(is_palidrome_v2("adYeda"))
print(is_palindrome_v3(""))
# print(len("12345") // 2)
