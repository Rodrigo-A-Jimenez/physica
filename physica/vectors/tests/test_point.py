from physica import Point

def test_coord():
    A = Point(1,2,3)
    assert A.coordinates == [1,2,3]
    
    A.coordinates = [4,5,6]
    assert A.coordinates == [4,5,6]
    
    
def test_dim():
    A = Point(1,2,3)
    assert A.dim == 3
    
    A.coordinates = [4,5]
    assert A.dim == 2

def test_str():
    A = Point(1,2,3)
    assert str(A) == 'Point(1,2,3)'
    
def test_operations():
    A = Point(1,2,3)
    B = Point(4,5,6)
    C1 = A + B
    C2 = A - B
    assert C1 == Point(5,7,9)
    assert C2 == Point(-3,-3,-3)
