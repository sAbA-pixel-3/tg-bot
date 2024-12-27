import asyncio
from aiogram import Bot, Dispatcher
from databases.models import *
import sys, logging
from config import TOKEN
from commands.command import command_router
from databases.models import create_tables
from databases.querysets import *
from commands.admin import *
from scrap.parsing import *



async def main():
    # await add_movies() 
    # await create_tables()

    # await add_series_actors()
    # await add_series_directors()
    # await add_series_genres() 

    # await add_genre() 
    # await add_url() 
    # await add_actors()
    # await add_directors() 
    # await add_movies() 
    # await add_series() 

    bot = Bot(token=TOKEN) 
    dp = Dispatcher() 
    dp.include_routers(command_router,admin_router)
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main()) 























