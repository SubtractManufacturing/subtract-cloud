from sqlmodel import SQLModel, create_engine, Session
from .config import settings

# Create a database URL for SQLAlchemy
DATABASE_URL = settings.DATABASE_URL

# Create SQLAlchemy engine
connect_args = {}
if DATABASE_URL.startswith("sqlite"):
    # Only needed for SQLite
    connect_args = {"check_same_thread": False}

engine = create_engine(DATABASE_URL, echo=True, connect_args=connect_args)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session