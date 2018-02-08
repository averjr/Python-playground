import math


def is_palindrome(n):
    string = str(n)
    if string == string[::-1]:
        return True
    return False


def multiply():
    result = []

    # [Finished in 70.334s] compare to 132. s without index
    # idx = primes.index(x)
    # for n in primes[idx::-1]:
    #     mult = x * n
    #
    #     if is_palindrome(mult):
    #         print([primes.index(x), primes.index(n), x, n, mult])
    #         # print([primes.index(x), primes.index(n), x, n, result])
    #         result.append([primes.index(x), primes.index(n), x, n, mult])

    # 44s
    for i in range(0, len(primes)):
        for j in range(0, len(primes)):
            # remove i*j j*i duplication [Finished in 24.739s]
            if(j < i):
                continue

            mult = primes[i] * primes[j]
            if is_palindrome(mult):
                result.append([primes[i], primes[j], mult])

    return result


def is_prime(n):
    # [Finished in 134.101s]
    # i = 2
    # while i < n:
    #     if n % i == 0:
    #         return False
    #     i += 1

    # [Finished in 1.794s]
    for j in range(2, int(math.sqrt(n)+1)):
        if n % j == 0:
            return False

    return True


def get_all_primes_between(start, end):
    result = []
    for p in range(start, end):
        if is_prime(p):
            result.append(p)
    return result


primes = get_all_primes_between(10000, 99999)
result = multiply()

# r = sorted(result, key=lambda tup: tup[2])
print(result)
