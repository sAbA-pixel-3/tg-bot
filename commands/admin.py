from aiogram import Router
from aiogram.filters import Command, CommandStart, StateFilter
from aiogram.types import Message, CallbackQuery, FSInputFile
from aiogram.utils.media_group import MediaGroupBuilder
from aiogram import F 
from commands.keyboards_tg import *
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from config import ADMIN_ID
from databases.querysets import *


admin_router = Router() 

class AddMovie(StatesGroup):
    add_m_title = State()
    add_m_poster = State() 
    add_m_release_date = State()
    add_m_description = State()
    add_m_country = State()
    add_m_age_limit = State()
    add_m_trailer = State()
    add_m_url = State() 


async def check_admin(message:Message):
    return message.from_user.id == ADMIN_ID

# ADDING MOVIES     
@admin_router.message(Command("add_movie"))
async def add_movie_admin(message: Message, state: FSMContext):
    if not await check_admin(message): 
        await message.answer("Это команда только для админа!") 
        return

    await message.answer("Введите название фильма: ")
    await state.set_state(AddMovie.add_m_title) 
@admin_router.message(AddMovie.add_m_title)
async def add_movie_title(message: Message, state: FSMContext):
    await state.update_data(add_m_title=message.text)

    await message.answer("Отправьте постер для фильма: ")
    await state.set_state(AddMovie.add_m_poster) 
@admin_router.message(AddMovie.add_m_poster) 
async def add_movie_poster(message: Message, state: FSMContext):
    await state.update_data(add_m_poster=message.photo[0].file_id)

    await message.answer("Введите год выпуска фильма: гг-мм-дд")
    await state.set_state(AddMovie.add_m_release_date) 
@admin_router.message(AddMovie.add_m_release_date)  
async def add_movie_release_date(message: Message, state: FSMContext):
    await state.update_data(add_m_release_date=message.text)

    await message.answer("Введите описание фильма: ")
    await state.set_state(AddMovie.add_m_description) 
@admin_router.message(AddMovie.add_m_description) 
async def add_movie_description(message: Message, state: FSMContext):
    await state.update_data(add_m_description=message.text)

    await message.answer("Введите страну: ")
    await state.set_state(AddMovie.add_m_country)
@admin_router.message(AddMovie.add_m_country) 
async def add_movie_country(message: Message, state: FSMContext):
    await state.update_data(add_m_country=message.text)

    await message.answer("Введите возрастное ограничение: ")
    await state.set_state(AddMovie.add_m_age_limit)
@admin_router.message(AddMovie.add_m_age_limit)  
async def add_movie_age_limit(message: Message, state: FSMContext):
    await state.update_data(add_m_age_limit=int(message.text))

    await message.answer("Введите трейлер фильма: ")
    await state.set_state(AddMovie.add_m_trailer)
@admin_router.message(AddMovie.add_m_trailer)  
async def add_movie_trailer(message: Message, state: FSMContext):
    await state.update_data(add_m_trailer=message.video.file_id) 

    await message.answer("Отправьте ссылку фильма: ") 
    await state.set_state(AddMovie.add_m_url)
@admin_router.message(AddMovie.add_m_url)
async def add_movie_url(message: Message, state: FSMContext):
    await add_url(message.text) 
    urls = await get_url()
    urs = []
    for url in urls:
        urs.append(url.id) 
    url_id = urs[-1] 
    await state.update_data(add_m_url=url_id)  
    data = await state.get_data()
    movie = Movies(
        title=data['add_m_title'],
        poster=data['add_m_poster'],
        release_date=data['add_m_release_date'],
        description=data['add_m_description'],
        country=data['add_m_country'],
        age_limit=data['add_m_age_limit'],
        trailer=data['add_m_trailer'],
        url_id=data['add_m_url'])
    
    await add_movies(movie)
    await message.answer(f'Название: {data.get("add_m_title")}\n'
                         f'Постер: {data.get("add_m_poster")}\n'
                         f'Год выпуска: {data.get("add_m_release_date")}\n'
                         f'Описание: {data.get("add_m_description")}\n'
                         f'Страна: {data.get("add_m_country")}\n'
                         f'Возрастное ограничение: {data.get("add_m_age_limit")}\n'
                         f'Трейлер: {data.get("add_m_trailer")}\n'
                         f'Ссылка: {message.text}\n'
                         f'Фильм добавлен')
    await state.clear() 



