from PIL import Image, ImageFilter

img = Image.open("F:\hydrabad\python\image processing with python\processing images\one.jpg")

# print(img)
# print(img.format)
# print(img.size)
# print(img.mode)
#print(dir(img))
filterd_img = img.filter(ImageFilter.BLUR)
filterd_img1 = img.filter(ImageFilter.SMOOTH)
filterd_img2=img.convert('L')
filterd_img.save("F:\hydrabad\python\image processing with python\processed image\one_blur.png", 'png')
filterd_img1.save("F:\hydrabad\python\image processing with python\processed image\one_smoth.JPEG", 'JPEG')
filterd_img2.save("F:\hydrabad\python\image processing with python\processed image\one_convert_black.JPEG", 'JPEG')
