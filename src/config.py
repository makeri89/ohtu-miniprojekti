import os
from dotenv import load_dotenv

dirname = os.path.dirname(__file__)

try:
    load_dotenv(dotenv_path=os.path.join(dirname, '..', '.env'))
except:
    pass

DATABASE_URL = os.getenv('DATABASE_URL').replace('postgres://', 'postgresql://', 1)
PORT = os.getenv('PORT')
HOST = os.getenv('HOST')