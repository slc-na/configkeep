import pandas as pd

from models import *
from utils import constants

def get_device_from_csv(source: str) -> list[NetworkDevice]:
    df = pd.read_csv(source)

    result: list[NetworkDevice] = []

    for _, row in df.iterrows():
        device: NetworkDevice = NetworkDeviceBuilder(NetworkDeviceType.from_string(row['OS']))\
                                    .set_host(row['Management IP'])\
                                    .set_username(constants.USERNAME)\
                                    .set_password(constants.PASSWORD)\
                                    .build()
        result.append(device)
    
    return result