---
field: programming
---
\
: Pyscript basically lets python programming language be used in webassembly
: Lets python programs be done in webpages

	: let there be index.html and main.py,
	to connect main.py to index.html:


```html

<html>
<head>

    <link rel="stylesheet" href="https://pyscript.net/releases/2026.3.1/core.css">

    <script type="module" src="https://pyscript.net/releases/2026.3.1/core.js"></script>
    
    <py-config>packages=["library_name"]</py-config>

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

## Display webpage in local server
: suppose the html and python files are settled

in terminal
```bash
cd "to the folder of the html and py files"
python -m http.server 8000
```

in browser
type `http://localhost:8000`