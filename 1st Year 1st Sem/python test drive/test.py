import importlib
import random
import traceback

# ------------------------------
# CONFIG
# ------------------------------
STUDENT_MODULE = "student"
FUNCTION_NAME = "solve"
NUM_TESTS = 50
INPUT_RANGE = (-100, 100)

# ------------------------------
# REFERENCE SOLUTION (ANSWER)
# ------------------------------
def reference_solution(x):
    return x * x

# ------------------------------
# TEST CASE GENERATOR
# ------------------------------
def generate_test_case():
    return random.randint(*INPUT_RANGE)

# ------------------------------
# JUDGE
# ------------------------------
def judge():
    try:
        student = importlib.import_module(STUDENT_MODULE)
        student_func = getattr(student, FUNCTION_NAME)
    except Exception:
        print("❌ IMPORT ERROR")
        traceback.print_exc()
        return

    for i in range(1, NUM_TESTS + 1):
        test_input = generate_test_case()

        try:
            expected = reference_solution(test_input)
            result = student_func(test_input)

            if result != expected:
                print(f"❌ FAIL on test {i}")
                print(f"Input: {test_input}")
                print(f"Expected: {expected}")
                print(f"Got: {result}")
                return

        except Exception:
            print(f"❌ RUNTIME ERROR on test {i}")
            traceback.print_exc()
            return

    print("✅ ALL TESTS PASSED")

# ------------------------------
# RUN
# ------------------------------
if __name__ == "__main__":
    judge()
