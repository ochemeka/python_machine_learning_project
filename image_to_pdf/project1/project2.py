import os
from os import listdir
from os.path import isfile, join 
from pgmagick import Image

mypath = "images/" # path to your Image directory

for each_file in listdir(mypath):
    if isfile(join(mypath,each_file)):
        image_path = os.path.join(mypath,each_file)
        pdf_path =  os.path.join(mypath,each_file.rsplit('.', 1)[0]+'.pdf')
        img = Image(image_path)
        img.write(pdf_path)