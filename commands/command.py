from aiogram import Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message, CallbackQuery, FSInputFile, URLInputFile
from aiogram.utils.media_group import MediaGroupBuilder
from aiogram import F 
from commands.keyboards_tg import *


command_router = Router() 
@command_router.message(Command('start')) 
async def start_handler(message: Message):
    await message.answer(f"Hello, @{message.from_user.username}, I'm bot, I'll help you choose a movie", reply_markup=kb)  


@command_router.message(F.text == "Movie catalog")
async def movie_handler(message: Message):
    await message.answer(f"Movie catalog:",
        reply_markup=await get_movies_kb(page=1)) 
    
@command_router.message(F.text == "Series catalog")
async def series_handler(message: Message):
    await message.answer(f"Series catalog:",
        reply_markup=await get_series_kb(page=1))
    
@command_router.message(F.text == "Genre catalog")
async def genre_handler(message: Message):
    await message.answer(f"Genre catalog:",
        reply_markup=await get_genre_kb(page=1))  
    
@command_router.message(F.text == "Actors")
async def actor_handler(message: Message):
    await message.answer(f"Actors:",
        reply_markup=await get_actores_kb())
    
# @command_router.message(F.text == "Search actors") 
# async def actor_handler(message: Message):
#     await message.answer(f"Actors:", 
#         reply_markup=await get_actors_kb()) 
    
@command_router.message(F.text == "Directors")
async def director_handler(message: Message):
    await message.answer(f"Directors:",
        reply_markup=await get_directores_kb())

# @command_router.message(F.text == "Directors")
# async def director_handler(message: Message):
#     await message.answer(f"Directors:",
#         reply_markup=await get_directors_kb(page=1)) 
    



@command_router.callback_query(F.data.startswith('movie_'))
async def movie_detail_handler(callback: CallbackQuery):
    movie_id = callback.data.split('_')[1] 
    movie = await get_movie_by_id(movie_id)
    album = MediaGroupBuilder(caption=f'Название: {movie.title}\n'
                                        f'Год выпуска: {movie.release_date}\n'
                                        f'Описание: {movie.description}\n'
                                        f'Страна: {movie.country}\n'
                                        f'Возрастное ограничение: {movie.age_limit}')
    
    if movie.poster.startswith('http') or movie.poster.startswith('https'):
        album.add_photo(media=URLInputFile(movie.poster)) 
    elif movie.poster.startswith('AgA'):
        album.add_photo(media=movie.poster) 
    else:
        album.add_photo(media=FSInputFile(movie.poster))

    if movie.trailer.startswith('http') or movie.trailer.startswith('https'):
        album.add_video(media=URLInputFile(movie.trailer))  
    elif movie.trailer.startswith('BAA'):
        album.add_video(medis=movie.trailer) 
    else:
        album.add_video(media=FSInputFile(movie.trailer)) 
    await callback.message.answer_media_group(media=album.build())

    await callback.message.answer_media_group(media=album.build()) 


@command_router.callback_query(F.data.startswith('series_'))
async def series_detail_handler(callback: CallbackQuery):
    series_id = callback.data.split('_')[1] 
    series = await get_series_by_id(series_id)  
    album = MediaGroupBuilder(caption=f'Название: {series.title}\n'
                                        f'Год выпуска: {series.release_date}\n'
                                        f'Сезоны: {series.seasons}\n'
                                        f'Описание: {series.description}\n'
                                        f'Страна: {series.country}\n'
                                        f'Возрастное ограничение: {series.age_limit}')

    if series.poster.startswith('http') or series.poster.startswith('AgA'):
        album.add_photo(media=series.poster) 
    else:
        album.add_photo(media=FSInputFile(series.poster)) 
    if series.trailer.startswith('http') or series.trailer.startswith('BAA'):
        album.add_video(media=series.trailer) 
    else:
        album.add_video(media=FSInputFile(series.trailer)) 
    await callback.message.answer_media_group(media=album.build())


@command_router.callback_query(F.data.startswith('actors_')) 
async def actors_detail_handler(callback: CallbackQuery):
    actors_id = callback.data.split('_')[1] 
    actors = await get_actors_by_id(actors_id)  
    album = MediaGroupBuilder(caption=f'Имя: {actors.first_name}\n'
                                        f'Фамилия: {actors.last_name}\n'
                                        f'Дата рождения: {actors.birth_day}\n'
                                        f'Об актёре: {actors.description}\n')
                                        

    if actors.image.startswith('http') or actors.image.startswith('AgA'):
        album.add_photo(media=actors.image) 
    else:
        album.add_photo(media=FSInputFile(actors.image)) 
    await callback.message.answer_media_group(media=album.build())


@command_router.callback_query(F.data.startswith('directors_'))
async def directors_detail_handler(callback: CallbackQuery):
    directors_id = callback.data.split('_')[1]  
    directors = await get_directors_by_id(directors_id)  
    album = MediaGroupBuilder(caption=f'Имя: {directors.first_name}\n'
                                        f'Фамилия: {directors.last_name}\n'
                                        f'Дата рождения: {directors.birth_day}\n'
                                        f'О режиссёре: {directors.description}\n') 
                                        

    if directors.image.startswith('http') or directors.image.startswith('AgA'):
        album.add_photo(media=directors.poster) 
    else:
        album.add_photo(media=FSInputFile(directors.image))  
    await callback.message.answer_media_group(media=album.build()) 



