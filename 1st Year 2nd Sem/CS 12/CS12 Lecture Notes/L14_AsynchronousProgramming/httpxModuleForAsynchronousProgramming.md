---
field: programming
---
## 1. httpx module `import httpx`

: a third-party module that quickly interprets json files and apis  
: can be used for synchronous and asynchronous programming (see [SynchronousAndAsynchronousProgramming](app://obsidian.md/SynchronousAndAsynchronousProgramming))
: also uses builtin asyncio module `import asyncio` to do asynchronous programming

## 2. Basic Offline Asynchronous Programming Setup

### 1) defining Coroutines
: use `async keyword` to label that this function is a coroutine (Functions that can pause and unpause)

e.g.
```python
async def letter():
```

### 2) plotting function body
: yes

e.g.
```python
async def letter():
    for letter in ['A', 'E', 'I', 'O', 'U']:
        print(letter)
```
### 3) plotting the await line
: use `await` before the line of code where the coroutine must be paused, and then unpaused once that line of code is finished operating/loading AND the other current operation is finished

: if you just want to give a time delay between pausing and unpausing, use `asyncio.sleep(num_of_sec_before_unpausing)`
: just set `asyncio.sleep(0)` for just pausing it then unpausing after the other current operation

e.g.
```python
async def letter():
    for letter in ['A', 'E', 'I', 'O', 'U']:
        print(letter)
        await asyncio.sleep(0) # literally like yield in generators
```

### 4) plotting other function body lines (if there are any)
: yes, you still can operate more lines after unpausing from the `await` line
: Note: these lines might be operated earlier or later depending on the other operation from other function calls before it

e.g.
```python
async def letter():
    for letter in ['A', 'E', 'I', 'O', 'U']:
        print(letter)
        await asyncio.sleep(0) # literally like yield in generators
        ...
```

### 5) Gathering and calling Coroutines in order
: After defining all coroutines, they can be gathered in a main coroutine
: inside this, the coroutines is gathered using `asyncio.gather()` like this

```python
async def main():
    await asyncio.gather(*[letter(), number(), color()])
    print('Done')
    
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


## 3. Online API-based Asynchronous Programming

### Declaring the API endpoint as a var (shortcut)
: instead of manually copy pasting the API endpoint for every coroutine, just make a variable for it

e.g.
```python
POKE_API_ENDPOINT = "https://pokeapi.co/api/v2/pokemon" # incomplete, must be https://pokeapi.co/api/v2/pokemon/{id or name}
```
### 1) defining Coroutines
: same thing like this

e.g. 
```python
async def fetch_pokemon(ev): # ev means its an eventhandler coroutine
```

### 2) plotting initial coroutine body (before getting the API response)
: simply define the coroutine body that runs before getting the API response

e.g.
```python
async def fetch_rand_poke(ev):
    rand_id = random.randint(1, 1000)
    params = {} # no conditions for the API to filter
```

### 2) getting the API response into the python code
: use an `async with` block (i.e. you're gonna open a file online asynchronously)
: after the `async` keyword, its line of code must open the API in an async client browser like this

e.g.
```python
async def fetch_rand_poke(ev):
    rand_id = random.randint(1, 1000)
    params = {} # no conditions for the API to filter


    async with httpx.AsyncClient() as client:
        res = await client.get(f"{POKE_API_ENDPOINT}/{rand_id}", params=params)
```

### 3) plotting other function body lines (if there are any)
: yes, you still can operate more lines after unpausing from the `await` line
: Note: these lines might be operated earlier or later depending on the other operation from other function calls before it

```python
async def fetch_rand_poke(ev):
    rand_id = random.randint(1, 1000)
    params = {} # no conditions for the API to filter


    async with httpx.AsyncClient() as client:
        res = await client.get(f"{POKE_API_ENDPOINT}/{rand_id}", params=params)
    res_dict = res.json()
    poke_name = res_dict["name"]
    poke_container.innerText = poke_name
    
```

: overall, whenever this event handler coroutine is called, it randomly gets a pokemon datus, then di