# ADDING SERIES
class AddSeries(StatesGroup):
    add_s_title = State()
    add_s_poster = State()
    add_s_seasons = State()  
    add_s_release_date = State()
    add_s_description = State()
    add_s_country = State() 
    add_s_age_limit = State()
    add_s_trailer = State()
    add_s_url = State() 

@admin_router.message(Command("add_series")) 
async def add_series_admin(message: Message, state: FSMContext):
    if not await check_admin(message):
        await message.answer("Это команда только для админа!") 
        return 
    await message.answer("Введите название сериала: ") 
    await state.set_state(AddSeries.add_s_title)  
@admin_router.message(AddSeries.add_s_title) 
async def add_series_title(message: Message, state: FSMContext):
    await state.update_data(add_s_title=message.text) 

    await message.answer("Отправьте постер для сериала: ")
    await state.set_state(AddSeries.add_s_poster) 
@admin_router.message(AddSeries.add_s_poster) 
async def add_series_poster(message: Message, state: FSMContext):
    await state.update_data(add_s_poster=message.photo[0].file_id)

    await message.answer("Сколько сезонов: ")
    await state.set_state(AddSeries.add_s_seasons)
@admin_router.message(AddSeries.add_s_seasons)  
async def add_series_seasons(message: Message, state: FSMContext):
    await state.update_data(add_s_seasons=int(message.text))

    await message.answer("Введите год выпуска сериала: гг-мм-дд")
    await state.set_state(AddSeries.add_s_release_date) 
@admin_router.message(AddSeries.add_s_release_date)  
async def add_series_release_date(message: Message, state: FSMContext):
    await state.update_data(add_s_release_date=message.text)

    await message.answer("Введите описание сериала: ")
    await state.set_state(AddSeries.add_s_description) 
@admin_router.message(AddSeries.add_s_description) 
async def add_series_description(message: Message, state: FSMContext):
    await state.update_data(add_s_description=message.text)

    await message.answer("Введите страну: ")
    await state.set_state(AddSeries.add_s_country)
@admin_router.message(AddSeries.add_s_country) 
async def add_series_country(message: Message, state: FSMContext):
    await state.update_data(add_s_country=message.text)

    await message.answer("Введите возрастное ограничение: ")
    await state.set_state(AddSeries.add_s_age_limit)
@admin_router.message(AddSeries.add_s_age_limit)  
async def add_series_age_limit(message: Message, state: FSMContext):
    await state.update_data(add_s_age_limit=int(message.text))

    await message.answer("Введите трейлер сериала: ")
    await state.set_state(AddSeries.add_s_trailer)
@admin_router.message(AddSeries.add_s_trailer)  
async def add_series_trailer(message: Message, state: FSMContext):
    await state.update_data(add_s_trailer=message.video.file_id) 

    await message.answer("Отправьте ссылку сериала: ") 
    await state.set_state(AddSeries.add_s_url)
@admin_router.message(AddSeries.add_s_url)
async def add_series_url(message: Message, state: FSMContext):
    await add_url(message.text) 
    urls = await get_url() 
    urs = []
    for url in urls:
        urs.append(url.id) 
    url_id = urs[-1] 
    await state.update_data(add_s_url=url_id) 
    
    data = await state.get_data()
    series = Series( 
        title=data['add_s_title'],
        poster=data['add_s_poster'],
        seasons=data['add_s_seasons'], 
        release_date=data['add_s_release_date'],
        description=data['add_s_description'],
        country=data['add_s_country'],
        age_limit=data['add_s_age_limit'],
        trailer=data['add_s_trailer'],
        url_id=data['add_s_url'])
    
    await add_series(series) 
    await message.answer(f'Название: {data.get("add_s_title")}\n'
                         f'Постер: {data.get("add_s_poster")}\n'
                         f'Сезоны: {data.get("add_s_seasons")}\n' 
                         f'Год выпуска: {data.get("add_s_release_date")}\n'
                         f'Описание: {data.get("add_s_description")}\n'
                         f'Страна: {data.get("add_s_country")}\n'
                         f'Возрастное ограничение: {data.get("add_s_age_limit")}\n'
                         f'Трейлер: {data.get("add_s_trailer")}\n'
                         f'Ссылка: {message.text}\n' 
                         f'Сериал добавлен')
    await state.clear()




