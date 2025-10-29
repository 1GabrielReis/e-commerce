import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv

load_dotenv()

Base = declarative_base()

class BD:
    def __init__(self):
        user = os.getenv("DB_USER")
        password = os.getenv("DB_PASSWORD")
        server = os.getenv("DB_SERVER")
        database = os.getenv("DB_NAME")
        driver = os.getenv("DB_DRIVER")

        # Corrigido: o nome do atributo precisa bater com o usado em connect()
        self.DATABASE_URL = (
            f"mssql+pyodbc://{user}:{password}@{server}/{database}"
            f"?driver={driver.replace(' ', '+')}"
        )

        self.engine = None
        self.SessionLocal = None

    

