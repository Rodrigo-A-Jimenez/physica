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

