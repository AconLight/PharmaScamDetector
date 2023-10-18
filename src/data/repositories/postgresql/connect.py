from sqlalchemy import create_engine
from dotenv import load_dotenv
import os


def postgresql_engine():
    load_dotenv()
    return create_engine(
        os.getenv("CONNECTION_STRING"),
        isolation_level="SERIALIZABLE",
    )
