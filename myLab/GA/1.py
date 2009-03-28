# encoding: utf-8

from PIL import Image, ImageDraw

if __name__ == "__main__":
    im = Image.open("ff.gif")
    #im.rotate(45).show()
    print im.getpixel((50, 60))
    draw = ImageDraw.Draw(im)
    draw.line((0, 0) + im.size, fill = 1)
    del draw
    im.show()
