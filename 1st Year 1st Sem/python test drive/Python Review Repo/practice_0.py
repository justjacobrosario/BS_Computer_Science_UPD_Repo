
def chair_count(r, c):
    return r*c

def dart_landed(x1, y1, x2, y2, x, y):
    return x1 <= x <= x2 and y1 <= y <= y2

def greet(n, greeting, name):
    return (f'{greeting}, {name}! '*n).strip()


def bmi_check(w, h):
    if (w // (h**2)) >= 25:
        return "Go on a diet!"
    else:
        return "You are too thin!"


# triangle area based on sides
# A = sqrt(s(s-a)(s-b)(s-c))

def distance(a1, b1, a2, b2):
    return (((a2-a1)**2 + (b2-b1)**2)**(1/2))

def tatsulok_area(x1, y1, x2, y2, x3, y3):
    j = distance(x1,y1,x2,y2)
    k = distance(x1,y1,x3,y3)
    l = distance(x2,y2,x3,y3)
    s = (j + k + l) / 2

    return round((s*(s-j)*(s-k)*(s-l))**(1/2), 1)

# triangle area based on points
# A  = (1/2) * abs(x1(y2-y3) + x2(y3 - y1) + x3(y1 - y2))

def tatsulok_area(x1, y1, x2, y2, x3, y3):
    return (1/2) * (((x1*(y2-y3) + x2*(y3 - y1) + x3*(y1 - y2))**2)**(1/2))


print(288.4 * .85)
print(370.8 * 0.28)
