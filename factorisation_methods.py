from typing import List, Callable
import math
import time


def naive_trial_factorisation(n: int) -> List[int]:
    '''
    Tests all i from 2 to n.
    If i divides n, then i is a factor, continue algorithm with n/i.
    Repeat until n is fully factorised.
    '''

    factors = [1]

    completely_factored = False
    while not completely_factored:
        for i in range(2, math.floor(math.sqrt(n)) + 1):
            if n % i == 0:
                factors.append(i)
                n = int(n / i)
                break
        else:
            factors.append(n)
            completely_factored = True

    return factors


def fermat_factorisation(n: int) -> (int, int):
    '''
    Tests all t from sqrt(n) to n.
    If s^2 = t^2 - n is a square, then return n = ab = (t + s)(t - s).
    '''

    if n % 2 == 0:
        return (int(n / 2), 2)

    for t in range(math.ceil(math.sqrt(n)), n + 1):
        s_squared = t ** 2 - n
        s = math.sqrt(s_squared)

        if int(s) == math.sqrt(s_squared):
            return [int(s + t), int(t - s)]


def fully_factorise(n: int, f: Callable) -> (int, int):
    ''' 
    Given a factorisation function that ouputs 2 factors,
    this function will recursively factor
    until we reach have reached prime factorisation.
    '''

    if n == 1:
        return [1]
    else:
        num0, num1 = f(n)
        if num0 == n or num1 == n:
            return [n]
        else:
            return fully_factorise(num0, f) + fully_factorise(num1, f)


if __name__ == "__main__":
    start = time.time()
    print(naive_trial_factorisation(1373 * 1291 * 1223))
    end = time.time()
    print(f"Time taken for trial factorisation: {round(end - start, 5)}")

    start = time.time()
    print(fermat_factorisation(1373 * 1291 * 1223))
    end = time.time()
    print(f"Time taken for 2-Fermat factorisation: {round(end - start, 5)}")

    start = time.time()
    print(fully_factorise(1373 * 1291 * 1223, fermat_factorisation))
    end = time.time()
    print(f"Time taken for full-Fermat factorisation: {round(end - start, 5)}")
