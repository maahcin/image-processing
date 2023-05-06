import numpy as np
from utils import normalize_image

def entropyfilt(img, window):
    if img.ndim == 3:
        r_entropies = entropyfilt(img[:, :, 0], window)
        g_entropies = entropyfilt(img[:, :, 1], window)
        b_entropies = entropyfilt(img[:, :, 2], window)
        return (r_entropies + g_entropies + b_entropies) / 3

    Nz, Nx = img.shape

    image_padded = np.pad(img, window // 2, mode='symmetric')
    entropies = np.zeros_like(img, dtype=np.float64)
    for i in range(Nz):
        for j in range(Nx):
            block = image_padded[i:i + window, j:j + window]
            hist, _ = np.histogram(block, 256)
            hist = hist.astype(np.float64)
            hist /= np.sum(hist)
            entropies[i, j] = -np.sum(hist * np.log10(hist + (hist == 0)))

    return normalize_image(entropies)