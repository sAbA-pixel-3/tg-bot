from aiogram import Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message, CallbackQuery
from aiogram import F 
from commands.keyboards_tg import *


command_router = Router() 
@command_router.message(Command('start')) 
async def start_handler(message: Message):
    await message.answer(f"Hello, @{message.from_user.username}, I'm bot, I'll help you choose a movie", reply_markup=kb)  


@command_router.message(F.text == "Movie catalog")
async def movie_handler(message: Message):
    await message.answer(f"Movie catalog:",
        reply_markup=await get_movies_kb())
    
@command_router.message(F.text == "Series catalog")
async def series_handler(message: Message):
    await message.answer(f"Series catalog:",
        reply_markup=await get_series_kb())
    
@command_router.message(F.text == "Genre catalog")
async def genre_handler(message: Message):
    await message.answer(f"Genre catalog:",
        reply_markup=await get_genre_kb()) 
    
@command_router.message(F.text == "Actors")
async def movie_handler(message: Message):
    await message.answer(f"Actors:",
        reply_markup=await get_actors_kb())
    
@command_router.message(F.text == "Directors")
async def movie_handler(message: Message):
    await message.answer(f"Directors:",
        reply_markup=await get_directors_kb())





# @command_router.message(F.text == 'Movies') 
# async def message_handler(message: Message): 
#     await message.answer(f"Choose a movie:", reply_markup=ikb) 

# @command_router.message(F.text == 'Genres') 
# async def message_handler(message: Message): 
#     await message.answer(f"Choose a genre:", reply_markup=ikb1)

# @command_router.message(F.text == 'Movie catalogs') 
# async def message_handler(message: Message): 
#     await message.answer(f"Choose one movie:", reply_markup=ikb2)

# @command_router.message(F.text == 'Series') 
# async def message_handler(message: Message): 
#     await message.answer(f"Choose one:", reply_markup=ikb3)

# @command_router.message(F.text == 'Actors') 
# async def message_handler(message: Message): 
#     await message.answer(f"Choose an actor:", reply_markup=ikb4)

# @command_router.message(F.text == 'Search movie by its name') 
# async def message_handler(message: Message): 
#     await message.answer(f"Type a movie title below:")



# # @command_router.callback_query(F.data == 'hello') 
# # async def message_handler(callback: CallbackQuery):
# #     await callback.message.answer(f"Hello, I'm a bot")

# # @command_router.message(Command('add'))
# # async def start_handler(message: Message):
# #     await message.answer("Here's an add about cute cats! \nYou like them?")

# # @command_router.message(Command('address'))
# # async def start_handler(message: Message):
# #     await message.answer("Our address is CodeCraft. \nWelcome, MotherFucker")

# # @command_router.message(Command('help'))
# # async def start_handler(message: Message):
# #     await message.answer("Contact +996312000000 \n24/7")

# # @command_router.message(F.text.lower() == 'hello') # responds to 'hello' no matter how you type it
# # async def message_handler(message: Message):
# #     await message.answer(f"Hello @{message.from_user.username}, I'm bot") 

# # @command_router.message(F.text) # echo-bot
# # async def message_handler(message: Message):
# #     await message.answer(f"{message.text}")







