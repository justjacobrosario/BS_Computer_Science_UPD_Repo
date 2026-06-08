
# 1. JavaScript, HTML, and, CSS

1. JS is a programming language used for dynamic interaction with markup languages HTML and CSS
2. JS provides interactive functionality while HTML and CSS is for structure and style

# 2. JS Syntax
1. `//` for comments
2. `;` for every code line
# 3. Data Types

1. `Number`

2. `Floating Point`

3. `String`

4. `Boolean` : lowercased

5. `undefined` : declared var but still no value

6. `null` : nothing value (similar to C's `NULL` and Python's `None`)

7. `Object` : collection of key-value pairs (similar to C's `struct` and Python's `dict`)

8. `Symbol` : fixed unchangeable value (like C's `const`)

9. `BigInt` : add `n` at the end of values exceeding `Number`'s limit (like C's `int64_t`)

* `console.log` prints values or variables in the console
* similar to Python's `print()`

```js
// comments

console.log(3); // Number
console.log(3.14159); // Floating Point
console.log("Hello:>") // String
console.log(true) // Boolean (lowercased)

// complex data types
// Object (like dictionaries)
{
	name : "Juan",
	age : 123
};
// Symbol (like const)
Symbol("MySymbol");
// BigInt
123456789123456789123456789123456789123456789n;
```

