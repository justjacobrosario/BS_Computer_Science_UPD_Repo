import random
import traceback
import string
import time




# === CONFIG (customizable) ===

case_count = 10

# set the types of parameters in the function solution
param_types = ['int', 'int', 'int']

# set the conditions for each type
int_input_range = (-100, 100)
char_input_length = (0, 10)
bool_input = (False, True)
manual = ['Juan', 'juan', 'cRuz', 'delA']
manual1 = ["can", "do", "many"]
# you can add more manual input lists, just add another elid statement for it in def get_inputs()


# === INPUT PICKER (customizable) ===

def get_inputs(param_types):
    res = []
    for type in param_types:

        if type == 'int':
            res.append(random.randint(*int_input_range))
        elif type == 'char':
            res.append("".join(random.choice(string.ascii_lowercase) for _ in range(random.randint(*char_input_length))))
        elif type == 'bool':
            res.append(random.choice(bool_input))
        elif type == 'manual':
            res.append(random.choice(manual)) 
        # add addtnl elif statement for new manual input lists

    return res

def get_unique_inputs(finished_inputs, input_params):
    while input_params in finished_inputs:
        new_input_params = get_inputs(param_types)
        if new_input_params not in finished_inputs:
            return new_input_params


# === REFERENCE SOLUTION (customizable) ===

def ref_func(x, y, z):
    for _ in range(7000):
        f = x+y+z
    return f

# === SUBMITTED FUNC ===
def solution(a, b, c):
    for _ in range(7000):
        f = a+b+c
    return f

# === CHECKER ===

def checker(submitted_func):
    finished_inputs = []
    for case in range(case_count):
        input_params = get_inputs(param_types)

        if input_params in finished_inputs:
            input_params = get_unique_inputs(finished_inputs, input_params)

        finished_inputs.append(input_params)

        expected = ref_func(*input_params)
        start_time = time.perf_counter()
        actual = submitted_func(*input_params)
        end_time = time.perf_counter()

        elapsed_time = end_time - start_time

        if expected == actual:
            print(f'✅ CASE {case} ; Duration: {(elapsed_time*1000):.2f}ms ; Inputs: {input_params}')
        else:
            print(f'❌ CASE {case} ; Duration: {(elapsed_time*1000):.2f}ms ; Inputs: {input_params}')
            break

checker(solution)

