
class Point:
    def __init__(self,*args, **kwargs) -> None:    
        self.__coordinates = [*args]
        self.__dim = len(self.__coordinates)
    
    def __len__(self) -> int:
        return self.__dim
    
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
        