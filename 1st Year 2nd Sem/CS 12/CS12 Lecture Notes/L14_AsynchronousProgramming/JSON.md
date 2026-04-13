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

### 1) Deserializing JSON dict str to Python dict
##### `import json`
#### `_dic = json.loads(_json_dict_str)`

### 2) Serializing Python dict to JSON dict str

 ##### `import json`
#### `_json_dict_str = json.dumps(_dic)`

### 3)  


