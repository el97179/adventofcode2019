import math
import numpy as np


def load_coordinates():
    with open("10") as f:
        asteroids = [x.rstrip() for x in f.readlines()]

    ast_coord = list()
    for y, row in enumerate(asteroids):
        for x, point in enumerate(row):
            if point == "#":
                # print(f"({x},{y})")
                ast_coord.append([x, y])
    return ast_coord


def create_line(point1, point2):
    # y1 = a*x1 + b
    # y2 = a*x2 + b
    x1 = point1[0]
    y1 = point1[1]
    x2 = point2[0]
    y2 = point2[1]
    if x1 == x2:
        # vertical line
        a = None
        b = x1
    else:
        a = (y2-y1)/(x2-x1)
        b = y1 - a*x1
    return a, b


def is_point_on_line(point, line):
    if line[0] is not None:
        # y = ax + b
        return math.isclose(point[1], line[0] * point[0] + line[1])
    else:
        return point[0] == line[1]


def is_blocking(base_ast, mid_ast, remote_ast):
    a, b = create_line(base_ast, remote_ast)
    line = [a, b]
    if not is_point_on_line(mid_ast, line):
        return False

    if mid_ast[0] < min(base_ast[0], remote_ast[0]) or mid_ast[0] > max(base_ast[0], remote_ast[0]):
        return False
    elif mid_ast[1] < min(base_ast[1], remote_ast[1]) or mid_ast[1] > max(base_ast[1], remote_ast[1]):
        return False
    else:
        return True


def has_line_of_sight(base_ast, remote_ast):
    for mid_ast in ast_coord:
        if mid_ast == base_ast or mid_ast == remote_ast:
            continue
        if is_blocking(base_ast, mid_ast, remote_ast):
            return False
    return True


def count_asteroids(ast_coord):
    clos = list()
    for base_ast in ast_coord:
        clos.append(0)
        for remote_ast in ast_coord:
            if remote_ast == base_ast:
                continue
            if has_line_of_sight(base_ast, remote_ast):
                clos[-1] += 1
    return clos


ast_coord = load_coordinates()
clos = count_asteroids(ast_coord)
print(clos)

clos_np = np.asarray(clos)
print(clos_np.argmax())
print(ast_coord[clos_np.argmax()])
print(max(clos))
