from moviepy.editor import *
import os
import cv2
import shutil
from datetime import date, timedelta

tmp = "./tmp/"

def clearTmp():
    if(os.path.exists(tmp)):
        shutil.rmtree(tmp)
    os.mkdir(tmp)

def makeTmpTimelapse(fps:int):
    clip = ImageSequenceClip(tmp, fps=fps)
    clip.write_videofile(f"{tmp}timelapse.mp4", audio=False)

def makeCurrentDayTimelapse():
    currentDate = date.today()
    dateString = f"{currentDate.year}-{str(currentDate.month).zfill(2)}-{str(currentDate.day).zfill(2)}"
    datePath = f"../cultibot-images/{currentDate.year}/{dateString}"

    clearTmp()

    for fileName in os.listdir(datePath):
        img = cv2.imread(f"{datePath}/{fileName}")
        dateTimeString = f"{dateString} {fileName[0:2]}:{fileName[2:4]}"
        cv2.rectangle(img, (40,10), (380, 70), (0,0,0), -1)
        cv2.putText(img=img, text=dateTimeString, org=(50, 50), fontFace=cv2.FONT_HERSHEY_TRIPLEX, fontScale=1, color=(0, 255, 0),thickness=3)
        cv2.imwrite(f"{tmp}{fileName}", img)
    
    makeTmpTimelapse(24)
    
    return dateString

def generateImagesMonth(year:int, month:int):
    yearPath = f"../cultibot-images/{str(year)}"
    for folderName in os.listdir(yearPath):
        sourceImagePath = f"{yearPath}/{folderName}/1500.jpeg"
        if(int(folderName.split("-")[1]) == month and os.path.exists(sourceImagePath)):
            img = cv2.imread(sourceImagePath)
            cv2.rectangle(img, (40,10), (270, 70), (0,0,0), -1)
            cv2.putText(img=img, text=folderName, org=(50, 50), fontFace=cv2.FONT_HERSHEY_TRIPLEX, fontScale=1, color=(0, 255, 0),thickness=3)
            cv2.imwrite(f"{tmp}{folderName}.jpeg", img)