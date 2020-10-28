import math

def addition(a,b):
    return int(a) + int(b)

def subtraction(a,b):
    return int(a) - int(b)

def multiplication(a,b):
    return int(a) * int(b)

def division(a,b):
    c = float(a) / float(b)
    return round(c, 9)

def square(a):
    return float(a) ** 2

def squareRoot(a):
    r = math.sqrt(float(a))
    roundRoot = round(r, 8)
    return roundRoot

class Calculator:
    result = 0

    def __init__(self):
        pass

    def add(self, a, b):
        self.result = addition(a, b)
        return self.result

    def subtract(self, a, b):
        self.result = subtraction(a, b)
        return self.result

    def multiply(self, a, b):
        self.result = multiplication(a, b)
        return self.result

    def divide(self, a, b):
        self.result = division(a, b)
        return self.result

    def square(self,a):
        self.result = square(a)
        return self.result

    def squareRoot(self,a):
        self.result = squareRoot(a)
        return self.result