import os
from PIL import Image

src = "./images/"
dst = "./imgs/"
size = (128, 128)
imgs = os.listdir(src)

for img in imgs:
    try:
        with Image.open(src + img) as im:
            im = im.convert('RGB')
            im = im.resize(size)
            im = im.rotate(270)
            im.save(dst + img, 'JPEG')
    except OSError:
        print("cannot convert", img)