# ADDING ACTORS
class AddActors(StatesGroup):
    add_a_first_name = State()
    add_a_last_name = State()
    add_a_image = State()
    add_a_birth_day = State()
    add_a_description = State()

@admin_router.message(Command("add_actors"))  
async def add_actors_admin(message: Message, state: FSMContext):
    if not await check_admin(message):
        await message.answer("Это команда только для админа!") 
        return 
    await message.answer("Введите имя актёра: ") 
    await state.set_state(AddActors.add_a_first_name)  
@admin_router.message(AddActors.add_a_first_name) 
async def add_actors_first_name(message: Message, state: FSMContext):
    await state.update_data(add_a_first_name=message.text) 

    await message.answer("Введите фамилию актёра: ")
    await state.set_state(AddActors.add_a_last_name) 
@admin_router.message(AddActors.add_a_last_name)  
async def add_actors_last_name(message: Message, state: FSMContext):
    await state.update_data(add_a_last_name=message.text) 

    await message.answer("Вставьте фото актёра: ")
    await state.set_state(AddActors.add_a_image) 
@admin_router.message(AddActors.add_a_image)   
async def add_actors_image(message: Message, state: FSMContext):
    await state.update_data(add_a_image=message.photo[0].file_id) 

    await message.answer("Введите год рождения актёра: гг-мм-дд")
    await state.set_state(AddActors.add_a_birth_day)  
@admin_router.message(AddActors.add_a_birth_day)   
async def add_actors_birth_day(message: Message, state: FSMContext):
    await state.update_data(add_a_birth_day=message.text) 

    await message.answer("Опишите актёра: ")
    await state.set_state(AddActors.add_a_description)  
@admin_router.message(AddActors.add_a_description) 
async def add_actors_description(message: Message, state: FSMContext):
    await state.update_data(add_a_description=message.text) 

    data = await state.get_data()
    actors = Actors( 
        first_name=data['add_a_first_name'],
        last_name=data['add_a_last_name'],
        image=data['add_a_image'], 
        birth_day=data['add_a_birth_day'],
        description=data['add_a_description'])  
    
    await add_actors(actors)  
    await message.answer(f'Имя актёра: {data.get("add_a_first_name")}\n'
                         f'Фамилия актёра: {data.get("add_a_last_name")}\n'
                         f'Фото актёра: {data.get("add_a_image")}\n' 
                         f'Дата рождения актёра: {data.get("add_a_birth_day")}\n'
                         f'Характеристики актёра: {data.get("add_a_description")}\n' 
                         f'Актёр добавлен')
    await state.clear() 



# ADDING DIRECTORS
class AddDirectors(StatesGroup):
    add_d_first_name = State()
    add_d_last_name = State()
    add_d_image = State()
    add_d_birth_day = State()
    add_d_description = State()

@admin_router.message(Command("add_directors"))  
async def add_directors_admin(message: Message, state: FSMContext):
    if not await check_admin(message):
        await message.answer("Это команда только для админа!") 
        return 
    await message.answer("Введите имя режиссёра: ") 
    await state.set_state(AddDirectors.add_d_first_name)  
@admin_router.message(AddDirectors.add_d_first_name) 
async def add_directors_first_name(message: Message, state: FSMContext):
    await state.update_data(add_d_first_name=message.text) 

    await message.answer("Введите фамилию режиссёра: ")
    await state.set_state(AddDirectors.add_d_last_name) 
@admin_router.message(AddDirectors.add_d_last_name)  
async def add_directors_last_name(message: Message, state: FSMContext):
    await state.update_data(add_d_last_name=message.text) 

    await message.answer("Вставьте фото режиссёра: ")
    await state.set_state(AddDirectors.add_d_image) 
@admin_router.message(AddDirectors.add_d_image)   
async def add_directors_image(message: Message, state: FSMContext):
    await state.update_data(add_d_image=message.photo[0].file_id) 

    await message.answer("Введите год рождения режиссёра: гг-мм-дд")
    await state.set_state(AddDirectors.add_d_birth_day)  
