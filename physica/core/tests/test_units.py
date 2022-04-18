from physica import dimensional_analysis
from sympy import Symbol

def test_length():
    L = Symbol('L')
    assert dimensional_analysis['length'] == L