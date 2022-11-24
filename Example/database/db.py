from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import configparser
import pathlib

file_config = pathlib.Path(__file__).parent.parent.joinpath('config.ini')
config = configparser.ConfigParser()
config.read(file_config)

user = config.get("DB-DEV", "user")
password = config.get("DB-DEV", "password")
host = config.get("DB-DEV", "domain")
port = config.get("DB-DEV", "port")
db_name = config.get("DB-DEV", "db_name")

url = f'postgresql://{user}:{password}@{host}:{port}/{db_name}'

engine = create_engine(url, echo=True)
DBSession = sessionmaker(bind=engine)
session = DBSession()
