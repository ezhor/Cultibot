from datetime import datetime
from datetime import timedelta
from datetime import date
import subprocess
import os

currentDate = datetime.now()
datePath = str(currentDate.year) +"/"+ str(currentDate.year) +"-"+ str(currentDate.month).zfill(2) +"-"+ str(currentDate.day).zfill(2)

def generatePaths():
    global path
    global tmp
    global fileName
    
    path = "../cultibot-images/"+ datePath + "/"
    fileName = str(currentDate.hour).zfill(2) + str(currentDate.minute).zfill(2) + ".jpeg"    
    if(not os.path.exists(path)):
        os.makedirs(path)


def takePicture():
    process = subprocess.Popen("libcamera-jpeg --width 1080 --height 1920 -o " + path + fileName, shell=True, stdout=subprocess.PIPE)
    process.wait()
    
def main():
    if(currentDate.hour >= 6 and currentDate.hour < 22 and currentDate.minute % 4 == 0):
        generatePaths()    
        takePicture()

main()
