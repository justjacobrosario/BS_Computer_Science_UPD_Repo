def greet(n, greeting, name):
	return (f"{greeting}, {name}! " * n).strip()

print(greet(3, "Welcome", "John"))
    