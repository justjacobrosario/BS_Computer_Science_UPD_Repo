---
field: programming
---
## 1. JSON (JavaScript Object Notation)
: Standardized way of encoding data as text on the web
: syntax of web data encoding

### JSON Datatypes

| **JSON Value **                                  | **Literal**                             |
| ------------------------------------------------ | --------------------------------------- |
| Null                                             | `null`                                  |
| Boolean                                          | `true, false` (lowercase in Javascript) |
| Number                                           | `1, 1.1, -1, -1.1`                      |
| String                                           | `"CS 12"`                               |
| Array                                            | `[null, true, 0, "hello`                |
| Object (dict of string-JSON val pairs {str:val}) | `{}, {"key":"value}`                    |

## 2.  Serialized Data
: raw light data (machine language)
: e.g. JSON, XML, binary

### Serialization
: converting complex data objs to byte/string format
### Deserialization
: converting byte/string data into complex data objs

## 3. API

### What are APIs
: Application Programming Interface (API)
: Defines or gives rules on how programs interact with another.

(e.g. ABCs and Protocols gives rules of what attributes and methods an object must have to interact with another object)

#### API Endpoint

: URL commonly consisting of JSON object (a hashmap)
: a JSON object is an API because it defines what a certain key will return (i.e. keys return a specific value)

: in Python, we use json, requests, httpx libraries to utilize API endpoints in python programs
## 4. json and requests Python Library

:  json and requests are preinstalled libraries
: lets python programs seriealize or deserialize JSON raw data into a python object/var

### 1) Parsing API response to JSON dict_string


### 1) Parsing JSON dict_string to Python dict

##### `import json`
#### `var_name = json.loads(json_obj_var)`

```python
import json

json_sample_obj = '''
{
"name": "Jacob",
"age": 19
}
'''

my_dict = json.loads(json_sample_obj)

print(my_dict) # { "name": "Jacob", "age": 19 }
print(my_dict[name]) # "Jacob"
```

### 2) Auto-Parsing JSON from API response to Python dict


##### `import requests`
#### `var_name = response.json()`

```python
import requests

response = requests.get('https://....com)
data = response.json()
print(data) # prints dict version of API data
```

### 3) Serializing Python dict to JSON str
##### `import json`
#### `var_name = json.dumps(python_dic)`

```python
import json

data = {"place":"UP Diliman"}
json_str = json.dumps(data)

print(json_str) # prints JSON str version of data

```

### 4) Notes in deserializing JSON to Python

1. JSON `null` becomes Python's `None`
2.  Raises `json.decoder.JSONDecodeError` if string is not valid JSON data for json.loads()
3. json.loads() and json.dumps() are inverses


## 5. httpx and asyncio libraries

### 1) httpx library
: third-party library including HTTP client for Python 3
: provides sync and async APIs (i.e. lets python program extract and use API endpoints)

`pip install httpx`

#### 1] `httpx.AsyncClient()`
: a multitasking browser inside the code that can get the data in the API Endpoint

#### 2] `_browser_client_name.get("_api_endpoint_url_str", params = {})`
: using the browser_client_name, it gets the specified parameters ( {} means all params) inside the api_endpoint
: this is where time is slow (needs to do smth for the program to not freeze bc of waiting)

### 2) asyncio library

: preinstalled library that lets python program run asynchronously
: * refer to [[L14_AsyncronousProgramming]] for more info about the term
: literally means asynchronous input/output process

#### 1] `async def _func_name(ev):`

: defines an event handler function to be asynchronous 
( i.e. whenever a line requests something and waits, the function doesnt freeze but instead proceeds to the next lines)

#### 2] `async with _file_address as _file_name:`

: opens a file and treats its block asynchronously

#### 3] `await`

: keyword that prompts the code on its right to be asynchronously run
(i.e. in await ..., the ... code tend to request something which takes time, so await prompts the program to see this as an asynchronous code to not freeze and proceed to the next line)


### 3) asynchronous event handler function using asyncio and httpx

: one can extract the JSON object in the api endpoint and use it in the python program like this

```python
import httpx
import asyncio

API_ENDPOINT = "https://some_website.com/"

async def get_data(ev):
	result = []
	
	async with httpx.AsyncClient() as my_client:
		data = await my_client.get(API_ENDPOINT, param={})
		result.append(data.json())

print(result) # [dict version of the json data]
	
```




