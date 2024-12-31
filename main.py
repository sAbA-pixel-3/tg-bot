import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters 
import youtube_dl 



logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO)
logger = logging.getLogger(__name__)



def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
    text="Hello! I'm a video downloader bot. Just send me the URL of the video you want me to download.")

def download_video(update, context):
    url = update.message.text

    ydl_opts = {
        'outtmpl': '%(title)s.%(ext)s',
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        try:
            info = ydl.extract_info(url, download=False)
            video_title = info['title']
            video_url = info['url']
            ydl.download([url])
            context.bot.send_message(chat_id=update.effective_chat.id, 
                text="Video downloaded successfully!")
            context.bot.send_video(chat_id=update.effective_chat.id, video=video_url, caption=video_title)
        except Exception as e:
            logger.error(f"Error downloading video: {e}")
            context.bot.send_message(chat_id=update.effective_chat.id, 
                text="Failed to download the video!")












