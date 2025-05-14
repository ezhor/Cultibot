from datetime import datetime
import subprocess
import os
import moisture

currentDate = datetime.now()
datePath = str(currentDate.year) +"/"+ str(currentDate.year) +"-"+ str(currentDate.month).zfill(2) +"-"+ str(currentDate.day).zfill(2)

def generatePaths():
    global picturePath
    global dataPath
    global pictureFileName
    global dataFileName
    
    picturePath = "../cultibot-images/"+ datePath + "/"
    dataPath = "../cultibot-data/"+ datePath + "/"
    fileName = str(currentDate.hour).zfill(2) + str(currentDate.minute).zfill(2)
    pictureFileName = fileName + ".jpeg"
    dataFileName = fileName + ".csv"
    if(not os.path.exists(picturePath)):
        os.makedirs(picturePath)
    if(not os.path.exists(dataPath)):
        os.makedirs(dataPath)


def takePicture():
    process = subprocess.Popen("libcamera-jpeg --width 1080 --height 1920 -o " + picturePath + pictureFileName, shell=True, stdout=subprocess.PIPE)
    process.wait()

def saveData():
    with open(dataPath + dataFileName, "w") as file:
        file.write(str(moisture.currentMoistureRaw()))
    
def main():
    if(currentDate.hour >= 6 and currentDate.hour < 22 and currentDate.minute % 4 == 0):
        generatePaths()    
        takePicture()
        saveData()

main()
