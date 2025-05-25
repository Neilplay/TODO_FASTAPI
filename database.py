from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://db_qtui_user:kTcS8SVLjEA5bLnTaiHPagxaQKXio9UD@dpg-d0papggdl3ps73ak05tg-a.singapore-postgres.render.com/db_qtui"
)

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
