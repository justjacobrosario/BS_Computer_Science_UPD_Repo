: before learning how to write in CSS, lets first know how to link CSS to HTML

## 1. Linking CSS to HTML
: there are three ways

##### A. External CSS
: this is where the CSS contents are located on a separate css file

: use `<link>` tag in the `<head>` section to link the css file through its href

:Suppose in the same directory of index.html, you made style.css
```html
<head>
	<link rel="stylesheet" href="style.css">
</head>
```
- `rel` attribute specifies the relationship of the file to the html file (since the file is a css file, it is a stylesheet)
- `href` attribute, like `<a>` tags, contain the location of the file

**Benefits**
-  HTML and CSS information are neatly separated
##### B. Internal CSS

: aka embedded CSS

: the CSS contents is within the HTML file, particularly inside the `<head>` section.

: use `<style>` tag to contain the CSS contents

e.g.
```html
<!DOCTYPE html>
<html>
<head>
	<style>
	CSS contents here ...
	<style>
</head>

<body>
</body>
</html>
```


##### C. Inline CSS

: every CSS content is contained as attributes per line of elements
: i.e. every style is declared as an attribute for each line of elements (unlike external or internal CSS which are grouped together in one place)


## 2. CSS Basic Syntax

: CSS is comprised of several rules. A rule containes: **selector, property-value declarations**

e.g.
```css
div {
	font-weight: 700;
	color: darkblue;
}
```
- **selector** : the element/s being modified (can be a tag, id, class, etc)
- **property** : a certain attribute of the selector
- **value** : a certain value assigned to a specific property

: selectors can be modified simultaneously

e.g.
```css
div, p, h1 {
	font-weight: 700;
	color: darkblue;
}
```
: here both `div`, `p`, and `h1` selectors are being modified

## 2.1 Common selectors

: selectors may represent every element (**universal**), a certain tag (**type**), a unique element (**id**), or a group of elements (**class**)
##### A. universal selector `*`

: basically represents all elements 

e.g.
```css
* {
	color : green;
}
```
: every element (that has a color attribute) will all turn to green

##### B. type selector

: represents a certain tag

e.g.
```css
p {
	color : blue;
}
```
: all `<p>` tag elements is modified here

- **`<div>` tag**

: like `<p>` and heading tags, `<div>` tag is an element that contains text contents (thus has closing tags)

: aside from that, it has more modifiable attributes than the other tags that will make elements more flexible to edit

: as we go to CSS, `<div>` tag may replace other text tags for consistency

##### C. id selector

: represents a certain element with the mentioned id (uses `#id_name`)

: used for modifying a single unique element

: suppose we have these html and css files
```html
<p id = "age"> I am 19 years old.</p>
```

```css
#age {
	font-weight : 800;
}
```
: by giving an id, a single unique element can be modified in CSS

*Note: do not start the id name with a number*
##### D. class selector

: represents a group of elements to be modified (uses `.class_name`)

: used for modifying a group of elements (not necessarily same tags)

: suppose we have these html and css files
```html
<p class = "animal">Kangaroo</p>
<p>Orange</p>
<p class = "animal">Orangutan</p>
```

```css
.animal { 
	color : tomato;
}
```
: since only the 1st and 3rd element has the `animal` class, they will also only be the elements modified in the CSS snippet

*Note: do not start the class name with a number*

