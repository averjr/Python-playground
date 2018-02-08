import math


def is_palindrome(n):
    string = str(n)
    if string == string[::-1]:
        return True
    return False


def is_prime(n):
    for j in range(2, int(math.sqrt(n)+1)):
        if n % j == 0:
            return False
    return True


def multiply(primes):
    # [first prime, second prime, multipl]
    result = [0, 0, 0]

    for i in range(0, len(primes)):
        for j in range(0, len(primes)):
            # remove i*j j*i duplication
            if(j < i):
                continue

            mult = primes[i] * primes[j]
            if not is_palindrome(mult):
                continue

            # to get highest polindrome
            if mult > result[2]:
                result = [primes[i], primes[j], mult]
    return result


def get_all_primes_between(start, end):
    result = []

    for p in range(start, end):
        if is_prime(p):
            result.append(p)
    return result


primes = get_all_primes_between(10000, 99999)
result = multiply(primes)
print(result)
