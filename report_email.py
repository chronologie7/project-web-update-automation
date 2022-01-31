#!/usr/bin/env python3

import datetime
import reports
import os
import emails

def data_to_matrix(data):
    inf = []
    dic = {
        "name": data[0],
        "weight": data[1]
    }
    """
    inf.append("name: " + dic["name"])
    inf.append("weight: " + dic["weight"])
    """
    return "name: {}<br/>weight: {}".format(dic["name"], dic["weight"])
    
 
#sourceFolder = "supplier-data/descriptions/"
sourceFolder = "./txt/"
fileList = os.listdir(sourceFolder)
#for linuz
#path_filename = "/tmp/processed.pdf"
path_filename = "processed.pdf"

info = []

if len(fileList) == 0:
    raise "No files found in source folder!"

for file in fileList:
    with open(sourceFolder + file) as f:
        d = f.read().strip().split("\n")
    info.append(data_to_matrix(d))


#print(info)

if __name__ == "__main__":
    today = datetime.datetime.now().date().strftime("%b %d, %Y")

    #print(today)
    #print(type(today))

    reports.generate_report(path_filename, "Processed Update on " + today, "<br/><br/>".join(info))

    sender = "automation@example.com"
    recipent = os.environ.get("USER") + "@example.com"
    subject = "Upload Completed - Online Fruit Store"
    body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."

    message = emails.generate(sender, recipent, subject, body, path_filename)
    emails.send(message)