import json
import urllib.request
import os
from PIL import Image 

count=0
with open("C:\ML_Project\Indian_Number_plates.json") as f:
    for line in f:
        count=count+1
        data=json.loads(line)
        image_url=data["content"]
        urllib.request.urlretrieve(image_url, "C:/ML_Project/Dataset/"+str(count)+".jpg")
        try: 
            img = Image.open("C:/ML_Project/Dataset/"+str(count)+".jpg") 
            width, height = img.size  
            x1=data["annotation"][0]["points"][0]["x"]
            y1=data["annotation"][0]["points"][0]["y"]
            x2=data["annotation"][0]["points"][1]["x"]
            y2=data["annotation"][0]["points"][1]["y"]
            area = (x1*width,y1*height,x2*width,y2*height)
            img = img.crop(area) 
            img.save("C:/ML_Project/Dataset/"+str(count)+".jpg")   
        except IOError: 
            pass
