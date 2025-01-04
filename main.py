from aiogram import Bot, Dispatcher, Router
from aiogram.types import Message, FSInputFile
from aiogram.filters import Command
from yt_dlp import YoutubeDL
import os
import asyncio

BOT_TOKEN = '8101133514:AAF-qC30hBRnbJjXORgjl0yTRE2Kcn7QVBc'

bot = Bot(token=BOT_TOKEN)
router = Router()

def download_yt_video(url: str) -> str:
    ydl_opts = {
        'format': 'best',
        'outtmpl': '%(title)s.%(ext)s'} # Save the video with its title as the filename

    with YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        return ydl.prepare_filename(info)

@router.message(Command("start"))
async def start_command(message: Message):
    await message.reply("Send me a YouTube video URL, and I'll download it for you!")

@router.message()
async def handle_video_request(message: Message):
    """Handle video download requests."""
    url = message.text
    try:
        video_path = download_yt_video(url)
        video_file = FSInputFile(video_path)
        await message.answer_document(video_file)
        os.remove(video_path)
    except Exception as e:
        await message.reply(f"An error occurred: {str(e)}")

async def main():
    dp = Dispatcher()
    dp.include_router(router)

    await bot.delete_webhook(drop_pending_updates=True)

    print("Bot is running...")

    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main()) 