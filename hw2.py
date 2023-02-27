import sympy


def primes(n):
    s = ''
    k = 1
    i = 1
    while n >= k:
        if sympy.isprime(i):
            s += str(i)
            k += 1
        i += 1
    return s


def naive(s):
    two_digit_counter = [0] * 90
    for i in range(len(s) - 1):
        number = int(s[i] + s[i + 1])
        if number >= 10:
            two_digit_counter[number - 10] += 1
    return two_digit_counter


def rabin_carp(s):
    two_digit_counter = [0] * 90
    dim = 10
    symbols = [str(i) for i in range(10)]
    symbols_hash = []
    for j in range(10, 100):
        hash = 0
        string = str(j)
        for i in range(2):
            for k in range(len(symbols)):
                if string[i - 1] == symbols[k]:
                    hash += int((symbols[k]) * (dim ** i))
        symbols_hash.append(hash)

    for r in range(len(s) - 1):
        hash = 0
        string = (s[r] + s[r + 1])
        for j in range(2):
            for k in range(len(symbols)):
                if string[j - 1] == symbols[k]:
                    hash += int((symbols[k]) * (dim **j))
        for p in range(len(symbols_hash)):
            if hash == symbols_hash[p] and int(string) == (p + 10):
                two_digit_counter[p] += 1
                break
    return two_digit_counter


def boyer_mur(s):
    two_digit_counter = [0] * 90
    i = 0
    while not (i == len(s) - 2):
        number = int(s[i] + s[i + 1])
        if number >= 10 and number <= 99:
            two_digit_counter[number - 10] += 1
            i += 1
        elif number >= 1:
            i += 1
        else:
            i += 2
    return two_digit_counter

def knut_morris_pratt(s):
    two_digit_counter = [0] * 90
    i = 0
    while not (i == len(s) - 2):
        if s[i] == s[i + 1] and s[i] == '0':
            prefix = 1
            i += prefix
        number = int(s[i] + s[i + 1])
        if number >= 10 and number <= 99:
            two_digit_counter[number - 10] += 1
            i += 1
        elif number >= 1:
            prefix = 1
            i += prefix
    return two_digit_counter


primes_str = primes(500)
print(primes_str)
print('Наивный алгоритм:',max(naive(primes_str)))
print('Алгоритм Рабина-Карпа:',max(rabin_carp(primes_str)))
print('Алгоритм Бойера-Мура:',max(boyer_mur(primes_str)))
print('Алгоритм Кнута-Морриса-Пратта:',max(knut_morris_pratt(primes_str)))