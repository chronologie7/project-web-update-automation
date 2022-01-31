#!/usr/bin/env python3

import requests
import os

url = "http://localhost/upload/"
#sourceFolder = "supplier-data/images/"
sourceFolder = "./images/"

fileList = os.listdir(sourceFolder)

if len(fileList) == 0:
    print("No files found in source folder!")
    exit(1)

for file in fileList:
    if os.path.splitext(file)[1] == ".jpg":
        with open(sourceFolder + file, 'rb') as f:
            print("uploading " + file + " to " + url + " ...")
            r = requests.post(url, files={"file": f})

print("done!")        