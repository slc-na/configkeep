import os
from datetime import datetime, timedelta
from logger import LogService

log = LogService()

class RemoveConfigService:
    def __init__(self):
        self.dir = ""
        self.year = 0
        self.month = 0
        self.day = 0

    def remove(self):
        self.checkDate()
        self.dirFolder()
        try:
            os.rmdir(self.dir)
        except FileNotFoundError:
            log.warning(f"Folder {self.dir} not found, skipping")

    def checkDate(self):
        now = datetime.now()
        date_90_days_ago = now - timedelta(days=90)

        self.year = date_90_days_ago.year
        self.month = date_90_days_ago.month
        if(self.month < 10):
            self.month = f"0{self.month}"
            
        self.day = date_90_days_ago.day - 1
        if(self.day < 10):
            self.day = f"0{self.day}"
         
    def dirFolder(self):
        self.dir = f"backups/{self.year}/{self.year}-{self.month}/{self.year}-{self.month}-{self.day}"
        log.info(f"Removing folder {self.dir}")