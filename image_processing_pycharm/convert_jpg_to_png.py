import sys
from PIL import Image,ImageFilter
import os

image_folder = sys.argv[1]
output_folder = sys.argv[2]

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

for img_name in os.listdir(image_folder):
    img = Image.open(f"{image_folder}{img_name}")
    imgname=os.path.splitext(img_name)
    # imagename = os.path.splitext(img_name)[0] we can allso do this
    img.save(f"{output_folder}{imgname[0]}.png",'png')
    #print(imgname[0])
