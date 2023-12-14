from time import sleep
from requests import get as zget
# from os import environ
from logging import error as logerror
from dotenv import load_dotenv
from os import getenv

# load_dotenv("credentials.env")
BASE_URL = getenv('BASE_URL', None)
try:
    if len(BASE_URL) == 0:
        raise TypeError
    BASE_URL = BASE_URL.rstrip("/")
except TypeError:
    BASE_URL = None
PORT = 8080
if PORT is not None and BASE_URL is not None:
    while True:
        try:
            zget(BASE_URL).status_code
            sleep(300)
            print('okay')
        except Exception as e:
            logerror(f"alive.py: {e}")
            sleep(2)
            continue
