import os
import shutil

images = "../cultibot-images"

for directory in os.listdir(images):
    for sub in os.listdir(os.path.join(images, directory)):
        path = os.path.join(images, directory, sub)
        if(os.path.isdir(path) and sub == "tmp"):
            print(path)
            shutil.rmtree(path)

