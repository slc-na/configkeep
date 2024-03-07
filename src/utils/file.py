import pandas as pd
import os

from models import *
from utils import constants

def ensure_dir_exists(path: str):
    if(not os.path.exists(path)):
        os.makedirs(path)

def get_device_from_csv(source: str) -> list[NetworkDevice]:
    df = pd.read_csv(source)

    result: list[NetworkDevice] = []

    for _, row in df.iterrows():
        # Khusus APSLC, menggunakan credential network device
        # ad = Credential active directory
        # nd = Credential network device
        username = constants.USERNAME if row['Credential'] == 'ad' else constants.NETWORK_DEVICE_USERNAME
        password = constants.PASSWORD if row['Credential'] == 'ad' else constants.NETWORK_DEVICE_PASSWORD

        device: NetworkDevice = NetworkDeviceBuilder(NetworkDeviceType.from_string(row['OS']))\
                                    .set_device_name(row["Device Name"])\
                                    .set_host(row['Management IP'])\
                                    .set_username(username)\
                                    .set_password(password)\
                                    .set_secret(constants.NETWORK_DEVICE_PASSWORD)\
                                    .build()
        result.append(device)
    
    return result

def make_backup(filename: str, content: str):
    with open(filename, 'w') as f:
        f.write(content)