# Complex Numbers

class Complex:

    def __init__(self, real_coef, complex_coef):
        self._real = real_coef
        self._complex = complex_coef

    def __str__(self):
        if self._real != 0:
            if self._complex > 0:
                if self._complex == 1:
                    return f"{self._real}+i"
                else:
                    return f"{self._real}+{self._complex}i"
            elif self._complex == 0:
                return f"{self._real}"
            else:
                if self._complex == -1:
                    return f"{self._real}-i"
                else:
                    return f"{self._real}{self._complex}i"
        else:
            if self._complex != 0:
                if self._complex == 1:
                    return "i"
                elif self._complex == -1:
                    return "-i"
                else:
                    return f"{self._complex}i"
            else:
                return "0"

    def __add__(self, other):
        return Complex(self._real + other._real, self._complex + other._complex)

    def __sub__(self, other):
        return Complex(self._real - other._real, self._complex - other._complex)

    def __mul__(self, other):
        return Complex(self._real * other._real - self._complex * other._complex,
                       self._complex * other._real + self._real * other._complex)

    def __truediv__(self, other):
        return Complex((self._real * other._real + self._complex * other._complex) /
                       (other._real **2 + other._complex ** 2),
                       (self._complex * other._real - self._real * other._complex) /
                       (other._real **2 + other._complex ** 2))


a = Complex(4, -3)
b = Complex(-2, 1)

print(a+b)
print(a-b)
print(a*b)
print(a/b)
