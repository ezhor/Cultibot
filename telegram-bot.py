import configparser
from telegram import Update, Bot
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import os
from urllib.request import urlopen
import time
import datetime
import pytz
from timelapse import makeCurrentDayTimelapse
import shutil
import moisture

config = configparser.ConfigParser()
config.read("../config.txt")
token = config["Telegram"]["token"]
imagesParentDirectory = "../cultibot-images"
dataParentDirectory = "../cultibot-data"
subscribersPath = "../subscribers"

def moistureInfo(dataPath: str) -> str:
    if(os.path.exists(dataPath)):
        with open(dataPath, "r") as file:
            return f"\nSoil moisture: {moisture.rawToNormalized(file.read())}%"
    return ""

async def picture(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    yearsList = os.listdir(imagesParentDirectory)
    yearsList.sort()
    lastYear = yearsList[-1]
    daysList = os.listdir(f"{imagesParentDirectory}/{lastYear}")
    daysList.sort()
    lastDay = daysList[-1]
    picturesList = os.listdir(f"{imagesParentDirectory}/{lastYear}/{lastDay}")
    picturesList.sort()
    lastPicture = picturesList[-1]
    imagePath = f"{imagesParentDirectory}/{lastYear}/{lastDay}/{lastPicture}"
    dataPath = f"{dataParentDirectory}/{lastYear}/{lastDay}/{lastPicture}".replace("jpeg", "csv")

    await update.message.reply_photo(photo = imagePath, caption = f"#picture\n{lastDay}\n{lastPicture[0:2]}:{lastPicture[2:4]}{moistureInfo(dataPath)}")

async def sendTimelapse(context: ContextTypes.DEFAULT_TYPE) -> None:
    dateString = makeCurrentDayTimelapse()
    file = open(subscribersPath)
    for chatId in file.read().split("\n"):
        if chatId:
            await context.bot.send_video(chat_id=chatId, video="./tmp/timelapse.mp4", caption=f"#Timelapse\n{dateString}", 
                                         read_timeout=1000, pool_timeout=1000, write_timeout=1000)
    shutil.rmtree("./tmp/")
    

async def subscribe(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    file = open(subscribersPath, "r")
    fileContent = file.read()
    file.close()    
    chatId = str(update.effective_message.chat_id)

    if(chatId not in fileContent):
        file = open(subscribersPath, "w+")
        fileContent = f"{chatId}\n{fileContent}"
        file.write(fileContent)
        file.close()
        await update.message.reply_text("You have been subscribed to timelapses! 🎉\nYou will receive a timelapse every night at 22:00 (Central European Time)")
    else:
        await update.message.reply_text("Looks like you were already subscribed to timelapses 🤔")


async def unsubscribe(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    file = open(subscribersPath, "r")
    fileContent = file.read()
    file.close()    
    chatId = str(update.effective_message.chat_id)

    if(chatId in fileContent):
        subscribers = fileContent.split("\n")
        subscribers.remove(chatId)
        file = open(subscribersPath, "w+")
        for i in range(len(subscribers)-1):
            subscribers[i] = subscribers[i] + "\n"
        file.writelines(subscribers)
        file.close()
        await update.message.reply_text("You have been unsubscribed to timelapses.\nSee you soon 😢")
    else:
        await update.message.reply_text("Looks like you weren't subscribed to timelapses 🤔")


if(not os.path.exists(subscribersPath)):
    open(subscribersPath, "x").close()

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
app.add_handler(CommandHandler("subscribe", subscribe))
app.add_handler(CommandHandler("unsubscribe", unsubscribe))
app.job_queue.run_daily(sendTimelapse, datetime.time(22,0,0, tzinfo=pytz.timezone('Europe/Madrid')), (0,1,2,3,4,5,6))
print("Polling...")
app.run_polling()
