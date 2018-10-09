import sys
import random
import numpy as np
from PIL import Image

size = 20
n, m = 50, 100

def get_random_img(imgs, rotate):
    img = random.choice(imgs)
    angle = random.randint(0, 4)*90
    if rotate:
        img = img.rotate(angle).convert('L')
    return img


def gen(filename, imgs, rotate):
    imgs = map(Image.open, imgs)
    shape = (size, size)
    imgs = [i.resize(shape) for i in imgs]
    imgs_comb = np.vstack(np.hstack((np.asarray(get_random_img(imgs, rotate)) for j in range(m))) for i in range(n))
    imgs_comb = Image.fromarray( imgs_comb)
    imgs_comb.save(filename)

imgs = ['0.png', '1.png', '2.png', '3.png']
gen('test.png', imgs, True)
digits = map('d{}.png'.format, range(10))
gen('digits.png', digits, False)
