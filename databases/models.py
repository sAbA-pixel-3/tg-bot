# поиск по названию фильмов, по году, по актёрам, по режиссерам, по описанию, по жанрам, по странам, по возрасту



from sqlalchemy import String, Integer, Column, ForeignKey, Date, create_engine, Text, Table
from sqlalchemy.orm import relationship, sessionmaker, Mapped, mapped_column, DeclarativeBase
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncAttrs



class Base(AsyncAttrs, DeclarativeBase): 
    pass

# отдельные ТАБЛИЦЫ для Many-to-Many отношений 
movie_actors = Table("movie_actors", Base.metadata,
    Column("movie_id", Integer, ForeignKey("movies.id"), primary_key=True),
    Column("actor_id", Integer, ForeignKey("actors.id"), primary_key=True))

series_actors = Table("series_actors", Base.metadata,
    Column("series_id", Integer, ForeignKey("series.id"), primary_key=True),
    Column("actor_id", Integer, ForeignKey("actors.id"), primary_key=True))

movie_directors = Table("movie_directors", Base.metadata,
    Column("movie_id", Integer, ForeignKey("movies.id"), primary_key=True),
    Column("director_id", Integer, ForeignKey("directors.id"), primary_key=True)) 

series_directors = Table("series_directors", Base.metadata,
    Column("series_id", Integer, ForeignKey("series.id"), primary_key=True),
    Column("director_id", Integer, ForeignKey("directors.id"), primary_key=True))

movie_genre = Table("movie_genre", Base.metadata,
    Column("movie_id", Integer, ForeignKey("movies.id"), primary_key=True),
    Column("genre_id", Integer, ForeignKey("genre.id"), primary_key=True))

series_genre = Table("series_genre", Base.metadata,
    Column("series_id", Integer, ForeignKey("series.id"), primary_key=True),
    Column("genre_id", Integer, ForeignKey("genre.id"), primary_key=True))



class Url(Base): # one-to-one with Movies and Series 
    __tablename__ =  "url"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    url: Mapped[str] = mapped_column(String(255), nullable=False)

    movies = relationship("Movies", back_populates="url") ###
    series = relationship("Series", back_populates="url") ###

class Movies(Base):
    __tablename__ = "movies" 

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    poster: Mapped[str] = mapped_column(String(255), nullable=False)
    title: Mapped[str] = mapped_column(String(100))
    release_date: Mapped[Date] = mapped_column(Date)
    description: Mapped[str] = mapped_column(Text) 
    country: Mapped[str] = mapped_column(String(100)) 
    age_limit: Mapped[int] = mapped_column(Integer, nullable=False)
    trailer: Mapped[str] = mapped_column(String(255))

    url_id: Mapped[int] = mapped_column(Integer, ForeignKey("url.id")) ###
    url = relationship("Url", back_populates="movies") ###

    genres = relationship("Genre", secondary=movie_genre, back_populates="movies")
    actors = relationship("Actors", secondary=movie_actors, back_populates="movies")
    directors = relationship("Directors", secondary=movie_directors, back_populates="movies")

class Series(Base): 
    __tablename__ = "series"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    poster: Mapped[str] = mapped_column(String(255), nullable=False)
    title: Mapped[str] = mapped_column(String(100))
    seasons: Mapped[int] = mapped_column(Integer)
    release_date: Mapped[Date] = mapped_column(Date)
    description: Mapped[str] = mapped_column(Text)
    country: Mapped[str] = mapped_column(String(100)) 
    age_limit: Mapped[int] = mapped_column(Integer, nullable=False)
    trailer: Mapped[str] = mapped_column(String(255)) 

    url_id: Mapped[int] = mapped_column(Integer, ForeignKey("url.id")) ###
    url = relationship("Url", back_populates="series") ###

    genres = relationship("Genre", secondary=series_genre, back_populates="series")
    actors = relationship("Actors", secondary=series_actors, back_populates="series")
    directors = relationship("Directors", secondary=series_directors, back_populates="series")

class Genre(Base):
    __tablename__ = "genre"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(50))
    description: Mapped[str] = mapped_column(Text)

    movies = relationship("Movies", secondary=movie_genre, back_populates="genres")
    series = relationship("Series", secondary=series_genre, back_populates="genres") 

class Actors(Base):
    __tablename__ = "actors"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    image: Mapped[str] = mapped_column(String(255), nullable=False)
    first_name: Mapped[str] = mapped_column(String(100), nullable=False)
    last_name: Mapped[str] = mapped_column(String(100)) 
    birth_day: Mapped[Date] = mapped_column(Date)
    description: Mapped[str] = mapped_column(Text)

    movies = relationship("Movies", secondary=movie_actors, back_populates="actors")
    series = relationship("Series", secondary=series_actors, back_populates="actors")

class Directors(Base):
    __tablename__ = "directors"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    image: Mapped[str] = mapped_column(String(255), nullable=False)
    first_name: Mapped[str] = mapped_column(String(100), nullable=False)
    last_name: Mapped[str] = mapped_column(String(100)) 
    birth_day: Mapped[Date] = mapped_column(Date) 
    description: Mapped[str] = mapped_column(Text) 

    movies = relationship("Movies", secondary=movie_directors, back_populates="directors")
    series = relationship("Series", secondary=series_directors, back_populates="directors")

from config import MYSQL_URL
engine = create_async_engine(MYSQL_URL, echo=True)
async_session = async_sessionmaker(engine, expire_on_commit=False) 

async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all) 



# Base.metadata.create_all(engine) 