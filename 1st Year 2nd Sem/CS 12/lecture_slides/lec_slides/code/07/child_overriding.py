class A:
    def __init__(self, a: int):
        self.attr_of_a = a
 
 
class B(A):
    def __init__(self, b: int):
        self.attr_of_b = b
 
 
b = B(12)           # Has constructor based on `__init__` override
 
print(b.attr_of_b)  # 12 (exists due to `__init__` of `B` being called)
 
print(b.attr_of_a)  # AttributeError: 'B' object has no attribute 'attr_of_a';
                    # inherited `__init__` is overridden; not called by default
