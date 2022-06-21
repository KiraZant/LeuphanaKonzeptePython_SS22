import cv2
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def read_img(path):
    img = cv2.imread(path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return img


def img_hist(img):
    img2 = img.flatten()
    plt.hist(img2, bins=255)
    plt.show()


def plot_before_after(img1, img2):
    fig, (ax1, ax2) = plt.subplots(1, 2)
    ax1.imshow(img1, cmap='gray')
    ax1.set_title("Original")
    ax2.imshow(img2, cmap='gray')
    ax2.set_title("Transformed")
    plt.show()


def plot_3d(img):
    # create the x and y coordinate arrays
    xs, ys = np.mgrid[:img.shape[0], :img.shape[1]]
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    ax.plot_surface(xs, ys, img, rstride=1, cstride=1, cmap=plt.cm.gray, linewidth=0)
    plt.show()


if __name__ == '__main__':
    img = read_img('images/001.png')
    plot_3d(img)
