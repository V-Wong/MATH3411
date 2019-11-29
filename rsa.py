from number_theory import gcd, modulo

class RSA:
    def __init__(self, p: int, q: int, e: int):
        self.p = p
        self.q = q
        self.n = p * q
        self.totient = (p - 1) * (q - 1)
        self.e = e

        self.verify_e()
        self.d = self.invert_e()

    def verify_e(self):
        coprimes = []
        for i in range(3, self.n):
            if gcd(i, self.totient):
                coprimes.append(i)

        assert self.e in coprimes

    def invert_e(self):
        for i in range(1, self.totient):
            if (i * self.e) % self.totient == 1:
                return i
    
    def encrypt(self, num: int):
        return modulo(num, self.e, self.n)


if __name__ == "__main__":
    rsa = RSA(17, 23, 235)
    print(rsa.encrypt(10))