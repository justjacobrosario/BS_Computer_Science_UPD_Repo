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

: use `<style>` tag





##### C. Inline CSS

