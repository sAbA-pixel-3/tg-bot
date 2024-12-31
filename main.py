import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters 
import youtube_dl 



logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO)
logger = logging.getLogger(__name__)



def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
    text="Hello! I'm a video downloader bot. Just send me the URL of the video you want me to download.")














