from netmiko import ConnectHandler as _ConnectHandler
from netmiko.ssh_exception import SSHException as _SSHException

import utils._time as _time
from utils._file import ensure_dir_exists as _ensure_dir_exists, make_backup as _make_backup
from models import NetworkDevice as _NetworkDevice

from logger import LogService

log = LogService()

class BackupService:
    def __init__(self, devices: 'list[_NetworkDevice]'):
        self.__not_done: list[_NetworkDevice] = devices
    
    def isDone(self):
        return len(self.__not_done) == 0
    
    def backup(self):
        path = f"backups/{_time.get_year()}/{_time.get_year_month()}/{_time.get_date()}"
        _ensure_dir_exists(path)

        device: _NetworkDevice = self.__not_done[0]
        
        try:
            with _ConnectHandler(**device.toDict()) as net_connect:
                output = device.getConfig(net_connect)
                _make_backup(f"{path}/{_time.get_date()}-{device.device_name}.config", output)
                log.info(f"Backup for {device.device_name} success")
        except _SSHException:
            log.error(f"Error occured during connection with network device: {device.device_name} using usernaem {device.username} and password {device.password}, will retry later")
            return

        self.__not_done.pop(0)