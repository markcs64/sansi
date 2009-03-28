# encoding: utf-8

from PIL import Image, ImageDraw, ImageMath

import lib.GA as GA

if __name__ == "__main__":
    im = Image.open("0.gif")
    im1 = Image.open("chrome.gif")
    im2 = Image.open("ff.gif")
    imn = Image.new("RGBA", (128, 128), (255, 255, 255))
    draw = ImageDraw.Draw(imn)
    draw.line((0, 0) + im.size, fill = (255, 255, 0))
    draw.polygon([(45, 95), (86, 28), (109, 88)], fill = (255, 0, 0, 128))
    draw.polygon([(25, 45), (56, 78), (99, 78)], fill = (255, 255, 0, 0))
    del draw
    imn.show()
    print imn.getpixel((50, 50))
    del imn
    #im.rotate(45).show()
    #print im.getpixel((50, 60))
    #print im.getdata()
    #im.show()
    #out = ImageMath.eval("convert(min(a, b), 'L')", a = im1, b = im2)
    #out.show()
