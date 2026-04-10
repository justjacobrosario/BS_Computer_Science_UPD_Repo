---
year: 1
subject: CS12
field: programming
---


1:  ==Hypertext Markup Language (HTML)==
===================================

![[HTML]]
  

==2: Pyscript and DOM Manipulation==
================================

  

## 1. Pyscript usage
![[Pyscript]]

	: let there be index.html and main.py,
	to connect main.py to index.html:


```html

<html>
<head>

    <link rel="stylesheet" href="https://pyscript.net/releases/2026.3.1/core.css">

    <script type="module" src="https://pyscript.net/releases/2026.3.1/core.js"></script>

<!-- above are to import pyscript. -->
<!--NOTE: link tag is self-closed while script tag is open-close pair -->

<head/>

<body>
    <div id="wrapper"></div>
    <!-- this just wraps/contains all of the things-->

    ...

    <script type="py" src="./main.py"></script>
<!-- above are to import the .py file-->
<!-- NOTE: place this script tag as the last tag of <body>-->

</body>

</html>

```


## 2. What is Document Object Model (DOM)

	: DOM basically translates tags in html into variables in python, and vice versa
	: objects in webpages are interpreted as variables in python

  

## 3. DOM Properties

	 * read means just get existing value (e.g. btn.checked # returns True or False)
	 * write means modify the value (e.g. btn.checked = True # makes it True)

  
#### 1) `elmt.innerText`

	 -> str
	: read/write visible text of the tag elmt

  

#### 2) `elmt.value`

	 -> str
	: read/write val of the tag elmt

  

#### 3) `elmt.checked`

	 -> bool
	: read/write if tag elmt is checked

  

#### 4) `elmt.disabled`

	 -> bool
	: read/write the tag elmt as greyed out (non-interactive)

  

#### 5) `elmt.hidden`

	 -> bool
	: read/write the tag elmt as invisible (dont take up space)

  

#### 6) `elmt.style`

	 -> str
	: write the tag elmt's inline css properties

  
  

## 4. DOM Templating

  
: pyscript methods are camelCased instead of snake_cased
: this is the usual python template for using DOM


```python

from pyscript import document, web


''' PART A: REFERENCE THE WRAPPER TAG
        : this is where all things will be contained'''

# document.getElementById("id_name")
root = document.getElementById("wrapper")

  
''' PART B: DEFINE EVENT FUNCTIONS
        : an event are where we add,remove,modify html tags'''

# make ev a parameter, it refers to the caller tag
# (e.g. if a button called this func, it is referred in ev.target)

def add_smiley_to_btn(ev):

    ev.target.innerText = "😃"

    ''' Other element modifiers (element.attr_name = "..."):

        element.innerText = "..." : set text inside the tag

        element.style = "..." : set inline css of the tag

        element.id = "..." : set id of the tag

        element.type = "..." : set type fo the tag

        element.src = "url" : set src attr of the tag

        element.alt = "..." : set refers to the alt text attr of the tag

        *most tag attr can be a method (as long as that tag has that attr)
    '''


''' PART C: CREATING INITIAL TAGS

        : each new tag must be created via tag_name = document.createElement("tag")'''

# tags can also be modified using the element modifiers
btn = document.createElement("button")

btn.innerText = "click me!"

# tags can link an event function via the method .addEventListener("input_type", web.create_proxy(event_func_name)
# the input type can be "click", "mouseover", "input" (value changes per keystroke), "keydown", "keyup"

btn.addEventListener("click", web.create_proxy(add_smiley_to_btn))

  
  

''' PART D: append created tags to the existing wrapper tag

        : to add the tags inside the wrapper tag in the html, use .appendChild("tag_name")'''

root.appendChild(btn)

  

''' OTHER USEFUL DOM METHODS'''

# 1. parent_name.removeChild(tag_name)
# 2. tag_name.remove()
# 3. parent_name.children : var of collections of children

```