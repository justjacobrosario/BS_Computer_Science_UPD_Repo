---
field: programming
---
## 1. Synchronous Programming
: basically what we have been doing in vanilla Python programs
: each line must finish their operation/s first 

### 1) Blocking Operations
: Operations that synchronously runs (i.e. they finish their operations then pass the runtime to the next line)

e.g.
```python
def letter():
    for letter in ['A', 'E', 'I', 'O', 'U']:
        print(letter)
        
def number():
    for number in [1, 2, 3, 4, 5]:
        print(number)


def color():
    for color in ['🔴', '🟠', '🟡','🟢','🔵']:
        print(color)

def main():
    letter()
    number()
    color()
    print("Done")

main()
'''
prints:
A
E
I
O
U
1
2
3
4
5
🔴
🟠
🟡
🟢
🔵
Done
'''
```

### 2) Synchronous Programming Runtime
: 1st function call, if 1st done then 2nd function call, ...
🟦🟦🟦🟩🟩🟩🟨🟨🟨


## 1. Asynchronous Programming
: operations can pause, give the runtime to the next operation, and then unpause after awaiting a certain line of code
: operations can pause and unpause instead of waiting each line to finish before running the next

### 1) Non-Blocking Operations (Coroutines)
: Operations that synchronously runs (i.e. they finish their operations then pass the runtime to the next line)

e.g.
```python
def letter():
    for letter in ['A', 'E', 'I', 'O', 'U']:
        print(letter)
        
def number():
    for number in [1, 2, 3, 4, 5]:
        print(number)


def color():
    for color in ['🔴', '🟠', '🟡','🟢','🔵']:
        print(color)

def main():
    letter()
    number()
    color()
    print("Done")

main()
'''
prints:
A
E
I
O
U
1
2
3
4
5
🔴
🟠
🟡
🟢
🔵
Done
'''
```

### 2) Synchronous Programming Runtime
: 1st function call, if 1st done then 2nd function call, ...
🟦🟦🟦🟩🟩🟩🟨🟨🟨