import numpy as np
import math


def linear_se(length, angle):
    angle = math.radians(angle)

    nx = 2 * round(((length * abs(math.cos(angle))) - 1) / 2) + 1
    ny = 2 * round(((length * abs(math.sin(angle))) - 1) / 2) + 1

    result = np.zeros([ny, nx])

    if math.cos(angle) >= 0:
        points = bresenham_line(0, ny - 1, nx - 1, 0)

    else:
        points = bresenham_line(nx - 1, ny - 1, 0, 0)

    for x in points:
        result[x[1], x[0]] = 1

    return result


def bresenham_line(x0, y0, x1, y1):
    dx = abs(x1 - x0)
    dy = abs(y1 - y0)
    sx = 1 if x0 < x1 else -1
    sy = 1 if y0 < y1 else -1
    err = dx - dy
    line = []

    while x0 != x1 or y0 != y1:
        line.append((x0, y0))
        e2 = 2 * err
        if e2 > -dy:
            err -= dy
            x0 += sx
        if e2 < dx:
            err += dx
            y0 += sy

    line.append((x1, y1))
    return line


def imclose(img, length, angle):
    SE = linear_se(length, angle)

    Nz, Nx = img.shape
    Sz, Sx = SE.shape

    Sz_half = Sz // 2
    Sx_half = Sx // 2

    eroded_img = np.zeros(img.shape)
    dilated_img = np.zeros(img.shape)

    for x in range(Sz_half, Nz - Sz_half):
        for y in range(Sx_half, Nx - Sx_half):
            on = img[x - Sz_half: x + Sz_half + 1, y - Sx_half: y + Sx_half + 1]
            dilated_img[x, y] = max(on[(SE == 1)])

    for x in range(Sz_half, Nz - Sz_half):
        for y in range(Sx_half, Nx - Sx_half):
            on = dilated_img[x - Sz_half: x + Sz_half + 1, y - Sx_half: y + Sx_half + 1]
            eroded_img[x, y] = min(on[(SE == 1)])

    if img.dtype == 'bool':
        return np.where(eroded_img >= eroded_img.max() / 2, True, False)
    else:
        return eroded_img
