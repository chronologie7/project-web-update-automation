#! /usr/bin/env python3

import os
import requests

def data_to_dic(d, fileName):
    dic = {
        "name": "",
        "weight": "",
        "description": "",
        "image_name": ""
    }

    dic["name"] = d[0]
    dic["weight"] = int(d[1][:-4])
    dic["description"] = d[2]
    dic["image_name"] = fileName + ".jpeg"

    return dic

#sourceFolder = "supplier-data/descriptions/"
sourceFolder = "./txt/"
fileList = os.listdir(sourceFolder)
info = []
url = "https://linux-instance-IP-Address/fruits/"

if len(fileList) == 0:
    raise "No files found in source folder!"

for file in fileList:
    with open(sourceFolder + file) as f:
        d = f.read().strip().split("\n")
    info.append(data_to_dic(d, os.path.splitext(file)[0]))

"""
for data in info:
    for k, v in data.items():
        print(k + ": " + str(v))
    print("=" * 50)
"""

for data in info:
    try:
        r = requests.post(url, json=data)
    except:
        raise "Connection failed."
    if r.status_code == 201:
        print("Request successful")
    else:
        print("Request failed")