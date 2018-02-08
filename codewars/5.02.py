def move_zeros(array):
    zeros = [int(x) for x in array if type(x) in [float, int] and int(x) is 0]

    new_arr = []
    for i in array:
        if type(i) in [float, int] and i == 0:
            continue

        new_arr.append(i)

    return new_arr + zeros


move_zeros(["a","b"])
print(move_zeros([9,0.0,0,9,1,2,0,1,0,1,0.0,3,0,1,9,0,0,0,0,9]))
print([9,9,1,2,1,1,3,1,9,9,0,0,0,0,0,0,0,0,0,0])
#
# def move_zeros(arr):
#     l = [i for i in arr if isinstance(i, bool) or i!=0]
#     return l+[0]*(len(arr)-len(l))
#
# def move_zeros(array):
#     return sorted(array, key=lambda x: x==0 and type(x) is not bool)
