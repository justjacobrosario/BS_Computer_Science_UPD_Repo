class BoundedIntList:
    def __init__(self, limit: int):
        self._limit = limit  # Should validate
        self._elems: list[int] = []
 
    def append(self, value: int):
        if len(self._elems) < self._limit:
            self._elems.append(value)


class UnboundedIntList(BoundedIntList):
    def append(self, value: int):
        self._elems.append(value)