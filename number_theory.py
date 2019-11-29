def gcd(a: int, b: int) -> int:
    '''
    a = q_0 * b + (a % b)
    b = q_1 * (a % b) + r
    '''

    if b == 0: 
        return a

    return gcd(b, a % b)


def modulo(base: int, pow: int, mod: int) -> int:
    res = 1

    for _ in range(1, pow + 1):
        res *= base
        res %= mod

    return res


if __name__ == "__main__":
    print(gcd(32, 6))