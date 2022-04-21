
class Point:
    def __init__(self,*args, **kwargs) -> None:
        self.__coordinates = [*args]
        self.__dim = len(self.__coordinates)
        