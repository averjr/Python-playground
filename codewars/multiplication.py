def first(s):
    print s

@first
def second(s):
    s = s + 10

second(10)

#
# def func1(list):
#      print list
#      list += [47,11]
#      print list
#
# fib = [0,1,1,2,3,5,8]
# func1(fib)
# print fib
#


def multiTable(number):
    results = list()
    for i in range(1, 11):
        sum = i*number
        results.append("%s * %s = %s" % (i,number,sum))
    return "\n".join(results)

def multiTable(number):
    return "\n".join("{} * {} = {}".format(i, number, i*number) for i in range(1,11))


def remove_char(s):
    return s[1 : -1]

def get_age(age):
    for x in age:
      if x.isdigit():
          return int(x)
