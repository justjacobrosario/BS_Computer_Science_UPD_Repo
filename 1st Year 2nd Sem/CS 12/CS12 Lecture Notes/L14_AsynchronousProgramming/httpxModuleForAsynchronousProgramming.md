---
field: programming
---
## 1. httpx module `import httpx`

: a third-party module that quickly interprets json files and apis  
: can be used for synchronous and asynchronous programming (see [SynchronousAndAsynchronousProgramming](app://obsidian.md/SynchronousAndAsynchronousProgramming))
: also uses builtin asyncio module `import asyncio` to do asynchronous programming

## 2. Asynchronous Programming Setup

### 1) defining Coroutines
: use `async keyword` to label that this function is a coroutine (Functions that can pause and unpause)

e.g.
```python
async def letter():
```

### 2) 