from moviepy.editor import *
import os
import cv2
import shutil

images = "./images/"
tmp = "./tmp/"

if(os.path.exists(tmp)):
    shutil.rmtree(tmp)
    
os.mkdir(tmp)

for directory in os.listdir(images):
    print(directory)
    path = images + directory + "/";
    for fileName in os.listdir(path):
        if(os.path.isfile(path + fileName)):
            hour = int(fileName[0:2])
            if(hour >= 8 and hour <= 20):
                img = cv2.imread(path + fileName)
                strDate = directory + " " + fileName[0:2] + ":" + fileName[2:4]
                cv2.rectangle(img, (40,10), (380, 70), (0,0,0), -1)
                cv2.putText(img=img, text=strDate, org=(50, 50), fontFace=cv2.FONT_HERSHEY_TRIPLEX, fontScale=1, color=(0, 255, 0),thickness=3)
                cv2.imwrite(tmp + directory + "_" + fileName, img)

clip = ImageSequenceClip(tmp, fps=100)
clip.write_videofile(tmp + "timelapse.mp4", audio=False)

print("Done")
