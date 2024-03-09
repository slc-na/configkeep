import pandas as _pd
import os as _os

import models as _m
from utils import _constants

def ensure_dir_exists(path: str):
    if(not _os.path.exists(path)):
        _os.makedirs(path)

def get_device_from_csv(source: str) -> 'list[_m.NetworkDevice]':
    df = _pd.read_csv(source)

    result: list[_m.NetworkDevice] = []

    for _, row in df.iterrows():
        # Khusus APSLC, menggunakan credential network device
        # ad = Credential active directory
        # nd = Credential network device
        username = _constants.USERNAME if row['Credential'] == 'ad' else _constants.NETWORK_DEVICE_USERNAME
        password = _constants.PASSWORD if row['Credential'] == 'ad' else _constants.NETWORK_DEVICE_PASSWORD

        device: _m.NetworkDevice = _m.NetworkDeviceBuilder(_m.NetworkDeviceType.from_string(row['OS']))\
                                    .set_device_name(row["Device Name"])\
                                    .set_host(row['Management IP'])\
                                    .set_username(username)\
                                    .set_password(password)\
                                    .set_secret(_constants.NETWORK_DEVICE_PASSWORD)\
                                    .build()
        result.append(device)
    
    return result

def make_backup(filename: str, content: str):
    with open(filename, 'w') as f:
        f.write(content)