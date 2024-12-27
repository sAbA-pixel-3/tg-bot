from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, KeyboardButton, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder
from databases.querysets import *



# Common Button
kb = ReplyKeyboardMarkup(keyboard=[ 
    [KeyboardButton(text='Movie catalog')], 
    [KeyboardButton(text='Series catalog')],
    [KeyboardButton(text='Genre catalog')],
    [KeyboardButton(text='Actors')],
    [KeyboardButton(text='Search actors')],
    [KeyboardButton(text='Directors')], 
    [KeyboardButton(text='Search directors')],
    [KeyboardButton(text='Search movie/series by its name')] 
], resize_keyboard=True, input_field_placeholder="Choose below:")



###
PAGE_SIZE = 2
async def get_movies_kb(page): 
    offset = (page - 1) * PAGE_SIZE 
    kb = InlineKeyboardBuilder()
    movies = await all_movies(offset=offset,limit=PAGE_SIZE)
    for movie in movies:
        kb.add(InlineKeyboardButton(text=movie.title,
            callback_data=f"movie_{movie.id}")) 
        
    if page > 1:
        kb.add(InlineKeyboardButton(text='<', callback_data=f"page2_{page-1}")) 
    if len(movies) == PAGE_SIZE: 
        kb.add(InlineKeyboardButton(text='>', callback_data=f"page2_{page+1}"))

    return kb.adjust(2).as_markup()

async def get_movies_kb_admin():
    kb = InlineKeyboardBuilder()
    movies = await all_movies2() 
    for movie in movies:
        kb.add(InlineKeyboardButton(text=movie.title,
            callback_data=f"movie2_admin_{movie.id}")) 
    return kb.adjust(2).as_markup() 
###
PAGE_SIZE = 2
async def get_series_kb(page):
    offset = (page - 1) * PAGE_SIZE
    kb = InlineKeyboardBuilder()
    series = await all_series(offset=offset,limit=PAGE_SIZE) 
    for serie in series: 
        kb.add(InlineKeyboardButton(text=serie.title, 
            callback_data=f"series_{serie.id}"))

    if page > 1:
        kb.add(InlineKeyboardButton(text='<', callback_data=f"page3_{page-1}")) 
    if len(series) == PAGE_SIZE:  
        kb.add(InlineKeyboardButton(text='>', callback_data=f"page3_{page+1}")) 

    return kb.adjust(2).as_markup()

async def get_series_kb_admin():
    kb = InlineKeyboardBuilder()
    series = await all_series() 
    for serie in series: 
        kb.add(InlineKeyboardButton(text=serie.title, 
            callback_data=f"series2_admin_{serie.id}")) 
    return kb.adjust(2).as_markup() 
### 
PAGE_SIZE = 2
async def get_genre_kb(page):
    offset = (page - 1) * PAGE_SIZE
    kb = InlineKeyboardBuilder() 
    genres = await all_genre(offset=offset,limit=PAGE_SIZE)  
    for genre in genres: 
        kb.add(InlineKeyboardButton(text=genre.name, 
            callback_data=f"genre_{genre.id}")) 

    if page > 1:
        kb.add(InlineKeyboardButton(text='<', callback_data=f"page_{page-1}")) 
    if len(genres) == PAGE_SIZE: 
        kb.add(InlineKeyboardButton(text='>', callback_data=f"page_{page+1}")) 

    return kb.adjust(2).as_markup()

async def get_genre_kb_admin():
    kb = InlineKeyboardBuilder()
    genres = await all_genre2() 
    for genre in genres: 
        kb.add(InlineKeyboardButton(text=genre.name, 
            callback_data=f"genre2_admin_{genre.id}")) 
    return kb.adjust(3).as_markup()
###
async def get_actors_kb():
    kb = InlineKeyboardBuilder()
    actors = await all_actors() 
    for actor in actors: 
        kb.add(InlineKeyboardButton(text=f"{actor.first_name} {actor.last_name}", 
            callback_data=f"actors_{actor.id}"))    
    return kb.adjust(2).as_markup()

async def get_actors_kb_admin():
    kb = InlineKeyboardBuilder()
    actors = await all_actors()  
    for actor in actors:  
        kb.add(InlineKeyboardButton(text=f"{actor.first_name} {actor.last_name}", 
            callback_data=f"actors2_admin_{actor.id}"))   
    return kb.adjust(2).as_markup()
