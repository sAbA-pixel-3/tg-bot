from aiogram import Bot, Dispatcher, Router
from aiogram.types import Message, FSInputFile
from aiogram.filters import Command
import os
import shutil
import asyncio
from yt_dlp import YoutubeDL
import instaloader
from config import BOT_TOKEN


bot = Bot(token=BOT_TOKEN)
router = Router()

loader = instaloader.Instaloader()

def download_yt_video(url: str): 
    ydl_opts = {
        'format': 'best',
        'outtmpl': '%(title)s.%(ext)s'}  # save the file with its name

    with YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        return ydl.prepare_filename(info)

def download_instagram_content(url: str):
    try:
        download_dir = "downloads"
        os.makedirs(download_dir, exist_ok=True)
        shortcode = url.split("/")[-2]
        post = instaloader.Post.from_shortcode(loader.context, shortcode)

        downloaded_files = []

        if post.is_video:
            loader.dirname_pattern = download_dir
            loader.download_post(post, target=download_dir)
            
            for root, dirs, files in os.walk(download_dir):
                for file in files:
                    if file.endswith(".mp4"):
                        downloaded_files.append(os.path.join(root, file))

        elif post.is_album:
            loader.dirname_pattern = download_dir
            loader.download_post(post, target=download_dir)
            
            for root, dirs, files in os.walk(download_dir):
                for file in files:
                    if file.endswith((".jpg", ".mp4")):
                        downloaded_files.append(os.path.join(root, file))

        else:
            loader.dirname_pattern = download_dir
            loader.download_post(post, target=download_dir)
            
            for root, dirs, files in os.walk(download_dir):
                for file in files:
                    if file.endswith(".jpg"):
                        downloaded_files.append(os.path.join(root, file))

        if not downloaded_files:
            raise Exception("No content downloaded. Please check the URL.")
        
        return downloaded_files

    except Exception as e:
        raise Exception(f"Failed to download Instagram content: {str(e)}")

@router.message(Command("start"))
async def start_command(message: Message):
    await message.reply("Отправьте ссылку на YouTube или Instagram (только видео, не посты и карусели), и я скачаю видео🙃")

@router.message()
async def handle_video_request(message: Message):
    url = message.text
    try:
        if "youtube.com" in url or "youtu.be" in url:
            video_path = download_yt_video(url)
            video_file = FSInputFile(video_path)
            await message.answer_document(video_file)
            os.remove(video_path)
        elif "instagram.com" in url:
            content_paths = download_instagram_content(url)
            
            if isinstance(content_paths, list):  # Carousel with multiple media
                for content_path in content_paths:
                    content_file = FSInputFile(content_path)
                    await message.answer_document(content_file)
                    os.remove(content_path)
            else:  # Single file (image or video)
                content_file = FSInputFile(content_paths)
                await message.answer_document(content_file)
                os.remove(content_paths)
        else:
            await message.reply("Пожалуйста, отправьте действительную ссылку на YouTube или Instagram.")
    except Exception as e:
        await message.reply(f"Произошла ошибка: {str(e)}")

async def main():
    dp = Dispatcher()
    dp.include_router(router)

    await bot.delete_webhook(drop_pending_updates=True)

    print("Бот иштеп жатат...") 

    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main()) 