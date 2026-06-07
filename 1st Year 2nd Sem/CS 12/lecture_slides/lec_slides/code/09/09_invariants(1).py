class ImmutablePoint:
    """Form a 2D point with unmodifiable coordinates."""
 
    def __init__(self, x: int, y: int):
        self._x = x
        self._y = y
 
    @property
    def x(self) -> int:
        return self._x
 
    @property
    def y(self) -> int:
        return self._y


class HalfMutablePoint(ImmutablePoint):
    @property
    def x(self) -> int:
        return self._x
 
    @x.setter
    def x(self, value: int):
        self._x = value


class Client:
    def __init__(self, point: ImmutablePoint):
        self._point = point
 
    def use_point(self):
        # Point is immutable, so...
        ...
 
point = HalfMutablePoint(1, 2)
c = Client(point)
 
c.use_point()
point.x = 100
c.use_point()