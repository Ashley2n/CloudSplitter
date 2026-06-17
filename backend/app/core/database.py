import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base


Base = declarative_base()

engine = None
SessionLocal = None

def init_db():
    global engine, SessionLocal

    DATABASE_URL = os.getenv("DATABASE_URL")

    if not DATABASE_URL:
        raise ValueError("DATABASE_URL is not set")

    engine = create_engine(DATABASE_URL)



    SessionLocal = sessionmaker(
        autoflush=False,
        autocommit=False,
        bind=engine
    )


def get_session():
    """ enabling the use of database session """

    if SessionLocal is None:
        raise RuntimeError("Database not initialized. Call init_db() first.")
    
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

