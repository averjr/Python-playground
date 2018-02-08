import math


def sum_dig_pow(a, b):
    # range(a, b + 1) will be studied by the function
    # your code here
    result = []

    for d in range(a, b+1):
        flag = False

        digits_count = len(str(d))
        summ = 0

        for i in range(0, digits_count):
            current_digit = int(str(d)[i])
            power = math.pow(current_digit, i+1)

            summ = summ + int(power)

        if summ == d:
            result.append(d)
    return result


print(sum_dig_pow(1, 10))
#
# def filter_func(a):
#     return sum(int(d) ** (i+1) for i, d in enumerate(str(a))) == a
#
# def sum_dig_pow(a, b):
#     return filter(filter_func, range(a, b+1))
