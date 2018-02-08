import collections
a = [3, 5, 6, 3, 3, 5]
import collections
import math



result = 0
l = [count for item, count in collections.Counter(a).items() if count > 1]
print("1234",l)

for el in l:
    result = result + math.ceil(el/2.0)
    print(math.ceil(el/2.0))
    print('el', el, result)

print( result )
