: before learning how to write in CSS, lets first know how to link CSS to HTML

## **1. Linking CSS to HTML**
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

```html
<div style = "color: red; font-size: 12px;">Hello</div>
```


## **2. CSS Basic Syntax**

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

### 2.1 Common selectors

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
<div id = "age"> I am 19 years old.</div>
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
<div class = "animal">Kangaroo</div>
<div>Orange</div>
<div class = "animal">Orangutan</div>
```

```css
.animal { 
	color : tomato;
}
```
: since only the 1st and 3rd element has the `animal` class, they will also only be the elements modified in the CSS snippet

*Note: do not start the class name with a number*

##### E. Grouping selector

: selectors can be modified simultaneously

e.g.
```css
div, p, h1 {
	font-weight: 700;
	color: darkblue;
}
```
: here both `div`, `p`, and `h1` selectors are being modified

##### F. Chaining selector

: an element can have multiple class, (and a single id)

**F.1. multiple classes**

e.g. suppose we have classes `sex`, and then `age`
```html
<div class = "male kid">John</div>
<div class = "male adult">Juan</div>
<div class = "female kid">Mary</div>
<div class = "female adult">Maria</div>
```

```css

.female {
	font-weight : 800;
}

.female.kid {
	color : pink;
}
```

: we can see that elements have multiple classes separated by a `space`. We chain classes to specify by simply linking the class name with `.`

**F.2. class and id**

: suppose we have class `nationality`, and id `name`
```html
<div class = "Filipino" id = "Juan">Magandang Umaga!</div>
<div class = "Filipino" id = "Bien">Mayag na aga!</div>
```

```css
.Filipino#Juan {
	color : blue;
}
```

##### G. Descendant selector

: we can select elements according to their parent's class/id and their own class/id

: suppose we have class `course` and id `year`

```html
<div class = "computer_science">
	<div id = "first">CS11</div>
</div>

<div class = "mathematics">
	<div class id = "first">MATH23</div>
</div>
```

```css
.computer_science #first {
	color : blue;
}
```

: we can see here that only the div with `#first` AND inside the  `.computer_science` is being modified


### 2.2. Common Properties

: these will be the properties commonly used in modifying  texts, links, and images

##### A. Color
: there are multiple possible values of color

```css
div {
	/* hexadecimal */
	color: #00000;
}

div {
	/* word */
	color: white;
}

div {
	/* rgb */
	color: rgb(255, 255, 255);
}

div {
	/* hsl */
	color: hsl(0, 0%, 100);
}

/* aside from color, background-color cna also be used*/
div {
	color: ___ ;
	background-color: ___;
}
```


##### B. Typography Properties

```css

div {
	font-family : "Times New Roman", "Helvetica", "sans-serif";
	/* you can list consecutive fonts for css to fallback in case one is unavailable */
	
	font-size : 22px; 
	/* NO SPACE IN 22 AND px */
	
	font-weight : 800; 
	/* 1-1000 or simply bold*/
	
	text-align : center; 
	/* left/right/justify */
}

```

##### C. Image Properties

```css
img {
	height : auto;
	width : 1000px;
}
```

## **3. CSS Cascade**

: cascade determines which rules to apply

: suppose **a > b**, that means property a will be applied rather than b
: **Cascade Priority list:**

> **inheritance > id > specificity > class > type > order**

NOTE: only similar conflicting properties will be affected by this. Properties without conflicts will be done.
##### A. Inheritance

: the property of the child is chosen than the property of the parent ( even if the parent has an id )

```html
<div id = "parent">
	<div class = "child1">Hello</div>
</div>
```

```css
.child1 {
	color: red;
}

#parent {
	color: blue;
}
```

: the parent forces blue, the child forces red. Thus the color will be red.

##### B. id beats all class


```html
<div class = "parent">

	<div id = "itemid" class = "child">Hello</div>

</div>
```

```css
#itemid {
	color: green;
}

.child {
	color: red;
}

.parent .child {
	color: blue;
}
```

: the id selector is greater than the class selector and the descendant selector (of all classes). Thus the color will be green.

: the id selector will only be ignored if there is a more specific (a descendant or chain selector) that ALSO has an id

```html
<div id = "parent">

	<div id = "itemid" class = "child">Hello</div>

</div>
```

```css
#itemid {
	color: green;
}

#parent .child {
	color: blue;
}
```

: since the `#parent .child` is more specific and also has an id selector, it will be focused than the id selector of the child. Thus its color is blue

##### C. Specificity over classes


```html
<div class = "parent">

	<div class = "child">Hello</div>

</div>
```

```css

.child {
	color: red;
}

.parent .child {
	color: blue;
}
```

: `.parent .child` is more specific than the class selector. Thus the color is blue.

##### D. Class over type

: basically class selectors will be done than generalized tag-type selectors

##### E. Order

: if both selectors have equal priority, the last declared selector will be done.

```html
<div class = "parent">
	<div class = "child greet">Hello</div>
</div>
```

```css
.parent .child {
	color: green;
}

.child.greet {
	color: blue;
}
```

: we mentioned that descendant selectors and chain selectors are of equal specificity and priority. The last selector will be done. Thus the color is blue.

## 4. **Chrome Devtools**

: simply click `f12` to enter inspect mode
: in there, you can inspect the HTML, CSS, AND JS contents, the latency of loading objects, and errors where you can debug and modify various parts of the webpage in real time via the Inspect Mode

: for more info, visit https://developer.chrome.com/docs/devtools/overview/

## **5.  The Box Model**

: See every element as a box consisting of different measurements in terms of its **border, padding, and margin**

##### A. Border

: The outline of the box

##### B. Padding

: Basically the space in between the border and the content of the box
##### C. Margin

: The space in between the element to other adjacent elements
