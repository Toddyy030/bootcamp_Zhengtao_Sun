import sys, os
from dotenv import load_dotenv
def get_key(name:str):
    return os.getenv(name)

def load_env():
    load_dotenv()