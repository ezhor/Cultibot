import configparser
from telegram import Update, Bot
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import os
from urllib.request import urlopen
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

internet = False

while not internet:
    try:
        urlopen("http://www.google.com/").read()
        internet = True
    except Exception as e:
        print(e)
        time.sleep(1)
        pass

app = ApplicationBuilder().token(token).build()
app.add_handler(CommandHandler("picture", picture))
app.add_handler(CommandHandler("start", picture))
print("Polling...")
app.run_polling()
