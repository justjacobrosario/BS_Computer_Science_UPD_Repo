'''def parallelepiped_volume(x, y, z):
    return int((((x[0] * (y[1]*z[2] - y[2]*z[1])) - (x[1] * (y[0]*z[2] - y[2]*z[0])) + (x[2] * (y[0]*z[1] - y[1]*z[0])))**2)**0.5)
'''

def parallelepiped_volume(x, y, z):
    result = int((x[0] * (y[1]*z[2] - y[2]*z[1])) - (x[1] * (y[0]*z[2] - y[2]*z[0])) + (x[2] * (y[0]*z[1] - y[1]*z[0])))
    if result < 0:
        return -1 * result
    else:
        return result


print(parallelepiped_volume((1, 1, 0), (1, 0, 1), (0, 1, 1)))