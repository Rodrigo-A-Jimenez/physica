
class Point:
    def __init__(self,*args, **kwargs) -> None:    
        self.__coordinates = [*args]
        self.__dim = len(self.__coordinates)
    
    def __len__(self) -> int:
        return self.__dim
    
    def __str__(self) -> str:
        return 'Point(' + ','.join(map(str, self.__coordinates)) + ')'
    
    def __repr__(self) -> str:
        return 'Point(' + ','.join(map(str, self.__coordinates)) + ')'
    
    def __eq__(self, __o: object) -> bool:
        if not isinstance(__o, Point):
            return False
        return self.__coordinates == __o.__coordinates
    
    def __add__(self, other: 'Point') -> 'Point':
        if len(self) != len(other):
            raise ValueError('Dimensions must agree')
        return Point(*(a+b for a,b in zip(self.__coordinates, other.__coordinates)))
    
    def __sub__(self, other: 'Point') -> 'Point':
        if len(self) != len(other):
            raise ValueError('Dimensions must agree')
        return Point(*(a-b for a,b in zip(self.__coordinates, other.__coordinates)))
    
    @property
    def coordinates(self) -> list:
        return self.__coordinates
    
    @property
    def dim(self) -> int:
        return self.__dim
    
    @coordinates.setter
    def coordinates(self, new_coordinates: list) -> None:
        self.__coordinates = new_coordinates
        self.__dim = len(self.__coordinates)
        
    