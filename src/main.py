from utils._file import get_device_from_csv
from backup_service import BackupService, RemoveConfigService
from logger import LogService

log = LogService("config.log")
devices = get_device_from_csv("src/data/network_devices.csv")
backup = BackupService(devices)
remove = RemoveConfigService()


def main():
    while(not backup.isDone()):
        backup.backup()
    
    remove.remove()
    
    
    
if __name__ == "__main__":
    main()