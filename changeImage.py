#!/usr/bin/env python3

from PIL import Image
import os

#sourceFolder = "supplier-data/images/"
sourceFolder = "./images/"
fileList = []

fileList = os.listdir(sourceFolder)

if len(fileList) == 0:
    print("No files found in source folder!")
    exit(1)

for file in fileList:
    fileName = os.path.splitext(file)
    path = sourceFolder + fileName[0] + ".jpg"
    try:
        im = Image.open(sourceFolder + file)
    except:
        print(file + " is not a image file format compatible.")
        continue
    print("handling file: " + file )
    im = im.convert("RGB")
    print("Creating file: "+ path)
    im.resize((600,400)).save(path, "JPEG")
    im.close()
print("done!")