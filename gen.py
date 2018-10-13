import sys
import random
import numpy as np
from PIL import Image

size = 20
scale = 1
n, m = 100, 141
n *= scale
m *= scale

def get_random_img(imgs, rotate):
  img = random.choice(imgs)
  angle = random.randint(0, 4)*90
  if rotate:
    img = img.rotate(angle)
  return img

def get_images(imgs):
  imgs = map(Image.open, imgs)
  shape = (size, size)
  imgs = [i.resize(shape) for i in imgs]
  return imgs

def gen(imgs, rotate):
  imgs = get_images(imgs)
  return np.vstack(np.hstack((np.asarray(get_random_img(imgs, rotate)) for j in range(m))) for i in range(n))

imgs = ['0.png', '1.png', '2.png', '3.png']
pandas_map = gen(imgs, True)
digits = map('d{}.png'.format, range(10))
digits_map = gen(digits, False)

def mark(i, j, val):
  il,jl = size*i, size*j
  panda = np.asarray(get_random_img(get_images(['panda.png']), True))
  pandas_map[il:il+size,jl:jl+size] = panda

  j = m - 1 - j
  il,jl = size*i, size*j
  num = np.asarray(get_images([digits[val]])[0])
  digits_map[il:il+size,jl:jl+size] = num

# 51.8201 0.0012
mark(17, 2, 8)
mark(41, 19, 2)
mark(71, 45, 0)
mark(12, 53, 1)
mark(81, 86, 0)
mark(11, 99, 0)
mark(99, 112, 1)
mark(9, 138, 2)

Image.fromarray(pandas_map).save('test.png')
Image.fromarray(digits_map).save('digits.png')
