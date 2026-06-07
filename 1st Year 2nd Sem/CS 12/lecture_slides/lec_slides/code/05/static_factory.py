class A:
    def __init__(self, b: B, c: C):   # Dependencies are injected; will have to supply
        self.b = b                    # them every time an A object is created
        self.c = c
 
    @classmethod
    def default(cls):        # Static factory method for A; may also have parameters
        b = B(123)
        c = C(123)
 
        return cls(b, c)     # Take default to be A with B(123) and C(123);
                             # no need to supply dependencies for default case;
                             # cls == A (can use `return A(b, c)` instead)
 
a = A.default()              # Called using the class itself (no need for an object)
