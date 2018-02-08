import re


def nums_sum(d):
    sm = 0
    for i in [int(d) for d in str(d)]:
        sm = sm + i
    return sm


def keyfunc(x):
    # print(x[0], x[1])
    sec = sort_func(x[1])
    return (sec-x[0])


def bubbleSort(nums):
    for passnum in range(len(nums)-1, 0, -1):
        for i in range(passnum):

            if nums_sum(nums[i][1]) > nums_sum(nums[i+1][1]):
                temp = nums[i]
                nums[i] = nums[i+1]
                nums[i+1] = temp

    return nums


def order_weight(strng):
    # r = sorted([int(s) for s in strng.split() if s.isdigit()], key=sort_func)
    # numbers = [int(s) for s in strng.split() if s.isdigit()]
    #
    # strng = re.sub('\d+', '{}', strng)
    # return strng.format(*r)
    r = []
    for count, elem in enumerate([int(s) for s in strng.split() if s.isdigit()]):
        # print(count, elem)
        r.append([count, elem])

    print( bubbleSort(r) )

    # list1 = sorted(r, key=keyfunc)
    # print("!!", list1)
    # r = sorted([int(s) for s in strng.split() if s.isdigit()], key=sort_func)


print(order_weight("2000 10003 1234000 44444444 9999 11 11 22 123"))
print("11 11 2000 10003 22 123 1234000 44444444 9999")


# 
# def order_weight(_str):
#     return ' '.join(sorted(sorted(_str.split(' ')), key=lambda x: sum(int(c) for c in x)))
#
# def sum_string(s):
#     sum = 0
#     for digit in s:
#         sum += int(digit)
#     return sum
#
# def order_weight(strng):
#     # your code
#     initial_list = sorted(strng.split())
#     result = " ".join(sorted(initial_list, key=sum_string))
#
#     return result
#
# def weight_key(s):
#     return (sum(int(c) for c in s), s)
# def order_weight(s):
#     return ' '.join(sorted(s.split(' '), key=weight_key))
