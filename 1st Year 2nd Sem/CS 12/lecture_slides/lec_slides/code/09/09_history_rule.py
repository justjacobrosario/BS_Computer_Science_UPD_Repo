class IntStack:
    """
    Element access is guaranteed
    to follow last-in, first-out
    (LIFO) pattern.
    """
 
    def __init__(self):
        ...
 
    def push(self, value: int):
        ...
 
    def pop(self) -> int:
        ...
 
    def is_empty(self) -> bool:
        ...


class NondecreasingIntStack(IntStack):
    def push(self, value: int):
        """Pops values larger than `value`,
        then places `value` on top."""
        ...