def full_names(surname, firstname):
    if firstname == ():
        return ()
    else:
        return ((firstname[0]) + " " + surname,) + full_names(surname, firstname[1:])

print(full_names('Addams', ('Gomez', 'Morticia', 'Wednesday', 'Pugsley')))

