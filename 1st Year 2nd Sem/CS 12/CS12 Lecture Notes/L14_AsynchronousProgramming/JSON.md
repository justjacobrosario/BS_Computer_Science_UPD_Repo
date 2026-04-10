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

## 3. JSON Python Library

### 1. JSON Object in '''...'''

```python
import json

json_sample_obj = '''
{
"name": "Jacob",
"age": 19
}
'''

```

### 2. Parsing str/byte JSON Obj to Python dict

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

### 3. Parsing JSON from API response to Python dict

##### `import requests`
#### `var_name = response.json()`

```python
import requests

response = requests.get('https://....com)
data = response.json()
print(data) # prints dict version of API data
```