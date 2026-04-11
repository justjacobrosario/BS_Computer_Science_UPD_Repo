---
field: programming
---
\
## 1. Requesting
: Whenever a code requests a data from a server, be it online or offline, there is a delay (typically 2 secs in the internet) in getting the request.

## 2. Synchronous Programming
: Python typically runs the code line by line
: Before the next line runs, the current line must finish first
: Requesting data causes the program to freeze (i. e. users are unable to interact with other elements until a request is settled, which is not ideal in making websites)

Visual:
let 
🟦 = operation A
🟩 = operation B
🟨 = operation C

🟦🟦🟦 🟩🟩🟩 🟨🟨🟨
* one operation finishes first then another

```python
import time

def f(letter):
	for num in range(5):
		print(f"{num+1}{letter}")
			time.sleep(1)
f("A")
f("B")
# A1 A2 A3 A4 B1 B2 B3 B4
# f("B") waits for f("A") to finish first

```

### 1) Blocking Operations
: default python function calls are blocking operations as it blocks succeeding line of codes to run
: (i.e. it must be completed before next operation is executed. Python runs operations from top to bottom)

## 3. Asynchronous Programming
: Prevents freezing by proceeding to the next line of codes while the previous code requests for data at the same time.

Visual:
let 
🟦 = operation A
🟩 = operation B
🟨 = operation C

🟦🟩🟨🟦🟩🟨🟦🟩🟨
* one operation pauses and unpauses to interleave one another
### 2) Non-Blocking Operations
: python lines where whenever it waits for a request, the program still proceeds to the next lines

### 3) Coroutines
: Non-blocking operations that can pause its executions and unpause it
: like generators ( `yield` pauses it and `next` unpauses it )

```python
def letter():
	for letter in ['A', 'E', 'I', 'O', 'U']:
		print(letter)
		yield
		
def number():
	for number in [1, 2, 3, 4, 5]:
		print(number)
		yield

def color():
	for color in ['🔴]
```