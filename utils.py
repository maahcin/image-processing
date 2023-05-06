import numpy as np
from matplotlib import image
from matplotlib import pyplot as plt

BINARY_IMAGE = 'coins_binary.png'
MONO_IMAGE = 'cameraman.tif'
RGB_IMAGE = 'peppers.jpg'


def normalize_image(img):
    if img.dtype == 'uint8':
        normalized_image = 255 * ((img - np.min(img)) / (np.max(img) - np.min(img)))
        return normalized_image.astype(np.uint8)
    else:
        normalized_image = 1.0 * ((img - np.min(img)) / (np.max(img) - np.min(img)))
        return normalized_image


def read_image(file_path):
    img = image.imread(file_path)
    if img.dtype == 'float32':
        img = convert_into_int(img)
    return img


def read_binary_image(file_path):
    img = image.imread(file_path)
    if len(img.shape) > 2:
        img = img[:, :, 0]
    return np.where(img >= img.max() / 2, True, False)


def convert_into_int(image):
    image = (image * 255).astype(np.uint8)
    return image


def process_image(file_name, file_type, fun, *args):
    path = "images/" + file_name
    name = str.split(file_name, '.')[0]
    if file_type == 'binary':
        img = read_binary_image(path)
    else:
        img = read_image(path)
    new_image = fun(img, *args)
    fig, ax = plt.subplots(1, 2, figsize=(20, 10))
    if file_type == 'rgb':
        ax[0].imshow(img)
        ax[0].set_title("Przed")
        ax[1].imshow(new_image)
        ax[1].set_title("Po")
    else:
        ax[0].imshow(img, cmap='gray')
        ax[0].set_title("Przed")
        if fun.__name__ == 'entropyfilt' or fun.__name__ == 'bwlabel':
            ax[1].imshow(new_image)
        else:
            ax[1].imshow(new_image, cmap='gray')
        ax[1].set_title("Po")
    fig.show()
    if file_type == 'rgb':
        image.imsave("processed_images/" + fun.__name__ + "_" + file_name, new_image, format='png')
    else:
        if fun.__name__ == 'entropyfilt' or fun.__name__ == 'bwlabel':
            image.imsave("processed_images/" + fun.__name__ + "_" + file_name, new_image, format='png')
        else:
            image.imsave("processed_images/" + fun.__name__ + "_" + file_name, new_image, format='png', cmap='gray')
