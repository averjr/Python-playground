import re


def iq_test(numbers):
    result = False
    r = re.findall('\d+', numbers)
    odds = []
    evans = []
    for pos, num in enumerate(r):
        if int(num) % 2 == 0:
            odds.append(pos + 1)
        else:
            evans.append(pos + 1)

    return odds[0] if len(odds) == 1 else evans[0]


print(iq_test("2 4 7 8 10"))

# def iq_test(numbers):
#     e = [int(i) % 2 == 0 for i in numbers.split()]
#
#     return e.index(True) + 1 if e.count(True) == 1 else e.index(False) + 1



import string


def is_pangram(s):
    s = s.strip(',.').lower()
    r = re.findall('[a-zA-Z]', s)
    if len(set(r)) == 26:
        return True

    return False


pangram = "Cwm fjord bank glyphs vext quiz"
is_pangram(pangram)
pangram = "The quick, brown fox jumps over the lazy dog!"
is_pangram(pangram)
pangram = "ABCD45EFGH,IJK,LMNOPQR56STUVW3XYZ"
is_pangram(pangram)
#
# import string
#
# def is_pangram(s):
#     return set(string.lowercase) <= set(s.lower())
