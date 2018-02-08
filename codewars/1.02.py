def countBits(n):
    result = 0
    for n in str(bin(n)):
        if n == "1":
            result = result + 1
    return result

# print(countBits(1234))

# def countBits(n):
#     return bin(n).count("1")


def divisors(integer):
    result = []
    for n in range(2, integer):
        if integer % n == 0:
            result.append(n)
    if result == []:
        result = "{} is prime".format(integer)
    return result

# def divisors(num):
#     l = [a for a in range(2,num) if num%a == 0]
#     if len(l) == 0:
#         return str(num) + " is prime"
#     return l


def mult(n):
    r = 1
    for i in [int(d) for d in str(n)]:
        r = r * i
    return r


def persistence(n):

    result = 0

    while not len(str(n)) == 1:
        n = mult(n)
        result = result + 1

    return result

# print(persistence(39))

# import operator
# def persistence(n):
#     i = 0
#     while n>=10:
#         n=reduce(operator.mul,[int(x) for x in str(n)],1)
#         i+=1
#     return i
