from number_theory import gcd, modulo
from factorisation_methods import naive_trial_factorisation

class RSA:
    def __init__(self, n: int, e: int):
        self.n = n
        self.e = e
        
        self.factors = self.factorise_n()
        self.p = self.factors[0]
        self.q = self.factors[1]
        self.totient = (self.p - 1) * (self.q - 1)
        
        self.verify_e()
        self.d = self.invert_e()

    def factorise_n(self):
        factors = naive_trial_factorisation(self.n)
        factors.remove(1)
        
        if len(factors) != 2:
            raise Exception(f"{self.n} is not pseudo prime.")
        else:
            return factors

    def verify_e(self):
        coprimes = []
        for i in range(3, self.n):
            if gcd(i, self.totient):
                coprimes.append(i)

        if self.e not in coprimes:
            raise Exception(f"{self.e} is not coprime with {self.n}")

    def invert_e(self):
        for i in range(1, self.totient):
            if (i * self.e) % self.totient == 1:
                return i
    
    def encrypt(self, num: int):
        return modulo(num, self.e, self.n)

    def decrypt(self, num: int):
        return modulo(num, self.d, self.n)


if __name__ == "__main__":
    rsa = RSA(533, 233)
    print(rsa.decrypt(383))

    