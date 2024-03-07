from netmiko import ConnectHandler
from netmiko.exceptions import SSHException

from utils.time import *
from utils.file import ensure_dir_exists, make_backup
from models import NetworkDevice

class BackupService:
    def __init__(self, devices: list[NetworkDevice]):
        self.__not_done: list[NetworkDevice] = devices
    
    def isDone(self):
        return len(self.__not_done) == 0
    
    def backup(self):
        path = f"backups/{get_year()}/{get_year_month()}/{get_date()}"
        ensure_dir_exists(path)

        device: NetworkDevice = self.__not_done[0]
        
        try:
            with ConnectHandler(**device.toDict()) as net_connect:
                output = device.getConfig(net_connect)
                make_backup(f"{path}/{get_date()}-{device.device_name}.config", output)
        except SSHException:
            print(f"Error occured during connection with network device: {device.device_name} using usernaem {device.username} and password {device.password}, will retry later")
            return

        self.__not_done.pop(0)