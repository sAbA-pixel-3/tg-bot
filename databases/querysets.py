from databases.models import *
from sqlalchemy import select, update

# url, actors, direc, mov, ser


async def add_genre(genre): 
    async with async_session() as session:
        # genre = Genre(name="Fantasy", description="It's beatiuful but painful to look at")
        # genre1 = Genre(name="Fiction", description="It's not real, but still fascinating")
        # genre2 = Genre(name="Science", description="You can learn a lot with this")
        # genre3 = Genre(name="Comedy", description="Laugh all you want")
        session.add(genre) 
        await session.commit()  

async def add_url(url): 
    async with async_session() as session:
        # url = Url(url="https://www.random.org/")
        url1 = Url(url=url) 
        # url2 = Url(url="https://www.boredpanda.com/")
        session.add(url1)
        session.refresh(url1) 
        await session.commit() 

async def add_actors(actors): 
    async with async_session() as session:
        # actors = Actors(image="images\dwayne.png", first_name="Dwayne", last_name="Johnson", birth_day="1985-08-03", description="Very skilleed and dedicated")
        # actors1 = Actors(image="images\DiCaprio.png", first_name="Leonardo", last_name="DiCaprio", birth_day="1985-12-12", description="Handsome pal")
        # actors2 = Actors(image="images\Streep.webp", first_name="Meryl", last_name="Streep", birth_day="1982-04-26", description="Pretty and gourgeous")
        session.add(actors) 
        await session.commit()

async def add_directors(directors):
    async with async_session() as session:
        # directors = Directors(image="images\tarantino.png", first_name="Quentin", last_name="Tarantino", birth_day="1966-03-08", description="Cant't descripe enough")
        # directors1 = Directors(image="images\Steven.jpg", first_name="Steven", last_name="Spielberg", birth_day="1966-09-23", description="Talanted guy with mustache")
        # directors2 = Directors(image="images\Martin.jpg", first_name="Martin", last_name="Scorsese", birth_day="1966-05-13", description="Funny one for all of us")
        session.add(directors)    
        await session.commit()

from scrap.parsing import parsing_main
async def add_movies():
    movie = parsing_main()
    async with async_session() as session:
        for m in movie:
            movies = Movies(poster=m['image'],
                             title=m['title'], 
                             release_date=m['release_date'], 
                             description=m['description'], 
                             country=m['country'],
                             age_limit=m['age_limit'], 
                             trailer=m['trailer'], 
                             url_id=m['url']) 
            session.add(movies)
        await session.commit()


async def add_series(series): 
    async with async_session() as session:
        # series = Series(poster="images\ST.jpg", title="Stranger Things", seasons=4, release_date="2016-12-22", description="Was happy to hear, but not watch", country="USA", age_limit=18, trailer="images\ST.mp4", url_id=1)
        # series1 = Series(poster="images\GOT.jpg", title="Game of Thrones", seasons=3, release_date="2011-09-29", description="Never watched it actually", country="USA", age_limit=18, trailer="images\GOT.mp4", url_id=2)
        # series2 = Series(poster="images\Friends.jpg", title="Friends", seasons=7, release_date="1994-11-11", description="Legends never die", country="USA", age_limit=18, trailer="images\Friends.mp4", url_id=3)  
        session.add(series)       
        await session.commit()



# delete    
# async def delete_movie(movie_id):
#     async with async_session() as session:
#         movie = await session.sacalar(select(Movies).where(Movies.id == movie_id))
#         await session.delete(movie)
#         await session.commit() 




async def get_movie_by_id(movie_id):
    async with async_session() as session:
        result = await session.scalar(select(Movies).where(Movies.id == movie_id)) 
        return result   

async def get_series_by_id(series_id):
    async with async_session() as session:
        result = await session.scalar(select(Series).where(Series.id == series_id)) 
        return result
    
async def get_actors_by_id(actors_id):
    async with async_session() as session:
        result = await session.scalar(select(Actors).where(Actors.id == actors_id)) 
        return result
    
async def get_directors_by_id(directors_id):
    async with async_session() as session:
        result = await session.scalar(select(Directors).where(Directors.id == directors_id)) 
        return result



