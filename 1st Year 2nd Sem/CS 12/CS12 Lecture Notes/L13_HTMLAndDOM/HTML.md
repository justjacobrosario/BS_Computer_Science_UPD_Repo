---
field: programming
---

## 1. Intro to HTML

: structure of web pages
: HTML elements can be:
	1. Open-Close Tag Pair (e.g. `<div><div/>`)
	2. Self-Closing Tag (e.g. `<hr/>`)

## 2. Block elements
  
: takes up all width, and starts a new line (next element is below it)
: e.g. div, p, h1...h6, table

## 3. Inline elements

: takes up only needed width, doesnt start new line (next element is on its right until no more space)
: e.g. span, a, input, img

## 4. HTML Universal Attributes

: attr that all tags possess

  
### 1. <tag_type id="...">

	: id is a unique identifier to call/identify a specific tag
	: id is unique (only one tag can possess a certain id name)

  
### 2. <tag_type class="...">

	: class is another identifier where multiple tags can possess

### 3. `<tag_type style="property1:val; property2:val; ...>`

	: inline css setup of a tag
	: consists of property:value pair, such that every pair is separated by ; .
	(e.g. `<p style="color:red; font-family:monospace;">`)

### 4. `<tag_type hidden>`

	: basically hides the tag on the page

### 5. `<tag_type title="...">`

	: title is the text that pops when a tag is hovered

  
## 5. HTML Input Elements

  
### 1. `<input type="text">`

	: method/s
	- elmt.value -> str

### 2. `<input type="number">`

	: methods/s
	- elmt.value -> int

### 3. `<input type="checkbox">`

	: method/s
	- elmt.checked -> bool

### 4. `<input type="range">`

	: method/s
	- elmt.value -> float

### 5. `<input type="button">`

	: method/s
	.addEventListener("click", web.create_proxy(event_func_name))
	: when the button is clicked, the event func will be called
