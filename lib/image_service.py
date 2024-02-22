import numpy as np
import requests
from PIL import Image


def _image_url(size: int) -> str:
    return "https://picsum.photos/{}".format(size)


def color_noise_image(size: int) -> Image:
    img_matrix = np.random.uniform(size=(3, size, size)) * 255
    img_matrix = np.ascontiguousarray(img_matrix.T)
    return Image.fromarray(img_matrix, mode="RGB")


def random_image_picsum(size: int) -> Image:
    url = _image_url(size)
    return Image.open(requests.get(url, stream=True).raw)


def get_image(size: int) -> Image:
    return color_noise_image(size)
