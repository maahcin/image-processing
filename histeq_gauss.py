import numpy as np
from matplotlib import pyplot as plt
from utils import normalize_image
import math


def f_gauss(x, mean, std_dev):
    return math.exp(-(x - mean) ** 2 / (2 * std_dev ** 2)) / (std_dev * math.sqrt(2 * math.pi))


def histeq_gauss(img, std):
    if img.ndim == 3:
        new_r = histeq_gauss(img[:, :, 0], std)
        new_g = histeq_gauss(img[:, :, 1], std)
        new_b = histeq_gauss(img[:, :, 2], std)
        return np.array([new_r, new_g, new_b]).transpose(1, 2, 0)
    hist, _ = np.histogram(img, 256, [0, 255])
    x = np.arange(0, 256)
    hist_normalized = hist / np.sum(hist)

    hist_cdf = hist_normalized.cumsum()

    gauss = np.array([f_gauss(i, 127.5, std) for i in x])
    gauss_normalized = gauss / np.sum(gauss)

    gauss_cdf = gauss_normalized.cumsum()

    thresholds = np.linspace(0, 255, 15, dtype=int)

    temp = []

    for i in img.flatten():
        new_val = 0
        for j in thresholds:
            if gauss_cdf[j] > hist_cdf[i]:
                break
            new_val = j
        temp.append(new_val)

    new_img = np.array(temp).reshape(*img.shape)

    new_hist, _ = np.histogram(new_img, 256, [0, 255])
    new_hist_normalized = new_hist / np.sum(new_hist)

    fig, ax = plt.subplots(2, 2, figsize=(20, 20))
    ax[0][0].bar(x, hist_normalized, alpha=0.5)
    ax[0][0].bar(x, gauss_normalized, alpha=0.5)
    ax[0][0].set_title("Znormalizowane histogramy obrazu oraz rozkładu Gaussa")
    ax[0][1].grid(True)
    ax[0][1].set_xlim([-1, 256])
    ax[0][1].set_ylim([-0.01, 1.01])
    ax[0][1].plot(x, hist_cdf)
    ax[0][1].plot(x, gauss_cdf, color='red')
    ax[0][1].set_title("Dystrybuanty obrazu oraz rozkładu Gaussa")
    ax[1][0].plot(thresholds, gauss_cdf[thresholds])
    ax[1][0].scatter(thresholds, gauss_cdf[thresholds])
    ax[1][0].grid(True)
    ax[1][0].set_title("Zaznaczone na siatce progi")
    ax[1][0].set_xlim([-1, 256])
    ax[1][0].set_ylim([-0.01, 1.01])
    ax[1][1].bar(x, new_hist_normalized)
    ax[1][1].set_title("Histogram obrazu po wyrównaniu")
    fig.show()

    return normalize_image(new_img)
