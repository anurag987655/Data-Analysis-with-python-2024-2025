#!/usr/bin/env python3
from fractions import Fraction

class Rational(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.af = Fraction(a, b)
        
    def __add__(self, other):
        result = self.af + other.af
        return Rational(result.numerator, result.denominator)
    
    def __sub__(self, other):
        result = self.af - other.af
        return Rational(result.numerator, result.denominator)
    
    def __mul__(self, other):
        result = self.af * other.af
        return Rational(result.numerator, result.denominator)
    
    def __truediv__(self, other):
        result = self.af / other.af
        return Rational(result.numerator, result.denominator)
    
    def __eq__(self, other):
        return self.af == other.af
    
    def __lt__(self, other):
        return self.af < other.af
    
    def __gt__(self, other):
        return self.af > other.af
    
    def __str__(self):
        return f"{self.a}/{self.b}"

def main():
    r1 = Rational(1, 4)
    r2 = Rational(2, 3)
    print(r1)  
    print(r2)  
    print(r1 * r2) 
    print(r1 / r2)  
    print(r1 + r2)  
    print(r1 - r2)  
    print(Rational(1, 2) == Rational(2, 4))  
    print(Rational(1, 2) > Rational(2, 4)) 
    print(Rational(1, 2) < Rational(2, 4))  

if __name__ == "__main__":
    main()