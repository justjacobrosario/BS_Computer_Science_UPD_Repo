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
    def f(self, student: UpStudent):
        print(student.student_number)
 
class B(A):
    def f(self, dcs_student: DcsStudent):
        print(dcs_student.cs31_grade)
 
class C(B):
    def f(self, student: UpStudent):
        print(student.student_number)


def client1(a: A):
    student = DcsStudent(...)
    a.f(student)
 
def client2(b: B):
    student = UpStudent(...)
    b.f(student)
 
def client3(c: C):
    student = DcsStudent(...)
    c.f(student)
 
a = A()
b = B()
c = C()
 
client1(a)
client1(b)
client1(c)
client2(b)
client2(c)
client3(c)