# CONNECTING MOVIES WITH GENRES SO THAT WHEN WE CLICK ON GENRES OR ACTORS OR DIRECTORS WE GET MOVIES AND SERIES THAT THEY RELATED TO
async def get_movie_by_genre(genre_id):
    async with async_session() as session:
        result_movie = await session.scalars(
            select(Movies).join(movie_genre).where(movie_genre.c.genre_id == genre_id)
        )
        result_series = await session.scalars(
            select(Series).join(series_genre).where(
                series_genre.c.genre_id == genre_id)
        )
        return list(result_movie) + (list(result_series)) 
    
async def get_movie_by_actor(actor_id):
    async with async_session() as session:
        result_movie = await session.scalars(
            select(Movies).join(movie_actors).where(movie_actors.c.actor_id == actor_id) 
        )
        result_series = await session.scalars(
            select(Series).join(series_actors).where(
                series_actors.c.actor_id == actor_id)
        )
        return list(result_movie) + (list(result_series)) 
    
async def get_movie_by_director(director_id):
    async with async_session() as session:
        result_movie = await session.scalars(
            select(Movies).join(movie_directors).where(movie_directors.c.director_id == director_id) 
        )
        result_series = await session.scalars(
            select(Series).join(series_actors).where(
                series_directors.c.director_id == director_id)
        )
        return list(result_movie) + (list(result_series)) 

# many-to-many associations

async def add_movie_actors(m,a):
    async with async_session() as session:
        stmt = movie_actors.insert().values(movie_id=m, actor_id=a) 
        await session.execute(stmt)
        await session.commit()

async def add_movie_directors():
    async with async_session() as session:
        stmt = movie_directors.insert().values(movie_id=3, director_id=3)
        await session.execute(stmt)
        await session.commit()

async def add_movie_genres(m,g):
    async with async_session() as session:
        stmt = movie_genre.insert().values(movie_id=m, genre_id=g) 
        await session.execute(stmt) 
        await session.commit()

async def add_series_actors(s,a): 
    async with async_session() as session:
        stmt = series_actors.insert().values(series_id=s, actor_id=a)  
        await session.execute(stmt) 
        await session.commit()

async def add_series_directors():
    async with async_session() as session:
        stmt = series_directors.insert().values(series_id=4, director_id=2)
        await session.execute(stmt)
        await session.commit()

async def add_series_genres(s,g):
    async with async_session() as session:
        stmt = series_genre.insert().values(series_id=s, genre_id=g)  
        await session.execute(stmt) 
        await session.commit()








# to add to bot like an inline button
async def all_movies(limit, offset):
    async with async_session() as session:
        result = await session.scalars(select(Movies).offset(offset).limit(limit))
        return result.all()

async def all_movies2():
    async with async_session() as session:
        result = await session.scalars(select(Movies))
        return result
    
async def get_url():
    async with async_session() as session:
        result = await session.scalars(select(Url)) 
        return result
    
async def all_series(limit, offset):
    async with async_session() as session:
        result = await session.scalars(select(Series).offset(offset).limit(limit))
        return result.all() 
    
async def all_series2():
    async with async_session() as session:
        result = await session.scalars(select(Series))
        return result

async def all_genre(limit, offset):
    async with async_session() as session:
        result = await session.scalars(select(Genre).offset(offset).limit(limit)) 
        return result.all()
# CREAT ANOTHER all_genre2() FOR get_genre_kb_admin() IN keyboards_tg.py ↓ 
async def all_genre2(): 
    async with async_session() as session:
        result = await session.scalars(select(Genre)) 
        return result 
    
async def all_actors():
    async with async_session() as session:
        result = await session.scalars(select(Actors))
        return result

async def all_directors(): 
    async with async_session() as session:
        result = await session.scalars(select(Directors)) 
        return result
    


# search by MOVIE TITLE 
async def get_movies_by_title(t):
    async with async_session() as session:
        movies = await session.scalars(select(Movies).where(
            Movies.title.ilike(f"%{t}%")))
        series = await session.scalars(select(Series).where(
            Series.title.ilike(f"%{t}%"))) 
        return movies.all() + series.all() 

from sqlalchemy.sql import func ###
async def get_actors_by_name(n):
    async with async_session() as session:
        actors = await session.scalars(select(Actors).where(
            func.concat(Actors.first_name, " ", Actors.last_name).ilike(f"%{n}%")))   
        return actors.all()

async def get_directors_by_name(n):
    async with async_session() as session:
        directors = await session.scalars(select(Directors).where(
            func.concat(Directors.first_name, " ", Directors.last_name).ilike(f"%{n}%")))   
        return directors.all()   
              
         

 


