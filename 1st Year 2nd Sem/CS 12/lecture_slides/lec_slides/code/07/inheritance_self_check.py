class A:
    def f(self):
        print("f of A")

    def g(self):
        print("g of A")

    def g2(self):
        print("g2 of A")
        self.g()


class B(A):
    def g(self):
        print("g of B")

    def h(self):
        print("h of B")
        super().f()
        super().g()
        self.f()
        self.g()


class C(B):
    def g(self):
        print("g of C")


b = B()
b.f()
b.g()
b.h()
b.g2()

print("---")

c = C()

c.f()
c.g()
c.h()
c.g2()