###

async def get_directors_kb():
    kb = InlineKeyboardBuilder()
    directors = await all_directors() 
    for director in directors: 
        kb.add(InlineKeyboardButton(text=f"{director.first_name} {director.last_name}", 
            callback_data=f"directors_{director.id}"))   
    return kb.adjust(2).as_markup() 



async def get_movies_by_genre_kb(genre_id):
    kb = InlineKeyboardBuilder()
    movies = await get_movie_by_genre(genre_id)
    for movie in movies:
        kb.add(InlineKeyboardButton(text=movie.title,
            callback_data=f"movie_{movie.id}")) 
    kb.add(InlineKeyboardButton(text='Назад', callback_data=f"back_to_genre"))
    return kb.adjust(2).as_markup() 

async def get_actores_kb():
    kb = InlineKeyboardBuilder()
    actores = await all_actors() 
    for actors in actores: 
        kb.add(InlineKeyboardButton(text=f"{actors.first_name} {actors.last_name}", 
            callback_data=f"actor_{actors.id}"))    
    return kb.adjust(2).as_markup()
# second get_actores_kb FOR THE get_movies_by_actors_kb
async def get_movies_by_actors_kb(actor_id):
    kb = InlineKeyboardBuilder()
    movies = await get_movie_by_actor(actor_id)  
    for movie in movies: 
        kb.add(InlineKeyboardButton(text=movie.title, 
            callback_data=f"movie_{movie.id}"))    
    return kb.adjust(2).as_markup() 

async def get_directores_kb():
    kb = InlineKeyboardBuilder()
    directores = await all_directors() 
    for directors in directores: 
        kb.add(InlineKeyboardButton(text=f"{directors.first_name} {directors.last_name}", 
            callback_data=f"director_{directors.id}"))   
    return kb.adjust(2).as_markup()
# second get_directores_kb FOR THE get_movies_by_directors_kb
async def get_movies_by_directors_kb(director_id):
    kb = InlineKeyboardBuilder()
    movies = await get_movie_by_director(director_id)  
    for movie in movies: 
        kb.add(InlineKeyboardButton(text=movie.title, 
            callback_data=f"movie_{movie.id}"))    
    return kb.adjust(2).as_markup() 



async def back_kb(): 
    kb = InlineKeyboardBuilder()
    kb.add(InlineKeyboardButton(text='Назад', callback_data=f"back_to_genre"))
    return kb.adjust(2).as_markup() 



# async def get_movies_by_title_kb(title):
#     kb = InlineKeyboardBuilder()
#     movies = await get_movies_by_title(title)
#     if movies:
#         for m in movies:
#             kb.add(InlineKeyboardButton(text=m.tite, callback_data=f"movie_{m.id}"))
#             return kb.adjust(2).as_markup()
    





# inLine Buttons
# ikb = InlineKeyboardMarkup(inline_keyboard=[
#     [InlineKeyboardButton(text='Deadpool', callback_data='hello')],
#     [InlineKeyboardButton(text="Interstellar", callback_data='bye')] 
# ])

# ikb1 = InlineKeyboardMarkup(inline_keyboard=[
#     [InlineKeyboardButton(text='Fantasy', callback_data='hello')],
#     [InlineKeyboardButton(text="Horror", callback_data='bye')],
#     [InlineKeyboardButton(text="Detective", callback_data='bye')] 
# ])

# ikb2 = InlineKeyboardMarkup(inline_keyboard=[
#     [InlineKeyboardButton(text='There should be a list of all movies!', callback_data='hello')] 
# ])

# ikb3 = InlineKeyboardMarkup(inline_keyboard=[
#     [InlineKeyboardButton(text='Friends', callback_data='hello')],
#     [InlineKeyboardButton(text="Game of Thrones", callback_data='bye')],
#     [InlineKeyboardButton(text="Stranger Things", callback_data='bye')] 
# ])

# ikb4 = InlineKeyboardMarkup(inline_keyboard=[
#     [InlineKeyboardButton(text='Dwayne Johnson', callback_data='hello')],
#     [InlineKeyboardButton(text="Leonardo DiCaprio", callback_data='bye')],
#     [InlineKeyboardButton(text="Ryan Gosling", callback_data='bye')] 
# ])

