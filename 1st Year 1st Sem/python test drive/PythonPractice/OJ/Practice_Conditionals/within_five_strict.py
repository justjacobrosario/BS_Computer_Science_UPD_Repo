def will_get_boomed(x1, y1, x2, y2):
    return (abs(x1 - x2) + abs(y1 - y2)) <= 4
# x = column, y = row
print(will_get_boomed(5, 5, 1, 1))

"""
Problem Statement
There is a bomb at cell (x1,y1)
! You are currently at cell (x2,y2)
, and you want to know whether or not you will get caught up in the blast.

By the way, the bomb's area of effect looks like this:

....X....
...XXX...
..XXXXX..
.XXXXXXX.
XXXXBXXXX
.XXXXXXX.
..XXXXX..
...XXX...
....X....
Here, B indicates where the bomb is, and any cell that isn't a . will get caught up in the blast.

Task Details
Your task is to implement a function named will_get_boomed, which should look like this:


def will_get_boomed(x1, y1, x2, y2):
    return ...
Here, you only need to replace the ... part with a Python expression.

The function must return a bool denoting the answer.

Your source code must have at most 100
 bytes.

Examples
Example 1 Function Call

will_get_boomed(11, 11, 11, 11)
Example 1 Return Value

True
Example 2 Function Call

will_get_boomed(11, 11, 33, 33)
Example 2 Return Value

False
Constraints
The function will_get_boomed will be called at most 104
 times.
−1050≤x1,y1,x2,y2≤1050
"""