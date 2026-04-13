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
: converting complex data objs to raw byte/string format
### Deserialization
: converting raw byte/string data into complex data objs

## 3. JSON-based Python Libraries
### 1) `import json`
### 2) `import httpx`


## 4. Serialization & Deserialization in Python
: To extract data from web APIs to our local program


### 1) .json() : API JSON response to Python dict
##### `import httpx`
#### `_dic = _api_response.json()`

e.g.
```python
_api_response = httpx.get(API_ENDPOINT_URL)
_dic = _api_response.json()

print(_dic) # prints the pyhton dic version of _api_response
```

### 2) json.loads() : JSON str to Python dict
##### `import json`
#### `_dic = json.loads(_json_dict_str)
`
e.g.
```python
_json_str = '''
{
"keychuchu":"valuechuchu"; ...
}'''
_dic = json.loads(_json_dict_str)

print(_dic) # prints the pyhton dic version of _api_response
```

### 3) json.dumps() : Serializing Python dict to JSON str

 ##### `import json`
#### `_json_dict_str = json.dumps(_dic)`

i..e. basically inverse of json.loads
### 3) JSON SERIALIZATION NOTES
#### 1] JSON `null` becomes Python `None`
#### 2] raises `json.decorder.JSONDecodeError` if supposed json dict str is not valid 


