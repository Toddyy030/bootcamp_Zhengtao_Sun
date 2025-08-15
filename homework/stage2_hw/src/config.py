import os
from dotenv import load_dotenv
#set up config helper
def get_key(name:str):
    return os.getenv(name)

def load_env():
    load_dotenv()