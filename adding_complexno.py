class Complex:
    def __init__(self, r, i):
        self.r = r
        self.i = i

    def __add__(self, num2):
        return Complex(self.r + num2.r, self.i + num2.i)

    def __str__(self):
        return f"{self.r} + {self.i}i"


c1 = Complex(1, 2)
num2 = Complex(3, 4)
print(c1 + num2)
