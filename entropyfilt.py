import numpy as np
from utils import normalize_image

def entropyfilt(img, window):
    Nz, Nx = img.shape[:2]
    half = (window - 1) // 2
    image_padded = np.pad(img, half, mode='symmetric')

    entropies = np.zeros_like(img, dtype=np.float64)
    for i in range(Nz):
        for j in range(Nx):
            if img.ndim == 3:
                block = image_padded[i:i + window, j:j + window, :]
            else:
                block = image_padded[i:i + window, j:j + window]
            block = block.flatten()
            hist, _ = np.histogram(block, 256)
            hist = hist.astype(np.float64)
            hist /= np.sum(hist)
            entropies[i, j] = -np.sum(hist * np.log10(hist + (hist == 0)))

    return normalize_image(entropies)