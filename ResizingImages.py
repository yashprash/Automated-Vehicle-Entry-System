from PIL import Image
avgw=0
avgh=0
count=0
for i in range(1,317):
    try:
        img = Image.open("C:/ML_Project/Dataset/PositiveExamples/"+str(i)+".jpg")
        width,height=img.size
        avgw+=width
        avgh+=height
    except IOError:
        pass
    else:
        count+=1
avgw=int(avgw/count)
avgh=int(avgh/count)
for i in range(1,317):
    try:
        img = Image.open("C:/ML_Project/Dataset/PositiveExamples/"+str(i)+".jpg")
        img=img.resize((avgw,avgh))
        img.save("C:/ML_Project/Dataset/PositiveExamplesResized/"+str(i)+".jpg") 
    except IOError:
        pass
