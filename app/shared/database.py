from sqlalchemy import create_engine
# from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, declarative_base
import os
from dotenv import load_dotenv

load_dotenv()


# BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# DATABASE_URL = f"sqlite:///{BASE_DIR}/flatipus.db"
DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True,
    # connect_args={"check_same_thread": False} # Needed for SQLite
    )
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

Base = declarative_base()
