from datetime import datetime
from datetime import timedelta
from datetime import date
import subprocess
import os
from moviepy.editor import *
import cv2
import shutil

currentDate = datetime.now()
dateString = str(currentDate.year) +"-"+ str(currentDate.month).zfill(2) +"-"+ str(currentDate.day).zfill(2)

def generatePaths():
    global path
    global tmp
    global fileName
    
    path = "./images/"+ dateString + "/"
    tmp = path + "tmp/"
    fileName = str(currentDate.hour).zfill(2) + str(currentDate.minute).zfill(2) + ".jpeg"    
    if(not os.path.exists(tmp)):
        os.makedirs(tmp)


def takePicture():
    process = subprocess.Popen("libcamera-jpeg --width 1080 --height 1920 -o " + path + fileName, shell=True, stdout=subprocess.PIPE)
    process.wait()

def createPictureWithDate():
    img = cv2.imread(path + fileName)
    dateTimeString = dateString + " " + fileName[0:2] + ":" + fileName[2:4]
    cv2.rectangle(img, (40,10), (380, 70), (0,0,0), -1)
    cv2.putText(img=img, text=dateTimeString, org=(50, 50), fontFace=cv2.FONT_HERSHEY_TRIPLEX, fontScale=1, color=(0, 255, 0),thickness=3)
    cv2.imwrite(tmp + fileName, img)

def uploadTimelapse():
    clip = ImageSequenceClip(tmp, fps=24)
    clip.write_videofile(tmp + "timelapse.mp4", audio=False)
    upload_result = apiV1.media_upload(tmp + "timelapse.mp4")
    clientV2.create_tweet(text=dateString, media_ids=[upload_result.media_id_string])
    shutil.rmtree(tmp)
    
def main():
    if(currentDate.hour >= 6 and currentDate.hour < 22 and currentDate.minute % 4 == 0):
        generatePaths()    
        takePicture()
        #createPictureWithDate()        
        #if(currentDate.hour == 21 and currentDate.minute == 56):
            #uploadTimelapse()

main()
