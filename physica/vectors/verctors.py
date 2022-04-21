from physica.vectors.points import Point


class Vector:
    def __init__(self, *args, **kwargs) -> None:
        self.__coordinates = [*args]
    
    @classmethod
    def unit_Vector_X(cls) -> 'Vector':
        return cls(1,0,0)
    
    @classmethod
    def unit_Vector_Y(cls) -> 'Vector':
        return cls(0,1,0)
    
    @classmethod
    def unit_Vector_Z(cls) -> 'Vector':
        return cls(0,0,1)
        
    @classmethod
    def from_point(cls, point: 'Point') -> 'Vector':
        return cls(*point.coordinates)
    
    @classmethod
    def from_two_points(cls, point1: 'Point', point2: 'Point') -> 'Vector':
        return cls(*(point2.coordinates[i] - point1.coordinates[i] for i in range(len(point1))))
    
    @classmethod
    def from_a_modulus(cls, modulus: float, direction: 'Point') -> 'Vector':
        return cls(*(modulus * direction.coordinates[i] for i in range(len(direction))))