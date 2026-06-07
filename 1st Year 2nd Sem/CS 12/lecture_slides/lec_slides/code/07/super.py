class A:
    def __init__(self, a: int):
        self.attr_of_a = a

class B(A):
    def __init__(self, a: int, b: int):  # Note new initializer parameter
        super().__init__(a)             # __init__ of superclass is called
        self.attr_of_b = b              # B's own fields initialized after

b = B(100, 12)      # Has constructor based on new `__init__`
print(b.attr_of_a)  # 100 (exists due to new `__init__` being called)
print(b.attr_of_b)  # 12
