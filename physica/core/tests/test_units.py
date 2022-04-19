from physica.core.units import dim_analysis
from sympy import Symbol

def test_length():
    L = Symbol('L')
    basicDims = dim_analysis.basic_dims
    print(basicDims)
    assert basicDims == 0
    assert dim_analysis.value == 0