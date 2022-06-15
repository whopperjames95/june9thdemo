# answer = int(float('3.99'))
# #this will round to the first digit
# print(answer)

# decimals:

# from decimal import Decimal

# Decimal('.1') * 10
# Decimal('1.0')
# sum([.1] * 10)


#fractions:




class Fraction:

    def _operator_fallbacks(monomorphic_operator, fallback_operator):
        def forward(a,b):
            if isinstance(b, (int, Fraction)):
                return monomorphic_operator(a.b)
            elif isinstance(b, float):
                return fallback_operator(float(a), b)
            elif isinstance(b, complex):
                return fallback_operator(complex(a), b)
            else:
                return NotImplemented
        forward.__name__ = '__' + fallback_operator.__name__ + '__'
        forward.__doc__ = monomorphic_operator.__doc__
        # reverse is similar omitted for length
        return forward, reverse


# exploring fraction types: 

class Cup:
    def __init__(self, num, denom, name):
        self.f = Fraction(num, denom)
        self.name = name
    def __repr__(self):
        gt = ''
        if self.f > 1:
            gt = 's'
        return f'{self.ff.numerator}/{self.f.denomiator} Cup{gt} {self.name}'
    def __mul__(self, other):
        val = self.f * other
        return Cup(val.numerator, val.denomiator, self.name)

c = Cup(3,2,'Sugar')
c * 6
# answer = 9/1 Cups Sugar






class Measurement:
    def __init__(self, num, denom, name):
        self.f = Fraction(num, denom)
        self.name = name
    def __repr__(self):
        gt = ''
        if self.f > 1:
            gt = 's'
        denom = f'/{self.f.denominator}'
        if self.f.denominator == 1:
            denom = ''
        return f'{self.f.numerator:2}{denom:6} {self.__class__.__name__}{gt} {self.name}'
    def __mul__(self, other):
        val = self.f * other
        try:
            return self.__class__(val.numerator, val.denominator, self.name)
        except AttributeError:
            val = Fraction.from_float(val).limit_denominator(8)
        return self.__class__(val.numerator, val.denominator, self.name)

class Cup(Measurement)
    pass

class Tablespoon(Measurement):
    def __mul__(self, other):
        res = super().__mul__(other)
        if res.f >= 3:
            val = res.f * Fraction(1,12)
            return Cup(val.numerator, val.denominator, self.name)
        return res

class Teaspoon(Measurement):
    def __mul__(self, other):
        res = super().__mul__(other)
        if res.f >= 3:
            val = res.f * Fraction(1,3)
            return Tablespoon(val.numerator, val.denominator, self.name)
        return res

c = Cup(3,2, 'Sugar')
t = Teaspoon(1,1, 'Vanilla')
T = Tablespoon(1,2, 'Baking Soda')
c * 6.6, t* 4, t*2, T * 6




# interest jup 
decimal.getcontext().prec = 28
p = 200_000
n = 30 * 12
r = Decimal('6.25') / 100 / 12

left = ppaid = 0
month = 1
print(r)
while True:
    c = (r * p) / (1 - (1 + r)**(-n))

    paid += c
    left -= c
    print(f'Month: {month} Paid: {paid:.2f} Remaining: {left:.2f} {c:.2f}')
    if month >= n:
        break
    month += 1

mortgage_sim(#number)


# vector class 

class Vector:
    def __init__(self,vals):
        self.vals = vals

    def __repr__(self):
        return f'{self.__class__.__name__}({repr(self.vals)})'

    def __len__(self):
        return len(self.vals)

    def __add__(self,other):
        if isinstance(other,Vector):
            return Vector([self.vals[i] + other.vals[i] for i in range(len(self))])
        else:
            return Vector([v + other for v in self.vals])

    def __mul__(self, other):
        return Vector([v * other for v in self.vals])

Vector([1,2,3])
