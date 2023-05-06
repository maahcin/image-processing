import numpy as np


def bwlabel(image):
    label_image = np.zeros(image.shape)
    N = 1
    Nz, Nx = image.shape
    for i in range(Nz):
        for j in range(Nx):
            if image[i, j] and label_image[i, j] == 0:
                label_image[i, j] = N + 1
                tab = [(i, j)]
                while len(tab) > 0:
                    z, x = tab.pop()
                    if z > 0 and image[z - 1, x] and label_image[z - 1, x] == 0:
                        label_image[z - 1, x] = N
                        tab.append((z - 1, x))
                    if z < Nz - 1 and image[z + 1, x] and label_image[z + 1, x] == 0:
                        label_image[z + 1, x] = N
                        tab.append((z + 1, x))
                    if x > 0 and image[z, x - 1] and label_image[z, x - 1] == 0:
                        label_image[z, x - 1] = N
                        tab.append((z, x - 1))
                    if x < Nx - 1 and image[z, x + 1] and label_image[z, x + 1] == 0:
                        label_image[z, x + 1] = N
                        tab.append((z, x + 1))
                N += 1
    return label_image
