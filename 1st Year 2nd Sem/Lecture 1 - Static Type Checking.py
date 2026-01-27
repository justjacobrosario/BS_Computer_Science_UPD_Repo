# ginawa to sa ipaddd

""" ■■■■■■■ TYPE HINTING ■■■■■■■ """
    # declares the type of variables and return values

    # Syntaxx

    # ◩◩◩ 1. VARIABLES ◩◩◩
        # A. Std. Type Hints
            # <variable> : <variable_type> = <variable value>
            # e.g.
            Juan : str = 'Tamad'

        # B. Type Alias
            # <variable> = <variable_type
            # e.g.
            Juan = str
            Juan = 'Tamad'

    # ◩◩◩ 2. FUNCTINONS (Params and Return Vals) ◩◩◩
        # - <func(parameter : type)> -> return_type:
        # e.g.
        def msg_to_value(msg: str) -> int:
            return int(msg)

    # ◩◩◩ 3. MULTIPLE TYPES USING UNION (|) ◩◩◩

        # ▤▤▤ Same param type, Diff return type ▤▤▤

        # same param types can ead to diff return types
        # e.g.
        def squared(n:int) -> (int | None):
            if n != 0:
                return n ** 2

        # ▤▤▤ Diff param type, Diff return type

        # diff param types can have corresponding diff return types
        #e.g.
        def func(nums: list[int] | None) -> int | None: # if list[int] then int, if None then None
            if nums is None:
                return None
            else:
                return sum(nums)

    # ◩◩◩ 4. USING LITERAL DATA TYPE ◩◩◩

        # Literal() stores values as constants not variables
        # e.g.
        from typing import Literal, get_args
        fixed_vals = Literal('pi', 'theta') # fixed_vals is a new data type

        def is_constant(x : fixed_vals) -> float:
            if x == 'pi':
                return 3.14159
            else:
                return 60.0

        # getargs() gets the args in a literal data type
        # e.g.
        print(get_args(fixed_vals)) # ('pi', 'theta')






""" ■■■■■■■ TYPE CHECKING ■■■■■■■ """
    # process if type hints are followed

    # 1. Static Type Checking : Before execution ; Not default
        # Via declaring type hints before running the code
        # Automated flagging via Pyright (Github) or Pylance (VS Code)

        # NOTE❗: All parameters and variables must be annotated 
                    # Optional for return value types in funcs




    # 2. Dynamic Type Checking : During execution ; done by default
