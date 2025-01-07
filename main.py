from aiogram import Bot, Dispatcher, Router
from aiogram.types import Message, FSInputFile
from aiogram.filters import Command
from yt_dlp import YoutubeDL
import os
import asyncio
from config import BOT_TOKEN 


bot = Bot(token=BOT_TOKEN)
router = Router()

def download_yt_video(url: str) -> str:
    ydl_opts = {
        'format': 'best',
        'outtmpl': '%(title)s.%(ext)s'} # save the file with its name

    with YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        return ydl.prepare_filename(info)

@router.message(Command("start"))
async def start_command(message: Message):
    await message.reply("Отправьте ссылку на YouTube и я скачаю видео🙃") 

@router.message()
async def handle_video_request(message: Message):
    url = message.text
    try:
        video_path = download_yt_video(url)
        video_file = FSInputFile(video_path)
        await message.answer_document(video_file)
        os.remove(video_path)
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