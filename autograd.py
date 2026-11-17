# Numerical helpers and plotting for the derivative examples below
import numpy as np
import math
import matplotlib.pyplot as plt

#creating a class for scalar value
class Value:
    def __init__(self, data, _children=(), _op=''):
        self.data = data
        self._children = set(_children)
        self._op = _op

    def __repr__(self):
        return f"Value(data={self.data}, _op={self._op})"

    def __add__(self, other):
        return Value(self.data + other.data, (self, other), '+')

    def __mul__(self, other):
        return Value(self.data * other.data, (self, other), '*')

print(Value(2.0) + Value(3.0))