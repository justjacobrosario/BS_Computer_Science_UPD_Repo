
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

8. `Symbol` : a unique value (doesn't have same value, even if typed the same to another variable)

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

# 4. Variables

## 4.1. Variable Declaration

```js
// 1]
let age;
console.log(age); // undefined
```

```js
// 2]
let age = 30;
console.log(age); // 30
```

```js
// 3]
const pi = 3.1415;

// NOTICE: `const` declarations MUST have an assigned value

const pi; // error
```
## 4.2. Variable Mutation

```js
let age = 25; // var declaration

age = 30 // var mutation (no need for `let`)

console.log(age) // 30
```

## 4.3. Variable Naming Restrictions & Conventions

```js
// 1] CASE-SENSITIVE
let name;
let Name; // different

// 2] camelCase
let thisIsAVariable;

// 3] ✅ CAN USE
let age;
let _age; // can start with _
let $age; // can start with $

// 4] ❌ CAN'T USE THESE
let 1stAge // don't start with a number

```