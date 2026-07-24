import random
import traceback
import string
import time
import tracemalloc



# === CONFIG (customizable) ===

case_count = 50

# set the types of parameters in the function solution
param_types = ['int', 'int', 'int']

# set the conditions for each type
int_input_range = (-10000, 10000)
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

# === CHECKER ===

def checker(submitted_func):
    success = True
    finished_inputs = []
    for case in range(case_count):
        input_params = get_inputs(param_types)

        if input_params in finished_inputs:
            input_params = get_unique_inputs(finished_inputs, input_params)

        finished_inputs.append(input_params)

        expected = ref_func(*input_params)

        start_time = time.perf_counter()
        tracemalloc.start()
        start_mem = tracemalloc.get_traced_memory()[1]

        actual = submitted_func(*input_params)

        end_mem = tracemalloc.get_traced_memory()[1]
        tracemalloc.stop()
        end_time = time.perf_counter()

        elapsed_time = end_time - start_time
        mem_used_kb = (end_mem - start_mem) / 1024

        if expected == actual:
            print(f'✅ CASE {case} ; Duration: {(elapsed_time*1000):.2f}ms ; Memory: {mem_used_kb:.2f}KB ; Inputs: {input_params}')
        else:
            print(f'❌ CASE {case} ; Duration: {(elapsed_time*1000):.2f}ms ; Memory: {mem_used_kb:.2f}KB ; Inputs: {input_params}')
            success = False
            break

    if success == True:
        print("✨Problem Solved Correctly✨")
    else:
        print("Try Again")

#checker(solution)

