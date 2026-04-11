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
## 4. Parsing Online API response into usable Python object (via json and requests libraries)

:  json and requests are preinstalled libraries
: lets python programs seriealize or deserialize JSON raw data into a python object/var

### Another important library: httpx library
: third-party library including HTTP client for Python 3
: provides sync and async APIs (i.e. lets python program extract and use API endpoints)

`pip install httpx`

### 1) [.text property] Parsing API response to JSON dict_string

in html
`<py-config>packages=["httpx"]</py-config>`
in python
##### `import httpx`
#### `_dic = _json_response.text`

```python
import httpx

API_ENDPOINT = "https://somewebsite.com/"

_json_reponse = httpx.get(API_ENDPOINT)
_dic = _json_reponse.text

print(_dic) # dict str format of the data
```

### 2) [json.loads() method] Parsing JSON dict_string to Python dict

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

### 3) [.json() method] Auto-Parsing JSON from API response to Python dict

##### `import requests`
#### `var_name = response.json()`

```python
import requests

response = requests.get('https://....com)
data = response.json()
print(data) # prints dict version of API data
```

: NOTE: Actually, we can pase JSON API response to Python dict by
1. JSON API Response -> JSON str_dict using `.text`property
2.  JSON str_dict -> Python dict using `json.loads()` method

### 4) [json.dumps()] Serializing Python dict to JSON str
##### `import json`
#### `var_name = json.dumps(python_dic)`

```python
import json

data = {"place":"UP Diliman"}
json_str = json.dumps(data)

print(json_str) # prints JSON str version of data

```

### 5) Notes in deserializing JSON to Python

1. JSON `null` becomes Python's `None`
2.  Raises `json.decoder.JSONDecodeError` if string is not valid JSON data for json.loads()
3. json.loads() and json.dumps() are inverses

## 5. Other libraries 
## 5. Deserialization by Synchronous Programming 

: we can deserialize an API response to a Python object by  using the libraries:

| **Libraries** | **Method/s**    | **Propert/ies** |
| ------------- | --------------- | --------------- |
| httpx         | .get(), .json() | .text           |
| json          | .loads()        |                 |

### 1) setting the variable of the API
##### `API_ENDPOINT = "https://API_url/`

### 2) extracting API response
##### `api_response = httpx.get(API_ENDPOINT`)
### 3) parsing api_response into a Python dict
##### `data_dict = api_response.json()`
or
##### `json_str_dict = api_response.text`
##### `data_dict = json.loads(json_str_dict)`
## 6. Deserialization by Asynchronous Programming (via httpx and asyncio libraries)

### Another important library: asyncio library

: preinstalled library that lets python program run asynchronously
: * refer to [[L14_AsyncronousProgramming]] for more info about the term
: literally means asynchronous input/output process

### 1) define event handler func as asynchronous
##### `async def _func_name(ev):`

: defines an event handler function to be asynchronous 
( i.e. whenever a line requests something and waits, the function doesnt freeze but instead proceeds to the next lines)

### 2) open a local browser to get the API response as asynchronous

##### `async with httpx.AyncClient as _client:`

: opens an Async client and treats its block asynchronously
: Async client is a multitasking browser inside the code that can get the data in the API Endpoint

### 3) await getting the API response in API endpoint

##### `_data = await client.get(API_ENDPOINT, param={})`
: NOTE: do this in the async with block
: the await keyword prompts that the async client getting the response may take long, so the program will treat it asynchronously
: param filters data (e.g. if param = {"sex":"male"}, it only get dict elements where the sex is male)
: setting param={} just get all elements without conditions

### 4) deserialize API response into Python dict
##### `data_dict = api_response.json()`

| **Libraries** | **Method/s**                    | **Propert/ies** | Keyword/s    |
| ------------- | ------------------------------- | --------------- | ------------ |
| httpx         | .AsyncClient(), .get(), .json() |                 |              |
| asyncio       |                                 |                 | async, await |

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




