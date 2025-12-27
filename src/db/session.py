from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

env_file='.env'
load_dotenv(dotenv_path=env_file)

DB_USERNAME=os.getenv("DB_USERNAME")
DB_HOST=os.getenv("DB_HOST")
DB_PASSWORD=os.getenv("DB_PASSWORD")
DB_NAME=os.getenv("DB_NAME")

DATABASE_URL=(
    f"mysql+mysqlconnector://{DB_USERNAME}:{DB_PASSWORD}"
    F"@{DB_HOST}/{DB_NAME}"
    )

engine=create_engine(
    DATABASE_URL,
    echo=True,
    future=True
    )

SessionLocal=sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False
)