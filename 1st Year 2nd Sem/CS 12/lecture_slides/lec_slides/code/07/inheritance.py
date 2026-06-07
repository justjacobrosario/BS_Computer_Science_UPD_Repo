class Base:
    def hello(self):
        print("Hello, world!")

    def super_secret(self): ...


#   Base
#  / |  \
# D  Y   A


class YetAnotherDerived(Base): ...


class Derived(Base):  # `Derived` inherits `hello`
    def hi(self):  # of `Base`; `Derived <: Base`
        print("Hi!")  # means `Derived` "is a" `Base`


class AnotherDerived(Base):
    def hey(self): ...


# d = Derived()
#
# d.hi()
# d.hello()


class Dog:
    def __init__(self, age: int):
        self.age = age

    def bark(self, name: str):
        print(f"[{name}] Arf arf!")

    def sit(self):
        print("no!")


# `TrainedDog <: Dog`; `TrainedDog` "is a" `Dog`
class TrainedDog(Dog):
    def sit(self):
        print("*sits down*")


jem = Dog(2)
print(jem.age)
# jem.sit()

juancho = TrainedDog(3)
# juancho.sit()
print(juancho.age)


class A:
    def f(self, x: int, y: int):
        print(x + y)


class B(A):
    pass


class C(B):
    pass


c = C()
# c.f(11, 1)  # 12


class A:
    def __init__(self, a: int):
        self.attr_of_a = a


class B(A):
    def __init__(self, b: int):
        self.attr_of_b = b


b = B(12)
print(b.attr_of_b)
print(b.attr_of_a)
