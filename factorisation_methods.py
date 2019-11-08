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


if __name__ == "__main__":
    print(naive_trial_factorisation(97))