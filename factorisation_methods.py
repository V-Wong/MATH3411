from typing import List
import math


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

    for t in range(math.ceil(math.sqrt(n)), n + 1):
        s_squared = t ** 2 - n
        s = math.sqrt(s_squared)

        if int(s) == math.sqrt(s_squared):
            return [int(s + t), int(t - s)]


if __name__ == "__main__":
    print(naive_trial_factorisation(12412312312412351))
    print(fermat_factorisation(231412312321))