@command_router.callback_query(F.data.startswith('genre_'))
async def movie_by_genre_handler(callback: CallbackQuery):
    g_id = callback.data.split('_')[1] 
    await callback.message.answer(f"Фильмы по жанру:", 
        reply_markup=await get_movies_by_genre_kb(g_id))

@command_router.callback_query(F.data.startswith('back_to_genre')) 
async def back_to_genre_handler(callback: CallbackQuery):
    await callback.message.answer('Выберите жанр', reply_markup=await get_genre_kb(page=1))



@command_router.callback_query(F.data.startswith('actor_'))
async def movie_by_actors_handler(callback: CallbackQuery):
    a_id = callback.data.split('_')[1] 
    await callback.message.answer(f"Фильмы с этим актёром:",
        reply_markup=await get_movies_by_actors_kb(a_id))

@command_router.callback_query(F.data.startswith('director_'))
async def movie_by_directors_handler(callback: CallbackQuery):
    d_id = callback.data.split('_')[1] 
    await callback.message.answer(f"Фильмы у этого режиссёра:",
        reply_markup=await get_movies_by_directors_kb(d_id)) 




@command_router.callback_query(F.data.startswith('page_')) 
async def genre_page_handler(callback: CallbackQuery):
    data = callback.data.split('_')[1] 
    id = int(data) 
    await callback.message.edit_reply_markup(reply_markup=await get_genre_kb(page=id))

@command_router.callback_query(F.data.startswith('page2_')) 
async def movie_page_handler(callback: CallbackQuery):
    data = callback.data.split('_')[1] 
    id = int(data) 
    await callback.message.edit_reply_markup(reply_markup=await get_movies_kb(page=id))

@command_router.callback_query(F.data.startswith('page3_')) 
async def series_page_handler(callback: CallbackQuery):
    data = callback.data.split('_')[1] 
    id = int(data) 
    await callback.message.edit_reply_markup(reply_markup=await get_series_kb(page=id))

# @command_router.callback_query(F.data.startswith('page4_')) 
# async def actors_page_handler(callback: CallbackQuery):
#     data = callback.data.split('_')[1] 
#     id = int(data) 
#     await callback.message.edit_reply_markup(reply_markup=await get_actors_kb(page=id))

# @command_router.callback_query(F.data.startswith('page5_')) 
# async def directors_page_handler(callback: CallbackQuery):
#     data = callback.data.split('_')[1] 
#     id = int(data) 
#     await callback.message.edit_reply_markup(reply_markup=await get_directors_kb(page=id))


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


from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State

class FindMovie(StatesGroup):
    title = State()

@command_router.message(F.text == "Search movie/series by its name")
async def find_movie_handler(message: Message, state: FSMContext):
    await message.answer("Введите название фильма/сериала: ")
    await state.set_state(FindMovie.title)

@command_router.message(FindMovie.title)
async def find_movie_handler(message: Message, state: FSMContext):
    search_title = message.text.strip()
    if search_title: 
        movies = await get_movies_by_title(search_title)
        if movies:       
            kb = InlineKeyboardBuilder() 
            for m in movies:
                kb.add(InlineKeyboardButton(text=m.title, 
                    callback_data=f"movie_{m.id}"))
            await message.answer("Фильм/сериал по вашему запросу: ",
                reply_markup=kb.adjust(2).as_markup())  
        else: 
            await message.answer("Фильм/сериал не найден!")
    else:
        await message.answer("Введите название фильма/сериала: ")  
    await state.clear()



class FindActors(StatesGroup):
    name = State() 

@command_router.message(F.text == "Search actors")
async def find_actors_handler(message: Message, state: FSMContext):
    await message.answer("Введите имя актёра: ") 
    await state.set_state(FindActors.name) 

@command_router.message(FindActors.name) 
async def find_actors_handler(message: Message, state: FSMContext):
    search_name = message.text.strip()
    if search_name:  
        actors = await get_actors_by_name(search_name) 
        if actors:        
            kb = InlineKeyboardBuilder() 
            for a in actors: 
                kb.add(InlineKeyboardButton(text=f"{a.first_name} {a.last_name}", 
                    callback_data=f"actor_{a.id}")) 
            await message.answer("Актёр по вашему запросу: ",
                reply_markup=kb.adjust(2).as_markup())  
        else: 
            await message.answer("Актёр не найден!")
    else:
        await message.answer("Введите имя актёра: ")  
    await state.clear()



class FindDirectors(StatesGroup):
    name = State() 

@command_router.message(F.text == "Search directors")
async def find_directors_handler(message: Message, state: FSMContext):
    await message.answer("Введите имя режиссёра: ") 
    await state.set_state(FindDirectors.name) 

@command_router.message(FindDirectors.name) 
async def finddireactors_handler(message: Message, state: FSMContext):
    search_name = message.text.strip()
    if search_name:  
        directors = await get_directors_by_name(search_name) 
        if directors:        
            kb = InlineKeyboardBuilder() 
            for d in directors: 
                kb.add(InlineKeyboardButton(text=f"{d.first_name} {d.last_name}", 
                    callback_data=f"director_{d.id}")) 
            await message.answer("Режиссёр по вашему запросу: ",
                reply_markup=kb.adjust(2).as_markup())  
        else: 
            await message.answer("Режиссёр не найден!")
    else:
        await message.answer("Введите имя режиссёра: ")  
    await state.clear()  




 


