import os as _os
from dotenv import load_dotenv as _load_dotenv

__dotenv_path = '.env'
_load_dotenv(__dotenv_path)

USERNAME=_os.environ.get('USERNAME')
PASSWORD=_os.environ.get('PASSWORD')
NETWORK_DEVICE_PASSWORD=_os.environ.get('NETWORK_DEVICE_PASSWORD')
NETWORK_DEVICE_USERNAME=_os.environ.get('NETWORK_DEVICE_USERNAME')