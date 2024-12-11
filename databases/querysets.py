from databases.models import *
from sqlalchemy import select, update

# url, actors, direc, mov, ser


# async def add_genre():
#     async with async_session() as session:
#         # genre = Genre(name="Fantasy", description="It's beatiuful but painful to look at")
#         # genre1 = Genre(name="Fiction", description="It's not real, but still fascinating")
#         # genre2 = Genre(name="Science", description="You can learn a lot with this")
#         genre3 = Genre(name="Horror", description="It's scary with sound")
#         session.add(genre3) 
#         await session.commit() 

# async def add_url():
#     async with async_session() as session:
#         # url = Url(url="https://www.random.org/")
#         # url1 = Url(url="https://theuselessweb.com/")
#         url2 = Url(url="https://www.boredpanda.com/")
#         session.add(url2)
#         await session.commit() 

# async def add_actors():
#     async with async_session() as session:
#         # actors = Actors(image="images\dwayne.png", first_name="Dwayne", last_name="Johnson", birth_day="1985-08-03", description="Very skilleed and dedicated")
#         # actors1 = Actors(image="images\DiCaprio.png", first_name="Leonardo", last_name="DiCaprio", birth_day="1985-12-12", description="Handsome pal")
#         actors2 = Actors(image="images\Streep.webp", first_name="Meryl", last_name="Streep", birth_day="1982-04-26", description="Pretty and gourgeous")
#         session.add(actors2) 
#         await session.commit()

# async def add_directors():
#     async with async_session() as session:
#         # directors = Directors(image="images\tarantino.png", first_name="Quentin", last_name="Tarantino", birth_day="1966-03-08", description="Cant't descripe enough")
#         # directors1 = Directors(image="images\Steven.jpg", first_name="Steven", last_name="Spielberg", birth_day="1966-09-23", description="Talanted guy with mustache")
#         directors2 = Directors(image="images\Martin.jpg", first_name="Martin", last_name="Scorsese", birth_day="1966-05-13", description="Funny one for all of us")
#         session.add(directors2)   
#         await session.commit()

# async def add_movies():
#     async with async_session() as session:
#         # movies = Movies(poster="images\interstellar.png", title="Interstellar", release_date="2020-07-18", description="Fantastic one to watch", country="USA", age_limit=16, trailer="images\interstellar.mp4", url_id=1)
#         # movies1 = Movies(poster="images\Batman.jpg", title="The Dark Knight", release_date="2008-08-08", description="Heroic acts for justice", country="USA", age_limit=18, trailer="images\Batman.mp4", url_id=2)
#         movies2 = Movies(poster="images\Deadpool.jpg", title="Deadpool", release_date="2016-06-16", description="Funny anti-hero journey", country="USA", age_limit=18, trailer="images\Deadpool.mp4", url_id=3)
#         session.add(movies2)  
#         await session.commit()

# async def add_series():
#     async with async_session() as session:
#         # series = Series(poster="images\ST.jpg", title="Stranger Things", seasons=4, release_date="2016-12-22", description="Was happy to hear, but not watch", country="USA", age_limit=18, trailer="images\ST.mp4", url_id=1)
#         # series1 = Series(poster="images\GOT.jpg", title="Game of Thrones", seasons=3, release_date="2011-09-29", description="Never watched it actually", country="USA", age_limit=18, trailer="images\GOT.mp4", url_id=2)
#         series2 = Series(poster="images\Friends.jpg", title="Friends", seasons=7, release_date="1994-11-11", description="Legends never die", country="USA", age_limit=18, trailer="images\Friends.mp4", url_id=3)  
#         session.add(series2)       
#         await session.commit()






# many-to-many associations

# async def add_movie_actors():
#     async with async_session() as session:
#         stmt = movie_actors.insert().values(movie_id=1, actor_id=6)
#         await session.execute(stmt)
#         await session.commit()

async def add_movie_directors():
    async with async_session() as session:
        stmt = movie_directors.insert().values(movie_id=1, directors_id=1)
        await session.execute(stmt)
        await session.commit()









async def all_movies():
    async with async_session() as session:
        result = await session.scalars(select(Movies))
        return result
    
async def all_series():
    async with async_session() as session:
        result = await session.scalars(select(Series))
        return result

async def all_genre():
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









