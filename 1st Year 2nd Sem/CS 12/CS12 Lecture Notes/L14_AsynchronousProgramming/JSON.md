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
### 1. Parsing str/byte JSON Obj to Python dict

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

### 2. Parsing JSON from API response to Python dict


##### `import requests`
#### `var_name = response.json()`

```python
import requests

response = requests.get('https://....com)
data = response.json()
print(data) # prints dict version of API data
```

### 3. Serializing Python dict to JSON str
##### `import json`
#### `var_name = json.dumps(python_dic)`

```python
import json

data = {"place":"UP Diliman"}
json_str = json.dumps(data)

print(json_str) # prints JSON str version of data

```

### 4. Notes in deserializing JSON to Python

1. JSON `null` becomes Python's `None`
2.  Raises `json.decoder.JSONDecodeError` if string is not valid JSON data for json.loads()
3. json.loads() and json.dumps() are inverses


## 5. httpx libraries

: third-party library including HTTP client for Python 3
: provides sync and async APIs (i.e. lets python program extract and use API endpoints)

`pip install httpx`

