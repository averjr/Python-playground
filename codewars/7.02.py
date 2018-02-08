# . [[1,2,[3]],4] -> [1,2,3,4].
def flater(arr):
    result = []
    for el in arr:
        if isinstance(el, list):
            result = result + flater(el)
        else:
            result.append(el)
    return result


def snail(array):
    results = []

    def move_right():
        for el in array[0]:
            results.append(el)
        del(array[0])

    def move_left():
        for el in array[-1][::-1]:
            results.append(el)
        del(array[-1])

    def move_down():
        for el in array:
            results.append(el.pop())

    def move_up():
        for el in array[::-1]:
            results.append(el[0])
            del(el[0])

    def check():
        if len(results) == all_elements:
            return True

    all_elements = sum(len(x) for x in array)
    for el in range(all_elements, 0, -1):
        try:
            move_right()
            move_down()
            move_left()
            move_up()
        except:
            break


    return results

array = [[1,2,3],
         [4,5,6],
         [7,8,9]]
expected = [1,2,3,6,9,8,7,4,5]
print(expected)
print(snail(array))

# def snail(array):
#     res = []
#     while True:
#         try:
#             res.append(array.pop(0))
#             res.append([x.pop(-1) for x in array])
#             res.append(array.pop(-1)[::-1])
#             res.append([x.pop(0) for x in array][::-1])
#         except:
#             break
#     return sum(res, [])

#
#
# def snail(array):
#     return list(array[0]) + snail(zip(*array[1:])[::-1]) if array else []
#
#
# def snail(array):
#     a = []
#     while array:
#         a.extend(list(array.pop(0)))
#         array = zip(*array)
#         array.reverse()
#     return a
#
#
# def snail(array):
# ret = []
# if array and array[0]:
#     size = len(array)
#     for n in xrange((size + 1) // 2):
#         for x in xrange(n, size - n):
#             ret.append(array[n][x])
#         for y in xrange(1 + n, size - n):
#             ret.append(array[y][-1 - n])
#         for x in xrange(2 + n, size - n + 1):
#             ret.append(array[-1 - n][-x])
#         for y in xrange(2 + n, size - n):
#             ret.append(array[-y][n])
# return ret
#
# # my implementation/explanation of the solution by foxxyz
# def snail(array):
#   if array:
#     # force to list because zip returns a list of tuples
#     top_row = list(array[0])
#     # rotate the array by switching remaining rows & columns with zip
#     # the * expands the remaining rows so they can be matched by column
#     rotated_array = zip(*array[1:])
#     # then reverse rows to make the formerly last column the next top row
#     rotated_array = rotated_array[::-1]
#     return top_row + snail(rotated_array)
#   else:
#     return []
#
#
# import numpy as np
#
# def snail(array):
#     arr = np.array(array)
#
#     if len(arr) < 2:
#         return arr.flatten().tolist()
#
#     tp = arr[0, :].tolist()
#     rt = arr[1:, -1].tolist()
#     bm = arr[-1:, :-1].flatten()[::-1].tolist()
#     lt = arr[1:-1, 0] [::-1].tolist()
#
#     return tp + rt + bm + lt + snail(arr[1:-1, 1:-1])
#
#
#
# def snail(array):
#     res = []
#     while len(array) > 1:
#         res = res + array.pop(0)
#         res = res + [row.pop(-1) for row in array]
#         res = res + list(reversed(array.pop(-1)))
#         res = res + [row.pop(0) for row in array[::-1]]
#     return res if not array else res + array[0]
