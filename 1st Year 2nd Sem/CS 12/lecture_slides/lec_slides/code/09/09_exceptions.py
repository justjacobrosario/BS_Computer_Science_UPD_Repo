class Original:
    def add(self, a: int, b: int) -> int:
        ...
        raise ArithmeticError()

class OverflowSubstitute(Original):
    def add(self, a: int, b: int) -> int:
        ...
        raise OverflowError()

class ExceptionSubstitute(Original):
    def add(self, a: int, b: int) -> int:
        ...
        raise Exception()

# OverflowSubstitute <: Original
# ExceptionSubstitute <: Original
 
def client(orig: Original):
    try:
        orig.add(150, 150)
    except ArithmeticError as e:
        print(f'Caught error {e}; good')
orig = Original()
overflow = OverflowSubstitute()
exception = ExceptionSubstitute()
 
client(orig)
client(overflow)
client(exception)