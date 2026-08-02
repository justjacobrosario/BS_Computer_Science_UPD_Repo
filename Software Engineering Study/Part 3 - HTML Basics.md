
## 1. The Front-end Triad

: websites has two parts (**Front-end and Back-end**).
: the Front-end is responsible for the things users see and interact
: the Back-end is responsible for the things that makes the app/website work behind the scenes.

: The front-end has three languages: (**HTML, CSS, and Javascript**)

1. **Hypertext Markup Language (HTML)** : is a markup language that gives structure and content to the website (i.e. the builder of the site).
2. **Cascading Style Sheet (CSS)**: gives style and color to the structures set by HTML (i.e. the designer of the site)
3. **JavaScript**: the *programming-language* that gives computational processes in the website, like adding search auto-suggestions (i.e. the wizard of the site, giving dynamic objects)

## 2. HTML Elements and Tags

: Websites consists of **elements** like texts, images, and buttons.

: elements consist of a **tag** and the **content** itself. The tag describes what type of content an element has.

### 2.1. Opening and Closing Tags
: Most elements have these. **Opening tags** is where the content of the element starts, and **closing tags** is where the content ends.

```html
<p>any text content</p>
```
: here we see the `<p>` tag which adds a paragraph text

for more tags refer here:
https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements

### 2.2. Void Elements

: there are some elements where it only has an opening tag (no closing tag)

: since there are no closing tag, the element obviously has no content.

: all of the element's information is within the **attributes** (i.e. parameters) of the opening tag.

e.g. 
```html
<img src="https://sample.com" alt="A cute dog" width="500" height="350">
```
: we can see here that the `img` tag refers to an image element from the `src` with a specified width and height. If the image cannot be displayed, the element will alternatively display the `alt` text.


## 3. HTML Boilerplate (i.e. starting template)

: the HTML file for the content of the homepage MUST BE **index.html**. (web servers usually check this file)

### 3.1. Parts of the HTML Boilerplate

: the html file consts of a **DOCTYPE declaration, html tag, head tag, and body tag**

1. **`DOCTYPE` declaration**

: this refers to which HTML version will the file run at. (must always be declared on the topmost line)
: in HTML 5 (current version as of 2026), has a DOCTYPE declaration of 

```html
<!DOCTYPE html>
```

2. **`<html>` tag**

: consists of an opening and closing tag where every tag will be contained

: the following two tags will be contained to the html tag

: it is advisable to declare the language attribute here

e.g.
```html
<html lang="en">
```

3. **`head` tag**

: has an opening and closing tag is where all metadata (data that exists does not literally a visible content) will be contained.

: never add tags of visible elements inside the head tag

: the following metadata tags are usually used:

- `meta` tag : declares a certain charset encoding to display characters properly

e.g. 
```html
<meta charset="UTF-8">
```

- `title` tag : declares the title of the webpage displayed by the current html file

e.g.
```html
<title>My first webpage</title>
```

4. **`body` tag**

: this is where all visible elements are contained

### 3.2. Combining everything

: you can manually do each part, or simply type `!` and then `tab` to an html file in vscode to automatically make the boilerplate

: this will be the complete boilerplate of a html file

```html
<!DOCTYPE html>

<html lang="en">

<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<title>Document</title>
</head>

<body>

</body>

</html>

```


## 4. HTML Text Manipulation


: there are multiple tags for customizing texts

##### A. `<p>` tag

: basically is a text paragraph element

```html
    <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor
  incididunt ut labore et dolore magna aliqua.</p>
```

##### B. Headings tags

: instead of manually changing the font size, you can use heading tags: `<h1>`,  `<h2>`,  `<h3>`,  `<h4>`,  `<h5>`,  `<h6>`,  which makes the text size smaller

```html
<html>
  <head>
  </head>
  <body>
    <h1>This is the biggest</h1>
    <h2>Smaller than heading 1</h2>
    <h3>Smaller than heading 2</h3>
    <h4>Smaller than heading 3</h4>
    <h5>Smaller than heading 4</h5>
    <h6>Smaller than heading 5</h6>
  </body>
 </html>
```

##### C. `<strong>`, `<em>` tags

: `<strong>` tag makes the content bold
: `<em>` tag makes the content italicized

```html
    <p>Lorem ipsum <em>dolor sit</em> amet, <strong>consectetur</strong> adipiscing elit.</p>
```
##### D. HTML Comments

: texts readable in the html file but will not be displayed
: in vs code, one can make a comment by typing `ctrl` + `/` and then click `tab`

```html
<p> This is a visible text </p>

<!-- This is an html comment -->

```


## 5. HTML Lists

: HTML can make an ordered list (numbered) using `<ol>` tag, and an unordered list (bulleted) using `<ul>` tag.

: Each object in both the ordered and unordered list must be contained within a `<li>` tag
e.g.

```html
<ul>
  <li>Item 1</li>
  <li>Item 2</li>
  <li>Item 3</li>
</ul>
```
 
 displays:
 - Item 1
 - Item 2
 - Item 3

```html
<ol>
  <li>Item 1</li>
  <li>Item 2</li>
  <li>Item 3</li>
</ol>
```

1. Item 1
2. Item 2
3. Item 3

## 6. Links and Images

: HTML adds links and images using the `<a>` tag (anchor tag) and the `<img>` tag (image tag) respectively

### A. `<a>` tag

: a link element that contains a text content (the anchor) where when clicked, will visit a certain hypertext reference (href) link.

```html
<a href="https://www.google.com/home">Click this to search</a>
```

: there are two types of links: absolute and relative links

###### Absolute Link

: an absolute link links to pages on other websites of the internet.

: an absolute link consists of `scheme://domain/path` like `https://www.google.com/home`

the previous example is an absolute link.

###### Relative Link

: a relative link links to pages saved locally in our computer and is addressed relative to where the current html file is.

e.g. 
1. Suppose we have an `about.html` at the same directory as our `index.html`

```html
<a href="about.html">About Us</a>
```


2. Suppose at the same directory as our `index.html`, we made another `other_pages` directory, in which inside that is our `about.html`

```html
<a href="./other_pages/about.html">About Us</a>
```
: as you can see, we added `./` at the front to specify that it should start looking for the file/directory to the current directory of our current html file.

### B. `<img>` tag

: `<img>` tag is an image element that does not have any text content. Thus, it has no ending tag.

: it contains
```html
<img src="" alt="" height="" width="">
```

1. the `src` attribute behaves like the `href` attribute of `<a>`tags. It can refer to absolute or relative links.
2. the `alt` attribute contains a string of text where it will be displayed alternatively whenever the image does not load.
3. the `height` and `width` declares the dimension of the image in pixels

e.g.
```html
<img src="./images/cat.jpg" alt="a cute cat" height= "75" width="75">
```

## 7. HTML Git Commit Messages

: we commit HTML changes whenever a new certain function is completely added (better to commit whenever such occurs, not occasionally nor too frequently)

: it is a good practice for commit messages to contain a subject (a concise title) and a body (a concise sentence describing what problem has solved or feature has added by the committed changes)

e.g.
```bash
git commit -m "Add alt texts to images\nSome large images occasionally do not display, so alt texts are added alternatively."
```