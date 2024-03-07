import os
from os.path import join, dirname
from dotenv import load_dotenv

__dotenv_path = '.env'
load_dotenv(__dotenv_path)

USERNAME=os.environ.get('USERNAME')
PASSWORD=os.environ.get('PASSWORD')
NETWORK_DEVICE_PASSWORD=os.environ.get('NETWORK_DEVICE_PASSWORD')
NETWORK_DEVICE_USERNAME=os.environ.get('NETWORK_DEVICE_USERNAME')