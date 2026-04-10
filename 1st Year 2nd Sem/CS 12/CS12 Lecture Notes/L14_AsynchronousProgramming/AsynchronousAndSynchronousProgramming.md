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

```python

def f(letter):
	for num in range(5):
		print(f"{num+1}{letter}")
f("A")
f("B")
# A1 A2 A3 A4 B1 B2 B3 B4
# f("B") waits for f("A") to finish first

```

## 3. Asynchronous Programming
: 