@admin_router.message(AddDirectors.add_d_birth_day)   
async def add_directors_birth_day(message: Message, state: FSMContext):
    await state.update_data(add_d_birth_day=message.text) 

    await message.answer("Опишите режиссёра: ")
    await state.set_state(AddDirectors.add_d_description)  
@admin_router.message(AddDirectors.add_d_description) 
async def add_directors_description(message: Message, state: FSMContext):
    await state.update_data(add_d_description=message.text) 

    data = await state.get_data()
    directors = Directors(  
        first_name=data['add_d_first_name'],
        last_name=data['add_d_last_name'],
        image=data['add_d_image'], 
        birth_day=data['add_d_birth_day'],
        description=data['add_d_description'])  
    
    await add_directors(directors)   
    await message.answer(f'Имя режиссёра: {data.get("add_d_first_name")}\n'
                         f'Фамилия режиссёра: {data.get("add_d_last_name")}\n'
                         f'Фото режиссёра: {data.get("add_d_image")}\n' 
                         f'Дата рождения режиссёра: {data.get("add_d_birth_day")}\n'
                         f'Характеристики режиссёра: {data.get("add_d_description")}\n' 
                         f'Режиссёр добавлен')
    await state.clear() 



# ADDING GENRES
class AddGenre(StatesGroup):
    add_g_name = State()
    add_g_description = State()

@admin_router.message(Command("add_genre"))  
async def add_genre_admin(message: Message, state: FSMContext):
    if not await check_admin(message):
        await message.answer("Это команда только для админа!") 
        return 
    await message.answer("Введите название жанра: ") 
    await state.set_state(AddGenre.add_g_name)   
@admin_router.message(AddGenre.add_g_name)  
async def add_genre_name(message: Message, state: FSMContext):
    await state.update_data(add_g_name=message.text)  

    await message.answer("Дайте короткое описание жанра: ")
    await state.set_state(AddGenre.add_g_description)  
@admin_router.message(AddGenre.add_g_description)  
async def add_genre_description(message: Message, state: FSMContext):
    await state.update_data(add_g_description=message.text)

    data = await state.get_data()
    genre = Genre(   
        name=data['add_g_name'],
        description=data['add_g_description'])   
    
    await add_genre(genre)    
    await message.answer(f'Название жанра: {data.get("add_g_name")}\n'
                         f'Описание жанра: {data.get("add_g_description")}\n' 
                         f'Жанр добавлен')
    await state.clear() 



# CONNECTING ADDED THINGS WITH EACH OTHER
class MovieToGenre(StatesGroup):
    choice_movie = State()
    choice_genre = State()

from commands.keyboards_tg import *

@admin_router.message(Command("mg_rel"))  
async def choice_movie_admin(message: Message, state: FSMContext):
    if not await check_admin(message):
        await message.answer("Это команда только для админа!") 
        return 
    await message.answer("Выберите фильм: ", reply_markup= await get_movies_kb_admin())  
    await state.set_state(MovieToGenre.choice_movie) 

@admin_router.callback_query(MovieToGenre.choice_movie) 
async def choice_movie_admin2(callback: CallbackQuery, state: FSMContext):
    await state.update_data(choice_movie=callback.data.split('_')[2]) 
    await callback.message.answer("Выберите жанр: ", reply_markup= await get_genre_kb_admin()) 
    await state.set_state(MovieToGenre.choice_genre)

@admin_router.callback_query(MovieToGenre.choice_genre)  
async def choice_genre_admin2(callback: CallbackQuery, state: FSMContext):
    await state.update_data(choice_genre=callback.data.split('_')[2])
    data = await state.get_data()
    # try:
    await add_movie_genres(data['choice_movie'], data['choice_genre'])
    await callback.message.answer(f"Фильм {data['choice_movie']} добавлен в жанр {data['choice_genre']}")
    # except Exception as e: 
    #     await callback.message.answer(f"Этот фильм и жанр уже имеют отношение")
    await state.clear() 


class MovieToActors(StatesGroup):
    choice_movie2 = State()
    choice_actors = State()

