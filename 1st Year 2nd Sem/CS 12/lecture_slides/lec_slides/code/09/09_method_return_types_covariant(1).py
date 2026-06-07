# DcsStudent <: UpStudent
 
@dataclass
class UpStudent:
    first_name: str
    last_name: str
    student_number: str
 
@dataclass
class DcsStudent(UpStudent):
    cs31_grade: str

class A:
    def f(self) -> UpStudent
        return UpStudent(...)
 
class B(A):
    def f(self) -> DcsStudent:
        return DcsStudent(...)
 
class C(B):
    def f(self) -> UpStudent:
        return UpStudent(...)


def client1(a: A):
    print(a.f().student_number)
 
def client2(b: B):
    print(b.f().cs31_grade)
 
def client3(c: C):
    print(c.f().cs31_grade)
 
a = A()
b = B()
c = C()
 
client1(a)
client1(b)
client1(c)
client2(b)
client2(c)
client3(c)