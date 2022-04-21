from physica import Point

def test_coord():
    A = Point(1,2,3)
    assert A.coordinates == [1,2,3]
    