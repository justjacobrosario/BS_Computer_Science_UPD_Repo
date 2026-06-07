class Demo:
    def __init__(self, a: int, b: int):
        self.a = a
        self.b = b
 
    @property
    def c(self):
        return self.a + self.b
 
x = Demo(1, 2)
print(x.a)        # 1
print(x.b)        # 2
print(x.c)        # 3
 
x.a = 10
print(x.a)        # 10
print(x.c)        # 12
 
x.c = 100         # AttributeError: property 'c' of
                  # 'Demo' object has no setter