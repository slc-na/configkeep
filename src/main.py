from utils._file import get_device_from_csv
from backup_service import BackupService

devices = get_device_from_csv("src/data/network_devices.csv")
backup = BackupService(devices)

while(not backup.isDone()):
    backup.backup()