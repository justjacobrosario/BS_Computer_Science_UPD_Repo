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
🟦 runs
🟦
🟦 finishes
🟩 runs
🟩
🟩 finishes
🟨 runs
🟨
🟨 finishes


## 2. Asynchronous Programming
: operations can pause, give the runtime to the next operation, and then unpause after awaiting a certain line of code
: operations can pause and unpause instead of waiting each line to finish before running the next

### 1) Non-Blocking Operations (Coroutines in Python)
: Operations that can pause (like yield in generators), and then unpause and continue (like next() in generators)

: instead of yield and next(), we use `await` keyword to pause the coroutine, then unpause once the line after it is finished running/loading/compiling

e.g. # Note, learn this in ![[httpxModuleForAsynchronousProgramming]]
```python
import asyncio

async def letter():
    for letter in ['A', 'E', 'I', 'O', 'U']:
        print(letter)
        await asyncio.sleep(0) # literally like yield then next() after 0 secs
        
async def number():
    for number in [1, 2, 3, 4, 5]:
        print(number)
        await asyncio.sleep(0)

async def color():
    for color in ['🔴', '🟠', '🟡','🟢','🔵']:
        print(color)
        await asyncio.sleep(0)

async def main():
    await asyncio.gather(*[letter(), number(), color()])
    print('Done')

asyncio.run(main())
    
'''
that prints:
A
1
🔴
E
2
🟠
I
3
🟡
O
4
🟢
U
5
🔵
Done
'''
```


### 2) Asynchronous Programming Runtime
🟦 runs and pauses, 
🟩 runs and pauses, 
🟨 runs and pauses, 
🟦 await line finishes and unpauses, 
🟩 await line finishes and unpauses, 
🟨 await line finishes and unpauses, 