@admin_router.message(Command("ma_rel"))  
async def choice_movie2_admin(message: Message, state: FSMContext):
    if not await check_admin(message):
        await message.answer("Это команда только для админа!") 
        return
    await message.answer("Выберите фильм: ", reply_markup= await get_movies_kb_admin())  
    await state.set_state(MovieToActors.choice_movie2)  

@admin_router.callback_query(MovieToActors.choice_movie2)  
async def choice_movie2_admin2(callback: CallbackQuery, state: FSMContext):
    await state.update_data(choice_movie2=callback.data.split('_')[2]) 
    await callback.message.answer("Выберите актёра: ", reply_markup= await get_actors_kb_admin()) 
    await state.set_state(MovieToActors.choice_actors) 

@admin_router.callback_query(MovieToActors.choice_actors)   
async def choice_actors_admin2(callback: CallbackQuery, state: FSMContext):
    await state.update_data(choice_actors=callback.data.split('_')[2])
    data = await state.get_data()
    # try:  
    await add_movie_actors(data['choice_movie2'], data['choice_actors'])
    await callback.message.answer(f"Фильм {data['choice_movie2']} добавлен с актёром {data['choice_actors']}")
    # except Exception as e: 
    #     await callback.message.answer(f"Этот фильм и актёр уже имеют отношение")
    await state.clear()  


class SeriesToGenre(StatesGroup):
    choice_series = State() 
    choice_genre2 = State()

@admin_router.message(Command("sg_rel"))  
async def choice_series_admin(message: Message, state: FSMContext):
    if not await check_admin(message):
        await message.answer("Это команда только для админа!") 
        return 
    await message.answer("Выберите сериал: ", reply_markup= await get_series_kb_admin())  
    await state.set_state(SeriesToGenre.choice_series)  

@admin_router.callback_query(SeriesToGenre.choice_series)  
async def choice_series_admin2(callback: CallbackQuery, state: FSMContext):
    await state.update_data(choice_series=callback.data.split('_')[2]) 
    await callback.message.answer("Выберите жанр: ", reply_markup= await get_genre_kb_admin()) 
    await state.set_state(SeriesToGenre.choice_genre2)

@admin_router.callback_query(SeriesToGenre.choice_genre2)   
async def choice_genre2_admin2(callback: CallbackQuery, state: FSMContext):
    await state.update_data(choice_genre2=callback.data.split('_')[2])
    data = await state.get_data() 
    # try:
    await add_series_genres(data['choice_series'], data['choice_genre2'])
    await callback.message.answer(f"Сериал {data['choice_series']} добавлен в жанр {data['choice_genre2']}")
    # except Exception as e: 
    #     await callback.message.answer(f"Этот сериал и жанр уже имеют отношение")
    await state.clear()


class SeriesToActors(StatesGroup):
    choice_series2 = State()
    choice_actors2 = State()

@admin_router.message(Command("sa_rel"))  
async def choice_series2_admin(message: Message, state: FSMContext):
    if not await check_admin(message):
        await message.answer("Это команда только для админа!") 
        return
    await message.answer("Выберите сериал: ", reply_markup= await get_series_kb_admin())  
    await state.set_state(SeriesToActors.choice_series2)   

@admin_router.callback_query(SeriesToActors.choice_series2)  
async def choice_series2_admin2(callback: CallbackQuery, state: FSMContext):
    await state.update_data(choice_series2=callback.data.split('_')[2]) 
    await callback.message.answer("Выберите актёра: ", reply_markup= await get_actors_kb_admin()) 
    await state.set_state(SeriesToActors.choice_actors2)  

@admin_router.callback_query(SeriesToActors.choice_actors2)    
async def choice_actors2_admin2(callback: CallbackQuery, state: FSMContext):
    await state.update_data(choice_actors2=callback.data.split('_')[2])
    data = await state.get_data() 
    # try:  
    await add_series_actors(data['choice_series2'], data['choice_actors2']) 
    await callback.message.answer(f"Сериал {data['choice_series2']} добавлен с актёром {data['choice_actors2']}")
    # except Exception as e: 
    #     await callback.message.answer(f"Этот сериал и актёр уже имеют отношение")
    await state.clear() 