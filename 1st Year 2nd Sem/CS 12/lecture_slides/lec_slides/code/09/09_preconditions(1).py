class MathUtils:
    def sqrt(self, n: float) -> float:
        """Returns the square root of the given float.
 
        `n` must be nonnegative.
        """
        ...


class MoreEfficientMathUtils(MathUtils):
    def sqrt(self, n: float) -> float:
        """Returns the square root of the given float.
 
        `n` must be a positive whole number.
        """
        ...


# MoreEfficientMathUtils <: MathUtils
 
def client(utils: MathUtils):
    x = utils.sqrt(1.5)
    ...
 
 
orig = MathUtils()
faster = MoreEfficientMathUtils()
 
client(orig)
client(faster)