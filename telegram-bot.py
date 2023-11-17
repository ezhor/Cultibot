import configparser
from telegram import Update, Bot
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import os

config = configparser.ConfigParser()
config.read("../config.txt")
token = config["Telegram"]["token"]
imagesParentDirectory = "./images"

async def picture(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    lastDay = os.listdir(imagesParentDirectory)[-1]
    lastPicture = os.listdir(f"{imagesParentDirectory}/{lastDay}")[-1]
    imagePath = f"{imagesParentDirectory}/{lastDay}/{lastPicture}"
    await update.message.reply_photo(photo = imagePath, caption = f"Last picture\n{lastDay}\n{lastPicture[0:2]}:{lastPicture[2:4]}")

async def timelapse(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Not implemented yet :(")

app = ApplicationBuilder().token(token).build()

app.add_handler(CommandHandler("picture", picture))
app.add_handler(CommandHandler("timelapse", timelapse))

app.run_polling()
