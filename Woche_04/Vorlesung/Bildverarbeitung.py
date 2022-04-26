import numpy as np
from matplotlib import pyplot as plt, image
from typing import Dict


def plot_images(images: Dict[str, np.ndarray], title: str):
    """ Plot multiple images next to each other.

    :param images: Dictionary with image caption as key and the image as value.
    :param title: Overall plot title and name used for saving the figure.
    """
    fig, axs = plt.subplots(ncols=len(images.keys()), figsize=(16, 6))
    i = 0
    for key, item in images.items():
        axs[i].imshow(item)
        axs[i].set(title=key)
        i += 1
    plt.tight_layout()
    fig.savefig(f'{title}.png')
    plt.show()


# Bild laden
image: np.ndarray = image.imread(fname='Zentralgebäude.jpg')

# Typ und Form ausgeben lassen
print(type(image))
print(image.dtype)
print(image.shape)

# Bild invertieren
image_inverted = 255 - image
plot_images(images={'Originalbild': image, 'Invertiertes Bild': image_inverted}, title='Bildinvertierung')

# Kopie erstellen vom Originalbild, dann blauen Farbkanal auf 0 setzen
image_manipulated = image.copy()
image_manipulated[:, :, 2] = np.zeros(shape=image.shape[:2])
plot_images(images={'Originalbild': image, 'Manipuliertes Bild': image_manipulated}, title='Bildmanipulation')
