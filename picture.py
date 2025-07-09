from datetime import datetime
import os
import moisture
from picamera2 import Picamera2
import time

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
    camera = None

    try:
        camera = Picamera2()
        camera_config = camera.create_still_configuration(main={"size": (1920, 1080)})
        camera.configure(camera_config)
        camera.start()
        time.sleep(2)

        camera.capture_file(picturePath + pictureFileName)
    
    finally:
        if camera is not None:
            try:
                camera.stop()
            except Exception as stop_e:
                print(str(stop_e))

def saveData():
    with open(dataPath + dataFileName, "w") as file:
        file.write(str(moisture.currentMoistureRaw()))
    
def main():
    if(currentDate.hour >= 6 and currentDate.hour < 22 and currentDate.minute % 4 == 0):
        generatePaths()    
        takePicture()
        saveData()

if __name__ == "__main__":
    picturePath = "./"
    pictureFileName = "test.jpeg"
    takePicture()