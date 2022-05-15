import sympy


class Rsa:
    def __init__(self):
        p = sympy.randprime(pow(10, 190), pow(10, 201))
        while True:
            q = sympy.randprime(pow(10, 190), pow(10, 201))
            if p != q:
                self.p = p
                self.q = q
                break
        self.n = p * q
        self.lcm = sympy.lcm(p-1, q-1)

        while True:
            e = sympy.randprime(max(p, q)+1, self.lcm)
            if sympy.gcd(e, self.lcm) == 1:
                self.e = e
                break

        d = sympy.gcdex(e, self.lcm)
        self.d = int(d[0] % self.lcm)

    def get_enc_key(self):
        return self.e, self.n

    def get_dec_key(self):
        return self.d, self.n