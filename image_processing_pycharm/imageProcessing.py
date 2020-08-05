from PIL import Image, ImageFilter
img = Image.open('imagess\one.jpg')
filterimage=img.filter(ImageFilter.DETAIL)
filterimage.save("one_blur.png", 'png')
filterimage1=img.convert("L")
filterimage1.save("one_L.png",'png')
#filterimage1.rotate(180).show()
#filterimage1.resize((800,800)).show()
#filterimage1.crop((20,50,200,200)).show()
#filterimage1.filter(ImageFilter.BLUR).show()
img.thumbnail((200,200))
img.show()



