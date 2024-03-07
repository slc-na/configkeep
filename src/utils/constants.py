import os
from os.path import join, dirname
from dotenv import load_dotenv

__dotenv_path = '.env'
load_dotenv(__dotenv_path)

USERNAME=os.environ.get('USERNAME')
PASSWORD=os.environ.get('PASSWORD')

print(os.environ)