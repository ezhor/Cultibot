import configparser
from telegram import Update, Bot
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import os
import urllib.request
import time

config = configparser.ConfigParser()
config.read("../config.txt")
token = config["Telegram"]["token"]
imagesParentDirectory = "./images"

async def picture(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    daysList = os.listdir(imagesParentDirectory)
    daysList.sort()
    lastDay = daysList[-1]
    picturesList = os.listdir(f"{imagesParentDirectory}/{lastDay}")
    picturesList.sort()
    lastPicture = picturesList[-1]
    imagePath = f"{imagesParentDirectory}/{lastDay}/{lastPicture}"
    await update.message.reply_photo(photo = imagePath, caption = f"#picture\n{lastDay}\n{lastPicture[0:2]}:{lastPicture[2:4]}")

app = None

while app == None:
    try:
        app = ApplicationBuilder().token(token).build()        
    except Exception as e:
        print(e)
        time.sleep(1)
        pass

app.add_handler(CommandHandler("picture", picture))
print("Polling")
app.run_polling()
